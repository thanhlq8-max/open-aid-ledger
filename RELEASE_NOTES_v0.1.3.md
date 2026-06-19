# Release Notes â€” v0.1.3 Restore README Cleanup

## Status

```text
STATUS: PATCH_RELEASE
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Summary

This patch restores the main project README after the v0.1.2 helper instructions were accidentally committed as `README.md`.

It also removes local patch-helper artifacts from the public repository tree.

## Changes

- Restore `README.md` to the main Open Aid Ledger project overview.
- Keep public status and donation guardrails visible at the top of README.
- Remove patch helper files from the repository tree:
  - `README_PATCH.md`
  - `README_RESTORE.md`
  - `apply_v0.1.1_post_publish_cleanup.ps1`
  - `apply_v0.1.2_public_repo_hygiene.ps1`
  - `apply_v0.1.3_restore_readme_cleanup.ps1`
- Update `VERSION` to `0.1.3-restore-readme-cleanup`.
- Add this release note.
- Record the incident in repository hygiene documentation.

## Validation

Run:

```powershell
python -m compileall scripts
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv
python scripts\check_public_safety.py .
python scripts\generate_report.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --out reports\local-smoke-report.md
```

## Scope guard

This release does not activate donations, publish wallets, add custody automation, add private-key handling, add trading behavior, or change ledger logic.