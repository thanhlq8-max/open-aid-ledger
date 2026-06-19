#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_FILES = [
    "docs/RC2_EXTERNAL_REVIEW_ACTIVATION_GATE.md",
    "docs/EXTERNAL_REVIEW_PANEL_GUIDE.md",
    "docs/ACTIVATION_GATE_SIGNOFF_RECORD.md",
    "docs/WALLET_PUBLICATION_PRECHECK.md",
    "examples/dry-run/rc2-external-review.example.json",
]

REQUIRED_README_TOKENS = [
    "DONATIONS_ACTIVE: NO",
    "WALLETS_PUBLISHED: NO",
    "CUSTODY_AUTOMATION: NO",
    "TRADING_USE: FORBIDDEN",
    "RETURN_PROMISE: FORBIDDEN",
]

REQUIRED_GATE_DOC_TOKENS = [
    "DONATIONS_ACTIVE: NO",
    "WALLETS_PUBLISHED: NO",
    "ACTIVATION_APPROVED: NO",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.as_posix()}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        fail(f"empty file: {path.as_posix()}")
    return text


def validate(root: Path) -> None:
    version_path = root / "VERSION"
    if not version_path.exists():
        fail("VERSION file is missing")
    if not version_path.read_text(encoding="utf-8").strip():
        fail("VERSION is empty")

    readme = read_text(root / "README.md")
    for token in REQUIRED_README_TOKENS:
        if token not in readme:
            fail(f"README missing marker: {token}")

    for rel in REQUIRED_FILES:
        text = read_text(root / rel)

        if rel == "docs/RC2_EXTERNAL_REVIEW_ACTIVATION_GATE.md":
            for token in REQUIRED_GATE_DOC_TOKENS:
                if token not in text:
                    fail(f"{rel} missing marker: {token}")

        if rel.endswith(".json"):
            data = json.loads(text)
            if data.get("donations_active") is not False:
                fail(f"{rel} must keep donations_active false")
            if data.get("wallets_published") is not False:
                fail(f"{rel} must keep wallets_published false")
            if data.get("activation_approved") is not False:
                fail(f"{rel} must keep activation_approved false")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    validate(root)
    print("rc2 external review activation gate: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
