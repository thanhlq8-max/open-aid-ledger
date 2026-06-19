# Open Aid Ledger v0.8.0 — Donation Readiness Dry Run

## Summary

This release adds a dry-run-only donation readiness layer.

It verifies that the repository has the structural controls needed for a future donation-ready release while keeping donation collection inactive.

## Added

- `docs/DONATION_READINESS_DRY_RUN.md`
- `docs/DRY_RUN_WALLET_PUBLICATION_REVIEW.md`
- `docs/DONATION_LAUNCH_RISK_REGISTER.md`
- `docs/DONATION_LAUNCH_RUNBOOK.md`
- `examples/dry-run/wallets.dry-run.example.json`
- `scripts/validate_readiness.py`
- `tests/test_readiness.py`

## Updated

- `README.md`
- `CHANGELOG.md`
- `VERSION`
- `.github/workflows/validate.yml`
- `docs/ROADMAP.md`
- `docs/POST_PUBLISH_STATUS.md`

## Safety boundary

This release does not:

- activate donations;
- publish real wallet addresses;
- store private keys;
- store seed phrases;
- sign transactions;
- move assets;
- call exchange APIs;
- automate custody;
- add trading logic;
- issue tokens;
- promise returns.
