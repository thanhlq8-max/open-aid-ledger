# Open Aid Ledger v0.1.4 â€” Final Helper Cleanup

## Status

This is a cleanup release for the public template state.

```text
PROJECT_STATUS: PUBLIC_TEMPLATE
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Changes

- Removes residual local patch helper artifacts from the public repository root.
- Preserves the restored project README.
- Updates the public template version to `0.1.4-final-helper-cleanup`.
- Documents that future patches must not leave apply scripts or patch README files in the repository root.

## Removed artifacts

The following local-only files must not remain tracked in the public repository:

```text
PATCH_README.txt
README_PATCH.md
README_RESTORE.md
apply_v0.1.1_post_publish_cleanup.ps1
apply_v0.1.2_public_repo_hygiene.ps1
apply_v0.1.3_restore_readme_cleanup.ps1
```

## Non-goals

This release does not:

- activate donations;
- publish real wallet addresses;
- add custody automation;
- add wallet signing;
- add trading behavior;
- change ledger semantics.

## Validation

Run from repository root:

```powershell
python -m compileall scripts
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv
python scripts\check_public_safety.py .
python scripts\generate_report.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --out reports\local-smoke-report.md
```