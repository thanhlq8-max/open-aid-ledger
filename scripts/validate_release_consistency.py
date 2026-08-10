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
RELEASE_PACKET_REQUIREMENTS = {
    "docs/RELEASE_NOTES_v1.0.0.md": [
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "RELEASE_STATUS: FINAL_VALIDATION_PENDING",
        "RELEASE_TAG_TARGET: NOT_SELECTED",
        "FINAL_CI_EVIDENCE: NOT_ATTACHED",
        "RELEASE_TAG_CREATED: NO",
        "GITHUB_RELEASE_CREATED: NO",
        "LIVE_OPERATION: NO",
    ],
    "docs/OFFICIAL_RELEASE_READINESS.md": [
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "RELEASE_STATUS: FINAL_VALIDATION_PENDING",
        "RELEASE_TAG_TARGET: NOT_SELECTED",
        "FINAL_CI_EVIDENCE: NOT_ATTACHED",
        "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PENDING_FINAL_TARGET",
        "TAGGING_STATUS: BLOCKED",
        "LIVE_OPERATION: NO",
    ],
    "docs/PUBLIC_STATUS_RECHECK_v1.0.0.md": [
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "RELEASE_TAG_TARGET: NOT_SELECTED",
        "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PENDING_FINAL_TARGET",
        "FINAL_CI_EVIDENCE: NOT_ATTACHED",
        "RELEASE_TAG_CREATED: NO",
        "GITHUB_RELEASE_CREATED: NO",
        "TAGGING_STATUS: BLOCKED",
    ],
    "docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md": [
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "RELEASE_TAG_TARGET: NOT_SELECTED",
        "FINAL_RUN_URL: NOT_ATTACHED",
        "TAGGING_STATUS: BLOCKED",
        "docs/RELEASE_NOTES_v1.0.0.md",
    ],
}
STALE_FINAL_CLAIMS = [
    "READY_FOR_TAGGING_REVIEW",
    "FINAL_CI_EVIDENCE: ATTACHED",
    "FINAL_COMMIT:",
    "TAGGING_MAY_PROCEED",
    "Status: ready for maintainer tagging approval.",
]


def _fail(message: str) -> int:
    print(f"release consistency validation failed: {message}", file=sys.stderr)
    return 1


def _read_required(root: Path, relative: str) -> str | None:
    path = root / relative
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def validate(root: Path) -> int:
    version_path = root / "VERSION"
    if not version_path.exists():
        return _fail("VERSION not found")

    version = version_path.read_text(encoding="utf-8").strip()
    if not version:
        return _fail("VERSION is empty")

    for relative in ["README.md", "docs/index.md"]:
        text = _read_required(root, relative)
        if text is None:
            return _fail(f"{relative} not found")
        if f"VERSION: {version}" not in text:
            return _fail(f"{relative} does not match VERSION")
        if f"RELEASE_TARGET: {RELEASE_TARGET}" not in text:
            return _fail(f"{relative} missing release target")
        if "RELEASE_TAG_CREATED: NO" not in text:
            return _fail(f"{relative} must not claim the release tag exists")

    evidence_relative = "docs/RELEASE_VALIDATION_EVIDENCE_v1.0.0.md"
    evidence = _read_required(root, evidence_relative)
    if evidence is None:
        return _fail(f"{evidence_relative} not found")
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

    if "RELEASE_TAG_TARGET: NOT_SELECTED" in evidence:
        for relative, required_tokens in RELEASE_PACKET_REQUIREMENTS.items():
            text = _read_required(root, relative)
            if text is None:
                return _fail(f"{relative} not found")
            for token in required_tokens:
                if token not in text:
                    return _fail(f"{relative} missing pending-release token: {token}")
            for token in STALE_FINAL_CLAIMS:
                if token in text:
                    return _fail(f"{relative} contains stale final-release claim: {token}")

        runbook = _read_required(root, "docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md")
        if runbook is None:
            return _fail("docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md not found")
        if "docs/RELEASE_NOTES_DRAFT_v1.0.0.md" in runbook:
            return _fail("tagging runbook must use final release notes, not the draft notes file")

    readiness_relative = "docs/DONATION_READINESS_REVIEW_PACKET.md"
    readiness = _read_required(root, readiness_relative)
    if readiness is None:
        return _fail(f"{readiness_relative} not found")
    for relative in REQUIRED_READINESS_DOCS:
        if f"`{relative}`" not in readiness:
            return _fail(f"readiness packet missing evidence index entry: {relative}")

    workflow_relative = ".github/workflows/validate.yml"
    workflow = _read_required(root, workflow_relative)
    if workflow is None:
        return _fail(f"{workflow_relative} not found")
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
