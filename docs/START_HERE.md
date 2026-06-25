# Start Here

This is the operating cockpit for Open Aid Ledger.

Current status:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

Do not send support while this status remains inactive.

## Use this flow

```text
1. Donor checks public status.
2. Maintainer runs dry-run operation.
3. Reviewer checks evidence and blockers.
4. Maintainer fixes blockers.
5. CI and public-safety checks pass.
6. Go-live is considered only in a separate reviewed proposal.
```

## Donor path

Read only these first:

```text
docs/index.md
docs/DONOR_QUICKSTART.md
docs/DONOR_FAQ.md
```

Rule:

```text
IF DONATIONS_ACTIVE is NO OR WALLETS_PUBLISHED is NO:
    DO_NOT_SEND
```

Use receiving information only from the official public status page or an approved repository source linked from it.

## Maintainer path

Before any future operating proposal, run:

```text
docs/DRY_RUN_OPERATIONS_RUNBOOK.md
examples/dry-run/DRY_RUN_001_OPERATION_REPORT.sample.md
docs/REVIEW_PACKET_TEMPLATE.md
docs/OPERATIONAL_READINESS_MATRIX.md
```

Rule:

```text
IF any blocker remains:
    GO_LIVE = NO
```

## Reviewer path

Check only what affects go/no-go:

```text
public status clarity
donor source-of-truth
receiving-channel control
account protection
beneficiary privacy
ledger and report reproducibility
freeze process
CI result
```

## Current go/no-go

```text
DONOR_ENTRYPOINT_READY: YES
DRY_RUN_READY: YES
REVIEW_PACKET_READY: YES
RECEIVING_CHANNEL_PUBLICATION: BLOCKED
DONATION_ACTIVATION: BLOCKED
GO_LIVE: NO
```

## Detailed docs

Use detailed docs only when the flow above points to them.
