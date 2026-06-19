# Release Notes v0.5.0 — Maintainer Governance Checklist

## Status

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Added

- `docs/MAINTAINER_GOVERNANCE_CHECKLIST.md`
- `docs/DONATION_ACTIVATION_CHECKLIST.md`
- `docs/EMERGENCY_FREEZE_PROCEDURE.md`
- `docs/CONFLICT_OF_INTEREST_DISCLOSURE_TEMPLATE.md`
- `docs/GOVERNANCE_DECISION_RECORD.md`
- `tests/test_governance_docs.py`

## Scope

This release adds operational governance documents and tests. It does not activate donations, publish real wallet addresses, handle private keys, sign transactions, automate transfers, connect to exchange withdrawal APIs, add trading logic, issue tokens, or promise returns.

## Validation

Expected local validation:

```powershell
python -m compileall scripts tests
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --enforce-balance
python scripts\validate_ledger.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --enforce-balance
python scripts\check_public_safety.py .
python -m pytest -q
```
