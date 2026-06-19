from __future__ import annotations

import json
from pathlib import Path

from scripts.validate_wallets import validate


def _base_wallets() -> dict:
    return {
        "schema_version": "1.1",
        "project_id": "open-aid-ledger",
        "last_updated": "2026-06-19",
        "donations_active": False,
        "wallets_published": False,
        "wallets": [
            {
                "wallet_id": "btc-community-001",
                "campaign_id": "community-hardship-2026",
                "chain": "bitcoin",
                "asset": "BTC",
                "network": "mainnet",
                "address": "bc1qexampleaddress000000000000000000000000",
                "controller_type": "multisig_2_of_3",
                "controller_disclosure": "2-of-3 maintainer reviewed public address metadata.",
                "custody_model": "read_only_public_address_metadata_only",
                "donation_use": "hardship_support_or_open_source_public_good_support_only",
                "status": "verified",
                "purpose": "community hardship support",
                "address_verification": "verified by two maintainers before publication",
                "last_reviewed_utc": "2026-06-19",
                "risk_note": "Only send the listed asset on the listed network.",
            }
        ],
        "prohibited": {
            "private_keys": "never_store",
            "seed_phrases": "never_store",
            "exchange_api_keys": "never_store",
            "custody_automation": "not_supported",
        },
    }


def _write_json(tmp_path: Path, data: dict) -> Path:
    path = tmp_path / "wallets.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def test_valid_wallet_metadata_passes(tmp_path: Path) -> None:
    path = _write_json(tmp_path, _base_wallets())
    assert validate(path, allow_placeholders=False) == []


def test_missing_wallet_field_fails(tmp_path: Path) -> None:
    data = _base_wallets()
    del data["wallets"][0]["address_verification"]
    path = _write_json(tmp_path, data)
    errors = validate(path, allow_placeholders=False)
    assert any("missing fields" in err for err in errors)


def test_placeholders_allowed_only_when_flagged(tmp_path: Path) -> None:
    data = _base_wallets()
    data["wallets"][0]["address"] = "TO_BE_FILLED_BY_MAINTAINER"
    path = _write_json(tmp_path, data)
    assert validate(path, allow_placeholders=True) == []
    assert validate(path, allow_placeholders=False)


def test_active_donations_require_verified_non_placeholder_wallets(tmp_path: Path) -> None:
    data = _base_wallets()
    data["donations_active"] = True
    data["wallets_published"] = True
    data["wallets"][0]["status"] = "placeholder"
    path = _write_json(tmp_path, data)
    errors = validate(path, allow_placeholders=True)
    assert any("requires every wallet status" in err for err in errors)

