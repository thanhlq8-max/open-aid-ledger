# Open Aid Ledger

Transparency-first public ledger template for voluntary digital-asset donations supporting hardship cases and open-source public goods.

## Current status

```text
PROJECT_STATUS: PUBLIC_TEMPLATE
VERSION: 1.0.0-rc3-external-review-evidence-pack
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

This repository is public, but donation collection is intentionally inactive until wallet governance, ledger validation, reporting, and public-safety checks are hardened.

## Purpose

Open Aid Ledger is a transparency template for communities that want to publish donation records without building a custody platform.

It is designed for:

- hardship-support campaigns;
- child and family support initiatives;
- homeless or emergency relief coordination;
- open-source public-good support;
- trader/community giving where people voluntarily donate from lawful profits to social-impact causes.

## What this repository does

- Publishes donation and disbursement policies.
- Keeps wallet metadata separate from private key material.
- Provides CSV ledger templates for incoming donations and outgoing support.
- Provides validator scripts for wallet metadata, ledger shape, and public-safety checks.
- Provides campaign templates and governance documentation.
- Keeps donation activation explicit and auditable.
- Provides a sample transparency report and static GitHub Pages status design.
- Documents a read-only blockchain explorer importer design for future public transaction reconciliation.
- Provides maintainer governance, donation activation, emergency freeze, and conflict-of-interest checklists.
- Provides campaign lifecycle, status metadata, campaign review checklist, and campaign validation.
- Provides beneficiary-safe intake, partner attestation, and disbursement decision record templates.
- Provides donation-readiness dry-run checks before any donation activation.
- Provides a static public status page and validator for GitHub Pages readiness.
- Provides donor trust, public summary, receiving-account protection, and receiving-channel publication guides while keeping donation collection inactive.
- Provides v1.0.0-rc1 donation-ready candidate review artifacts while keeping donation collection inactive.
- Provides v1.0.0-rc2 external review and activation-gate artifacts while keeping donation collection inactive.
- Provides v1.0.0-rc3 external review evidence-pack artifacts while keeping donation collection inactive.

## What this repository does not do

This repository is not:

- a payment processor;
- a charity registration claim;
- a custody wallet;
- a wallet signing system;
- a trading fund;
- a copy-trading, managed-account, or profit-sharing scheme;
- a margin-call or trading-loss rescue fund;
- an investment product;
- a token issuance project;
- a promise of financial return.

## Core guardrails

```text
NO_PRIVATE_KEYS
NO_SEED_PHRASES
NO_AUTO_TRANSFER
NO_EXCHANGE_WITHDRAWAL_API
NO_MIXER
NO_CUSTODY_AUTOMATION
NO_TRADING_ACCOUNT_TOP_UP
NO_MARGIN_CALL_SUPPORT
NO_RETURN_PROMISE
NO_BENEFICIARY_DOXXING
```

## Repository structure

```text
.github/                         GitHub workflows and templates
campaigns/                       Campaign proposal templates and examples
campaigns/campaigns.example.json    Campaign lifecycle metadata template
docs/                            Governance, legal notes, roadmap, and operating docs
  docs/MAINTAINER_GOVERNANCE_CHECKLIST.md      Maintainer launch and operating checklist
  docs/DONATION_ACTIVATION_CHECKLIST.md        Donation activation gate
  docs/EMERGENCY_FREEZE_PROCEDURE.md           Incident freeze procedure
  docs/CONFLICT_OF_INTEREST_DISCLOSURE_TEMPLATE.md Conflict disclosure template
  docs/ISSUE_RELEASE_MAPPING.md           Initial backlog to release mapping
  docs/CAMPAIGN_REVIEW_CHECKLIST.md       Campaign review checklist
  docs/CAMPAIGN_STATUS_SCHEMA.md          Campaign metadata schema
  docs/CAMPAIGN_LIFECYCLE.md              Campaign status lifecycle
  docs/BENEFICIARY_INTAKE_REVIEW.md       Beneficiary-safe intake and review workflow
  docs/PARTNER_ATTESTATION_TEMPLATE.md    Partner attestation template
  docs/DISBURSEMENT_DECISION_RECORD_TEMPLATE.md Disbursement decision record template
  docs/PUBLIC_SUMMARY_CHECKLIST.md        Public-safe case summary checklist
  docs/RECEIVING_ACCOUNT_PROTECTION.md    Future receiving-account protection checklist
  docs/RECEIVING_CHANNEL_PUBLICATION_POLICY.md Future receiving-channel publication policy
  docs/DONOR_TRUST_GUIDE.md               Future donor trust and verification guide
  docs/PUBLIC_STATUS_PAGE.md              Static public status page rules
  docs/DONATION_READINESS_DRY_RUN.md          Donation readiness dry-run gates
  docs/DRY_RUN_WALLET_PUBLICATION_REVIEW.md Dry-run wallet publication checklist
  docs/DONATION_LAUNCH_RISK_REGISTER.md    Launch risk register
  docs/DONATION_LAUNCH_RUNBOOK.md          Future launch runbook
examples/sample-ledger/           Fictional sample ledger rows
examples/relief-review/           Fictional beneficiary-safe relief review records
examples/importer/                Fictional importer-normalization sample rows
ledger/                          CSV ledger templates
reports/                         Generated or sample transparency reports
scripts/                         Local validation and report-generation scripts
tests/                           Regression tests for validators, reports, and docs
wallets.example.json             Placeholder wallet metadata template
DONATION_POLICY.md               Donation rules and restrictions
TRANSPARENCY_POLICY.md           Public reporting rules
BENEFICIARY_PRIVACY_POLICY.md    Privacy rules for supported people
SECURITY.md                      Security reporting policy
CONTRIBUTING.md                  Contributor guide
```

## Local validation

Run from the repository root:

```powershell
python -m compileall scripts tests
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_campaigns.py campaigns\campaigns.example.json --allow-inactive-template
python scripts\validate_readiness.py .
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --enforce-balance
python scripts\validate_ledger.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --enforce-balance
python scripts\validate_static_status.py .
python scripts\validate_candidate.py .
python scripts\validate_rc1.py .
python scripts\validate_rc2.py .
python scripts\validate_rc3.py .
python scripts\check_public_safety.py .
python -m pip install -r requirements-dev.txt
python -m pytest -q
python scripts\generate_report.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --out reports\local-sample-report.md --title "Open Aid Ledger Sample Transparency Report"
```

The local sample report is for validation only unless intentionally reviewed and committed.

## Sample reporting

The repository includes a non-production sample report and sample ledger rows:

```text
reports/sample-transparency-report.md
examples/sample-ledger/donations.csv
examples/sample-ledger/disbursements.csv
```

These files are sample-only and do not activate donation collection.

For the static public status-page design, see:

```text
docs/GITHUB_PAGES_STATIC_REPORT.md
docs/index.md
```

## Read-only importer design

The repository now includes a design-only foundation for future public blockchain explorer importers:

```text
docs/BLOCKCHAIN_EXPLORER_IMPORTER_DESIGN.md
docs/IMPORTER_NORMALIZED_TX_SCHEMA.md
docs/IMPORTER_MANUAL_RECONCILIATION.md
examples/importer/normalized_transactions.sample.csv
```

The importer scope is intentionally read-only. It must not sign transactions, move assets, handle private keys, use exchange withdrawal APIs, or write directly to donation ledgers without manual review.

## Campaign lifecycle

The repository includes campaign lifecycle documentation and a campaign metadata validator:

```text
campaigns/campaigns.example.json
docs/CAMPAIGN_LIFECYCLE.md
docs/CAMPAIGN_STATUS_SCHEMA.md
docs/CAMPAIGN_REVIEW_CHECKLIST.md
scripts/validate_campaigns.py
```

Campaigns must remain inactive unless donation activation gates are explicitly reviewed and `DONATIONS_ACTIVE` is changed in a reviewed commit.

## Beneficiary-safe relief workflow

The repository includes review-only workflow documents for handling real hardship-support cases without exposing vulnerable people in the public repository:

```text
docs/BENEFICIARY_INTAKE_REVIEW.md
docs/PARTNER_ATTESTATION_TEMPLATE.md
docs/DISBURSEMENT_DECISION_RECORD_TEMPLATE.md
docs/PUBLIC_SUMMARY_CHECKLIST.md
BENEFICIARY_PRIVACY_POLICY.md
```

These documents help maintainers review need, privacy, partner confirmation, future disbursement records, and public summaries while keeping donation collection inactive and wallet publication blocked.

The repository also includes fictional relief-review examples:

```text
examples/relief-review/README.md
examples/relief-review/FAM-2026-001_intake_review.sample.md
examples/relief-review/FAM-2026-001_partner_attestation.sample.md
examples/relief-review/FAM-2026-001_disbursement_decision.sample.md
```

These samples do not use real beneficiary data and do not imply that funds have been collected or moved.

## Donor trust and future receiving protection

The repository includes future-facing donor trust and receiving-account protection docs:

```text
docs/DONOR_TRUST_GUIDE.md
docs/RECEIVING_CHANNEL_PUBLICATION_POLICY.md
docs/RECEIVING_ACCOUNT_PROTECTION.md
docs/PUBLIC_SUMMARY_CHECKLIST.md
```

These documents explain how future donors should verify status, approved receiving channels, campaign status, ledger reporting, privacy controls, and freeze procedures before sending support.

They do not activate donation collection and do not publish live receiving details.

## Donation readiness dry run

The repository includes a dry-run-only donation readiness layer:

```text
docs/DONATION_READINESS_DRY_RUN.md
docs/DRY_RUN_WALLET_PUBLICATION_REVIEW.md
docs/DONATION_LAUNCH_RISK_REGISTER.md
docs/DONATION_LAUNCH_RUNBOOK.md
examples/dry-run/wallets.dry-run.example.json
scripts/validate_readiness.py
```

The dry run checks readiness while keeping `DONATIONS_ACTIVE: NO` and `WALLETS_PUBLISHED: NO`.

## External review and evidence gates

The repository has completed RC2 external review activation-gate scaffolding and is now at RC3 external review evidence-pack stage.

RC3 requires external review evidence, unresolved finding records, activation blockers, and maintainer response documentation before any later activation proposal can be considered.

RC2 and RC3 do not activate donations and do not publish real wallet addresses.

## Donation activation policy

Donation collection must remain inactive until all of the following are complete:

1. wallet metadata schema is hardened;
2. validator tests exist and pass in CI;
3. address-change procedure is reviewed;
4. multisig or equivalent governance is documented;
5. public transparency report format is approved;
6. beneficiary privacy controls are reviewed;
7. read-only importer design is reviewed if transaction import is used;
8. the maintainer explicitly changes `DONATIONS_ACTIVE` from `NO` to `YES` in a reviewed commit.

## Legal and tax note

This repository does not provide legal, tax, accounting, financial, or investment advice.

Digital-asset rules vary by jurisdiction and may change. Maintainers and donors are responsible for complying with applicable law, reporting obligations, tax obligations, platform rules, and exchange policies.

For Vietnam-specific context, see:

```text
docs/VN_LEGAL_AND_TAX_NOTE.md
```

## Pre-1.0 candidate review

This repository is now in pre-1.0 candidate-review mode. The review checks whether the public template, ledger validation, campaign lifecycle, governance controls, readiness dry run, public status page, and beneficiary-safe relief workflow are coherent enough to prepare a future donation-ready release.

This does not activate donations and does not publish real wallet addresses.

See:

```text
docs/PRE_1_0_DONATION_READY_CANDIDATE_REVIEW.md
docs/DONATION_READY_CANDIDATE_CHECKLIST.md
```

## Development roadmap

Near-term priorities:

1. collect and assess RC3 external review evidence;
2. test the beneficiary-safe relief workflow with fictional review records;
3. keep donor trust, receiving-channel publication, account protection, and public summary docs easy to understand;
4. keep the static public status page aligned with current inactive status;
5. resolve legal/tax review and wallet-governance blockers before any activation proposal;
6. keep read-only importer implementation behind reviewed design and manual reconciliation gates;
7. keep donation activation inactive until all launch gates pass.

The first donation-ready release should not be cut until the safety and reporting foundation is stable.


## Release closeout

The initial six public seed issues are mapped to completed releases in:

```text
docs/INITIAL_ISSUE_COMPLETION_MAP.md
docs/ISSUE_CLOSEOUT_COMMENTS.md
docs/RELEASE_CLOSEOUT.md
```

This closeout does not activate donations or publish real wallet addresses.

## License

See `LICENSE`.

## RC3 external review evidence pack

The current release candidate adds a review evidence-pack layer.

This RC3 checkpoint remains non-activating:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

External review evidence must be collected and assessed before any separate activation proposal can be considered.
