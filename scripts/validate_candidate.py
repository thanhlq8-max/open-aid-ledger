#!/usr/bin/env python3
"""Validate pre-1.0 candidate review materials.

This script is read-only. It validates documentation and status files only.
It does not access networks, wallets, exchanges, or account systems.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT_REQUIRED = {
    "README.md": [
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "CUSTODY_AUTOMATION: NO",
        "TRADING_USE: FORBIDDEN",
        "RETURN_PROMISE: FORBIDDEN",
    ],
    "VERSION": ["0.10.0-pre-1.0-candidate-review"],
    "RELEASE_NOTES_v0.10.0.md": ["Donation-ready candidate review", "DONATIONS_ACTIVE: NO"],
}

DOC_REQUIRED = {
    "docs/PRE_1_0_DONATION_READY_CANDIDATE_REVIEW.md": [
        "DONATIONS_ACTIVE: NO",
        "WALLETS_PUBLISHED: NO",
        "PASS_FOR_DONATION_READY_CANDIDATE",
    ],
    "docs/DONATION_READY_CANDIDATE_CHECKLIST.md": [
        "CANDIDATE_STATUS: PENDING_REVIEW",
        "DONATIONS_ACTIVE: NO",
    ],
    "docs/EXTERNAL_REVIEW_REQUEST_TEMPLATE.md": ["REVIEW_RESULT"],
    "docs/CANDIDATE_DECISION_RECORD.md": ["CDR-2026-001"],
    "docs/OPERATIONAL_RISK_ACCEPTANCE.md": ["BLOCKING"],
}


def _read(path: Path) -> str:
    if not path.exists():
        raise ValueError(f"missing required file: {path.as_posix()}")
    return path.read_text(encoding="utf-8")


def _require_contains(root: Path, mapping: dict[str, list[str]]) -> None:
    for rel, tokens in mapping.items():
        content = _read(root / rel)
        for token in tokens:
            if token not in content:
                raise ValueError(f"{rel} missing token: {token}")


def _validate_candidate_json(root: Path) -> None:
    path = root / "examples/dry-run/candidate-review.example.json"
    data = json.loads(_read(path))
    if data.get("donations_active") is not False:
        raise ValueError("candidate review example must keep donations inactive")
    if data.get("wallets_published") is not False:
        raise ValueError("candidate review example must keep wallets unpublished")
    if data.get("candidate_status") != "PENDING_REVIEW":
        raise ValueError("candidate status must remain PENDING_REVIEW")
    required_reviews = data.get("required_reviews")
    if not isinstance(required_reviews, list) or len(required_reviews) < 5:
        raise ValueError("candidate review example must list review areas")


def validate(root: Path) -> None:
    _require_contains(root, ROOT_REQUIRED)
    _require_contains(root, DOC_REQUIRED)
    _validate_candidate_json(root)


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    try:
        validate(root.resolve())
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print("pre-1.0 candidate review: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
