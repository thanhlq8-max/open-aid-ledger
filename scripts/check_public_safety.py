#!/usr/bin/env python3
"""Scan public repository text files for obvious unsafe disclosures.

This is a lightweight guardrail, not a full secret scanner. Use it together with
GitHub secret scanning and human review.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    "dist",
    "build",
}

TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".csv",
    ".json",
    ".yml",
    ".yaml",
    ".py",
    ".ps1",
    ".gitignore",
}

DANGEROUS_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----", re.IGNORECASE),
    re.compile(r"\b(seed phrase|mnemonic phrase)\b\s*[:=]", re.IGNORECASE),
    re.compile(r"\b(private key|secret key|api key|exchange key)\b\s*[:=]", re.IGNORECASE),
    re.compile(r"\b(password|passwd|pwd)\b\s*[:=]", re.IGNORECASE),
    re.compile(r"\b(buy now|sell now|entry now|guaranteed profit|risk[- ]free yield)\b", re.IGNORECASE),
]

ALLOWLIST_PHRASES = {
    "private keys",
    "private key",
    "seed phrases",
    "api keys",
    "exchange credentials",
    "guaranteed profitability",
}


def _should_scan(path: Path) -> bool:
    if any(part in SKIP_DIRS for part in path.parts):
        return False
    if path.name in {"LICENSE"}:
        return True
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name.startswith(".")


def _is_allowlisted_line(line: str) -> bool:
    lowered = line.lower()
    if any(phrase in lowered for phrase in ALLOWLIST_PHRASES):
        # Policy documents intentionally mention forbidden items. Only assignments
        # or key-like blocks should fail, handled by stricter patterns above.
        return not any(token in lowered for token in [":", "=", "-----begin"])
    return False


def scan(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(root.rglob("*")):
        if path.name in {"check_public_safety.py", "validate_static_status.py"}:
            continue
        if not path.is_file() or not _should_scan(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            if _is_allowlisted_line(line):
                continue
            for pattern in DANGEROUS_PATTERNS:
                if pattern.search(line):
                    errors.append(f"{path}:{line_no}: unsafe public content pattern: {pattern.pattern}")
                    break
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan repository for obvious unsafe public disclosures.")
    parser.add_argument("root", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()

    errors = scan(args.root.resolve())
    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1
    print("public safety scan OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
