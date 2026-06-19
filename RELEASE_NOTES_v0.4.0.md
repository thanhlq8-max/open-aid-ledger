# Release Notes — v0.4.0

## Read-only Blockchain Explorer Importer Design

This release adds a design-only foundation for future public blockchain explorer importers.

## Added

- `docs/BLOCKCHAIN_EXPLORER_IMPORTER_DESIGN.md`
- `docs/IMPORTER_NORMALIZED_TX_SCHEMA.md`
- `docs/IMPORTER_MANUAL_RECONCILIATION.md`
- `examples/importer/normalized_transactions.sample.csv`
- `tests/test_importer_design_docs.py`

## Scope

The importer design is read-only and manual-review-first. It may be used in a future release to help reconcile public incoming transactions into staging files.

## Explicit non-goals

This release does not add:

- donation activation;
- real wallet addresses;
- private key handling;
- seed phrase handling;
- transaction signing;
- asset transfer;
- exchange withdrawal APIs;
- custody automation;
- mixer integration;
- trading logic;
- return promises;
- beneficiary doxxing.

## Validation

Run:

```powershell
python -m compileall scripts tests
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --enforce-balance
python scripts\validate_ledger.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --enforce-balance
python scripts\check_public_safety.py .
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
