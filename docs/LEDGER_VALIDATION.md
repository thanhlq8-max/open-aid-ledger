# Ledger Validation Contract

Open Aid Ledger uses CSV files as the source of truth for public donation and disbursement records.

## Files

- `ledger/donations.csv`
- `ledger/disbursements.csv`

## Core rules

The validator checks:

- exact column order;
- required values for non-empty rows;
- positive numeric amounts;
- allowed status values;
- date format;
- safe identifier format;
- duplicate transaction references;
- beneficiary privacy level values;
- optional asset-level balance enforcement.

## Commands

Base validation:

```powershell
python scripts
alidate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv
```

Balance enforcement:

```powershell
python scripts
alidate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --enforce-balance
```

## Non-goals

The validator does not:

- query blockchains;
- sign transactions;
- transfer funds;
- connect to exchanges;
- decide who should receive support;
- provide legal, tax, financial, or investment advice.

