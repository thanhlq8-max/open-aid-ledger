from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_donation_governance_model_file_exists() -> None:
    assert (ROOT / "docs" / "DONATION_GOVERNANCE_MODEL.md").is_file()
