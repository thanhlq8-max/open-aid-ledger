"""Donation-readiness dry-run validator.

This script performs repository-local checks only. It does not call networks,
sign transactions, move assets, read private keys, or activate donations.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


FORBIDDEN_PATTERNS = [
    "private key",
    "seed phrase",
    "mnemonic",
    "exchange api secret",
    "withdrawal api",
    "auto transfer",
    "guaranteed return",
    "profit sharing",
]

REQUIRED_PATHS = [
    "README.md",
    "VERSION",
    "wallets.example.json",
    "campaigns/campaigns.example.json",
    "ledger/donations.csv",
    "ledger/disbursements.csv",
    "examples/sample-ledger/donations.csv",
    "examples/sample-ledger/disbursements.csv",
    "reports/sample-transparency-report.md",
    "docs/DONATION_ACTIVATION_CHECKLIST.md",
    "docs/MAINTAINER_GOVERNANCE_CHECKLIST.md",
    "docs/EMERGENCY_FREEZE_PROCEDURE.md",
    "docs/GITHUB_PAGES_STATIC_REPORT.md",
    "docs/BLOCKCHAIN_EXPLORER_IMPORTER_DESIGN.md",
    "docs/CAMPAIGN_LIFECYCLE.md",
    "DONATION_POLICY.md",
    "TRANSPARENCY_POLICY.md",
    "BENEFICIARY_PRIVACY_POLICY.md",
    "SECURITY.md",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def _readme_flag(readme: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", readme, flags=re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip()


def validate(root: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    checks: dict[str, bool] = {}

    root = root.resolve()

    for rel in REQUIRED_PATHS:
        exists = (root / rel).exists()
        checks[f"path:{rel}"] = exists
        if not exists:
            errors.append(f"Missing required path: {rel}")

    readme_path = root / "README.md"
    readme = _read(readme_path) if readme_path.exists() else ""

    donations_active = _readme_flag(readme, "DONATIONS_ACTIVE")
    wallets_published = _readme_flag(readme, "WALLETS_PUBLISHED")
    custody_automation = _readme_flag(readme, "CUSTODY_AUTOMATION")
    trading_use = _readme_flag(readme, "TRADING_USE")
    return_promise = _readme_flag(readme, "RETURN_PROMISE")

    checks["readme:donations_inactive"] = donations_active == "NO"
    checks["readme:wallets_unpublished"] = wallets_published == "NO"
    checks["readme:no_custody_automation"] = custody_automation == "NO"
    checks["readme:no_trading_use"] = trading_use == "FORBIDDEN"
    checks["readme:no_return_promise"] = return_promise == "FORBIDDEN"

    if donations_active != "NO":
        errors.append("README must keep DONATIONS_ACTIVE: NO for dry-run mode")
    if wallets_published != "NO":
        errors.append("README must keep WALLETS_PUBLISHED: NO for dry-run mode")
    if custody_automation != "NO":
        errors.append("README must keep CUSTODY_AUTOMATION: NO")
    if trading_use != "FORBIDDEN":
        errors.append("README must keep TRADING_USE: FORBIDDEN")
    if return_promise != "FORBIDDEN":
        errors.append("README must keep RETURN_PROMISE: FORBIDDEN")

    wallet_path = root / "wallets.example.json"
    if wallet_path.exists():
        try:
            wallets = _load_json(wallet_path)
            checks["wallets:donations_inactive"] = wallets.get("donations_active") is False
            checks["wallets:wallets_unpublished"] = wallets.get("wallets_published") is False
            if wallets.get("donations_active") is not False:
                errors.append("wallets.example.json must keep donations_active false")
            if wallets.get("wallets_published") is not False:
                errors.append("wallets.example.json must keep wallets_published false")
        except Exception as exc:  # pragma: no cover - defensive CLI path
            errors.append(f"Unable to parse wallets.example.json: {exc}")

    dry_run_wallet_path = root / "examples/dry-run/wallets.dry-run.example.json"
    if dry_run_wallet_path.exists():
        try:
            dry_wallets = _load_json(dry_run_wallet_path)
            checks["dry_run_wallets:dry_run_only"] = dry_wallets.get("dry_run_only") is True
            checks["dry_run_wallets:donations_inactive"] = dry_wallets.get("donations_active") is False
            checks["dry_run_wallets:wallets_unpublished"] = dry_wallets.get("wallets_published") is False
            if dry_wallets.get("dry_run_only") is not True:
                errors.append("dry-run wallet example must declare dry_run_only true")
            if dry_wallets.get("donations_active") is not False:
                errors.append("dry-run wallet example must keep donations_active false")
            if dry_wallets.get("wallets_published") is not False:
                errors.append("dry-run wallet example must keep wallets_published false")
        except Exception as exc:  # pragma: no cover
            errors.append(f"Unable to parse dry-run wallet example: {exc}")

    sample_report = root / "reports/sample-transparency-report.md"
    if sample_report.exists():
        report_text = _read(sample_report).lower()
        sample_markers = ["sample", "fictional", "non-production", "not activate"]
        marker_ok = any(marker in report_text for marker in sample_markers)
        checks["sample_report:marked_sample"] = marker_ok
        if not marker_ok:
            errors.append("sample transparency report must clearly be marked sample/non-production")

    dry_run_doc = root / "docs/DONATION_READINESS_DRY_RUN.md"
    if dry_run_doc.exists():
        dry_text = _read(dry_run_doc).lower()
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in dry_text and "forbidden" not in dry_text and "does not" not in dry_text:
                warnings.append(f"Review wording around: {pattern}")

    status = "PASS" if not errors else "FAIL"
    version = _read(root / "VERSION").strip() if (root / "VERSION").exists() else "UNKNOWN"

    return {
        "status": status,
        "version": version,
        "donations_active": donations_active,
        "wallets_published": wallets_published,
        "checks": checks,
        "warnings": warnings,
        "errors": errors,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate donation-readiness dry-run gates.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    parser.add_argument("--json", action="store_true", help="Print JSON output")
    args = parser.parse_args(argv)

    result = validate(Path(args.root))

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"readiness dry run: {result['status']}")
        for error in result["errors"]:
            print(f"ERROR: {error}")
        for warning in result["warnings"]:
            print(f"WARN: {warning}")

    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
