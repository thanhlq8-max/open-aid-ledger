# Pre-1.0 Donation-Ready Candidate Review

This document defines the review gate before Open Aid Ledger can be considered donation-ready.

The project remains inactive during this release:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Purpose

The candidate review checks whether the repository has enough transparency, governance, validation, and public-safety controls to move toward a future donation-ready release.

This is not a launch approval. It is a structured review stage.

## Review areas

1. Wallet metadata schema and placeholder controls.
2. Ledger validation and balance checks.
3. Campaign lifecycle and inactive-template controls.
4. Public status page accuracy.
5. Read-only importer design boundaries.
6. Governance checklist completeness.
7. Beneficiary privacy controls.
8. Emergency freeze procedure readiness.
9. Public-safety scan behavior.
10. Release notes and issue closeout traceability.

## Candidate outcome

A candidate review may end with one of these outcomes:

```text
PASS_FOR_DONATION_READY_CANDIDATE
PASS_WITH_FOLLOW_UPS
BLOCKED_BY_SAFETY_GAP
BLOCKED_BY_GOVERNANCE_GAP
BLOCKED_BY_LEGAL_OR_TAX_REVIEW_GAP
```

Only a future reviewed commit may change `DONATIONS_ACTIVE` from `NO` to `YES`.
