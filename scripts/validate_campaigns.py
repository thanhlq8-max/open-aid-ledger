"""Validate Open Aid Ledger campaign metadata.

Boundary:
- read-only validation only;
- no wallet signing;
- no asset transfer;
- no private key handling;
- no exchange API;
- no donation activation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL = {
    "schema_version",
    "project_id",
    "donations_active",
    "wallets_published",
    "campaigns",
}

REQUIRED_CAMPAIGN_FIELDS = {
    "campaign_id",
    "title",
    "status",
    "purpose",
    "beneficiary_privacy_level",
    "donation_activation_allowed",
    "wallets_required",
    "ledger_required",
    "decision_record_path",
    "report_path",
    "created_utc",
    "last_reviewed_utc",
    "guardrails",
}

ALLOWED_STATUSES = {
    "proposed",
    "review",
    "approved_inactive",
    "active",
    "paused",
    "closed",
    "cancelled",
}

ALLOWED_PRIVACY_LEVELS = {
    "redacted_public_summary",
    "redacted_receipts",
    "partner_attestation_only",
    "public_project_summary",
}

REQUIRED_GUARDRAILS = {
    "NO_PRIVATE_KEYS",
    "NO_SEED_PHRASES",
    "NO_AUTO_TRANSFER",
    "NO_CUSTODY_AUTOMATION",
    "NO_TRADING_ACCOUNT_TOP_UP",
    "NO_MARGIN_CALL_SUPPORT",
    "NO_RETURN_PROMISE",
    "NO_BENEFICIARY_DOXXING",
}

CAMPAIGN_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,80}$")
PATH_RE = re.compile(r"^[A-Za-z0-9_./\\-]+$")

FORBIDDEN_TEXT = {
    "private key",
    "private-key",
    "seed phrase",
    "seed-phrase",
    "recovery phrase",
    "mnemonic",
    "auto transfer",
    "autotransfer",
    "withdrawal api",
    "exchange withdrawal",
    "copy trading",
    "profit sharing",
    "guaranteed return",
    "margin call",
    "gỡ lỗ",
    "go lo",
}


def _fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def _load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        _fail(f"file not found: {path}")
    except json.JSONDecodeError as exc:
        _fail(f"invalid JSON in {path}: {exc}")
    if not isinstance(data, dict):
        _fail("campaign metadata root must be a JSON object")
    return data


def _require_bool(value: Any, field: str) -> None:
    if not isinstance(value, bool):
        _fail(f"{field} must be boolean")


def _require_text(value: Any, field: str, *, min_len: int = 1) -> None:
    if not isinstance(value, str) or len(value.strip()) < min_len:
        _fail(f"{field} must be non-empty text")


def _require_date(value: Any, field: str) -> None:
    _require_text(value, field)
    try:
        date.fromisoformat(value)
    except ValueError:
        _fail(f"{field} must be YYYY-MM-DD")


def _check_forbidden_text(value: str, field: str) -> None:
    lowered = value.lower()
    for term in FORBIDDEN_TEXT:
        if term in lowered:
            _fail(f"{field} contains forbidden wording: {term}")


def _validate_path(value: str, field: str) -> None:
    _require_text(value, field)
    if ".." in value or value.startswith(("/", "\\")):
        _fail(f"{field} must be a relative repository path")
    if not PATH_RE.match(value):
        _fail(f"{field} contains unsupported path characters")


def validate_campaigns(data: dict[str, Any], *, allow_inactive_template: bool = False) -> None:
    missing = sorted(REQUIRED_TOP_LEVEL - set(data))
    if missing:
        _fail(f"missing top-level fields: {', '.join(missing)}")

    if data["schema_version"] != "campaigns.v1.0":
        _fail("schema_version must be campaigns.v1.0")
    _require_text(data["project_id"], "project_id")
    _require_bool(data["donations_active"], "donations_active")
    _require_bool(data["wallets_published"], "wallets_published")

    campaigns = data["campaigns"]
    if not isinstance(campaigns, list):
        _fail("campaigns must be a list")
    if not campaigns and not allow_inactive_template:
        _fail("campaigns must not be empty unless --allow-inactive-template is used")

    seen_ids: set[str] = set()
    active_seen = False

    for idx, campaign in enumerate(campaigns, start=1):
        if not isinstance(campaign, dict):
            _fail(f"campaign #{idx} must be an object")

        missing_campaign = sorted(REQUIRED_CAMPAIGN_FIELDS - set(campaign))
        if missing_campaign:
            _fail(f"campaign #{idx} missing fields: {', '.join(missing_campaign)}")

        campaign_id = campaign["campaign_id"]
        _require_text(campaign_id, "campaign_id", min_len=3)
        if not CAMPAIGN_ID_RE.match(campaign_id):
            _fail(f"campaign_id has invalid format: {campaign_id}")
        if campaign_id in seen_ids:
            _fail(f"duplicate campaign_id: {campaign_id}")
        seen_ids.add(campaign_id)

        for field in ("title", "purpose"):
            _require_text(campaign[field], field, min_len=5)
            _check_forbidden_text(campaign[field], field)

        status = campaign["status"]
        if status not in ALLOWED_STATUSES:
            _fail(f"campaign {campaign_id} has invalid status: {status}")
        if status == "active":
            active_seen = True

        privacy_level = campaign["beneficiary_privacy_level"]
        if privacy_level not in ALLOWED_PRIVACY_LEVELS:
            _fail(f"campaign {campaign_id} has invalid beneficiary_privacy_level: {privacy_level}")

        for field in ("donation_activation_allowed", "wallets_required", "ledger_required"):
            _require_bool(campaign[field], f"{campaign_id}.{field}")

        _validate_path(campaign["decision_record_path"], f"{campaign_id}.decision_record_path")
        _validate_path(campaign["report_path"], f"{campaign_id}.report_path")
        _require_date(campaign["created_utc"], f"{campaign_id}.created_utc")
        _require_date(campaign["last_reviewed_utc"], f"{campaign_id}.last_reviewed_utc")

        guardrails = campaign["guardrails"]
        if not isinstance(guardrails, list) or not all(isinstance(item, str) for item in guardrails):
            _fail(f"campaign {campaign_id} guardrails must be a string list")
        missing_guardrails = sorted(REQUIRED_GUARDRAILS - set(guardrails))
        if missing_guardrails:
            _fail(f"campaign {campaign_id} missing guardrails: {', '.join(missing_guardrails)}")

    if active_seen and not data["donations_active"]:
        _fail("active campaigns are not allowed while donations_active is false")
    if data["donations_active"] and not data["wallets_published"]:
        _fail("donations_active cannot be true while wallets_published is false")



def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Open Aid Ledger campaign metadata.")
    parser.add_argument("campaigns_file", type=Path)
    parser.add_argument("--allow-inactive-template", action="store_true")
    args = parser.parse_args()

    data = _load_json(args.campaigns_file)
    validate_campaigns(data, allow_inactive_template=args.allow_inactive_template)
    print("campaign metadata OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
