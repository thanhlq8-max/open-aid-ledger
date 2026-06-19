# Release Notes — v0.9.0 Static Public Status Page

## Summary

This release finalizes the static public status page foundation for Open Aid Ledger.

## Added

- `docs/index.md` as the canonical public status page.
- `docs/PUBLIC_STATUS_PAGE.md`.
- `docs/PAGES_DEPLOYMENT_CHECKLIST.md`.
- `docs/STATUS_BADGE_GUIDE.md`.
- `scripts/validate_static_status.py`.
- Static status page regression tests.

## Safety boundary

This release does not activate donations, publish wallets, implement custody automation, add private-key handling, call exchange APIs, add trading logic, issue tokens, or promise financial return.

## Validation

Expected local validation:

```powershell
python -m compileall scripts tests
python scripts\validate_static_status.py .
python scripts\check_public_safety.py .
python -m pytest -q
```
