# Open Aid Ledger v0.1.1 Post-Publish Cleanup Patch

This bundle applies documentation-only post-publish cleanup for `thanhlq8-max/open-aid-ledger`.

It does **not** activate donations, publish wallets, add custody automation, add trading behavior, or change ledger logic.

## Apply

```powershell
cd F:\GitHub\open-aid-ledger
powershell -ExecutionPolicy Bypass -File .\apply_v0.1.1_post_publish_cleanup.ps1
```

Then run the validation commands shown by the script and commit through GitHub Desktop:

```text
Summary: Document v0.1.1 post-publish cleanup
```
