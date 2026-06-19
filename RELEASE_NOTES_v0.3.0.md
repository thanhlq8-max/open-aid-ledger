# Open Aid Ledger v0.3.0 — Sample Transparency Report + GitHub Pages Foundation

## Status

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Added

- Sample transparency report under `reports/sample-transparency-report.md`.
- Sample ledger CSVs under `examples/sample-ledger/`.
- GitHub Pages static-report design under `docs/GITHUB_PAGES_STATIC_REPORT.md`.
- Initial `docs/index.md` public status page.
- Report-generation tests for non-empty and cancelled-row scenarios.
- CI check that generates a sample report from sample ledger rows.

## Not changed

- No real wallet address is published.
- Donation collection remains inactive.
- No blockchain network fetching is added.
- No custody, signing, transfer, exchange, or trading logic is added.
