from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_FIXTURE_FILES = [
    "VERSION",
    "README.md",
    "docs/index.md",
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


def test_public_status_keeps_release_candidate_distinct_from_release_target() -> None:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    for relative in ["README.md", "docs/index.md"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        assert f"VERSION: {version}" in text
        assert "RELEASE_TARGET: v1.0.0" in text
        assert "RELEASE_TAG_CREATED: NO" in text


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
            "TAGGING_STATUS: BLOCKED",
        ],
        "docs/PUBLIC_STATUS_RECHECK_v1.0.0.md": [
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


def test_release_consistency_rejects_draft_notes_as_runbook_base(tmp_path: Path) -> None:
    target = _copy_validator_fixture(tmp_path)
    path = target / "docs" / "RELEASE_TAGGING_RUNBOOK_v1.0.0.md"
    text = path.read_text(encoding="utf-8").replace(
        "docs/RELEASE_NOTES_v1.0.0.md",
        "docs/RELEASE_NOTES_DRAFT_v1.0.0.md",
    )
    path.write_text(text, encoding="utf-8")

    result = _run_validator(target)

    assert result.returncode != 0
    assert "final release notes" in result.stderr
