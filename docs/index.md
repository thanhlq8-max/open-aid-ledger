# Open Aid Ledger public status

Open Aid Ledger is a transparency-first public ledger template for voluntary digital-asset support to hardship cases and open-source public goods.

## Start here

- [Start Here](START_HERE.md)
- [Donor Quickstart](DONOR_QUICKSTART.md)
- [Donor FAQ](DONOR_FAQ.md)

Use `Start Here` as the front door. Use detailed docs only when the flow points to them.

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

## Status dashboard

| Area | Status | Meaning |
|---|---:|---|
| Donor entry point | READY | `Start Here`, Donor Quickstart, and Donor FAQ are available. |
| Public ledger template | READY | Ledger templates and validators exist. |
| Dry-run operation | READY | Maintainers can test the flow with sample data. |
| Review packet | READY | Reviewers can record evidence and blockers. |
| Receiving-channel publication | BLOCKED | No live receiving detail is published yet. |
| Donation activation | BLOCKED | `DONATIONS_ACTIVE` remains `NO`. |
| Custody automation | FORBIDDEN | No signing, transfer automation, withdrawal APIs, or custody flow. |

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

The next milestone is dry-run evidence review and donation-readiness final review. It remains dry-run only unless a maintainer deliberately changes donation status in a separate reviewed proposal.
