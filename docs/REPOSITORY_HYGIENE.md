# Repository Hygiene

This repository should remain clean enough for public review.

## Do not commit

- `apply_v*.ps1`
- `PATCH_README.txt`
- `README_PATCH.md`
- `README_RESTORE.md`
- `reports/local-smoke-report.md`
- `reports/ci-report.md`
- private keys
- seed phrases
- exchange credentials
- real beneficiary private data

## Required checks before commit

```powershell
python -m compileall scripts
python scripts
alidate_wallets.py wallets.example.json --allow-placeholders
python scripts
alidate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --enforce-balance
python scripts\check_public_safety.py .
python -m pytest
```

## Release discipline

A patch script may be used locally, but it must delete itself or be removed before commit.

