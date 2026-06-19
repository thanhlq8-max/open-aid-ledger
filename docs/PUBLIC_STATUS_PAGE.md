# Public Status Page

This document defines the static public status page for Open Aid Ledger.

## Objective

Provide a simple GitHub-rendered status page that lets visitors see the project state without reading the full repository.

The status page must make the inactive donation state obvious.

## Canonical page

The canonical public status page is:

```text
docs/index.md
```

If GitHub Pages is enabled later, the same file may be served as the project site entry page.

## Required status block

The public status page must include these exact safety values:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

These values may only change through a dedicated reviewed release process.

## Required sections

The page should include:

- current status;
- public status dashboard;
- links to sample reports;
- links to governance documents;
- links to policy documents;
- safety boundaries;
- next milestone.

## Prohibited content

The status page must not include:

- real wallet addresses before approval;
- private keys or seed phrases;
- transaction signing instructions;
- exchange withdrawal API instructions;
- trading-account top-up language;
- margin-call support language;
- financial return promises;
- beneficiary-identifying private information.

## Update procedure

When the project changes, update:

1. `VERSION`;
2. `README.md`;
3. `docs/index.md`;
4. `docs/POST_PUBLISH_STATUS.md`;
5. `CHANGELOG.md`;
6. release notes.

Then run:

```powershell
python scripts\validate_static_status.py .
python scripts\check_public_safety.py .
python -m pytest -q
```
