"""Validate the static public dashboard.

This validator is intentionally local and read-only. It does not call GitHub,
blockchain explorers, exchanges, or wallet APIs.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


REQUIRED_TOKENS = [
    "DONATIONS_ACTIVE: NO",
    "WALLETS_PUBLISHED: NO",
    "ACTIVATION_APPROVED: NO",
    "CUSTODY_AUTOMATION: NO",
    "TRADING_USE: FORBIDDEN",
    "RETURN_PROMISE: FORBIDDEN",
    "Donation activation | BLOCKED",
    "Custody automation | FORBIDDEN",
    "EASY_TO_ACCESS: YES",
    "EASY_TO_USE: YES",
    "EASY_TO_SHARE: YES",
    "USER_DASHBOARD: YES",
]

REQUIRED_LINK_TARGETS = [
    "START_HERE.md",
    "DONOR_QUICKSTART.md",
    "DONOR_FAQ.md",
    "DRY_RUN_OPERATIONS_RUNBOOK.md",
    "REVIEW_PACKET_TEMPLATE.md",
    "OPERATIONAL_READINESS_MATRIX.md",
]

FORBIDDEN_TOKENS = [
    "DONATIONS_ACTIVE: YES",
    "WALLETS_PUBLISHED: YES",
    "CUSTODY_AUTOMATION: YES",
    "TRADING_USE: ALLOWED",
    "RETURN_PROMISE: ALLOWED",
    "guaranteed return",
    "guaranteed profit",
    "margin call rescue",
    "private key:",
    "seed phrase:",
]


def _fail(message: str) -> int:
    print(f"static status validation failed: {message}", file=sys.stderr)
    return 1


def validate(root: Path) -> int:
    index = root / "docs" / "index.md"
    if not index.exists():
        return _fail("docs/index.md not found")

    text = index.read_text(encoding="utf-8")

    for token in REQUIRED_TOKENS:
        if token not in text:
            return _fail(f"missing required token: {token}")

    lower_text = text.lower()
    for token in FORBIDDEN_TOKENS:
        if token.lower() in lower_text:
            return _fail(f"forbidden token found: {token}")

    for target in REQUIRED_LINK_TARGETS:
        if target not in text:
            return _fail(f"missing required public dashboard link target: {target}")

    for doc in [
        root / "docs" / "START_HERE.md",
        root / "docs" / "DONOR_QUICKSTART.md",
        root / "docs" / "DONOR_FAQ.md",
        root / "docs" / "STATUS_BADGE_GUIDE.md",
    ]:
        if not doc.exists():
            return _fail(f"required static dashboard doc missing: {doc.relative_to(root)}")

    print("static public status page OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate static public dashboard safety boundaries.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root.")
    args = parser.parse_args()
    return validate(Path(args.root).resolve())


if __name__ == "__main__":
    raise SystemExit(main())
