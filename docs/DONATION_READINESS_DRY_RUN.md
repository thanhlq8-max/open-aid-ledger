# Donation Readiness Dry Run

This document defines a dry-run-only process for checking whether Open Aid Ledger is structurally prepared for a future donation-ready release.

The dry run does not activate donations, publish real wallet addresses, custody funds, move assets, sign transactions, call exchange APIs, or claim charity registration.

## Current dry-run position

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
REAL_WALLETS_REQUIRED: NO
PRIVATE_KEYS_REQUIRED: NO
TRANSFER_AUTOMATION: FORBIDDEN
DRY_RUN_ONLY: YES
```

## Purpose

The dry run checks the readiness of:

- wallet metadata governance;
- campaign lifecycle metadata;
- ledger validation;
- sample transparency reporting;
- public status-page design;
- read-only importer design;
- maintainer governance;
- emergency freeze controls;
- conflict-of-interest disclosure;
- beneficiary privacy guardrails.

## Required inputs

The dry run uses these repository files:

```text
README.md
VERSION
wallets.example.json
campaigns/campaigns.example.json
ledger/donations.csv
ledger/disbursements.csv
examples/sample-ledger/donations.csv
examples/sample-ledger/disbursements.csv
reports/sample-transparency-report.md
docs/DONATION_ACTIVATION_CHECKLIST.md
docs/MAINTAINER_GOVERNANCE_CHECKLIST.md
docs/EMERGENCY_FREEZE_PROCEDURE.md
docs/BENEFICIARY_PRIVACY_POLICY.md
docs/GITHUB_PAGES_STATIC_REPORT.md
docs/BLOCKCHAIN_EXPLORER_IMPORTER_DESIGN.md
docs/CAMPAIGN_LIFECYCLE.md
```

Some files may live at the repository root instead of `docs/`, depending on the policy document. The validator accepts the root policy files that already exist in this repository.

## Dry-run checklist

A dry run passes only when:

1. donation activation is still explicitly inactive;
2. wallet publication is still explicitly disabled;
3. wallet examples are placeholders or dry-run-only;
4. campaign examples remain inactive/template-safe;
5. ledgers validate;
6. sample report exists and is marked non-production/sample-only;
7. emergency freeze procedure exists;
8. donation activation checklist exists;
9. public safety scan passes;
10. tests pass in CI.

## Output

The dry run emits a machine-readable status object with:

```text
status
version
donations_active
wallets_published
checks
warnings
errors
```

Valid statuses:

```text
PASS
FAIL
```

## Non-goals

This dry run does not provide:

- legal advice;
- tax advice;
- financial advice;
- investment advice;
- charity registration;
- payment processing;
- exchange integration;
- wallet custody;
- private-key management;
- automated donation acceptance;
- automatic transfer or disbursement.
