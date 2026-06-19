# Open Aid Ledger

[![Validate](https://github.com/thanhlq8-max/open-aid-ledger/actions/workflows/validate.yml/badge.svg)](https://github.com/thanhlq8-max/open-aid-ledger/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Status:** public-release candidate template  
**Mode:** transparency-first public donation ledger  
**Donation status:** inactive until maintainers publish verified wallet addresses  
**Last updated:** 2026-06-19

Open Aid Ledger is a public, read-only transparency repository for voluntary digital-asset donations used to support hardship cases and open-source public-good work.

This project exists because a single person usually cannot create meaningful social support alone, while many small voluntary donations from a transparent community can become useful support for real hardship cases.

This repository is designed for:

- children and families facing hardship;
- homeless or vulnerable people;
- community members in urgent difficulty;
- open-source maintainers and tooling that provide real public utility;
- trader communities that want to donate part of legitimate profits to social support.

This repository is **not** a trading project, investment fund, exchange, broker, payment processor, custody service, charity registration substitute, or payment institution.

---

## Current public status

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

Donations should not be sent until the maintainers create a real `wallets.json`, publish the first transparency report, and make the policy files consistent with the active campaign.

---

## Core principles

1. **Voluntary only** — all donations are optional.
2. **No return promise** — donors receive no profit, yield, token, allocation, ownership, signal, or financial benefit.
3. **No trading use** — donations must not be used to fund trading accounts, margin calls, revenge trading, copy trading, or managed accounts.
4. **No private-key handling** — this repository never stores seed phrases, private keys, API keys, exchange credentials, or custody automation.
5. **Transparency first** — incoming donations, outgoing support, campaign rules, and reports should be auditable.
6. **Privacy by default** — beneficiary identity must be protected unless they explicitly consent to disclosure.
7. **Local-law respect** — contributors and donors are responsible for their own legal, tax, and reporting obligations.

---

## Vietnam note

Vietnam does not treat digital assets as legal tender or legal means of payment. Public reporting indicates that owning crypto is not explicitly banned, while the regulatory framework continues to evolve. This repository therefore avoids payment-language and uses only voluntary digital-asset donation/transparency language.

When donations are converted to VND or otherwise realized, maintainers and recipients should keep records and handle tax/reporting obligations according to applicable Vietnamese law. This is not legal or tax advice.

See: [`docs/VN_LEGAL_AND_TAX_NOTE.md`](docs/VN_LEGAL_AND_TAX_NOTE.md)

---

## Supported assets and wallets

Wallet addresses are intentionally not filled in this template.

Before accepting donations, maintainers must complete:

- copy `wallets.example.json` to `wallets.json`;
- verify wallet addresses outside GitHub before publishing;
- update [`DONATION_POLICY.md`](DONATION_POLICY.md);
- update [`TRANSPARENCY_POLICY.md`](TRANSPARENCY_POLICY.md);
- update [`BENEFICIARY_PRIVACY_POLICY.md`](BENEFICIARY_PRIVACY_POLICY.md);
- run all validation commands.

Recommended minimum practice:

- start with a small number of public addresses;
- use a dedicated address per campaign where possible;
- move to multisig before accepting large amounts;
- publish monthly reports;
- never accept private keys, seed phrases, or exchange credentials.

---

## What this repo does

- Publishes donation wallet metadata after maintainer activation.
- Maintains public incoming/outgoing ledgers.
- Generates Markdown transparency reports.
- Documents campaign rules and disbursement decisions.
- Protects beneficiary privacy while keeping fund flow auditable.
- Provides validation scripts to catch common ledger and secret-handling mistakes.

## What this repo does not do

- No buy/sell signals.
- No investment advice.
- No profit sharing.
- No managed trading.
- No trading-account rescue.
- No token issuance.
- No custody automation.
- No private-key collection.
- No mixer, obfuscation, or laundering support.
- No claim of being a registered charity unless a legal entity is added later.

---

## Quick start

Copy wallet template only when ready to activate donations:

```bash
cp wallets.example.json wallets.json
python scripts/validate_wallets.py wallets.json
```

Add donation records to:

```text
ledger/donations.csv
```

Add support/disbursement records to:

```text
ledger/disbursements.csv
```

Validate public safety:

```bash
python scripts/validate_ledger.py --donations ledger/donations.csv --disbursements ledger/disbursements.csv
python scripts/check_public_safety.py .
```

Generate a report:

```bash
python scripts/generate_report.py --donations ledger/donations.csv --disbursements ledger/disbursements.csv --out reports/monthly-report.md
```

---

## Campaigns

Current starter campaigns:

- [`campaigns/2026-community-hardship-support.md`](campaigns/2026-community-hardship-support.md)
- [`campaigns/2026-trader-community-giving.md`](campaigns/2026-trader-community-giving.md)
- [`campaigns/2026-open-source-public-good-support.md`](campaigns/2026-open-source-public-good-support.md)

Trader-community giving is allowed only as voluntary social giving from legitimate profits. It must not fund trading losses, margin calls, revenge trading, copy trading, or managed accounts.

---

## Public release checklist

See [`docs/PUBLISHING.md`](docs/PUBLISHING.md) and [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md).

Minimum before public activation:

```bash
python -m compileall scripts
python scripts/validate_wallets.py wallets.example.json
python scripts/validate_ledger.py --donations ledger/donations.csv --disbursements ledger/disbursements.csv
python scripts/check_public_safety.py .
python scripts/generate_report.py --donations ledger/donations.csv --disbursements ledger/disbursements.csv --out reports/local-smoke-report.md
```

---

## Security

Never submit private keys, seed phrases, screenshots containing wallet secrets, exchange credentials, identity documents, or private beneficiary data into GitHub issues, pull requests, commits, or comments.

See [`SECURITY.md`](SECURITY.md) and [`docs/SCAM_PREVENTION.md`](docs/SCAM_PREVENTION.md).
