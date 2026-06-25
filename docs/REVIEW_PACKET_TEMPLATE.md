# Review Packet Template

This template helps maintainers prepare a review packet before any future operating proposal.

Current status:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

This template is documentation-only. It does not change project status.

## Purpose

A review packet should make the project easy to inspect from repository evidence.

The packet should show:

- current status;
- validation evidence;
- dry-run evidence;
- unresolved blockers;
- reviewer notes;
- next actions.

## Packet metadata

```text
PACKET_ID:
DATE:
REPOSITORY_COMMIT:
PREPARED_BY:
REVIEW_SCOPE:
STATUS:
```

## Evidence index

| Area | Repository reference | Status | Notes |
|---|---|---:|---|
| Public status | `docs/index.md` |  |  |
| Activation checklist | `docs/DONATION_ACTIVATION_CHECKLIST.md` |  |  |
| Operational readiness | `docs/OPERATIONAL_READINESS_MATRIX.md` |  |  |
| Dry-run runbook | `docs/DRY_RUN_OPERATIONS_RUNBOOK.md` |  |  |
| Donor trust guide | `docs/DONOR_TRUST_GUIDE.md` |  |  |
| Receiving channel policy | `docs/RECEIVING_CHANNEL_PUBLICATION_POLICY.md` |  |  |
| Account protection checklist | `docs/RECEIVING_ACCOUNT_PROTECTION.md` |  |  |
| Beneficiary privacy policy | `BENEFICIARY_PRIVACY_POLICY.md` |  |  |
| Public summary checklist | `docs/PUBLIC_SUMMARY_CHECKLIST.md` |  |  |
| Ledger validation | `scripts/validate_ledger.py` |  |  |
| Campaign validation | `scripts/validate_campaigns.py` |  |  |
| Public safety scan | `scripts/check_public_safety.py` |  |  |
| Latest CI run | GitHub Actions Validate |  |  |

## Reviewer note template

```text
REVIEW_ID:
REVIEWER_ROLE:
DATE:
SCOPE:
DECISION: PASS | PASS_WITH_NOTES | BLOCKED | OUT_OF_SCOPE
SUMMARY:
FINDINGS:
BLOCKERS:
RECOMMENDATIONS:
```

## Evidence quality checklist

- [ ] The packet references a commit or pull request.
- [ ] The packet uses repository files where possible.
- [ ] The packet clearly labels sample-only and dry-run-only evidence.
- [ ] The packet records unresolved blockers.
- [ ] The packet does not change project status.
- [ ] The packet does not imply go-live approval.

## Blocker handling

If an area is marked `BLOCKED`:

1. create or update a tracked task;
2. fix only the blocked scope;
3. run validation;
4. update the packet with the new evidence;
5. keep project status inactive until a separate reviewed proposal changes it.

## Maintainer note

This packet is an operating-control template. It is not legal, tax, security, privacy, accounting, or financial advice.
