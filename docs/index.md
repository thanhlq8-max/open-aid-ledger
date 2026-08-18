# Open Aid Ledger

Open Aid Ledger is a reusable open-source template for making a support workflow easier to inspect: what is active, what was recorded, how funds were used, and what evidence supports the public record.

**This is a template and working demo, not a live donation campaign. It is not accepting funds right now.**

## Start with one of these

- **See a finished example:** [Open the generated sample transparency report](SAMPLE_TRANSPARENCY_REPORT.md)
- **Try it yourself:** [Reproduce the report in about 5 minutes](REPRODUCIBLE_SAMPLE_WALKTHROUGH.md)
- **Understand your role:** [Start Here](START_HERE.md)

If you are thinking about donating later, read [Donor Quickstart](DONOR_QUICKSTART.md) and [Donor FAQ](DONOR_FAQ.md). The current status is inactive.

## See what the tool produces

The [Sample Transparency Report](SAMPLE_TRANSPARENCY_REPORT.md) is committed as a public demo result generated from the fictional CSV records in `examples/sample-ledger/`.

It contains:

- 3 fictional donation records;
- 2 fictional disbursement records;
- incoming totals by asset;
- outgoing totals by asset;
- net sample balances after the recorded disbursements.

A regression test compares this public file with the output of `scripts/generate_report.py`, so the demo cannot silently drift away from the tool that produces it.

**The values are fictional sample data, not live balances or real donations.**

## What problem does this help solve?

A public support project should make it easy to answer basic questions without relying on private messages or scattered spreadsheets:

- Is support collection active right now?
- Which public records describe incoming and outgoing funds?
- Can a report be reproduced from the ledger?
- How is beneficiary privacy protected?
- What happens when evidence is missing or something does not reconcile?

Open Aid Ledger provides a starting structure for those questions: a public status page, sample ledgers, validators, transparency-report generation, review records, reconciliation steps, and a freeze process.

## What you can see today

The repository release is published and the sample workflow is ready to inspect or reproduce. The sample data is fictional.

You can:

1. open the generated sample report immediately;
2. validate the bundled sample ledger;
3. reproduce the same Markdown transparency report;
4. compare the generated totals with known expected results;
5. inspect the dry-run and review process used before any future live operation is considered.

[Open the sample report →](SAMPLE_TRANSPARENCY_REPORT.md)

[Try the sample workflow →](REPRODUCIBLE_SAMPLE_WALKTHROUGH.md)

## Current status in plain language

**Do not send funds.** Donation collection is inactive and no live receiving details are published.

If the public status still says `DONATIONS_ACTIVE: NO`, do not send funds.

The repository can demonstrate the transparency workflow without activating a real support operation. A future activation would require a separate reviewed decision and a clearly updated public status.

## Choose your role

### New user

Open the [Sample Transparency Report](SAMPLE_TRANSPARENCY_REPORT.md) first. If the result looks useful, run the [Reproducible Sample Walkthrough](REPRODUCIBLE_SAMPLE_WALKTHROUGH.md) to reproduce it yourself.

### Donor or observer

Read [Donor Quickstart](DONOR_QUICKSTART.md). The current answer is simple: support is not active yet.

### Maintainer

Use the [Dry-run Operations Runbook](DRY_RUN_OPERATIONS_RUNBOOK.md) to test the workflow with fictional data before considering any live operation.

### Reviewer

Use the [Review Packet Template](REVIEW_PACKET_TEMPLATE.md) and [Operational Readiness Matrix](OPERATIONAL_READINESS_MATRIX.md) to record evidence, unresolved findings, and the current go/no-go decision.

[Dry-run Evidence Loop](../examples/dry-run/README.md)

## What this project does not do

Open Aid Ledger is not a payment processor, custody wallet, charity-registration claim, investment product, trading fund, token project, or promise of financial return.

It does not sign transactions or automate transfers. It is designed to keep public evidence separate from private beneficiary information and to keep repository publication separate from permission to operate live.

## Safety status

| Area | Status | What it means for people |
|---|---:|---|
| Repository release | RELEASED | The `v1.0.0` template release is published. |
| Sample report | READY | A generated fictional transparency report can be viewed directly. |
| Sample workflow | READY | Fictional ledger records can be validated and converted into the same sample report. |
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

## Maintainer compatibility snapshot

The following block keeps stable wording used by existing regression checks. It is intentionally below the human-facing explanation.

Open Aid Ledger public dashboard

### One-screen operating board

| Role | Next action | Use this file | Done when |
|---|---|---|---|
| Donor | Check current status before sending. | `docs/DONOR_QUICKSTART.md` | Public status is clear. |
| Maintainer | Run the dry-run evidence loop with sample data. | `examples/dry-run/README.md` | Sample evidence loop is complete. |
| Reviewer | Check evidence and unresolved blockers. | `docs/REVIEW_PACKET_TEMPLATE.md` | Findings are recorded. |

### Current blockers

```text
RECEIVING_CHANNEL_PUBLICATION: BLOCKED
DONATION_ACTIVATION: BLOCKED
GO_LIVE: NO
```

### Shareable status snapshot

```text
Official dashboard: docs/index.md
Start here: docs/START_HERE.md
Dry-run evidence loop: examples/dry-run/README.md
```

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

The current public-utility milestone is to keep the generated sample report visible and reproducible without weakening the inactive safety state.
