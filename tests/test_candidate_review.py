from pathlib import Path
import subprocess
import sys


def test_candidate_validator_passes_repository_root():
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "scripts/validate_candidate.py", "."],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    assert "pre-1.0 candidate review: PASS" in result.stdout


def test_candidate_review_docs_keep_inactive_status():
    root = Path(__file__).resolve().parents[1]
    docs = [
        root / "docs/PRE_1_0_DONATION_READY_CANDIDATE_REVIEW.md",
        root / "docs/DONATION_READY_CANDIDATE_CHECKLIST.md",
    ]
    for path in docs:
        content = path.read_text(encoding="utf-8")
        assert "DONATIONS_ACTIVE: NO" in content
        assert "WALLETS_PUBLISHED: NO" in content
