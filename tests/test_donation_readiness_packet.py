from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "docs" / "DONATION_READINESS_REVIEW_PACKET.md"


def read_packet() -> str:
    return PACKET.read_text(encoding="utf-8")


def test_donation_readiness_packet_exists() -> None:
    assert PACKET.is_file()


def test_donation_readiness_packet_preserves_not_ready_status() -> None:
    text = read_packet()
    for phrase in [
        "Donation Readiness Review Packet",
        "DONATION_READINESS: NOT_READY",
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "GO_LIVE: NO",
    ]:
        assert phrase in text


def test_donation_readiness_packet_tracks_required_blockers() -> None:
    text = read_packet()
    for phrase in [
        "RECEIVING_CHANNEL_PUBLICATION: BLOCKED",
        "ACCOUNT_PROTECTION_REVIEW: REQUIRED",
        "LEGAL_TAX_REVIEW: REQUIRED",
        "WALLET_INVENTORY: PLACEHOLDER_ONLY",
        "ACTIVATION_COMMIT: NOT_PREPARED",
        "IF any blocker remains:",
        "GO_LIVE = NO",
    ]:
        assert phrase in text
