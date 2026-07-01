from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_profile_setup_guide_exists() -> None:
    path = ROOT / "docs" / "GITHUB_PROFILE_SETUP.md"
    assert path.is_file()
    text = path.read_text(encoding="utf-8")
    assert "GitHub Profile Setup" in text
    assert "https://thanhlq8-max.github.io/open-aid-ledger/" in text
    assert "https://github.com/thanhlq8-max/open-aid-ledger" in text
