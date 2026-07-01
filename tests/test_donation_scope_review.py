from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_donation_scope_review_file_exists() -> None:
    assert (ROOT / "docs" / "DONATION_SCOPE_REVIEW.md").is_file()
