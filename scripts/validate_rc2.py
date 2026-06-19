#!/usr/bin/env python3
"""Validate RC2 external-review activation-gate artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FILES = [
    "docs/RC2_EXTERNAL_REVIEW_ACTIVATION_GATE.md",
    "docs/EXTERNAL_REVIEW_PANEL_GUIDE.md",
    "docs/ACTIVATION_GATE_SIGNOFF_RECORD.md",
    "docs/WALLET_PUBLICATION_PRECHECK.md",
    "examples/dry-run/rc2-external-review.example.json",
    "RELEASE_NOTES_v1.0.0-rc2.md",
]

REQUIRED_README_TOKENS = [
    "VERSION: 1.0.0-rc2-external-review-activation-gate",
    "DONATIONS_ACTIVE: NO",
    "WALLETS_PUBLISHED: NO",
    "CUSTODY_AUTOMATION: NO",
    "RETURN_PROMISE: FORBIDDEN",
]

REQUIRED_DOC_TOKENS = [
    "DONATIONS_ACTIVE: NO",
    "WALLETS_PUBLISHED: NO",
    "ACTIVATION_APPROVED: NO",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        if not (root / rel).is_file():
            errors.append(f"missing required RC2 file: {rel}")

    version_path = root / "VERSION"
    if not version_path.is_file():
        errors.append("missing VERSION")
    elif "1.0.0-rc2-external-review-activation-gate" not in _read(version_path):
        errors.append("VERSION missing RC2 token")

    readme = _read(root / "README.md") if (root / "README.md").is_file() else ""
    for token in REQUIRED_README_TOKENS:
        if token not in readme:
            errors.append(f"README missing token: {token}")

    gate_doc = root / "docs/RC2_EXTERNAL_REVIEW_ACTIVATION_GATE.md"
    if gate_doc.is_file():
        text = _read(gate_doc)
        for token in REQUIRED_DOC_TOKENS:
            if token not in text:
                errors.append(f"RC2 gate doc missing token: {token}")

    sample_path = root / "examples/dry-run/rc2-external-review.example.json"
    if sample_path.is_file():
        try:
            sample = json.loads(_read(sample_path))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid RC2 sample JSON: {exc}")
        else:
            if sample.get("release_candidate") != "1.0.0-rc2":
                errors.append("RC2 sample has wrong release_candidate")
            if sample.get("donations_active") is not False:
                errors.append("RC2 sample must keep donations inactive")
            if sample.get("wallets_published") is not False:
                errors.append("RC2 sample must keep wallets unpublished")
            if sample.get("activation_approved") is not False:
                errors.append("RC2 sample must not approve activation")
            if sample.get("external_review_required") is not True:
                errors.append("RC2 sample must require external review")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate RC2 external review activation-gate artifacts.")
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()

    errors = validate(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("rc2 external review activation gate: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
