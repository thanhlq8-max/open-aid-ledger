from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_official_release_readiness_files_exist() -> None:
    for path in [
        "docs/OFFICIAL_RELEASE_READINESS.md",
        "docs/RELEASE_NOTES_DRAFT_v1.0.0.md",
    ]:
        assert (ROOT / path).is_file()
