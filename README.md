# Open Aid Ledger v0.1.2 Public Repository Hygiene Patch

This patch removes helper artifacts that were used to apply v0.1.1 but should not remain in the public repository.

## Apply

Copy `apply_v0.1.2_public_repo_hygiene.ps1` into the root of `F:\GitHub\open-aid-ledger`, then run:

```powershell
cd F:\GitHub\open-aid-ledger
powershell -ExecutionPolicy Bypass -File .\apply_v0.1.2_public_repo_hygiene.ps1
```

## Commit

After validation passes, commit in GitHub Desktop:

```text
Clean public repository helper artifacts
```

## Scope

This patch does not activate donations, publish wallets, add custody automation, add private-key handling, add trading behavior, or change ledger logic.
