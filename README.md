# Open Aid Ledger

Transparency-first public ledger template for voluntary digital-asset support to hardship cases and open-source public goods.

Open Aid Ledger is designed to make support easier to access, easier to use, easier to share, safer to operate, and clearer for donors.

## Quick access

Open the shortest user guide first:

```text
docs/QUICK_ACCESS.md
```

Public dashboard:

```text
https://thanhlq8-max.github.io/open-aid-ledger/
```

## Project goals

```text
EASY_TO_ACCESS: YES
EASY_TO_USE: YES
EASY_TO_SHARE: YES
USER_DASHBOARD: YES
PUBLIC_TRANSPARENCY: YES
SAFETY_FIRST: YES
```

## Public dashboard

Open the published dashboard:

```text
https://thanhlq8-max.github.io/open-aid-ledger/
```

Repository dashboard source:

```text
docs/index.md
```

## Start here

Use one front door first:

```text
docs/START_HERE.md
```

Then follow only the links needed for your role: donor, maintainer, or reviewer.

## Current status

```text
PROJECT_STATUS: PUBLIC_TEMPLATE
VERSION: 1.0.0-rc3-external-review-evidence-pack
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
CUSTODY_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

Current rule:

```text
IF DONATIONS_ACTIVE is NO:
    DO_NOT_SEND
```

Donation collection is inactive. Live receiving details are not published.

## User dashboard

Open the public dashboard source:

```text
docs/index.md
```

The dashboard shows current status, donor safety warning, operating readiness, blocked items, and the shortest path for donors, maintainers, and reviewers.

## What this repo is for

This repo provides a public template for:

- donor-facing status and safety guidance;
- public-safe support-case workflows;
- ledger and transparency-report templates;
- dry-run operations before any future activation proposal;
- review packets and go/no-go checks;
- emergency freeze and reconciliation procedures.

## Simple operating path

```text
1. Donor checks Public Status.
2. Maintainer runs dry-run operation.
3. Reviewer checks evidence and blockers.
4. Maintainer fixes blockers.
5. CI and public-safety checks pass.
6. Activation is considered only in a separate reviewed proposal.
```

Key files:

```text
docs/QUICK_ACCESS.md
docs/START_HERE.md
docs/index.md
docs/DONOR_QUICKSTART.md
docs/DONOR_FAQ.md
docs/DRY_RUN_OPERATIONS_RUNBOOK.md
docs/REVIEW_PACKET_TEMPLATE.md
docs/OPERATIONAL_READINESS_MATRIX.md
```

## What this repo is not

This repo is not:

- a payment processor;
- a charity-registration claim;
- a custody wallet;
- a wallet-signing system;
- a trading fund;
- an investment product;
- a token issuance project;
- a promise of financial return.

## Safety guardrails

```text
NO_PRIVATE_KEYS
NO_SEED_PHRASES
NO_AUTO_TRANSFER
NO_EXCHANGE_WITHDRAWAL_API
NO_CUSTODY_AUTOMATION
NO_RETURN_PROMISE
NO_BENEFICIARY_DOXXING
```

## Validation

The repository uses GitHub Actions `Validate` to run compile checks, ledger validators, readiness validators, RC gates, public-safety scan, tests, and sample report generation.

For local development, install dev requirements and run:

```powershell
python -m compileall scripts tests
python scripts\check_public_safety.py .
python -m pytest -q
```

Use the full validation command list from the workflow when preparing a release.

## License

See `LICENSE`.
