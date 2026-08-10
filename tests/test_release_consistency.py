from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_release_consistency_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_release_consistency.py", "."],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
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
