#!/usr/bin/env python3
"""Validate the v1.0.0-rc1 donation-ready candidate gate."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_FILES = [
    "docs/RC1_DONATION_READY_CANDIDATE.md",
    "docs/RC1_RELEASE_CHECKLIST.md",
    "docs/RC1_SIGNOFF_RECORD.md",
    "docs/RC1_NON_ACTIVATION_NOTICE.md",
    "examples/dry-run/rc1-candidate.example.json",
]

REQUIRED_README_MARKERS = [
        "DONATIONS_ACTIVE: NO",
    "WALLETS_PUBLISHED: NO",
    "CUSTODY_AUTOMATION: NO",
    "TRADING_USE: FORBIDDEN",
    "RETURN_PROMISE: FORBIDDEN",
]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate v1.0.0-rc1 candidate gate.")
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()
    root = args.root.resolve()

    version_path = root / "VERSION"
    if not version_path.exists():
        fail("VERSION file is missing")
    version = version_path.read_text(encoding="utf-8").strip()
    if not version:
        fail("VERSION is empty")

    readme_path = root / "README.md"
    if not readme_path.exists():
        fail("README.md is missing")
    readme = readme_path.read_text(encoding="utf-8")
    for marker in REQUIRED_README_MARKERS:
        if marker not in readme:
            fail(f"README marker missing: {marker}")

    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            fail(f"required RC1 file missing: {rel}")

    metadata_path = root / "examples/dry-run/rc1-candidate.example.json"
    data = json.loads(metadata_path.read_text(encoding="utf-8"))
    expected_false = ["donations_active", "wallets_published", "custody_automation", "transfer_automation"]
    for key in expected_false:
        if data.get(key) is not False:
            fail(f"dry-run metadata must keep {key}=false")
    if data.get("candidate") != "v1.0.0-rc1":
        fail("dry-run metadata candidate mismatch")

    print("rc1 candidate gate: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
