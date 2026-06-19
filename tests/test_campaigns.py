from __future__ import annotations

import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_campaigns.py"
SAMPLE = ROOT / "campaigns" / "campaigns.example.json"


def run_validator(path: Path, *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(path), *extra],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


def write_json(tmp_path: Path, data: dict) -> Path:
    path = tmp_path / "campaigns.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


def load_sample() -> dict:
    return json.loads(SAMPLE.read_text(encoding="utf-8"))


def test_campaign_sample_passes() -> None:
    result = run_validator(SAMPLE, "--allow-inactive-template")
    assert result.returncode == 0, result.stderr
    assert "campaign metadata OK" in result.stdout


def test_missing_campaign_field_fails(tmp_path: Path) -> None:
    data = load_sample()
    del data["campaigns"][0]["purpose"]
    result = run_validator(write_json(tmp_path, data), "--allow-inactive-template")
    assert result.returncode != 0
    assert "missing fields" in result.stderr


def test_active_campaign_blocked_when_donations_inactive(tmp_path: Path) -> None:
    data = load_sample()
    data["campaigns"][0]["status"] = "active"
    data["campaigns"][0]["donation_activation_allowed"] = True
    result = run_validator(write_json(tmp_path, data), "--allow-inactive-template")
    assert result.returncode != 0
    assert "active campaigns are not allowed" in result.stderr


def test_invalid_campaign_id_fails(tmp_path: Path) -> None:
    data = load_sample()
    data["campaigns"][0]["campaign_id"] = "Invalid ID"
    result = run_validator(write_json(tmp_path, data), "--allow-inactive-template")
    assert result.returncode != 0
    assert "invalid format" in result.stderr


def test_forbidden_campaign_text_fails(tmp_path: Path) -> None:
    data = load_sample()
    data["campaigns"][0]["title"] = "Margin call support campaign"
    result = run_validator(write_json(tmp_path, data), "--allow-inactive-template")
    assert result.returncode != 0
    assert "forbidden wording" in result.stderr
