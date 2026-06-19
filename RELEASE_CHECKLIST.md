# Release Checklist

Use this checklist before publishing the repository or activating donation wallets.

## Repository publication

- [ ] Repository name is neutral and non-scammy, such as `open-aid-ledger`.
- [ ] Repository is public.
- [ ] README states that donations are inactive until real wallet addresses are published.
- [ ] `LICENSE` exists.
- [ ] `SECURITY.md` exists.
- [ ] Issue templates are present.
- [ ] GitHub Actions validation passes.
- [ ] No private keys, seed phrases, identity documents, or private beneficiary data are committed.

## Wallet activation

- [ ] `wallets.example.json` has been copied to `wallets.json`.
- [ ] Wallet addresses have been verified outside GitHub.
- [ ] At least two maintainers have reviewed wallet addresses.
- [ ] If expected balances are meaningful, multisig has been used.
- [ ] Address-change process is documented.
- [ ] Donation policy matches active campaigns.
- [ ] Transparency policy matches active reporting cadence.

## Campaign activation

- [ ] Campaign scope is precise.
- [ ] Prohibited uses are clear.
- [ ] Beneficiary privacy policy is enforced.
- [ ] Evidence process is documented.
- [ ] Disbursement approval process is documented.
- [ ] Conflict-of-interest rule is active.

## Validation commands

```bash
python -m compileall scripts
python scripts/validate_wallets.py wallets.example.json --allow-placeholders
python scripts/validate_ledger.py --donations ledger/donations.csv --disbursements ledger/disbursements.csv
python scripts/check_public_safety.py .
python scripts/generate_report.py --donations ledger/donations.csv --disbursements ledger/disbursements.csv --out reports/local-smoke-report.md
```
