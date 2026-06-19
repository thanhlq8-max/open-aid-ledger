#!/usr/bin/env python3
"""Validate wallet metadata without touching private keys or network APIs.

The validator is deliberately local-only. It checks schema shape, placeholder
usage, wallet governance metadata, and obvious unsafe disclosure risks. It does
not query blockchains, sign transactions, or validate ownership of any address.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

SUPPORTED_SCHEMA_VERSIONS = {"1.1"}

REQUIRED_TOP_LEVEL_FIELDS = {
    "schema_version",
    "project_id",
    "last_updated",
    "donations_active",
    "wallets_published",
    "wallets",
    "prohibited",
}

REQUIRED_PROHIBITED_FIELDS = {
    "private_keys",
    "seed_phrases",
    "exchange_api_keys",
    "custody_automation",
}

REQUIRED_WALLET_FIELDS = {
    "wallet_id",
    "campaign_id",
    "chain",
    "asset",
    "network",
    "address",
    "controller_type",
    "controller_disclosure",
    "custody_model",
    "donation_use",
    "status",
    "purpose",
    "address_verification",
    "last_reviewed_utc",
    "risk_note",
}

ALLOWED_CONTROLLER_TYPES = {
    "single_maintainer",
    "multisig_2_of_3",
    "multisig_3_of_5",
    "organization_controlled",
    "single_maintainer_or_multisig",
}

ALLOWED_WALLET_STATUSES = {
    "placeholder",
    "proposed",
    "verified",
    "retired",
}

PLACEHOLDER_RE = re.compile(r"TO_BE_FILLED|CHANGE_ME|TBD|TODO", re.IGNORECASE)
SECRET_RE = re.compile(
    r"(seed phrase|mnemonic|private key|secret key|api key|password)",
    re.IGNORECASE,
)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URL_RE = re.compile(r"https?://", re.IGNORECASE)


def _contains_placeholder(value: Any) -> bool:
    return bool(PLACEHOLDER_RE.search(str(value)))


def _walk_strings(value: Any) -> list[str]:
    if isinstance(value, dict):
        out: list[str] = []
        for item in value.values():
            out.extend(_walk_strings(item))
        return out
    if isinstance(value, list):
        out = []
        for item in value:
            out.extend(_walk_strings(item))
        return out
    if isinstance(value, str):
        return [value]
    return []


def _validate_top_level(data: dict[str, Any], *, allow_placeholders: bool, errors: list[str]) -> None:
    missing = sorted(REQUIRED_TOP_LEVEL_FIELDS - data.keys())
    if missing:
        errors.append(f"top-level missing fields: {', '.join(missing)}")

    version = str(data.get("schema_version", "")).strip()
    if version not in SUPPORTED_SCHEMA_VERSIONS:
        errors.append(f"schema_version must be one of {sorted(SUPPORTED_SCHEMA_VERSIONS)!r}")

    project_id = str(data.get("project_id", "")).strip()
    if not project_id:
        errors.append("project_id must not be empty")

    last_updated = str(data.get("last_updated", "")).strip()
    if last_updated and not _contains_placeholder(last_updated) and not DATE_RE.match(last_updated):
        errors.append("last_updated must be YYYY-MM-DD or placeholder text")

    for flag in ("donations_active", "wallets_published"):
        if flag in data and not isinstance(data.get(flag), bool):
            errors.append(f"{flag} must be a boolean")

    prohibited = data.get("prohibited")
    if not isinstance(prohibited, dict):
        errors.append("prohibited must be an object")
    else:
        missing_prohibited = sorted(REQUIRED_PROHIBITED_FIELDS - prohibited.keys())
        if missing_prohibited:
            errors.append(f"prohibited missing fields: {', '.join(missing_prohibited)}")
        for field in REQUIRED_PROHIBITED_FIELDS:
            if prohibited.get(field) != "never_store" and field != "custody_automation":
                errors.append(f"prohibited.{field} must be 'never_store'")
        if prohibited.get("custody_automation") not in {"not_supported", "never_store"}:
            errors.append("prohibited.custody_automation must be 'not_supported' or 'never_store'")

    if not allow_placeholders:
        for value in _walk_strings(data):
            if _contains_placeholder(value):
                errors.append("wallet metadata still contains placeholder text")
                break


def _validate_address(idx: int, wallet: dict[str, Any], *, allow_placeholders: bool, errors: list[str]) -> None:
    address = str(wallet.get("address", "")).strip()
    if not address:
        errors.append(f"wallets[{idx}].address must not be empty")
        return

    if _contains_placeholder(address):
        if not allow_placeholders:
            errors.append(f"wallets[{idx}].address still contains placeholder text")
        return

    if any(ch.isspace() for ch in address):
        errors.append(f"wallets[{idx}].address must not contain whitespace")
    if len(address) < 16:
        errors.append(f"wallets[{idx}].address is too short to be a reviewed public address")
    if URL_RE.search(address):
        errors.append(f"wallets[{idx}].address must be an address, not a URL")
    if SECRET_RE.search(address):
        errors.append(f"wallets[{idx}].address appears to contain secret/private-key wording")


def _validate_wallet(idx: int, wallet: dict[str, Any], *, allow_placeholders: bool, errors: list[str]) -> None:
    missing = sorted(REQUIRED_WALLET_FIELDS - wallet.keys())
    if missing:
        errors.append(f"wallets[{idx}] missing fields: {', '.join(missing)}")

    serialized = json.dumps(wallet, ensure_ascii=False)
    if SECRET_RE.search(serialized):
        # wallet metadata may reference "private keys" only in policy-level top metadata;
        # individual wallet entries should not contain those phrases.
        errors.append(f"wallets[{idx}] appears to contain secret/private-key wording")

    for field in REQUIRED_WALLET_FIELDS:
        value = str(wallet.get(field, "")).strip()
        if not value:
            errors.append(f"wallets[{idx}].{field} must not be empty")
        if _contains_placeholder(value) and not allow_placeholders:
            errors.append(f"wallets[{idx}].{field} still contains placeholder text")

    controller_type = str(wallet.get("controller_type", "")).strip()
    if controller_type and controller_type not in ALLOWED_CONTROLLER_TYPES:
        errors.append(f"wallets[{idx}] unsupported controller_type: {controller_type}")

    status = str(wallet.get("status", "")).strip().lower()
    if status and status not in ALLOWED_WALLET_STATUSES:
        errors.append(f"wallets[{idx}] unsupported status: {status}")

    last_reviewed = str(wallet.get("last_reviewed_utc", "")).strip()
    if last_reviewed and not _contains_placeholder(last_reviewed) and not DATE_RE.match(last_reviewed):
        errors.append(f"wallets[{idx}].last_reviewed_utc must be YYYY-MM-DD or placeholder text")

    _validate_address(idx, wallet, allow_placeholders=allow_placeholders, errors=errors)


def validate(path: Path, *, allow_placeholders: bool) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc}"]

    errors: list[str] = []
    if not isinstance(data, dict):
        return ["wallet metadata root must be an object"]

    _validate_top_level(data, allow_placeholders=allow_placeholders, errors=errors)

    wallets = data.get("wallets")
    if not isinstance(wallets, list) or not wallets:
        errors.append("wallets must be a non-empty list")
        return errors

    seen_wallet_ids: set[str] = set()
    active_or_published = bool(data.get("donations_active")) or bool(data.get("wallets_published"))

    for idx, wallet in enumerate(wallets):
        if not isinstance(wallet, dict):
            errors.append(f"wallets[{idx}] must be an object")
            continue

        wallet_id = str(wallet.get("wallet_id", "")).strip()
        if wallet_id:
            if wallet_id in seen_wallet_ids:
                errors.append(f"wallets[{idx}] duplicate wallet_id: {wallet_id}")
            seen_wallet_ids.add(wallet_id)

        _validate_wallet(idx, wallet, allow_placeholders=allow_placeholders, errors=errors)

        if active_or_published:
            for value in _walk_strings(wallet):
                if _contains_placeholder(value):
                    errors.append("donations_active/wallets_published cannot be true while wallet placeholders remain")
                    break
            if str(wallet.get("status", "")).strip().lower() != "verified":
                errors.append("donations_active/wallets_published requires every wallet status to be 'verified'")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Open Aid Ledger wallet metadata.")
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--allow-placeholders",
        action="store_true",
        help="Allow TO_BE_FILLED placeholders for example/template files only.",
    )
    args = parser.parse_args()

    errors = validate(args.path, allow_placeholders=args.allow_placeholders)
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print("wallet metadata shape OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

