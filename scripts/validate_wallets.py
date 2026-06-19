#!/usr/bin/env python3
"""Validate wallet metadata without touching private keys or network APIs."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REQUIRED_WALLET_FIELDS = {
    "wallet_id",
    "campaign_id",
    "chain",
    "asset",
    "network",
    "address",
    "controller_type",
    "controller_disclosure",
    "risk_note",
}

ALLOWED_CONTROLLER_TYPES = {
    "single_maintainer",
    "multisig_2_of_3",
    "multisig_3_of_5",
    "organization_controlled",
    "single_maintainer_or_multisig",
}

PLACEHOLDER_RE = re.compile(r"TO_BE_FILLED|CHANGE_ME|TBD|TODO", re.IGNORECASE)
SECRET_RE = re.compile(r"(seed phrase|mnemonic|private key|secret key|api key|password)", re.IGNORECASE)


def validate(path: Path, *, allow_placeholders: bool) -> list[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []

    if data.get("schema_version") != "1.0":
        errors.append("schema_version must be '1.0'")

    wallets = data.get("wallets")
    if not isinstance(wallets, list) or not wallets:
        errors.append("wallets must be a non-empty list")
        return errors

    seen_wallet_ids: set[str] = set()
    for idx, wallet in enumerate(wallets):
        if not isinstance(wallet, dict):
            errors.append(f"wallets[{idx}] must be an object")
            continue

        missing = sorted(REQUIRED_WALLET_FIELDS - wallet.keys())
        if missing:
            errors.append(f"wallets[{idx}] missing fields: {', '.join(missing)}")

        serialized = json.dumps(wallet, ensure_ascii=False)
        if SECRET_RE.search(serialized):
            # risk_note may mention private keys in policies, but wallet metadata itself should not.
            errors.append(f"wallets[{idx}] appears to contain secret/private-key wording")

        wallet_id = str(wallet.get("wallet_id", "")).strip()
        if wallet_id:
            if wallet_id in seen_wallet_ids:
                errors.append(f"wallets[{idx}] duplicate wallet_id: {wallet_id}")
            seen_wallet_ids.add(wallet_id)

        controller_type = str(wallet.get("controller_type", "")).strip()
        if controller_type and controller_type not in ALLOWED_CONTROLLER_TYPES:
            errors.append(f"wallets[{idx}] unsupported controller_type: {controller_type}")

        for field in REQUIRED_WALLET_FIELDS:
            value = str(wallet.get(field, "")).strip()
            if not value:
                errors.append(f"wallets[{idx}].{field} must not be empty")
            if PLACEHOLDER_RE.search(value) and not allow_placeholders:
                errors.append(f"wallets[{idx}].{field} still contains placeholder text")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate wallets.json schema shape.")
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
