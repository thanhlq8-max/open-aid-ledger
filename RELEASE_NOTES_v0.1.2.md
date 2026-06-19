# Release Notes â€” v0.1.2 Public Repository Hygiene

Status: PUBLIC_REPO_HYGIENE_CLEANUP

This release removes local patch helper artifacts that were accidentally committed during the v0.1.1 post-publish cleanup flow.

## Changes

- Remove `README_PATCH.md` from the public repository.
- Remove `apply_v0.1.1_post_publish_cleanup.ps1` from the public repository.
- Add `docs/REPOSITORY_HYGIENE.md`.
- Update `VERSION` to `0.1.2-public-repo-hygiene`.
- Keep all donation safety guardrails unchanged.

## Safety statement

This release does not:

- activate donations
- publish real wallet addresses
- add custody automation
- add private-key handling
- add trading or investment behavior
- add return promises
- change ledger semantics

## Validation

Run:

```powershell
python -m compileall scripts
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv
python scripts\check_public_safety.py .
python scripts\generate_report.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --out reports\local-smoke-report.md
```

Expected result: all commands pass.