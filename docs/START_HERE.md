# Start Here

Open Aid Ledger is a reusable template for making a support workflow easier to inspect: public status, ledger records, transparency reports, review evidence, and safety checks live in one repository.

**The project is not accepting donations right now. Do not send funds.**

## What do you want to do?

### I want to understand the project quickly

Start with the [public dashboard](index.md).

It explains what the project is, what is currently active, what is blocked, and where to go next.

### I want to see a working example

Open the [Reproducible Sample Walkthrough](REPRODUCIBLE_SAMPLE_WALKTHROUGH.md).

It uses fictional sample records. You can validate the ledger and generate a transparency report locally without connecting to a blockchain or using real funds.

### I may want to donate in the future

Read the [Donor Quickstart](DONOR_QUICKSTART.md) and [Donor FAQ](DONOR_FAQ.md).

For now, the answer is simple: **support collection is inactive and no receiving details are published.**

### I want to operate or adapt this template

Start with the [Dry-run Operations Runbook](DRY_RUN_OPERATIONS_RUNBOOK.md).

Use fictional or sample data first. The runbook walks through status checks, privacy review, ledger validation, report generation, reconciliation, freeze handling, and go/no-go review.

### I want to review whether the workflow is ready

Use the [Review Packet Template](REVIEW_PACKET_TEMPLATE.md) and [Operational Readiness Matrix](OPERATIONAL_READINESS_MATRIX.md).

The purpose is to record evidence and blockers, not to assume that document existence means approval.

## A simple mental model

Think of the repository as four layers:

1. **Public status** — tells people what is active and what is not.
2. **Ledger and report** — shows the public-safe record of incoming and outgoing amounts.
3. **Review evidence** — records what was checked and what remains unresolved.
4. **Safety controls** — prevent live operation from being implied before a separate approval process.

Most people only need the first two layers. Maintainers and reviewers use the deeper material when required.

## Current status

In plain language:

- the repository/template release is published;
- the sample workflow can be reproduced;
- donation collection is not active;
- no live receiving wallet is published;
- live operation has not been approved.

Machine-readable status:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
GO_LIVE: NO
```

If any public page says donations or wallets are inactive, **do not send funds**.

## Need the shortest possible route?

Open [Quick Access](QUICK_ACCESS.md).
