# Open Aid Ledger v1.0.0

Status: released repository/template baseline.

## Release summary

Open Aid Ledger v1.0.0 is the published public repository/template release for transparent status dashboards, review packets, dry-run evidence, and safety-first operating controls.

This release does not activate collection, publish receiving details, or approve live operation.

## Release evidence

```text
RELEASE_TARGET: v1.0.0
RELEASE_STATUS: RELEASED
RELEASE_TAG_TARGET: 21b341c50d8e2277eda4134c66bd2ea3155a816e
FINAL_CI_EVIDENCE: VALIDATE_147_ATTEMPT_2_PASS
FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PASS
PAGES_RUNTIME: PAGES_62_PASS
RELEASE_TAG_CREATED: YES
GITHUB_RELEASE_CREATED: YES
TAG_VALIDATE: VALIDATE_148_PASS
LIVE_OPERATION: NO
```

The exact release target is the merge commit for PR #28. Validate #147 attempt 2 passed on that exact commit before tagging. GitHub Pages run #62 built and deployed successfully on the same commit. The `v1.0.0` tag points to that commit, and tag-triggered Validate #148 passed after publication.

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

## Operating-status boundary

Repository release publication is separate from operating activation. The following locks remain unchanged:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
CUSTODY_AUTOMATION: NO
GO_LIVE: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

Do not send funds while `DONATIONS_ACTIVE` or `WALLETS_PUBLISHED` remains `NO`.

## Validation references

- Final exact-target validation: GitHub Actions `Validate` #147, attempt 2.
- GitHub Pages exact-target runtime: Pages #62.
- Tag-triggered validation: GitHub Actions `Validate` #148.
- Historical and final evidence index: `docs/RELEASE_VALIDATION_EVIDENCE_v1.0.0.md`.
- Final public-status evidence: `docs/PUBLIC_STATUS_RECHECK_v1.0.0.md`.

## Post-release work

Future repository changes should preserve the released `v1.0.0` record as history. New utility or adoption work belongs on `main` after review and does not alter the already-published tag target.
