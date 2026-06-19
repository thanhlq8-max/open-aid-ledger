from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_release_closeout_documents_exist() -> None:
    required = [
        "docs/RELEASE_CLOSEOUT.md",
        "docs/INITIAL_ISSUE_COMPLETION_MAP.md",
        "docs/ISSUE_CLOSEOUT_COMMENTS.md",
        "docs/GITHUB_RELEASE_v0.7.0_DRAFT.md",
        "RELEASE_NOTES_v0.7.0.md",
    ]
    for path in required:
        assert (ROOT / path).exists(), path


def test_initial_issue_completion_map_mentions_all_seed_issues() -> None:
    body = read("docs/INITIAL_ISSUE_COMPLETION_MAP.md")
    for number in range(1, 7):
        assert f"#{number}" in body
    for version in ["v0.2.0", "v0.3.0", "v0.4.0", "v0.5.0"]:
        assert version in body


def test_issue_closeout_comments_are_copy_ready() -> None:
    body = read("docs/ISSUE_CLOSEOUT_COMMENTS.md")
    for number in range(1, 7):
        assert f"Issue #{number}" in body
        assert "This issue can be closed as completed." in body


def test_release_closeout_keeps_donation_inactive_guardrails() -> None:
    combined = "\n".join(
        read(path)
        for path in [
            "docs/RELEASE_CLOSEOUT.md",
            "docs/GITHUB_RELEASE_v0.7.0_DRAFT.md",
            "RELEASE_NOTES_v0.7.0.md",
        ]
    )
    assert "DONATIONS_ACTIVE: NO" in combined
    assert "WALLETS_PUBLISHED: NO" in combined
    assert "CUSTODY_AUTOMATION: NO" in combined
    assert "TRADING_USE: FORBIDDEN" in combined
    assert "RETURN_PROMISE: FORBIDDEN" in combined
