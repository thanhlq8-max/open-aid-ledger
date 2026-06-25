# Open Aid Ledger public status

Open Aid Ledger is a transparency-first public ledger template for voluntary digital-asset donations supporting hardship cases and open-source public goods.

## Current status

```text
PROJECT_STATUS: PUBLIC_TEMPLATE
VERSION: 1.0.0-rc3-external-review-evidence-pack
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

Donation collection is intentionally inactive. Live receiving details are intentionally unpublished until governance, ledger validation, privacy controls, reporting, and public-safety checks are complete.

## Do not send yet

Do not send funds based on private messages, screenshots, comments, or copies of old receiving information.

A future active release must publish status, asset, network, approved receiving channel, ledger policy, reporting policy, privacy controls, and freeze procedure from an approved repository source.

If the public status still says `DONATIONS_ACTIVE: NO` or `WALLETS_PUBLISHED: NO`, do not send.

## Public status dashboard

| Area | Status | Notes |
|---|---:|---|
| Repository publication | READY | Public template and safety docs are present. |
| Ledger validators | READY | Empty and sample ledgers are validated in CI. |
| Receiving-channel publication | BLOCKED | No live receiving detail is published yet. |
| Donation activation | BLOCKED | `DONATIONS_ACTIVE` remains `NO`. |
| Custody automation | FORBIDDEN | No signing, transfers, withdrawal APIs, or private keys. |
| Beneficiary privacy | REQUIRED | Public reports must redact beneficiary-sensitive information. |
| Donor trust guidance | READY FOR REVIEW | Donor-facing trust and verification guides are documented. |
| Governance | READY FOR REVIEW | Maintainer checklists and emergency freeze procedure are documented. |
| Blockchain importer | DESIGN ONLY | Read-only importer design exists; no network fetcher is implemented. |

## Donor trust and verification

- [Donor quickstart](DONOR_QUICKSTART.md)
- [Donor FAQ](DONOR_FAQ.md)
- [Donor trust guide](DONOR_TRUST_GUIDE.md)
- [Receiving channel publication policy](RECEIVING_CHANNEL_PUBLICATION_POLICY.md)
- [Receiving account protection checklist](RECEIVING_ACCOUNT_PROTECTION.md)
- [Public summary checklist](PUBLIC_SUMMARY_CHECKLIST.md)

## Reports

- [Sample transparency report](../reports/sample-transparency-report.md)
- [Static report design](GITHUB_PAGES_STATIC_REPORT.md)
- [Public status page guide](PUBLIC_STATUS_PAGE.md)
- [GitHub Pages deployment checklist](PAGES_DEPLOYMENT_CHECKLIST.md)

## Readiness and governance

- [Donation readiness dry run](DONATION_READINESS_DRY_RUN.md)
- [Donation activation checklist](DONATION_ACTIVATION_CHECKLIST.md)
- [Maintainer governance checklist](MAINTAINER_GOVERNANCE_CHECKLIST.md)
- [Emergency freeze procedure](EMERGENCY_FREEZE_PROCEDURE.md)
- [Conflict-of-interest disclosure template](CONFLICT_OF_INTEREST_DISCLOSURE_TEMPLATE.md)

## Campaign lifecycle

- [Campaign lifecycle](CAMPAIGN_LIFECYCLE.md)
- [Campaign status schema](CAMPAIGN_STATUS_SCHEMA.md)
- [Campaign review checklist](CAMPAIGN_REVIEW_CHECKLIST.md)
- [Issue and release mapping](ISSUE_RELEASE_MAPPING.md)

## Policies

- [Donation policy](../DONATION_POLICY.md)
- [Transparency policy](../TRANSPARENCY_POLICY.md)
- [Beneficiary privacy policy](../BENEFICIARY_PRIVACY_POLICY.md)
- [Security policy](../SECURITY.md)

## Safety boundaries

This project is not a payment processor, charity-registration claim, custody wallet, wallet-signing system, trading fund, managed account, margin-call rescue fund, investment product, token issuance project, or promise of financial return.

## Next milestone

The next milestone is RC3 evidence review and donation-readiness final review. It must remain dry-run only unless a maintainer deliberately publishes reviewed receiving-channel metadata and changes donation status in a dedicated reviewed commit.
