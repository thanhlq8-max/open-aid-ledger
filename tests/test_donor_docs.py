from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_donor_docs_exist() -> None:
    for path in [
        "index.md",
        "docs/START_HERE.md",
        "docs/DONOR_QUICKSTART.md",
        "docs/DONOR_FAQ.md",
    ]:
        assert (ROOT / path).is_file(), path


def test_pages_landing_page_links_public_dashboard_and_preserves_status() -> None:
    text = read("index.md")
    for phrase in [
        "Open Aid Ledger",
        "Public dashboard",
        "[Open the public dashboard](docs/index.md)",
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "GO_LIVE: NO",
        "docs/START_HERE.md",
        "docs/DONOR_QUICKSTART.md",
        "examples/dry-run/README.md",
        "documentation-only",
    ]:
        assert phrase in text


def test_start_here_keeps_operating_cockpit() -> None:
    text = read("docs/START_HERE.md")
    for phrase in [
        "This is the operating cockpit",
        "EASY_TO_ACCESS: YES",
        "EASY_TO_USE: YES",
        "EASY_TO_SHARE: YES",
        "USER_DASHBOARD: YES",
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "Donor path",
        "Maintainer path",
        "Reviewer path",
        "dry-run evidence loop",
        "examples/dry-run/README.md",
        "examples/dry-run/DRY_RUN_001_REVIEW_PACKET.sample.md",
        "IF DONATIONS_ACTIVE is NO OR WALLETS_PUBLISHED is NO:",
        "IF any blocker remains:",
        "DRY_RUN_EVIDENCE_LOOP_READY: YES",
        "DASHBOARD_READY: YES",
        "RECEIVING_CHANNEL_PUBLICATION: BLOCKED",
        "DONATION_ACTIVATION: BLOCKED",
        "GO_LIVE: NO",
    ]:
        assert phrase in text


def test_dashboard_keeps_user_goals_and_shareable_snapshot() -> None:
    text = read("docs/index.md")
    for phrase in [
        "Open Aid Ledger public dashboard",
        "EASY_TO_ACCESS: YES",
        "EASY_TO_USE: YES",
        "EASY_TO_SHARE: YES",
        "USER_DASHBOARD: YES",
        "Shareable status snapshot",
        "Official dashboard: docs/index.md",
        "Start here: docs/START_HERE.md",
        "Dry-run evidence loop: examples/dry-run/README.md",
        "Donation activation | BLOCKED",
        "Custody automation | FORBIDDEN",
    ]:
        assert phrase in text


def test_dashboard_keeps_one_screen_operating_board() -> None:
    text = read("docs/index.md")
    for phrase in [
        "One-screen operating board",
        "Role | Next action | Use this file | Done when",
        "Donor | Check current status before sending.",
        "Maintainer | Run the dry-run evidence loop with sample data.",
        "examples/dry-run/README.md",
        "Reviewer | Check evidence and unresolved blockers.",
        "Current blockers",
        "RECEIVING_CHANNEL_PUBLICATION: BLOCKED",
        "DONATION_ACTIVATION: BLOCKED",
        "GO_LIVE: NO",
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
    assert "[Dry-run Evidence Loop](../examples/dry-run/README.md)" in text
    assert "If the public status still says `DONATIONS_ACTIVE: NO`" in text
