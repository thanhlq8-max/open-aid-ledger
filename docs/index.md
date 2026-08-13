# Open Aid Ledger

Open Aid Ledger is a reusable open-source template for making a support workflow easier to inspect: what is active, what was recorded, how funds were used, and what evidence supports the public record.

**This is a template and working demo, not a live donation campaign. It is not accepting funds right now.**

## Start with one of these

- **See a working example:** [Try the 5-minute sample walkthrough](REPRODUCIBLE_SAMPLE_WALKTHROUGH.md)
- **Understand your role:** [Start Here](START_HERE.md)
- **Thinking about donating later:** [Donor Quickstart](DONOR_QUICKSTART.md) and [Donor FAQ](DONOR_FAQ.md)

## What problem does this help solve?

A public support project should make it easy to answer basic questions without relying on private messages or scattered spreadsheets:

- Is support collection active right now?
- Which public records describe incoming and outgoing funds?
- Can a report be reproduced from the ledger?
- How is beneficiary privacy protected?
- What happens when evidence is missing or something does not reconcile?

Open Aid Ledger provides a starting structure for those questions: a public status page, sample ledgers, validators, transparency-report generation, review records, reconciliation steps, and a freeze process.

## What you can see today

The repository release is published and the sample workflow is ready to try. The sample data is fictional.

You can:

1. validate the bundled sample ledger;
2. generate a Markdown transparency report;
3. compare the generated totals with known expected results;
4. inspect the dry-run and review process used before any future live operation is considered.

[Try the sample workflow →](REPRODUCIBLE_SAMPLE_WALKTHROUGH.md)

## Current status in plain language

**Do not send funds.** Donation collection is inactive and no live receiving details are published.

The repository can demonstrate the transparency workflow without activating a real support operation. A future activation would require a separate reviewed decision and a clearly updated public status.

## Choose your role

### New user

Run the [Reproducible Sample Walkthrough](REPRODUCIBLE_SAMPLE_WALKTHROUGH.md). This is the fastest way to see the project produce a useful result.

### Donor or observer

Read [Donor Quickstart](DONOR_QUICKSTART.md). The current answer is simple: support is not active yet.

### Maintainer

Use the [Dry-run Operations Runbook](DRY_RUN_OPERATIONS_RUNBOOK.md) to test the workflow with fictional data before considering any live operation.

### Reviewer

Use the [Review Packet Template](REVIEW_PACKET_TEMPLATE.md) and [Operational Readiness Matrix](OPERATIONAL_READINESS_MATRIX.md) to record evidence, unresolved findings, and the current go/no-go decision.

## What this project does not do

Open Aid Ledger is not a payment processor, custody wallet, charity-registration claim, investment product, trading fund, token project, or promise of financial return.

It does not sign transactions or automate transfers. It is designed to keep public evidence separate from private beneficiary information and to keep repository publication separate from permission to operate live.

## Safety status

| Area | Status | What it means for people |
|---|---:|---|
| Repository release | RELEASED | The `v1.0.0` template release is published. |
| Sample workflow | READY | Fictional ledger records can be validated and converted into a sample report. |
| Public status | READY | The current inactive state is visible. |
| Donation activation | BLOCKED | Do not send funds. |
| Receiving details | BLOCKED | No live receiving wallet is published. |
| Custody automation | FORBIDDEN | No signing, transfer, withdrawal, or custody automation is part of this repo. |

## For maintainers who need the deeper controls

Most visitors do not need the control documents below. They exist for operating and review work:

- [Dry-run Operations Runbook](DRY_RUN_OPERATIONS_RUNBOOK.md)
- [Review Packet Template](REVIEW_PACKET_TEMPLATE.md)
- [Operational Readiness Matrix](OPERATIONAL_READINESS_MATRIX.md)
- [Donation policy](../DONATION_POLICY.md)
- [Transparency policy](../TRANSPARENCY_POLICY.md)
- [Beneficiary privacy policy](../BENEFICIARY_PRIVACY_POLICY.md)
- [Emergency freeze procedure](EMERGENCY_FREEZE_PROCEDURE.md)

## Technical status

This block is machine-readable and is kept for automated consistency checks. Most users can rely on the plain-language status above.

```text
PROJECT_STATUS: PUBLIC_TEMPLATE
VERSION: 1.0.0
RELEASE_TARGET: v1.0.0
RELEASE_TAG_CREATED: YES
GITHUB_RELEASE_CREATED: YES
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
CUSTODY_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
GO_LIVE: NO
```

Repository usability goals checked by the static validator:

```text
EASY_TO_ACCESS: YES
EASY_TO_USE: YES
EASY_TO_SHARE: YES
USER_DASHBOARD: YES
PUBLIC_TRANSPARENCY: YES
SAFETY_FIRST: YES
```

The next public-utility milestone is to show a generated sample transparency report directly in the public demo, after this human-first navigation layer is validated.
