# Try the Sample in 5 Minutes

This is the fastest way to see what Open Aid Ledger actually does.

You will use fictional sample records that are already included in the repository. The exercise validates the ledger, generates a Markdown transparency report, and lets you compare the result with known expected totals.

**No real funds, wallet, blockchain connection, or live receiving details are involved.**

## What you should get at the end

If everything works, you will have:

- a validated sample ledger;
- a generated file at `artifacts/sample-transparency-report.md`;
- 3 fictional donation records and 2 fictional disbursement records;
- net sample balances of `0.0125 BTC`, `65 USDT` on ERC20, and `40 USDT` on TRC20.

## Before you begin

You need:

- a local copy of this repository;
- Python available from your terminal;
- PowerShell or another shell from the repository root.

The walkthrough uses these committed files:

```text
examples/sample-ledger/donations.csv
examples/sample-ledger/disbursements.csv
scripts/validate_ledger.py
scripts/generate_report.py
```

The commands below use Windows-style paths so they can be copied directly into PowerShell:

```text
examples\sample-ledger\donations.csv
examples\sample-ledger\disbursements.csv
scripts\validate_ledger.py
scripts\generate_report.py
```

## Step 1 — check the sample ledger

Run:

```powershell
python scripts\validate_ledger.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --enforce-balance
```

Expected result:

```text
ledger CSV files OK
```

This command checks the committed fictional CSV files. It does not modify them.

## Step 2 — generate the sample report

Run:

```powershell
python scripts\generate_report.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --out artifacts\sample-transparency-report.md --title "Open Aid Ledger Sample Transparency Report"
```

Expected terminal output includes a message similar to:

```text
Wrote ...sample-transparency-report.md
```

Now open:

```text
artifacts/sample-transparency-report.md
```

You should see a transparency report generated from the two sample CSV files.

## Step 3 — check that the result makes sense

The fictional sample contains:

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

If your report matches these totals, you have reproduced the repository's basic ledger-to-report workflow.

These are fictional sample values. They are not live balances, real donations, or real disbursements.

## What did you just prove?

You proved something narrow but useful: a person can start with committed ledger records, validate them, generate a public-style report, and independently check the expected totals.

You did **not** prove that the project is ready to collect donations, legally approved, safe for custody, or operating in production.

## Want to go deeper?

If you are evaluating the repository as a maintainer or reviewer, the next useful documents are:

- [Start Here](START_HERE.md)
- [Dry-run Operations Runbook](DRY_RUN_OPERATIONS_RUNBOOK.md)
- [Review Packet Template](REVIEW_PACKET_TEMPLATE.md)
- [Operational Readiness Matrix](OPERATIONAL_READINESS_MATRIX.md)

Optional repository checks:

```powershell
python scripts\validate_static_status.py .
python scripts\validate_release_consistency.py .
python scripts\check_public_safety.py .
python -m pytest -q
```

## Safety status

The block below is kept explicit for both people and automated checks:

```text
PROJECT_STATUS: PUBLIC_TEMPLATE
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
CUSTODY_AUTOMATION: NO
GO_LIVE: NO
```

If any public status says donations or wallets are inactive, do not send funds.

## Reproducibility checklist

The walkthrough passes when:

- sample ledger validation exits successfully;
- output includes `ledger CSV files OK`;
- `artifacts/sample-transparency-report.md` is created;
- record counts are 3 donations and 2 disbursements;
- the incoming, outgoing, and net totals match the tables above;
- the source sample CSV files remain unchanged;
- no live receiving details are introduced;
- `DONATIONS_ACTIVE`, `WALLETS_PUBLISHED`, `ACTIVATION_APPROVED`, and `GO_LIVE` remain `NO`.
