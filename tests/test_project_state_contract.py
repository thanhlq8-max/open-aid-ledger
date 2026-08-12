from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_STATE = ROOT / "PROJECT_STATE.md"
RELEASE_TAG_TARGET = "21b341c50d8e2277eda4134c66bd2ea3155a816e"


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


def test_project_state_records_verified_release() -> None:
    text = PROJECT_STATE.read_text(encoding="utf-8")
    for token in [
        "STATUS: ACTIVE_RELEASED_PUBLIC_TEMPLATE",
        "RELEASE_STATUS: RELEASED",
        f"RELEASE_TAG_TARGET: {RELEASE_TAG_TARGET}",
        "RELEASE_TAG_CREATED: YES",
        "GITHUB_RELEASE_CREATED: YES",
        "TAG_VALIDATE: VALIDATE_148_PASS",
    ]:
        assert token in text


def test_project_state_does_not_regress_to_pre_release_gate() -> None:
    text = PROJECT_STATE.read_text(encoding="utf-8")
    for stale in [
        "RELEASE_TAG_TARGET: NOT_SELECTED",
        "FINAL_CI_EVIDENCE: NOT_ATTACHED",
        "FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PENDING_FINAL_TARGET",
        "TAGGING_STATUS: BLOCKED",
        "RELEASE_TAG_CREATED: NO",
        "GITHUB_RELEASE_CREATED: NOT_VERIFIED",
    ]:
        assert stale not in text
