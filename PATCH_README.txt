# Open Aid Ledger v0.1.3 Restore README Cleanup Patch

This patch fixes the v0.1.2 mistake where patch instructions were committed as the main `README.md`.

## Apply

Copy `apply_v0.1.3_restore_readme_cleanup.ps1` into the root of `F:\GitHub\open-aid-ledger`, then run:

```powershell
cd F:\GitHub\open-aid-ledger
powershell -ExecutionPolicy Bypass -File .\apply_v0.1.3_restore_readme_cleanup.ps1
```

## Commit

After validation passes, commit in GitHub Desktop:

```text
Restore project README and clean helper artifacts
```

## Scope

This patch restores the project README, removes helper patch artifacts, updates release notes/docs, and keeps donation activation disabled.
