# PROJECT_STATE — Open Aid Ledger

STATUS: STARTER_TEMPLATE_READY  
PROJECT: Open Aid Ledger  
VERSION: v0.1.0-TRANSPARENCY-FOUNDATION  
LAST_UPDATED: 2026-06-19  
PRIMARY_MODE: CONTROL  
SYSTEM_TYPE: public transparency ledger + read-only reporting scripts  
TARGET_USE: voluntary digital-asset donation transparency for social hardship support and OSS public-good support  

## OBJECTIVE_LOCK

Build a transparency-first repository for voluntary digital-asset donations.

The project must support:

- hardship support transparency;
- trader community giving transparency;
- open-source public-good donation transparency;
- privacy-safe beneficiary reporting;
- read-only ledger/report generation.

## NON_NEGOTIABLE

- No trading signal.
- No investment promise.
- No profit sharing.
- No token issuance.
- No wallet private-key handling.
- No automated transfer.
- No exchange custody.
- No beneficiary doxxing.
- No charity/legal-status claim unless separately established.
- No use of crypto as legal tender wording.
- No support for trading account rescue.

## MODULE_MAP

### MODULE-01 — Policy Layer

Files:

- `DONATION_POLICY.md`
- `TRANSPARENCY_POLICY.md`
- `BENEFICIARY_PRIVACY_POLICY.md`
- `docs/VN_LEGAL_AND_TAX_NOTE.md`

### MODULE-02 — Wallet Metadata

Files:

- `wallets.example.json`
- future `wallets.json` ignored by default until maintainer intentionally publishes a sanitized version.

### MODULE-03 — Ledger Layer

Files:

- `ledger/donations.csv`
- `ledger/disbursements.csv`

### MODULE-04 — Report Generator

Files:

- `scripts/generate_report.py`

### MODULE-05 — Wallet Metadata Validator

Files:

- `scripts/validate_wallets.py`

## CURRENT_STATE

Starter template generated. Wallet addresses are not filled. No donation campaign is active until maintainers complete policy, wallet, and approval details.

## OPEN_ISSUES

- Add real wallet metadata after maintainer decision.
- Decide whether to use multisig before public launch.
- Add tests for report generator.
- Add GitHub Actions for validation.
- Add read-only blockchain explorer importers if needed.
