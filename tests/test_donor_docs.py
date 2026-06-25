from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_donor_docs_exist() -> None:
    for path in [
        "docs/START_HERE.md",
        "docs/DONOR_QUICKSTART.md",
        "docs/DONOR_FAQ.md",
    ]:
        assert (ROOT / path).is_file(), path


def test_start_here_keeps_simple_front_door() -> None:
    text = read("docs/START_HERE.md")
    for phrase in [
        "This is the shortest operating path",
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "Donor reads Donor Quickstart.",
        "GO_LIVE = NO",
        "Use it as the front door.",
    ]:
        assert phrase in text


def test_donor_quickstart_preserves_inactive_status_and_safe_flow() -> None:
    text = read("docs/DONOR_QUICKSTART.md")
    for phrase in [
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "Do not send support while this status remains inactive.",
        "Confirm DONATIONS_ACTIVE is YES.",
        "Confirm WALLETS_PUBLISHED is YES.",
        "approved receiving channel",
        "Check the public ledger or report after reconciliation.",
    ]:
        assert phrase in text


def test_donor_faq_preserves_public_source_and_no_return_promise() -> None:
    text = read("docs/DONOR_FAQ.md")
    for phrase in [
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "Only from the official public status page",
        "Do not rely on private messages",
        "Wrong-network transfers may be delayed",
        "Open Aid Ledger is not an investment product",
        "Wait for a separate reviewed activation proposal",
    ]:
        assert phrase in text


def test_public_status_links_donor_entry_points() -> None:
    text = read("docs/index.md")
    assert "[Start Here](START_HERE.md)" in text
    assert "[Donor Quickstart](DONOR_QUICKSTART.md)" in text
    assert "[Donor FAQ](DONOR_FAQ.md)" in text
    assert "If the public status still says `DONATIONS_ACTIVE: NO`" in text
