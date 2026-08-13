from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_report import generate_report  # noqa: E402


PUBLIC_REPORT = ROOT / "docs" / "SAMPLE_TRANSPARENCY_REPORT.md"
DONATIONS = ROOT / "examples" / "sample-ledger" / "donations.csv"
DISBURSEMENTS = ROOT / "examples" / "sample-ledger" / "disbursements.csv"
TITLE = "Open Aid Ledger Sample Transparency Report"


def test_public_sample_report_matches_generator() -> None:
    expected = generate_report(DONATIONS, DISBURSEMENTS, title=TITLE)
    actual = PUBLIC_REPORT.read_text(encoding="utf-8")
    assert actual == expected


def test_public_sample_report_is_linked_from_human_front_doors() -> None:
    for relative in ["README.md", "docs/index.md", "docs/REPRODUCIBLE_SAMPLE_WALKTHROUGH.md"]:
        text = (ROOT / relative).read_text(encoding="utf-8")
        assert "SAMPLE_TRANSPARENCY_REPORT.md" in text, relative
