from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_final_release_notes_file_exists() -> None:
    assert (ROOT / "docs" / "RELEASE_NOTES_v1.0.0.md").is_file()
