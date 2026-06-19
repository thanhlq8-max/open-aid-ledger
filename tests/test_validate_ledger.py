from __future__ import annotations

from pathlib import Path

from scripts.validate_ledger import DONATION_COLUMNS, DISBURSEMENT_COLUMNS, validate


def _write_csv(path: Path, columns: list[str], rows: list[dict[str, str]]) -> None:
    lines = [",".join(columns)]
    for row in rows:
        lines.append(",".join(row.get(col, "") for col in columns))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_empty_ledgers_pass(tmp_path: Path) -> None:
    donations = tmp_path / "donations.csv"
    disbursements = tmp_path / "disbursements.csv"
    _write_csv(donations, DONATION_COLUMNS, [])
    _write_csv(disbursements, DISBURSEMENT_COLUMNS, [])
    assert validate(donations, disbursements) == []


def test_invalid_amount_fails(tmp_path: Path) -> None:
    donations = tmp_path / "donations.csv"
    disbursements = tmp_path / "disbursements.csv"
    _write_csv(
        donations,
        DONATION_COLUMNS,
        [
            {
                "date_utc": "2026-06-19",
                "campaign_id": "community-hardship-2026",
                "chain": "bitcoin",
                "asset": "BTC",
                "network": "mainnet",
                "amount": "0",
                "tx_hash": "abc123456789",
                "donor_label": "anonymous",
                "source_note": "public chain record",
                "status": "confirmed",
            }
        ],
    )
    _write_csv(disbursements, DISBURSEMENT_COLUMNS, [])
    errors = validate(donations, disbursements)
    assert any("amount must be > 0" in err for err in errors)


def test_duplicate_tx_hash_fails(tmp_path: Path) -> None:
    donations = tmp_path / "donations.csv"
    disbursements = tmp_path / "disbursements.csv"
    row = {
        "date_utc": "2026-06-19",
        "campaign_id": "community-hardship-2026",
        "chain": "bitcoin",
        "asset": "BTC",
        "network": "mainnet",
        "amount": "0.01",
        "tx_hash": "abcdef1234567890",
        "donor_label": "anonymous",
        "source_note": "public chain record",
        "status": "confirmed",
    }
    _write_csv(donations, DONATION_COLUMNS, [row, row])
    _write_csv(disbursements, DISBURSEMENT_COLUMNS, [])
    errors = validate(donations, disbursements)
    assert any("duplicate tx_hash" in err for err in errors)


def test_enforce_balance_fails_when_outgoing_exceeds_incoming(tmp_path: Path) -> None:
    donations = tmp_path / "donations.csv"
    disbursements = tmp_path / "disbursements.csv"
    _write_csv(
        donations,
        DONATION_COLUMNS,
        [
            {
                "date_utc": "2026-06-19",
                "campaign_id": "community-hardship-2026",
                "chain": "bitcoin",
                "asset": "BTC",
                "network": "mainnet",
                "amount": "0.01",
                "tx_hash": "donationtx123456",
                "donor_label": "anonymous",
                "source_note": "public chain record",
                "status": "confirmed",
            }
        ],
    )
    _write_csv(
        disbursements,
        DISBURSEMENT_COLUMNS,
        [
            {
                "date_utc": "2026-06-20",
                "campaign_id": "community-hardship-2026",
                "beneficiary_code": "BEN-001",
                "category": "hardship",
                "chain": "bitcoin",
                "asset": "BTC",
                "network": "mainnet",
                "amount": "0.02",
                "tx_hash": "spendtx123456789",
                "purpose": "redacted support",
                "evidence_ref": "redacted-evidence-001",
                "approval_ref": "approval-001",
                "status": "reported",
                "privacy_level": "public_redacted",
            }
        ],
    )
    errors = validate(donations, disbursements, enforce_balance=True)
    assert any("disbursements exceed donations" in err for err in errors)

