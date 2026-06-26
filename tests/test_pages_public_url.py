from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_URL = "https://thanhlq8-max.github.io/open-aid-ledger/"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_public_pages_url_is_documented_in_entrypoints() -> None:
    for path in [
        "README.md",
        "index.md",
        "docs/REPOSITORY_ABOUT_SETUP.md",
    ]:
        assert PUBLIC_URL in read(path), path


def test_repository_about_setup_keeps_sidebar_metadata_contract() -> None:
    text = read("docs/REPOSITORY_ABOUT_SETUP.md")
    for phrase in [
        "Repository About Setup",
        "Website field",
        "public dashboard entrypoint",
        "Suggested description",
        "Suggested topics",
        "github-pages",
        "dry-run",
        "Repository -> About gear icon",
        "Project status remains controlled by repository files and review gates.",
    ]:
        assert phrase in text
