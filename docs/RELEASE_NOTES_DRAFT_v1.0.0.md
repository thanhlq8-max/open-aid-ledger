# Release Notes Draft: v1.0.0

Status: draft. Do not tag until final validation evidence is attached.

## Release summary

Open Aid Ledger v1.0.0 prepares a public template for transparent status dashboards, review packets, dry-run evidence, and safety-first operating controls.

This release is an inactive repository/template release. It does not activate collection, publish receiving details, or approve live operation.

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
- Regression tests for key public files.

## Validation required before tag

```powershell
python -m compileall scripts tests
python scripts\check_public_safety.py .
python -m pytest -q
```

Attach the final GitHub Actions run result before creating the release.

## Release status

```text
RELEASE_STATUS: DRAFT
RELEASE_TAG_CREATED: NO
LIVE_OPERATION: NO
```
