# Start Here

This is the shortest operating path for Open Aid Ledger.

Current status:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

Do not send support while this status remains inactive.

## One-page flow

Use this order:

```text
1. Donor reads Donor Quickstart.
2. Donor checks Public Status.
3. Maintainer runs dry-run operation.
4. Reviewer checks the review packet.
5. Blockers are fixed and validated.
6. Activation is considered only in a separate reviewed proposal.
```

## For donors

Read:

1. `docs/DONOR_QUICKSTART.md`
2. `docs/DONOR_FAQ.md`
3. `docs/index.md`

Donor rule:

```text
IF public status is inactive:
    DO_NOT_SEND
```

Only use receiving information from the official public status page or an approved repository source linked from it.

## For maintainers

Run this path before any future operating proposal:

1. `docs/DRY_RUN_OPERATIONS_RUNBOOK.md`
2. `examples/dry-run/DRY_RUN_001_OPERATION_REPORT.sample.md`
3. `docs/REVIEW_PACKET_TEMPLATE.md`
4. `docs/OPERATIONAL_READINESS_MATRIX.md`

Maintainer rule:

```text
IF any blocker remains:
    GO_LIVE = NO
```

## For reviewers

Check:

- public status is clear;
- donor instructions are simple;
- receiving-channel source is unambiguous;
- account protection is reviewed;
- privacy rules protect supported people;
- ledger and report process is reproducible;
- freeze process is documented;
- CI passes.

## What is intentionally not here

This page does not include every policy.

Use it as the front door. Use detailed docs only when the flow points to them.

## Current decision

```text
DONOR_ENTRYPOINT_READY: YES
DRY_RUN_READY: YES
REVIEW_PACKET_READY: YES
GO_LIVE: NO
```
