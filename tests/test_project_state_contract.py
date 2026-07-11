from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_STATE = ROOT / "PROJECT_STATE.md"


def test_project_state_contract_exists() -> None:
    assert PROJECT_STATE.is_file()


def test_project_state_preserves_core_locks() -> None:
    text = PROJECT_STATE.read_text(encoding="utf-8")
    for token in [
        "PROJECT_STATUS: PUBLIC_TEMPLATE",
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "ACTIVATION_APPROVED: NO",
        "CUSTODY_AUTOMATION: NO",
        "TRADING_USE: FORBIDDEN",
        "RETURN_PROMISE: FORBIDDEN",
        "GO_LIVE: NO",
    ]:
        assert token in text


def test_project_state_blocks_unverified_release_claim() -> None:
    text = PROJECT_STATE.read_text(encoding="utf-8")
    assert "RELEASE_TAG_CREATED: NO" in text
    assert "RELEASE_STATUS: BLOCKED_FOR_CONSISTENCY_PATCHES" in text
