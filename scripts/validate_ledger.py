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


def _validate_amount(path: Path, row_no: int, raw: str, errors: list[str]) -> None:
    try:
        amount = Decimal((raw or "").strip())
    except InvalidOperation:
        errors.append(f"{path}:{row_no}: invalid amount {raw!r}")
        return
    if amount <= 0:
        errors.append(f"{path}:{row_no}: amount must be > 0")


def _validate_common(path: Path, rows: Iterable[dict[str, str]], errors: list[str]) -> None:
    for idx, row in enumerate(rows, start=2):
        if _is_empty_row(row):
            continue
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


def validate(donations: Path, disbursements: Path) -> list[str]:
    errors: list[str] = []

    donation_cols, donation_rows = _read_rows(donations)
    disbursement_cols, disbursement_rows = _read_rows(disbursements)

    _validate_columns(donations, donation_cols, DONATION_COLUMNS, errors)
    _validate_columns(disbursements, disbursement_cols, DISBURSEMENT_COLUMNS, errors)
    _validate_common(donations, donation_rows, errors)
    _validate_common(disbursements, disbursement_rows, errors)

    for idx, row in enumerate(disbursement_rows, start=2):
        if _is_empty_row(row):
            continue
        privacy_level = (row.get("privacy_level") or "").strip().lower()
        if privacy_level and privacy_level not in ALLOWED_PRIVACY_LEVELS:
            errors.append(f"{disbursements}:{idx}: privacy_level {privacy_level!r} is not allowed")
        beneficiary_code = (row.get("beneficiary_code") or "").strip()
        if beneficiary_code and any(ch.isspace() for ch in beneficiary_code):
            errors.append(f"{disbursements}:{idx}: beneficiary_code must not contain spaces")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Open Aid Ledger CSV files.")
    parser.add_argument("--donations", required=True, type=Path)
    parser.add_argument("--disbursements", required=True, type=Path)
    args = parser.parse_args()

    errors = validate(args.donations, args.disbursements)
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1
    print("ledger CSV files OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
