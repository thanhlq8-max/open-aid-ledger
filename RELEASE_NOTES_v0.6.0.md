# Release Notes v0.6.0 — Campaign Lifecycle Foundation

## Summary

v0.6.0 adds campaign lifecycle documentation and campaign metadata validation.

## Added

- `campaigns/campaigns.example.json`
- `scripts/validate_campaigns.py`
- `tests/test_campaigns.py`
- `docs/CAMPAIGN_LIFECYCLE.md`
- `docs/CAMPAIGN_STATUS_SCHEMA.md`
- `docs/CAMPAIGN_REVIEW_CHECKLIST.md`
- `docs/ISSUE_RELEASE_MAPPING.md`

## Updated

- `README.md`
- `CHANGELOG.md`
- `VERSION`
- `.github/workflows/validate.yml`
- `docs/ROADMAP.md`
- `docs/POST_PUBLISH_STATUS.md`

## Safety boundary

This release does not activate donations, publish wallets, sign transactions, move assets, use exchange APIs, create tokens, add trading logic, or promise financial return.

## Validation

Expected validation commands:

```powershell
python -m compileall scripts tests
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_campaigns.py campaigns\campaigns.example.json --allow-inactive-template
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --enforce-balance
python scripts\validate_ledger.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --enforce-balance
python scripts\check_public_safety.py .
python -m pip install -r requirements-dev.txt
python -m pytest -q
```
