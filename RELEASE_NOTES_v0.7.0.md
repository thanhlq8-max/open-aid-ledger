# Release Notes — v0.7.0 Release Closeout Foundation

## Status

`v0.7.0-release-closeout-foundation`

This release documents completion mapping for the initial six public issues and prepares the repository for clean release tagging.

## Added

- `docs/RELEASE_CLOSEOUT.md`
- `docs/INITIAL_ISSUE_COMPLETION_MAP.md`
- `docs/ISSUE_CLOSEOUT_COMMENTS.md`
- `docs/GITHUB_RELEASE_v0.7.0_DRAFT.md`
- `tests/test_release_closeout_docs.py`

## Completed issue mapping

- #1 — Harden wallet metadata schema: completed by v0.2.0.
- #2 — Add unit tests for wallet and ledger validators: completed by v0.2.0.
- #3 — Add sample transparency report: completed by v0.3.0.
- #4 — Add GitHub Pages static report design: completed by v0.3.0.
- #5 — Design read-only blockchain explorer importer: completed by v0.4.0.
- #6 — Add maintainer governance checklist: completed by v0.5.0.

## Guardrails unchanged

This release does not activate donations, publish real wallet addresses, add signing, add transfers, add custody automation, add trading behavior, issue a token, or promise returns.

## Validation

Expected local validation:

```powershell
python -m compileall scripts tests
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_campaigns.py campaigns\campaigns.example.json --allow-inactive-template
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --enforce-balance
python scripts\validate_ledger.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --enforce-balance
python scripts\check_public_safety.py .
python -m pytest -q
```
