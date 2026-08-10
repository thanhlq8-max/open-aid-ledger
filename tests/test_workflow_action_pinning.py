from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOWS_DIR = ROOT / ".github" / "workflows"
REMOTE_USE_RE = re.compile(r"uses:\s*([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)@([^\s#]+)")
FULL_SHA_RE = re.compile(r"[0-9a-f]{40}")


def test_remote_workflow_actions_are_pinned_to_full_commit_shas() -> None:
    violations: list[str] = []
    remote_uses = 0

    for path in sorted(WORKFLOWS_DIR.glob("*.y*ml")):
        text = path.read_text(encoding="utf-8")
        for line_no, line in enumerate(text.splitlines(), start=1):
            match = REMOTE_USE_RE.search(line)
            if not match:
                continue

            remote_uses += 1
            action, ref = match.groups()
            if not FULL_SHA_RE.fullmatch(ref):
                violations.append(f"{path.relative_to(ROOT)}:{line_no}: {action}@{ref}")

    assert remote_uses > 0, "expected at least one remote workflow action"
    assert violations == [], "mutable workflow action refs found:\n" + "\n".join(violations)
