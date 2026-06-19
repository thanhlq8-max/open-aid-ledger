# Repository Hygiene

Open Aid Ledger is a public transparency project. The repository must remain clean, reviewable, and safe for public contributors.

## Public repository rules

Do not commit:

- local patch application scripts after they have been used
- temporary patch readme files
- local smoke-test output unless intentionally published as a sample report
- private wallet material
- seed phrases, mnemonics, recovery phrases, or API tokens
- real beneficiary personal data
- exchange account credentials
- generated caches or build artifacts

## Allowed helper files

Helper files may be committed only when they are intended as stable project tooling, for example:

- validator scripts under `scripts/`
- documented GitHub workflows under `.github/workflows/`
- official policy documents under `docs/`
- release notes for published versions

## Cleanup checklist before every push

Before pushing to GitHub, check:

```powershell
git status --short
python -m compileall scripts
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv
python scripts\check_public_safety.py .
```

Do not push if any command fails.

## Donation safety lock

Repository hygiene cleanup must not change donation state. The project remains inactive for donations until wallet governance, address verification, reporting, and maintainer approval are complete.