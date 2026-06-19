from pathlib import Path
import importlib.util


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_rc1", ROOT / "scripts" / "validate_rc1.py")
validate_rc1 = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(validate_rc1)


def test_rc1_required_files_exist():
    for rel in validate_rc1.REQUIRED_FILES:
        assert (ROOT / rel).exists(), rel


def test_rc1_readme_markers_exist():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for marker in validate_rc1.REQUIRED_README_MARKERS:
        assert marker in readme


def test_rc1_metadata_is_inactive():
    import json
    data = json.loads((ROOT / "examples/dry-run/rc1-candidate.example.json").read_text(encoding="utf-8"))
    assert data["candidate"] == "v1.0.0-rc1"
    assert data["donations_active"] is False
    assert data["wallets_published"] is False
    assert data["custody_automation"] is False
    assert data["transfer_automation"] is False
