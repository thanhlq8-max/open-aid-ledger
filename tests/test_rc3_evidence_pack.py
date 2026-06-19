from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_rc3_validator_passes_repository_root():
    result = subprocess.run(
        [sys.executable, "scripts/validate_rc3.py", "."],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout


def test_rc3_dry_run_flags_remain_inactive():
    data = json.loads((ROOT / "examples/dry-run/rc3-evidence-pack.example.json").read_text(encoding="utf-8"))
    assert data["donations_active"] is False
    assert data["wallets_published"] is False
    assert data["activation_approved"] is False
    assert data["decision"]["activation_decision"] == "BLOCKED"


def test_rc3_docs_do_not_publish_wallets():
    text = (ROOT / "docs/RC3_EXTERNAL_REVIEW_EVIDENCE_PACK.md").read_text(encoding="utf-8")
    assert "RC3 does not activate donations" in text
    assert "WALLETS_PUBLISHED: NO" in text
