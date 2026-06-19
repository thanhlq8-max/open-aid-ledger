# Initial Issue Completion Map

This document maps the first six public issues to the releases that completed them.

| Issue | Title | Completed by | Evidence |
|---:|---|---|---|
| #1 | Harden wallet metadata schema | v0.2.0 | `wallets.example.json`, `scripts/validate_wallets.py`, `docs/WALLET_SCHEMA.md`, wallet validator tests |
| #2 | Add unit tests for wallet and ledger validators | v0.2.0 | `tests/test_wallets.py`, `tests/test_ledger.py`, CI pytest step |
| #3 | Add sample transparency report | v0.3.0 | `reports/sample-transparency-report.md`, `examples/sample-ledger/`, report generation tests |
| #4 | Add GitHub Pages static report design | v0.3.0 | `docs/GITHUB_PAGES_STATIC_REPORT.md`, `docs/index.md` |
| #5 | Design read-only blockchain explorer importer | v0.4.0 | `docs/BLOCKCHAIN_EXPLORER_IMPORTER_DESIGN.md`, `docs/IMPORTER_NORMALIZED_TX_SCHEMA.md`, `docs/IMPORTER_MANUAL_RECONCILIATION.md` |
| #6 | Add maintainer governance checklist | v0.5.0 | `docs/MAINTAINER_GOVERNANCE_CHECKLIST.md`, `docs/DONATION_ACTIVATION_CHECKLIST.md`, `docs/EMERGENCY_FREEZE_PROCEDURE.md` |

## Closeout status

All six issues are eligible to be closed after v0.7.0 is merged and GitHub Actions passes.

## Guardrail note

None of these closures activate donations, publish real wallet addresses, create custody automation, add transaction signing, add trading behavior, or promise returns.
