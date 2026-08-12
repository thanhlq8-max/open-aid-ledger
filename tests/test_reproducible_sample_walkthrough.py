from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WALKTHROUGH = ROOT / "docs" / "REPRODUCIBLE_SAMPLE_WALKTHROUGH.md"


def test_reproducible_sample_walkthrough_exists() -> None:
    assert WALKTHROUGH.is_file()


def test_reproducible_sample_walkthrough_contract() -> None:
    text = WALKTHROUGH.read_text(encoding="utf-8")
    for token in [
        "examples\\sample-ledger\\donations.csv",
        "examples\\sample-ledger\\disbursements.csv",
        "scripts\\validate_ledger.py",
        "scripts\\generate_report.py",
        "ledger CSV files OK",
        "Donation records: 3",
        "Disbursement records: 2",
        "| Bitcoin | BTC | Bitcoin | 0.0125 |",
        "| Ethereum | USDT | ERC20 | 125 | 60 | 65 |",
        "| Tron | USDT | TRC20 | 80 | 40 | 40 |",
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "CUSTODY_AUTOMATION: NO",
        "GO_LIVE: NO",
    ]:
        assert token in text


def test_public_front_doors_link_walkthrough() -> None:
    for relative in ["README.md", "docs/index.md"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        assert "REPRODUCIBLE_SAMPLE_WALKTHROUGH.md" in text, relative
