# Open Aid Ledger public dashboard

Open Aid Ledger is a transparency-first public ledger template for voluntary digital-asset support to hardship cases and open-source public goods.

## Start here

- [Start Here](START_HERE.md)
- [Donor Quickstart](DONOR_QUICKSTART.md)
- [Donor FAQ](DONOR_FAQ.md)

Use `Start Here` as the front door. Use detailed docs only when the flow points to them.

## User goals

```text
EASY_TO_ACCESS: YES
EASY_TO_USE: YES
EASY_TO_SHARE: YES
USER_DASHBOARD: YES
PUBLIC_TRANSPARENCY: YES
SAFETY_FIRST: YES
```

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

Donation collection is inactive. Live receiving details are not published.

## Do not send yet

Do not send funds based on private messages, screenshots, comments, or copies of old receiving information.

A future active release must publish status, asset, network, approved receiving channel, ledger policy, reporting policy, privacy controls, and freeze procedure from an approved repository source.

If the public status still says `DONATIONS_ACTIVE: NO` or `WALLETS_PUBLISHED: NO`, do not send.

## Visual dashboard

| Area | Status | User meaning |
|---|---:|---|
| Access path | READY | Start with one page: `START_HERE.md`. |
| Donor guidance | READY | Donor Quickstart and FAQ are available. |
| Shareability | READY | Share this dashboard or `START_HERE.md`, not screenshots or copied receiving data. |
| Public status | READY | Current status is visible and explicit. |
| Public ledger template | READY | Ledger templates and validators exist. |
| Dry-run operation | READY | Maintainers can test the flow with sample data. |
| Review packet | READY | Reviewers can record evidence and blockers. |
| Receiving-channel publication | BLOCKED | No live receiving detail is published yet. |
| Donation activation | BLOCKED | `DONATIONS_ACTIVE` remains `NO`. |
| Custody automation | FORBIDDEN | No signing, transfer automation, withdrawal APIs, or custody flow. |

## One-screen operating board

| Role | Next action | Use this file | Done when |
|---|---|---|---|
| Donor | Check current status before sending. | `docs/DONOR_QUICKSTART.md` | Status is active and official source is clear. |
| Maintainer | Run a dry-run operation with sample data. | `docs/DRY_RUN_OPERATIONS_RUNBOOK.md` | Dry-run report is complete. |
| Reviewer | Check evidence and unresolved blockers. | `docs/REVIEW_PACKET_TEMPLATE.md` | Review result is recorded. |
| Maintainer | Decide go/no-go from readiness matrix. | `docs/OPERATIONAL_READINESS_MATRIX.md` | `GO_LIVE` remains `NO` while blockers remain. |

## Current blockers

```text
RECEIVING_CHANNEL_PUBLICATION: BLOCKED
DONATION_ACTIVATION: BLOCKED
CUSTODY_AUTOMATION: FORBIDDEN
GO_LIVE: NO
```

## Shareable status snapshot

```text
Open Aid Ledger status:
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
GO_LIVE: NO
Official dashboard: docs/index.md
Start here: docs/START_HERE.md
```

## Minimal path

```text
README.md -> docs/START_HERE.md -> docs/index.md
```

Then use only the document needed for the task:

```text
Donor: docs/DONOR_QUICKSTART.md
Maintainer: docs/DRY_RUN_OPERATIONS_RUNBOOK.md
Reviewer: docs/REVIEW_PACKET_TEMPLATE.md
Go/no-go: docs/OPERATIONAL_READINESS_MATRIX.md
```

## Reference docs

Use these only when needed:

- [Donation policy](../DONATION_POLICY.md)
- [Transparency policy](../TRANSPARENCY_POLICY.md)
- [Beneficiary privacy policy](../BENEFICIARY_PRIVACY_POLICY.md)
- [Receiving channel publication policy](RECEIVING_CHANNEL_PUBLICATION_POLICY.md)
- [Receiving account protection checklist](RECEIVING_ACCOUNT_PROTECTION.md)
- [Public summary checklist](PUBLIC_SUMMARY_CHECKLIST.md)
- [Emergency freeze procedure](EMERGENCY_FREEZE_PROCEDURE.md)

## Safety boundary

This project is not a payment processor, charity-registration claim, custody wallet, wallet-signing system, trading fund, investment product, token issuance project, or promise of financial return.

## Next milestone

The next milestone is dry-run evidence review, dashboard review, and donation-readiness final review. It remains dry-run only unless a maintainer deliberately changes donation status in a separate reviewed proposal.
