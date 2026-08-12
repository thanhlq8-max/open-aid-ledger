from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
POST_PUBLISH_HISTORY_MARKER = "## Historical release-candidate checkpoints"
RELEASE_TAG_TARGET = "21b341c50d8e2277eda4134c66bd2ea3155a816e"
VALIDATOR_FIXTURE_FILES = [
    "VERSION",
    "PROJECT_STATE.md",
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


def test_current_identity_files_match_published_release() -> None:
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
        assert "RELEASE_TAG_CREATED: YES" in text, relative
        assert "GITHUB_RELEASE_CREATED: YES" in text, relative


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


def test_release_evidence_preserves_historical_baseline_and_final_target() -> None:
    text = (ROOT / "docs" / "RELEASE_VALIDATION_EVIDENCE_v1.0.0.md").read_text(encoding="utf-8")
    assert "VALIDATED_BASELINE_COMMIT:" in text
    assert f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}" in text
    assert "FINAL_TARGET_VALIDATE: VALIDATE_147_ATTEMPT_2_PASS" in text
    assert "TAG_VALIDATE: VALIDATE_148_PASS" in text
    assert "FINAL_COMMIT:" not in text


def test_release_packet_records_published_state() -> None:
    required = {
        "docs/RELEASE_NOTES_v1.0.0.md": [
            "RELEASE_STATUS: RELEASED",
            f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
            "FINAL_CI_EVIDENCE: VALIDATE_147_ATTEMPT_2_PASS",
            "RELEASE_TAG_CREATED: YES",
            "GITHUB_RELEASE_CREATED: YES",
            "TAG_VALIDATE: VALIDATE_148_PASS",
        ],
        "docs/OFFICIAL_RELEASE_READINESS.md": [
            "RELEASE_STATUS: RELEASED",
            "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PASS",
            "POST_MERGE_PAGES_RUNTIME: PAGES_62_PASS",
            "TAGGING_STATUS: COMPLETE",
        ],
        "docs/PUBLIC_STATUS_RECHECK_v1.0.0.md": [
            "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PASS",
            "PAGES_RUNTIME: PAGES_62_PASS",
            "TAGGING_STATUS: COMPLETE",
        ],
        "docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md": [
            "TAGGING_RUNBOOK: COMPLETE",
            f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
            "TAGGING_STATUS: COMPLETE",
            "docs/RELEASE_NOTES_v1.0.0.md",
        ],
    }
    for relative, tokens in required.items():
        text = (ROOT / relative).read_text(encoding="utf-8")
        for token in tokens:
            assert token in text, (relative, token)


@pytest.mark.parametrize(
    ("relative", "stale_claim"),
    [
        ("README.md", "RELEASE_TAG_CREATED: NO"),
        ("docs/RELEASE_NOTES_v1.0.0.md", "RELEASE_STATUS: FINAL_VALIDATION_PENDING"),
        ("docs/OFFICIAL_RELEASE_READINESS.md", "FINAL_CI_EVIDENCE: NOT_ATTACHED"),
        ("docs/PUBLIC_STATUS_RECHECK_v1.0.0.md", "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PENDING_FINAL_TARGET"),
        ("docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md", "TAGGING_STATUS: BLOCKED"),
    ],
)
def test_release_consistency_rejects_stale_pre_release_claims(
    tmp_path: Path,
    relative: str,
    stale_claim: str,
) -> None:
    target = _copy_validator_fixture(tmp_path)
    path = target / relative
    path.write_text(path.read_text(encoding="utf-8") + f"\n{stale_claim}\n", encoding="utf-8")

    result = _run_validator(target)

    assert result.returncode != 0
    assert "stale pre-release token" in result.stderr


def test_release_consistency_rejects_wrong_release_target(tmp_path: Path) -> None:
    target = _copy_validator_fixture(tmp_path)
    path = target / "docs" / "RELEASE_NOTES_v1.0.0.md"
    text = path.read_text(encoding="utf-8").replace(
        f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
        "RELEASE_TAG_TARGET: deadbeef",
        1,
    )
    path.write_text(text, encoding="utf-8")

    result = _run_validator(target)

    assert result.returncode != 0
    assert "missing published-release token" in result.stderr


def test_release_consistency_rejects_draft_notes_as_runbook_base(tmp_path: Path) -> None:
    target = _copy_validator_fixture(tmp_path)
    path = target / "docs" / "RELEASE_TAGGING_RUNBOOK_v1.0.0.md"
    text = path.read_text(encoding="utf-8") + "\nUse docs/RELEASE_NOTES_DRAFT_v1.0.0.md as the release base.\n"
    path.write_text(text, encoding="utf-8")

    result = _run_validator(target)

    assert result.returncode != 0
    assert "final release notes" in result.stderr
