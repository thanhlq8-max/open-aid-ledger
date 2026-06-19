from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_rc2_validator_passes_repository_root():
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "scripts/validate_rc2.py", "."],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_rc2_documents_keep_donation_inactive():
    root = Path(__file__).resolve().parents[1]
    text = (root / "docs/RC2_EXTERNAL_REVIEW_ACTIVATION_GATE.md").read_text(encoding="utf-8")
    assert "DONATIONS_ACTIVE: NO" in text
    assert "WALLETS_PUBLISHED: NO" in text
    assert "ACTIVATION_APPROVED: NO" in text
