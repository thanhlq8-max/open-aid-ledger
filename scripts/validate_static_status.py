"""Validate the static public status page.

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
    "CUSTODY_AUTOMATION: NO",
    "PRIVATE_KEYS_IN_REPO: FORBIDDEN",
    "TRADING_USE: FORBIDDEN",
    "RETURN_PROMISE: FORBIDDEN",
]

REQUIRED_LINK_TARGETS = [
    "PUBLIC_STATUS_PAGE.md",
    "PAGES_DEPLOYMENT_CHECKLIST.md",
    "DONATION_READINESS_DRY_RUN.md",
    "DONATION_ACTIVATION_CHECKLIST.md",
    "MAINTAINER_GOVERNANCE_CHECKLIST.md",
]

FORBIDDEN_TOKENS = [
    "DONATIONS_ACTIVE: YES",
    "WALLETS_PUBLISHED: YES",
    "CUSTODY_AUTOMATION: YES",
    "PRIVATE_KEYS_IN_REPO: ALLOWED",
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
            return _fail(f"missing required public status link target: {target}")

    for doc in [
        root / "docs" / "PUBLIC_STATUS_PAGE.md",
        root / "docs" / "PAGES_DEPLOYMENT_CHECKLIST.md",
        root / "docs" / "STATUS_BADGE_GUIDE.md",
    ]:
        if not doc.exists():
            return _fail(f"required static status doc missing: {doc.relative_to(root)}")

    print("static public status page OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate static public status page safety boundaries.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root.")
    args = parser.parse_args()
    return validate(Path(args.root).resolve())


if __name__ == "__main__":
    raise SystemExit(main())
