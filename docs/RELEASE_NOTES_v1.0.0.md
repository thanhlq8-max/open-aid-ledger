# Release Notes: v1.0.0

Status: ready for maintainer tagging approval.

## Release summary

Open Aid Ledger v1.0.0 is a public repository/template release for transparent status dashboards, review packets, dry-run evidence, and safety-first operating controls.

This release does not activate collection, publish receiving details, or approve live operation.

## Highlights

- Public dashboard entrypoint.
- Quick access guide.
- Share kit for consistent public links and descriptions.
- Dry-run evidence loop.
- Operational readiness matrix.
- Donation readiness review packet.
- Governance model draft.
- Account-protection review record.
- Legal/tax review status record.
- Scope review record.
- Active-mode donor guide draft.
- Reconciliation dry-run review.
- Freeze dry-run review.
- Two-reviewer approval rule.
- Official release readiness checklist.
- Public status recheck evidence.
- Final validation evidence.
- Release tagging runbook.
- Regression tests for key public files.

## Final validation evidence

```text
FINAL_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/77196823903
FINAL_RUN_LABEL: Validate #116
FINAL_COMMIT: 95f6424
VALIDATION_RESULT: PASS
```

## Validation checks

```powershell
python -m compileall scripts tests
python scripts\check_public_safety.py .
python -m pytest -q
```

Maintainer-provided log evidence shows public safety scan passed and pytest completed with `81 passed in 0.53s`.

## Release status

```text
RELEASE_STATUS: READY_FOR_TAGGING_REVIEW
RELEASE_TAG_CREATED: NO
GITHUB_RELEASE_CREATED: NO
LIVE_OPERATION: NO
```

## Manual tagging

Use `docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md` for the final manual tag and GitHub Release steps.
