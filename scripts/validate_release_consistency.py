#!/usr/bin/env python3
"""Validate release-candidate identity and release-preparation consistency."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


RELEASE_TARGET = "v1.0.0"
REQUIRED_READINESS_DOCS = [
    "docs/DONATION_SCOPE_REVIEW.md",
    "docs/DONOR_ACTIVE_MODE_GUIDE_DRAFT.md",
    "docs/DONATION_RECONCILIATION_DRY_RUN_REVIEW.md",
    "docs/DONATION_FREEZE_DRY_RUN_REVIEW.md",
    "docs/DONATION_TWO_REVIEWER_APPROVAL_RULE.md",
]


def _fail(message: str) -> int:
    print(f"release consistency validation failed: {message}", file=sys.stderr)
    return 1


def validate(root: Path) -> int:
    version_path = root / "VERSION"
    if not version_path.exists():
        return _fail("VERSION not found")

    version = version_path.read_text(encoding="utf-8").strip()
    if not version:
        return _fail("VERSION is empty")

    for relative in ["README.md", "docs/index.md"]:
        path = root / relative
        if not path.exists():
            return _fail(f"{relative} not found")
        text = path.read_text(encoding="utf-8")
        if f"VERSION: {version}" not in text:
            return _fail(f"{relative} does not match VERSION")
        if f"RELEASE_TARGET: {RELEASE_TARGET}" not in text:
            return _fail(f"{relative} missing release target")
        if "RELEASE_TAG_CREATED: NO" not in text:
            return _fail(f"{relative} must not claim the release tag exists")

    evidence_path = root / "docs" / "RELEASE_VALIDATION_EVIDENCE_v1.0.0.md"
    evidence = evidence_path.read_text(encoding="utf-8")
    for token in [
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "VALIDATED_BASELINE_COMMIT:",
        "RELEASE_METADATA_COMMIT: RESOLVE_FROM_GIT_AT_RUNTIME",
        "RELEASE_TAG_TARGET: NOT_SELECTED",
        "RELEASE_TAG_CREATED: NO",
    ]:
        if token not in evidence:
            return _fail(f"release evidence missing token: {token}")
    if "FINAL_COMMIT:" in evidence:
        return _fail("release evidence contains self-referential FINAL_COMMIT")

    readiness_path = root / "docs" / "DONATION_READINESS_REVIEW_PACKET.md"
    readiness = readiness_path.read_text(encoding="utf-8")
    for relative in REQUIRED_READINESS_DOCS:
        if f"`{relative}`" not in readiness:
            return _fail(f"readiness packet missing evidence index entry: {relative}")

    workflow_path = root / ".github" / "workflows" / "validate.yml"
    workflow = workflow_path.read_text(encoding="utf-8")
    if 'tags: ["v*"]' not in workflow:
        return _fail("Validate workflow does not run for v* tags")
    if "python scripts/validate_release_consistency.py ." not in workflow:
        return _fail("Validate workflow does not run release consistency validator")

    print("release consistency OK")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate release-candidate and release-target consistency.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root.")
    args = parser.parse_args()
    return validate(Path(args.root).resolve())


if __name__ == "__main__":
    raise SystemExit(main())
