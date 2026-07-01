from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_donation_readiness_packet_is_linked_from_readme() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "docs/DONATION_READINESS_REVIEW_PACKET.md" in readme
