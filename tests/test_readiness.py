import json
from pathlib import Path

from scripts.validate_readiness import validate


def test_readiness_validator_passes_repository_root():
    result = validate(Path("."))
    assert result["status"] == "PASS"
    assert result["donations_active"] == "NO"
    assert result["wallets_published"] == "NO"


def test_dry_run_wallet_example_is_inactive():
    data = json.loads(Path("examples/dry-run/wallets.dry-run.example.json").read_text(encoding="utf-8"))
    assert data["dry_run_only"] is True
    assert data["donations_active"] is False
    assert data["wallets_published"] is False
    assert data["wallets"][0]["status"] == "placeholder"


def test_readiness_docs_keep_no_transfer_boundary():
    text = Path("docs/DONATION_READINESS_DRY_RUN.md").read_text(encoding="utf-8").lower()
    assert "does not activate donations" in text
    assert "sign transactions" in text
    assert "move assets" in text
    assert "private-key management" in text
