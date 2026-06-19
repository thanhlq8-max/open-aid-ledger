from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_importer_design_docs_exist() -> None:
    for path in [
        "docs/BLOCKCHAIN_EXPLORER_IMPORTER_DESIGN.md",
        "docs/IMPORTER_NORMALIZED_TX_SCHEMA.md",
        "docs/IMPORTER_MANUAL_RECONCILIATION.md",
        "examples/importer/normalized_transactions.sample.csv",
    ]:
        assert (ROOT / path).exists(), path


def test_importer_design_keeps_read_only_guardrails() -> None:
    content = read("docs/BLOCKCHAIN_EXPLORER_IMPORTER_DESIGN.md").lower()

    required_phrases = [
        "read-only",
        "must not",
        "private keys",
        "seed phrases",
        "sign transactions",
        "transfer assets",
        "exchange",
        "must not directly modify",
        "ledger/donations.csv",
    ]

    for phrase in required_phrases:
        assert phrase in content


def test_importer_schema_defaults_to_manual_review() -> None:
    content = read("docs/IMPORTER_NORMALIZED_TX_SCHEMA.md").lower()

    assert "review-only" in content
    assert "pending_review" in content
    assert "must not default to `accepted`" in content
    assert "must not be used for active donation operations" in content


def test_manual_reconciliation_forbids_direct_ledger_writes() -> None:
    content = read("docs/IMPORTER_MANUAL_RECONCILIATION.md").lower()

    assert "manually copied" in content
    assert "must never directly write production ledger rows" in content
    assert "no part of this workflow requires" in content
