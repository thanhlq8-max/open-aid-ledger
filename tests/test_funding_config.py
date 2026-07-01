from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_github_sponsors_funding_config_points_to_repo_owner() -> None:
    funding = ROOT / ".github" / "FUNDING.yml"
    assert funding.is_file()
    assert funding.read_text(encoding="utf-8") == "github: [thanhlq8-max]\n"
