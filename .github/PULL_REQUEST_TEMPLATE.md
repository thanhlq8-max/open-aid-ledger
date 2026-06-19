## Summary


## Change type

- [ ] Documentation
- [ ] Ledger update
- [ ] Wallet metadata change
- [ ] Campaign update
- [ ] Script/tooling update
- [ ] Policy/governance update

## Safety checks

- [ ] No private keys or seed phrases
- [ ] No exchange credentials or API keys
- [ ] No private beneficiary data
- [ ] No trading signal / investment promise wording
- [ ] No wallet address change without following `docs/ADDRESS_CHANGE_PROCEDURE.md`

## Validation

```bash
python -m compileall scripts
python scripts/validate_wallets.py wallets.example.json --allow-placeholders
python scripts/validate_ledger.py --donations ledger/donations.csv --disbursements ledger/disbursements.csv
python scripts/check_public_safety.py .
```
