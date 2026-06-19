from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_maintainer_governance_checklist_keeps_activation_gated():
    text = read("docs/MAINTAINER_GOVERNANCE_CHECKLIST.md")
    assert "DONATIONS_ACTIVE: NO" in text
    assert "WALLETS_PUBLISHED: NO" in text
    assert "Maintainer explicitly changes `DONATIONS_ACTIVE`" in text
    assert "private key handling" in text
    assert "return promises" in text


def test_donation_activation_checklist_requires_reviewed_activation_commit():
    text = read("docs/DONATION_ACTIVATION_CHECKLIST.md")
    assert "DONATIONS_ACTIVE: NO -> YES" in text
    assert "WALLETS_PUBLISHED: NO -> YES" in text
    assert "GitHub Actions validation passes" in text
    assert "No private keys or seed phrases" in text


def test_emergency_freeze_procedure_can_disable_donations():
    text = read("docs/EMERGENCY_FREEZE_PROCEDURE.md")
    assert "INCIDENT_STATUS: FROZEN" in text
    assert "DONATIONS_ACTIVE: NO" in text
    assert "wrong wallet address published" in text
    assert "beneficiary privacy leak" in text


def test_conflict_of_interest_template_blocks_trading_related_abuse():
    text = read("docs/CONFLICT_OF_INTEREST_DISCLOSURE_TEMPLATE.md")
    assert "Conflict-of-Interest Disclosure Template" in text
    assert "trading account top-up" in text
    assert "margin-call support" in text
    assert "return promises" in text


def test_governance_decision_record_preserves_guardrails():
    text = read("docs/GOVERNANCE_DECISION_RECORD.md")
    assert "activating donations" in text
    assert "publishing real wallet addresses" in text
    assert "NO_PRIVATE_KEYS" in text
    assert "NO_BENEFICIARY_DOXXING" in text
