from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_static_status_validator_passes() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/validate_static_status.py", "."],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    assert "static public status page OK" in result.stdout


def test_static_status_page_keeps_inactive_donation_boundary() -> None:
    text = (ROOT / "docs" / "index.md").read_text(encoding="utf-8")
    assert "DONATIONS_ACTIVE: NO" in text
    assert "WALLETS_PUBLISHED: NO" in text
    assert "RETURN_PROMISE: FORBIDDEN" in text
    assert "DONATIONS_ACTIVE: YES" not in text
    assert "WALLETS_PUBLISHED: YES" not in text
