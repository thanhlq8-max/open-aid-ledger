from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
POST_PUBLISH_HISTORY_MARKER = "## Historical release-candidate checkpoints"
VALIDATOR_FIXTURE_FILES = [
    "VERSION",
    "README.md",
    "docs/index.md",
    "docs/POST_PUBLISH_STATUS.md",
    "docs/RELEASE_VALIDATION_EVIDENCE_v1.0.0.md",
    "docs/RELEASE_NOTES_v1.0.0.md",
    "docs/OFFICIAL_RELEASE_READINESS.md",
    "docs/PUBLIC_STATUS_RECHECK_v1.0.0.md",
    "docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md",
    "docs/DONATION_READINESS_REVIEW_PACKET.md",
    ".github/workflows/validate.yml",
    "scripts/validate_release_consistency.py",
]


def _run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(root / "scripts" / "validate_release_consistency.py"), str(root)],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )


def _copy_validator_fixture(tmp_path: Path) -> Path:
    target = tmp_path / "repo"
    for relative in VALIDATOR_FIXTURE_FILES:
        source = ROOT / relative
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    return target


def test_release_consistency_validator_passes() -> None:
    result = _run_validator(ROOT)
    assert result.returncode == 0, result.stderr + result.stdout
    assert "release consistency OK" in result.stdout


def test_current_identity_files_match_version_and_release_target() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    current_texts = {
        "README.md": (ROOT / "README.md").read_text(encoding="utf-8"),
        "docs/index.md": (ROOT / "docs" / "index.md").read_text(encoding="utf-8"),
    }
    post_publish = (ROOT / "docs" / "POST_PUBLISH_STATUS.md").read_text(encoding="utf-8")
    current_texts["docs/POST_PUBLISH_STATUS.md"] = post_publish.split(POST_PUBLISH_HISTORY_MARKER, 1)[0]

    for relative, text in current_texts.items():
        assert f"VERSION: {version}" in text, relative
        assert "RELEASE_TARGET: v1.0.0" in text, relative
        assert "RELEASE_TAG_CREATED: NO" in text, relative


def test_release_consistency_rejects_stale_current_post_publish_identity(tmp_path: Path) -> None:
    target = _copy_validator_fixture(tmp_path)
    path = target / "docs" / "POST_PUBLISH_STATUS.md"
    text = path.read_text(encoding="utf-8")
    current, history = text.split(POST_PUBLISH_HISTORY_MARKER, 1)
    current += "\nVERSION: stale-current-identity\n"
    path.write_text(current + POST_PUBLISH_HISTORY_MARKER + history, encoding="utf-8")

    result = _run_validator(target)

    assert result.returncode != 0
    assert "stale current identity" in result.stderr


def test_release_evidence_does_not_claim_self_referential_final_commit() -> None:
    text = (ROOT / "docs" / "RELEASE_VALIDATION_EVIDENCE_v1.0.0.md").read_text(encoding="utf-8")
    assert "VALIDATED_BASELINE_COMMIT:" in text
    assert "RELEASE_METADATA_COMMIT: RESOLVE_FROM_GIT_AT_RUNTIME" in text
    assert "RELEASE_TAG_TARGET: NOT_SELECTED" in text
    assert "FINAL_COMMIT:" not in text


def test_release_packet_stays_blocked_until_final_target_is_selected() -> None:
    required = {
        "docs/RELEASE_NOTES_v1.0.0.md": [
            "RELEASE_STATUS: FINAL_VALIDATION_PENDING",
            "RELEASE_TAG_TARGET: NOT_SELECTED",
            "FINAL_CI_EVIDENCE: NOT_ATTACHED",
        ],
        "docs/OFFICIAL_RELEASE_READINESS.md": [
            "RELEASE_STATUS: FINAL_VALIDATION_PENDING",
            "CURRENT_RELEASE_IDENTITY: 1.0.0",
            "RELEASE_IDENTITY_TRANSITION_COMPLETE: YES",
            "TAGGING_STATUS: BLOCKED",
        ],
        "docs/PUBLIC_STATUS_RECHECK_v1.0.0.md": [
            "CURRENT_RELEASE_IDENTITY: 1.0.0",
            "RELEASE_IDENTITY_TRANSITION_COMPLETE: YES",
            "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PENDING_FINAL_TARGET",
            "TAGGING_STATUS: BLOCKED",
        ],
        "docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md": [
            "RELEASE_TAG_TARGET: NOT_SELECTED",
            "FINAL_RUN_URL: NOT_ATTACHED",
            "docs/RELEASE_NOTES_v1.0.0.md",
        ],
    }
    for relative, tokens in required.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for token in tokens:
            assert token in text, (relative, token)

    runbook = (ROOT / "docs" / "RELEASE_TAGGING_RUNBOOK_v1.0.0.md").read_text(encoding="utf-8")
    assert "docs/RELEASE_NOTES_DRAFT_v1.0.0.md" not in runbook


@pytest.mark.parametrize(
    ("relative", "stale_claim"),
    [
        ("docs/RELEASE_NOTES_v1.0.0.md", "RELEASE_STATUS: READY_FOR_TAGGING_REVIEW"),
        ("docs/OFFICIAL_RELEASE_READINESS.md", "FINAL_CI_EVIDENCE: ATTACHED"),
        ("docs/PUBLIC_STATUS_RECHECK_v1.0.0.md", "FINAL_COMMIT: deadbeef"),
        ("docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md", "TAGGING_MAY_PROCEED"),
    ],
)
def test_release_consistency_rejects_stale_final_claims(
    tmp_path: Path,
    relative: str,
    stale_claim: str,
) -> None:
    target = _copy_validator_fixture(tmp_path)
    path = target / relative
    path.write_text(path.read_text(encoding="utf-8") + f"\n{stale_claim}\n", encoding="utf-8")

    result = _run_validator(target)

    assert result.returncode != 0
    assert "stale final-release claim" in result.stderr


@pytest.mark.parametrize(
    ("relative", "stale_claim"),
    [
        (
            "docs/OFFICIAL_RELEASE_READINESS.md",
            "- [ ] Complete the release identity transition consistently across public status files.",
        ),
        (
            "docs/PUBLIC_STATUS_RECHECK_v1.0.0.md",
            "Perform the final public-status recheck only after the separately reviewed release identity transition produces an exact final candidate.",
        ),
    ],
)
def test_release_consistency_rejects_stale_post_identity_transition_claims(
    tmp_path: Path,
    relative: str,
    stale_claim: str,
) -> None:
    target = _copy_validator_fixture(tmp_path)
    path = target / relative
    path.write_text(path.read_text(encoding="utf-8") + f"\n{stale_claim}\n", encoding="utf-8")

    result = _run_validator(target)

    assert result.returncode != 0
    assert "stale post-identity transition claim" in result.stderr


def test_release_consistency_rejects_draft_notes_as_runbook_base(tmp_path: Path) -> None:
    target = _copy_validator_fixture(tmp_path)
    path = target / "docs" / "RELEASE_TAGGING_RUNBOOK_v1.0.0.md"
    text = path.read_text(encoding="utf-8") + "\nUse docs/RELEASE_NOTES_DRAFT_v1.0.0.md as the release base.\n"
    path.write_text(text, encoding="utf-8")

    result = _run_validator(target)

    assert result.returncode != 0
    assert "final release notes" in result.stderr
