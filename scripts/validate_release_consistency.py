#!/usr/bin/env python3
"""Validate published v1.0.0 release and current public-status consistency."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


RELEASE_TARGET = "v1.0.0"
RELEASE_TAG_TARGET = "21b341c50d8e2277eda4134c66bd2ea3155a816e"
CURRENT_IDENTITY_FILES = ["README.md", "docs/index.md"]
POST_PUBLISH_STATUS = "docs/POST_PUBLISH_STATUS.md"
POST_PUBLISH_HISTORY_MARKER = "## Historical release-candidate checkpoints"
PROJECT_STATE = "PROJECT_STATE.md"
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
        "RELEASE_STATUS: RELEASED",
        f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
        "FINAL_CI_EVIDENCE: VALIDATE_147_ATTEMPT_2_PASS",
        "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PASS",
        "PAGES_RUNTIME: PAGES_62_PASS",
        "RELEASE_TAG_CREATED: YES",
        "GITHUB_RELEASE_CREATED: YES",
        "TAG_VALIDATE: VALIDATE_148_PASS",
        "LIVE_OPERATION: NO",
    ],
    "docs/OFFICIAL_RELEASE_READINESS.md": [
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "RELEASE_STATUS: RELEASED",
        "CURRENT_RELEASE_IDENTITY: 1.0.0",
        "RELEASE_IDENTITY_TRANSITION_COMPLETE: YES",
        f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
        "FINAL_CI_EVIDENCE: VALIDATE_147_ATTEMPT_2_PASS",
        "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PASS",
        "POST_MERGE_PAGES_RUNTIME: PAGES_62_PASS",
        "RELEASE_TAG_CREATED: YES",
        "GITHUB_RELEASE_CREATED: YES",
        "TAG_VALIDATE: VALIDATE_148_PASS",
        "TAGGING_STATUS: COMPLETE",
        "LIVE_OPERATION: NO",
    ],
    "docs/PUBLIC_STATUS_RECHECK_v1.0.0.md": [
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "CURRENT_RELEASE_IDENTITY: 1.0.0",
        "RELEASE_IDENTITY_TRANSITION_COMPLETE: YES",
        f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
        "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PASS",
        "FINAL_CI_EVIDENCE: VALIDATE_147_ATTEMPT_2_PASS",
        "PAGES_RUNTIME: PAGES_62_PASS",
        "RELEASE_TAG_CREATED: YES",
        "GITHUB_RELEASE_CREATED: YES",
        "TAG_VALIDATE: VALIDATE_148_PASS",
        "TAGGING_STATUS: COMPLETE",
    ],
    "docs/RELEASE_VALIDATION_EVIDENCE_v1.0.0.md": [
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "RELEASE_STATUS: RELEASED",
        f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
        "FINAL_TARGET_VALIDATE: VALIDATE_147_ATTEMPT_2_PASS",
        "PAGES_RUNTIME: PAGES_62_PASS",
        "RELEASE_TAG_CREATED: YES",
        "GITHUB_RELEASE_CREATED: YES",
        "TAG_VALIDATE: VALIDATE_148_PASS",
        "GITHUB_RELEASE_ID: 369005821",
        "LIVE_OPERATION: NO",
    ],
    "docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md": [
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "TAGGING_RUNBOOK: COMPLETE",
        f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
        "RELEASE_TAG_CREATED: YES",
        "GITHUB_RELEASE_CREATED: YES",
        "FINAL_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/31373591930",
        "TAG_VALIDATE: VALIDATE_148_PASS",
        "TAGGING_STATUS: COMPLETE",
        "LIVE_OPERATION: NO",
        "docs/RELEASE_NOTES_v1.0.0.md",
    ],
}
STALE_PRE_RELEASE_TOKENS = [
    "RELEASE_STATUS: FINAL_VALIDATION_PENDING",
    "RELEASE_TAG_TARGET: NOT_SELECTED",
    "FINAL_CI_EVIDENCE: NOT_ATTACHED",
    "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PENDING_FINAL_TARGET",
    "TAGGING_STATUS: BLOCKED",
    "RELEASE_TAG_CREATED: NO",
    "GITHUB_RELEASE_CREATED: NO",
    "RELEASE_TAG: NOT_CREATED",
    "GITHUB_RELEASE: NOT_VERIFIED",
]
CORE_OPERATING_LOCKS = [
    "PROJECT_STATUS: PUBLIC_TEMPLATE",
    "DONATIONS_ACTIVE: NO",
    "WALLETS_PUBLISHED: NO",
    "ACTIVATION_APPROVED: NO",
    "CUSTODY_AUTOMATION: NO",
    "TRADING_USE: FORBIDDEN",
    "RETURN_PROMISE: FORBIDDEN",
    "GO_LIVE: NO",
]


def _fail(message: str) -> int:
    print(f"release consistency validation failed: {message}", file=sys.stderr)
    return 1


def _read_required(root: Path, relative: str) -> str | None:
    path = root / relative
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def _validate_current_identity_text(relative: str, text: str, version: str) -> int | None:
    required = [
        f"VERSION: {version}",
        f"RELEASE_TARGET: {RELEASE_TARGET}",
        "RELEASE_TAG_CREATED: YES",
        "GITHUB_RELEASE_CREATED: YES",
    ]
    for token in required:
        if token not in text:
            return _fail(f"{relative} missing current release token: {token}")
    return None


def _reject_stale_pre_release(relative: str, text: str) -> int | None:
    for token in STALE_PRE_RELEASE_TOKENS:
        if token in text:
            return _fail(f"{relative} contains stale pre-release token: {token}")
    return None


def validate(root: Path) -> int:
    version_path = root / "VERSION"
    if not version_path.exists():
        return _fail("VERSION not found")

    version = version_path.read_text(encoding="utf-8").strip()
    if version != "1.0.0":
        return _fail(f"VERSION must remain 1.0.0 for this release contract, got: {version}")

    for relative in CURRENT_IDENTITY_FILES:
        text = _read_required(root, relative)
        if text is None:
            return _fail(f"{relative} not found")
        result = _validate_current_identity_text(relative, text, version)
        if result is not None:
            return result
        result = _reject_stale_pre_release(relative, text)
        if result is not None:
            return result

    post_publish = _read_required(root, POST_PUBLISH_STATUS)
    if post_publish is None:
        return _fail(f"{POST_PUBLISH_STATUS} not found")
    if POST_PUBLISH_HISTORY_MARKER not in post_publish:
        return _fail(f"{POST_PUBLISH_STATUS} missing historical-section boundary")
    current_post_publish = post_publish.split(POST_PUBLISH_HISTORY_MARKER, 1)[0]
    result = _validate_current_identity_text(POST_PUBLISH_STATUS, current_post_publish, version)
    if result is not None:
        return result
    for token in [
        f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
        "TAG_VALIDATE: VALIDATE_148_PASS",
    ]:
        if token not in current_post_publish:
            return _fail(f"{POST_PUBLISH_STATUS} missing post-release token: {token}")
    for line in current_post_publish.splitlines():
        if line.startswith("VERSION:") and line != f"VERSION: {version}":
            return _fail(f"{POST_PUBLISH_STATUS} contains stale current identity: {line}")
    result = _reject_stale_pre_release(POST_PUBLISH_STATUS, current_post_publish)
    if result is not None:
        return result

    for relative, required_tokens in RELEASE_PACKET_REQUIREMENTS.items():
        text = _read_required(root, relative)
        if text is None:
            return _fail(f"{relative} not found")
        for token in required_tokens:
            if token not in text:
                return _fail(f"{relative} missing published-release token: {token}")
        result = _reject_stale_pre_release(relative, text)
        if result is not None:
            return result

    evidence = _read_required(root, "docs/RELEASE_VALIDATION_EVIDENCE_v1.0.0.md")
    if evidence is None:
        return _fail("release evidence not found")
    if "VALIDATED_BASELINE_COMMIT:" not in evidence:
        return _fail("release evidence must preserve historical baseline")
    if "FINAL_COMMIT:" in evidence:
        return _fail("release evidence contains self-referential FINAL_COMMIT")

    runbook = _read_required(root, "docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md")
    if runbook is None:
        return _fail("docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md not found")
    if "docs/RELEASE_NOTES_DRAFT_v1.0.0.md" in runbook:
        return _fail("tagging runbook must use final release notes, not the draft notes file")

    project_state = _read_required(root, PROJECT_STATE)
    if project_state is None:
        return _fail(f"{PROJECT_STATE} not found")
    for token in [
        "STATUS: ACTIVE_RELEASED_PUBLIC_TEMPLATE",
        f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
        "RELEASE_STATUS: RELEASED",
        "RELEASE_TAG_CREATED: YES",
        "GITHUB_RELEASE_CREATED: YES",
        "TAG_VALIDATE: VALIDATE_148_PASS",
        *CORE_OPERATING_LOCKS,
    ]:
        if token not in project_state:
            return _fail(f"{PROJECT_STATE} missing post-release contract token: {token}")
    result = _reject_stale_pre_release(PROJECT_STATE, project_state)
    if result is not None:
        return result

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
    parser = argparse.ArgumentParser(description="Validate published release and public-status consistency.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root.")
    args = parser.parse_args()
    return validate(Path(args.root).resolve())


if __name__ == "__main__":
    raise SystemExit(main())
