from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_URL = "https://thanhlq8-max.github.io/open-aid-ledger/"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_quick_access_page_exists_and_is_visible_from_readme() -> None:
    assert (ROOT / "docs" / "QUICK_ACCESS.md").is_file()
    assert "docs/QUICK_ACCESS.md" in read("README.md")


def test_quick_access_keeps_shortest_user_paths() -> None:
    text = read("docs/QUICK_ACCESS.md")
    for phrase in [
        "Quick Access",
        PUBLIC_URL,
        "One-minute map",
        "docs/index.md",
        "docs/DONOR_QUICKSTART.md",
        "docs/DONOR_FAQ.md",
        "examples/dry-run/README.md",
        "docs/REVIEW_PACKET_TEMPLATE.md",
        "docs/OPERATIONAL_READINESS_MATRIX.md",
        "Share card",
        "Status: public template, not live operation",
    ]:
        assert phrase in text


def test_quick_access_preserves_inactive_status() -> None:
    text = read("docs/QUICK_ACCESS.md")
    for phrase in [
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "GO_LIVE: NO",
    ]:
        assert phrase in text
