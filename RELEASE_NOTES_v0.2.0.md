# Release Notes — v0.2.0 Ledger Safety Foundation

## Status

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Added

- Wallet metadata schema v1.1.
- Stronger wallet validator checks.
- Stronger ledger validator checks.
- Optional balance enforcement for outgoing support.
- Validator regression tests.
- `requirements-dev.txt` for test dependencies.
- Wallet schema documentation.
- Ledger validation documentation.

## Changed

- CI now installs dev dependencies and runs `pytest`.
- Transparency report now includes net balance by asset.
- `.gitignore` now ignores local patch helper scripts and patch README artifacts.

## Not included

- No wallet publication.
- No donation activation.
- No private-key handling.
- No blockchain explorer importer.
- No custody automation.
- No trading or investment logic.

