from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_URL = "https://thanhlq8-max.github.io/open-aid-ledger/"
REPO_URL = "https://github.com/thanhlq8-max/open-aid-ledger"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_share_kit_exists_and_is_visible_from_readme() -> None:
    assert (ROOT / "docs" / "SHARE_KIT.md").is_file()
    assert "docs/SHARE_KIT.md" in read("README.md")


def test_share_kit_keeps_public_links_and_tags() -> None:
    text = read("docs/SHARE_KIT.md")
    for phrase in [
        "Share Kit",
        PUBLIC_URL,
        REPO_URL,
        "docs/QUICK_ACCESS.md",
        "One-line description",
        "public-dashboard",
        "dry-run",
        "governance",
    ]:
        assert phrase in text
