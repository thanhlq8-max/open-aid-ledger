from __future__ import annotations

from pathlib import Path

from scripts.check_public_safety import scan


def test_public_safety_scan_passes_clean_file(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("No trading. No custody automation.\n", encoding="utf-8")
    assert scan(tmp_path) == []


def test_public_safety_scan_flags_unsafe_assignment(tmp_path: Path) -> None:
    token = "password" + ": hunter2\n"
    (tmp_path / "unsafe.txt").write_text(token, encoding="utf-8")
    errors = scan(tmp_path)
    assert errors

