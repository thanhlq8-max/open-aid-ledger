from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_two_reviewer_approval_rule_file_exists() -> None:
    assert (ROOT / "docs" / "DONATION_TWO_REVIEWER_APPROVAL_RULE.md").is_file()
