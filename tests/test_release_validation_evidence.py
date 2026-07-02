from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_release_validation_evidence_file_exists() -> None:
    assert (ROOT / "docs" / "RELEASE_VALIDATION_EVIDENCE_v1.0.0.md").is_file()
