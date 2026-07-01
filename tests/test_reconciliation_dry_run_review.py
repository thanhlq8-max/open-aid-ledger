from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_reconciliation_dry_run_review_file_exists() -> None:
    assert (ROOT / "docs" / "DONATION_RECONCILIATION_DRY_RUN_REVIEW.md").is_file()
