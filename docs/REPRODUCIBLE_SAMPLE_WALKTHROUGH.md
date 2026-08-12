# Reproducible Sample Walkthrough

This walkthrough gives a new user one deterministic, local, read-only path from the bundled sample ledger to a validated transparency report.

It uses fictional sample records only. It does not query a blockchain, sign a transaction, publish a receiving address, activate donations, or change repository operating status.

## Safety boundary

```text
PROJECT_STATUS: PUBLIC_TEMPLATE
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
CUSTODY_AUTOMATION: NO
GO_LIVE: NO
```

If any public status says donations or wallets are inactive, do not send funds.

## Prerequisite

Run the commands from the repository root with Python available.

The sample path uses only repository files:

```text
examples/sample-ledger/donations.csv
examples/sample-ledger/disbursements.csv
scripts/validate_ledger.py
scripts/generate_report.py
```

## Step 1 — validate the bundled sample ledger

PowerShell:

```powershell
python scripts\validate_ledger.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --enforce-balance
```

Expected result:

```text
ledger CSV files OK
```

The command must exit successfully. It is read-only and does not modify the CSV files.

## Step 2 — generate a sample transparency report

PowerShell:

```powershell
python scripts\generate_report.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --out artifacts\sample-transparency-report.md --title "Open Aid Ledger Sample Transparency Report"
```

Expected result:

```text
Wrote ...sample-transparency-report.md
```

Open:

```text
artifacts/sample-transparency-report.md
```

The report is generated locally from the two bundled CSV files.

## Step 3 — compare deterministic expected output

The sample inputs contain:

```text
Donation records: 3
Disbursement records: 2
```

Expected incoming totals:

| Chain | Asset | Network | Amount |
|---|---|---|---:|
| Bitcoin | BTC | Bitcoin | 0.0125 |
| Ethereum | USDT | ERC20 | 125 |
| Tron | USDT | TRC20 | 80 |

Expected outgoing totals:

| Chain | Asset | Network | Amount |
|---|---|---|---:|
| Ethereum | USDT | ERC20 | 60 |
| Tron | USDT | TRC20 | 40 |

Expected net balances:

| Chain | Asset | Network | Incoming | Outgoing | Net |
|---|---|---|---:|---:|---:|
| Bitcoin | BTC | Bitcoin | 0.0125 | 0 | 0.0125 |
| Ethereum | USDT | ERC20 | 125 | 60 | 65 |
| Tron | USDT | TRC20 | 80 | 40 | 40 |

These values are derived only from the committed fictional sample rows. They are not live balances and must not be presented as real donations or real disbursements.

## Step 4 — optional repository checks

After the sample path succeeds, run the normal safety and regression checks:

```powershell
python scripts\validate_static_status.py .
python scripts\validate_release_consistency.py .
python scripts\check_public_safety.py .
python -m pytest -q
```

## Success contract

The walkthrough passes only when all of the following are true:

- sample ledger validation exits successfully;
- output includes `ledger CSV files OK`;
- the generated report is created at the requested local output path;
- record counts are 3 donations and 2 disbursements;
- expected incoming, outgoing and net totals match the tables above;
- no source sample CSV is changed;
- no live receiving details are introduced;
- `DONATIONS_ACTIVE`, `WALLETS_PUBLISHED`, `ACTIVATION_APPROVED` and `GO_LIVE` remain `NO`.

## What this proves

This walkthrough proves that a user can reproduce the repository's basic sample-ledger validation and Markdown-report workflow from committed fictional data.

It does not prove legal readiness, donation activation, custody readiness, real-world adoption, or production operation.
