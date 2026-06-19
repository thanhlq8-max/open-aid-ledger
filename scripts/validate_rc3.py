#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

VERSION_TOKEN = "1.0.0-rc3"
REQUIRED_FILES = [
    "docs/RC3_EXTERNAL_REVIEW_EVIDENCE_PACK.md",
    "docs/EXTERNAL_REVIEW_FEEDBACK_REGISTER.md",
    "docs/REVIEW_EVIDENCE_ACCEPTANCE_CRITERIA.md",
    "docs/RC3_ACTIVATION_DECISION_PACKET.md",
    "docs/RC3_NON_ACTIVATION_NOTICE.md",
    "examples/dry-run/rc3-evidence-pack.example.json",
]
REQUIRED_README_MARKERS = [
    "DONATIONS_ACTIVE: NO",
    "WALLETS_PUBLISHED: NO",
    "CUSTODY_AUTOMATION: NO",
    "TRADING_USE: FORBIDDEN",
    "RETURN_PROMISE: FORBIDDEN",
]
REQUIRED_DOC_MARKERS = [
    "DONATIONS_ACTIVE: NO",
    "WALLETS_PUBLISHED: NO",
    "ACTIVATION_APPROVED: NO",
    "RC3 does not activate donations",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.as_posix()}")
    return path.read_text(encoding="utf-8")


def validate(root: Path) -> None:
    version = read_text(root / "VERSION").strip()
    if VERSION_TOKEN not in version:
        fail(f"VERSION missing token: {VERSION_TOKEN}")

    readme = read_text(root / "README.md")
    for marker in REQUIRED_README_MARKERS:
        if marker not in readme:
            fail(f"README missing marker: {marker}")

    for relative in REQUIRED_FILES:
        text = read_text(root / relative)
        if relative.endswith(".md"):
            if "private key:" in text.lower() or "seed phrase:" in text.lower():
                fail(f"unsafe secret-like wording in {relative}")

    rc3_doc = read_text(root / "docs/RC3_EXTERNAL_REVIEW_EVIDENCE_PACK.md")
    for marker in REQUIRED_DOC_MARKERS:
        if marker not in rc3_doc:
            fail(f"RC3 evidence pack missing marker: {marker}")

    example = json.loads(read_text(root / "examples/dry-run/rc3-evidence-pack.example.json"))
    if example.get("release_candidate") != "1.0.0-rc3":
        fail("rc3 example release_candidate mismatch")
    for key in ("donations_active", "wallets_published", "activation_approved"):
        if example.get(key) is not False:
            fail(f"rc3 example must keep {key}=false")
    decision = example.get("decision", {})
    if decision.get("activation_decision") != "BLOCKED":
        fail("rc3 example decision must be BLOCKED")
    evidence_items = example.get("evidence_items")
    if not isinstance(evidence_items, list) or not evidence_items:
        fail("rc3 example needs at least one evidence item")


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    validate(root.resolve())
    print("rc3 external review evidence pack: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
