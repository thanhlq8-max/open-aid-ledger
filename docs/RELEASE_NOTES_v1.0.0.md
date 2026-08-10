# Release Notes: v1.0.0

Status: release-candidate closeout. Tagging is blocked until the exact final release target is selected and freshly validated.

## Release summary

Open Aid Ledger v1.0.0 is planned as a public repository/template release for transparent status dashboards, review packets, dry-run evidence, and safety-first operating controls.

This planned release does not activate collection, publish receiving details, or approve live operation.

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
- Public status recheck workflow.
- Release validation evidence index.
- Release tagging runbook.
- Public-safety scanner hardening.
- Immutable GitHub Actions pinning with regression coverage.

## Current release evidence

```text
RELEASE_TARGET: v1.0.0
RELEASE_STATUS: FINAL_VALIDATION_PENDING
RELEASE_TAG_TARGET: NOT_SELECTED
FINAL_CI_EVIDENCE: NOT_ATTACHED
RELEASE_TAG_CREATED: NO
GITHUB_RELEASE_CREATED: NO
LIVE_OPERATION: NO
```

Historical validation records are indexed in `docs/RELEASE_VALIDATION_EVIDENCE_v1.0.0.md`. Historical runs are not final evidence for the future release tag target.

## Validation required before tagging

Run the complete repository validation on the exact final intended release commit, including:

```powershell
python -m compileall scripts tests
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_campaigns.py campaigns\campaigns.example.json --allow-inactive-template
python scripts\validate_readiness.py .
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --enforce-balance
python scripts\validate_ledger.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --enforce-balance
python scripts\validate_static_status.py .
python scripts\validate_release_consistency.py .
python scripts\validate_candidate.py .
python scripts\validate_rc1.py .
python scripts\validate_rc2.py .
python scripts\validate_rc3.py .
python scripts\check_public_safety.py .
python -m pytest -q
```

The exact final intended commit must also have fresh GitHub Actions validation evidence. Any required Pages runtime evidence must be attached before release readiness is claimed.

## Release gate

Tagging remains blocked until all of the following are true:

1. the exact final release target is selected;
2. the release identity transition is complete and internally consistent;
3. fresh complete validation passes on that exact target;
4. final public-status and Pages evidence requirements are satisfied;
5. the maintainer gives explicit final tag approval.

Use `docs/RELEASE_TAGGING_RUNBOOK_v1.0.0.md` only after those gates are satisfied.
