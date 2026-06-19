from decimal import Decimal
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_report import generate_report  # noqa: E402


def _write_csv(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def test_generate_report_with_sample_rows(tmp_path: Path) -> None:
    donations = tmp_path / "donations.csv"
    disbursements = tmp_path / "disbursements.csv"

    _write_csv(
        donations,
        """record_id,campaign_id,received_utc,chain,asset,network,amount,tx_hash,source_type,donor_public_note,status,reviewed_by,review_note
DON-1,CAM-1,2026-06-01T00:00:00Z,Ethereum,USDT,ERC20,100,tx-in-1,community,note,confirmed,reviewer,ok
DON-2,CAM-1,2026-06-01T00:00:00Z,Ethereum,USDT,ERC20,25,tx-in-2,community,note,confirmed,reviewer,ok
""",
    )
    _write_csv(
        disbursements,
        """record_id,campaign_id,sent_utc,chain,asset,network,amount,tx_hash,beneficiary_ref,purpose,status,reviewed_by,review_note,privacy_level
DISB-1,CAM-1,2026-06-02T00:00:00Z,Ethereum,USDT,ERC20,40,tx-out-1,BEN-1,Hardship support,confirmed,reviewer,ok,redacted
""",
    )

    report = generate_report(donations, disbursements, title="Sample Report")

    assert "# Sample Report" in report
    assert "- Donation records: 2" in report
    assert "- Disbursement records: 1" in report
    assert "| Ethereum | USDT | ERC20 | 125 | 40 | 85 |" in report
    assert "No custody automation" in report


def test_generate_report_ignores_cancelled_rows(tmp_path: Path) -> None:
    donations = tmp_path / "donations.csv"
    disbursements = tmp_path / "disbursements.csv"

    _write_csv(
        donations,
        """record_id,campaign_id,received_utc,chain,asset,network,amount,tx_hash,source_type,donor_public_note,status,reviewed_by,review_note
DON-1,CAM-1,2026-06-01T00:00:00Z,Bitcoin,BTC,Bitcoin,1,tx-in-1,community,note,confirmed,reviewer,ok
DON-2,CAM-1,2026-06-01T00:00:00Z,Bitcoin,BTC,Bitcoin,9,tx-in-2,community,note,cancelled,reviewer,ok
""",
    )
    _write_csv(
        disbursements,
        """record_id,campaign_id,sent_utc,chain,asset,network,amount,tx_hash,beneficiary_ref,purpose,status,reviewed_by,review_note,privacy_level
""",
    )

    report = generate_report(donations, disbursements, title="Cancelled Rows")

    assert "| Bitcoin | BTC | Bitcoin | 1 |" in report
    assert "| Bitcoin | BTC | Bitcoin | 10 |" not in report
