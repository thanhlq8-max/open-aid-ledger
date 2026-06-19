# Open Aid Ledger

Transparency-first public ledger template for voluntary digital-asset donations supporting hardship cases and open-source public goods.

## Current status

```text
PROJECT_STATUS: PUBLIC_TEMPLATE
VERSION: 0.2.0-ledger-safety-foundation
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
docs/                            Governance, legal notes, roadmap, and operating docs
ledger/                          CSV ledger templates
reports/                         Generated or sample transparency reports
scripts/                         Local validation and report-generation scripts
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
python -m compileall scripts
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv
python scripts\check_public_safety.py .
python scripts\generate_report.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --out reports\local-smoke-report.md
```

The smoke report is for local validation only unless intentionally reviewed and committed.

## Donation activation policy

Donation collection must remain inactive until all of the following are complete:

1. wallet metadata schema is hardened;
2. validator tests exist and pass in CI;
3. address-change procedure is reviewed;
4. multisig or equivalent governance is documented;
5. public transparency report format is approved;
6. beneficiary privacy controls are reviewed;
7. the maintainer explicitly changes `DONATIONS_ACTIVE` from `NO` to `YES` in a reviewed commit.

## Legal and tax note

This repository does not provide legal, tax, accounting, financial, or investment advice.

Digital-asset rules vary by jurisdiction and may change. Maintainers and donors are responsible for complying with applicable law, reporting obligations, tax obligations, platform rules, and exchange policies.

For Vietnam-specific context, see:

```text
docs/VN_LEGAL_AND_TAX_NOTE.md
```


## v0.2.0 ledger safety foundation

The ledger safety layer now includes:

- wallet metadata schema v1.1;
- stricter wallet metadata validation;
- stricter ledger CSV validation;
- optional balance enforcement;
- validator regression tests;
- public report foundation improvements.

See:

- `docs/WALLET_SCHEMA.md`
- `docs/LEDGER_VALIDATION.md`
- `RELEASE_NOTES_v0.2.0.md`
## Development roadmap

Near-term priorities:

1. harden wallet metadata schema;
2. add tests for validator scripts;
3. add sample transparency report;
4. design GitHub Pages static reporting;
5. design read-only blockchain explorer importer;
6. add maintainer governance checklist.

The first donation-ready release should not be cut until the safety and reporting foundation is stable.

## License

See `LICENSE`.