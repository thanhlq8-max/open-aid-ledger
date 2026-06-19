#!/usr/bin/env python3
"""Validate donation and disbursement CSV files.

This validator is intentionally local and read-only:
- no blockchain queries
- no transfers
- no wallet signing
- no exchange APIs
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Iterable

DONATION_COLUMNS = [
    "date_utc",
    "campaign_id",
    "chain",
    "asset",
    "network",
    "amount",
    "tx_hash",
    "donor_label",
    "source_note",
    "status",
]

DISBURSEMENT_COLUMNS = [
    "date_utc",
    "campaign_id",
    "beneficiary_code",
    "category",
    "chain",
    "asset",
    "network",
    "amount",
    "tx_hash",
    "purpose",
    "evidence_ref",
    "approval_ref",
    "status",
    "privacy_level",
]

ALLOWED_STATUSES = {
    "pending",
    "confirmed",
    "reported",
    "reconciled",
    "cancelled",
    "void",
}

ALLOWED_PRIVACY_LEVELS = {
    "public_redacted",
    "private_review",
    "partner_confirmed",
    "maintainer_attested",
    "not_applicable",
}

SECRET_WORDS = re.compile(
    r"(seed phrase|mnemonic|private key|secret key|api key|password|passport|national id|identity card|phone number|home address)",
    re.IGNORECASE,
)

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}:\d{2}Z)?$")
SAFE_ID_RE = re.compile(r"^[A-Za-z0-9._:-]+$")
TX_HASH_PLACEHOLDERS = {"", "n/a", "na", "not_applicable", "offchain"}


def _read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def _is_empty_row(row: dict[str, str]) -> bool:
    return not any((value or "").strip() for value in row.values())


def _validate_columns(path: Path, actual: list[str], expected: list[str], errors: list[str]) -> None:
    if actual != expected:
        errors.append(f"{path}: columns mismatch. expected={expected!r} actual={actual!r}")


def _validate_amount(path: Path, row_no: int, raw: str, errors: list[str]) -> Decimal | None:
    try:
        amount = Decimal((raw or "").strip())
    except InvalidOperation:
        errors.append(f"{path}:{row_no}: invalid amount {raw!r}")
        return None
    if amount <= 0:
        errors.append(f"{path}:{row_no}: amount must be > 0")
    return amount


def _validate_required_values(path: Path, row_no: int, row: dict[str, str], columns: list[str], errors: list[str]) -> None:
    for column in columns:
        value = (row.get(column) or "").strip()
        if not value:
            errors.append(f"{path}:{row_no}: {column} must not be empty")


def _validate_safe_id(path: Path, row_no: int, field: str, raw: str, errors: list[str]) -> None:
    value = (raw or "").strip()
    if value and not SAFE_ID_RE.match(value):
        errors.append(f"{path}:{row_no}: {field} must use only letters, numbers, dot, dash, underscore, or colon")


def _normalize_tx_hash(raw: str) -> str:
    return (raw or "").strip().lower()


def _validate_tx_hash(path: Path, row_no: int, raw: str, errors: list[str]) -> str | None:
    value = _normalize_tx_hash(raw)
    if value in TX_HASH_PLACEHOLDERS:
        return None
    if any(ch.isspace() for ch in value):
        errors.append(f"{path}:{row_no}: tx_hash must not contain whitespace")
    if value.startswith("http://") or value.startswith("https://"):
        errors.append(f"{path}:{row_no}: tx_hash must be a hash/reference, not a URL")
    if len(value) < 8:
        errors.append(f"{path}:{row_no}: tx_hash is too short")
    return value


def _validate_common(path: Path, rows: Iterable[dict[str, str]], columns: list[str], errors: list[str]) -> None:
    seen_tx_hashes: set[str] = set()
    for idx, row in enumerate(rows, start=2):
        if _is_empty_row(row):
            continue

        _validate_required_values(path, idx, row, columns, errors)

        joined = " ".join((value or "") for value in row.values())
        if SECRET_WORDS.search(joined):
            errors.append(f"{path}:{idx}: row appears to contain sensitive/private data wording")

        date = (row.get("date_utc") or "").strip()
        if date and not DATE_RE.match(date):
            errors.append(f"{path}:{idx}: date_utc should be YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ")

        _validate_amount(path, idx, row.get("amount") or "", errors)

        status = (row.get("status") or "").strip().lower()
        if status and status not in ALLOWED_STATUSES:
            errors.append(f"{path}:{idx}: status {status!r} is not allowed")

        for field in ("campaign_id", "chain", "asset", "network"):
            _validate_safe_id(path, idx, field, row.get(field) or "", errors)

        tx_hash = _validate_tx_hash(path, idx, row.get("tx_hash") or "", errors)
        if tx_hash:
            if tx_hash in seen_tx_hashes:
                errors.append(f"{path}:{idx}: duplicate tx_hash {tx_hash!r}")
            seen_tx_hashes.add(tx_hash)


def _balance_errors(
    donations: list[dict[str, str]],
    disbursements: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    incoming: dict[tuple[str, str, str], Decimal] = defaultdict(Decimal)
    outgoing: dict[tuple[str, str, str], Decimal] = defaultdict(Decimal)

    for row in donations:
        if _is_empty_row(row):
            continue
        if (row.get("status") or "").strip().lower() in {"cancelled", "void"}:
            continue
        key = ((row.get("chain") or "").strip(), (row.get("asset") or "").strip(), (row.get("network") or "").strip())
        try:
            incoming[key] += Decimal((row.get("amount") or "0").strip())
        except InvalidOperation:
            pass

    for row in disbursements:
        if _is_empty_row(row):
            continue
        if (row.get("status") or "").strip().lower() in {"cancelled", "void"}:
            continue
        key = ((row.get("chain") or "").strip(), (row.get("asset") or "").strip(), (row.get("network") or "").strip())
        try:
            outgoing[key] += Decimal((row.get("amount") or "0").strip())
        except InvalidOperation:
            pass

    for key, spent in sorted(outgoing.items()):
        received = incoming.get(key, Decimal("0"))
        if spent > received:
            errors.append(f"disbursements exceed donations for {key}: spent={spent} received={received}")

    return errors


def validate(donations: Path, disbursements: Path, *, enforce_balance: bool = False) -> list[str]:
    errors: list[str] = []

    donation_cols, donation_rows = _read_rows(donations)
    disbursement_cols, disbursement_rows = _read_rows(disbursements)

    _validate_columns(donations, donation_cols, DONATION_COLUMNS, errors)
    _validate_columns(disbursements, disbursement_cols, DISBURSEMENT_COLUMNS, errors)

    _validate_common(donations, donation_rows, DONATION_COLUMNS, errors)
    _validate_common(disbursements, disbursement_rows, DISBURSEMENT_COLUMNS, errors)

    for idx, row in enumerate(disbursement_rows, start=2):
        if _is_empty_row(row):
            continue
        privacy_level = (row.get("privacy_level") or "").strip().lower()
        if privacy_level and privacy_level not in ALLOWED_PRIVACY_LEVELS:
            errors.append(f"{disbursements}:{idx}: privacy_level {privacy_level!r} is not allowed")
        beneficiary_code = (row.get("beneficiary_code") or "").strip()
        _validate_safe_id(disbursements, idx, "beneficiary_code", beneficiary_code, errors)

    if enforce_balance:
        errors.extend(_balance_errors(donation_rows, disbursement_rows))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Open Aid Ledger CSV files.")
    parser.add_argument("--donations", required=True, type=Path)
    parser.add_argument("--disbursements", required=True, type=Path)
    parser.add_argument(
        "--enforce-balance",
        action="store_true",
        help="Fail when outgoing support exceeds incoming donations per chain/asset/network.",
    )
    args = parser.parse_args()

    errors = validate(args.donations, args.disbursements, enforce_balance=args.enforce_balance)
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1
    print("ledger CSV files OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

