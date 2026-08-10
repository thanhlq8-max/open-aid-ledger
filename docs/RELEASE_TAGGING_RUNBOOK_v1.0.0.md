# Release Tagging Runbook: v1.0.0

This runbook prepares the final manual steps for the `v1.0.0` repository/template release.

It does not create a release tag, create a GitHub Release, publish receiving details, or change operating status.

## Current status

```text
RELEASE_TARGET: v1.0.0
TAGGING_RUNBOOK: READY
RELEASE_TAG_TARGET: NOT_SELECTED
RELEASE_TAG_CREATED: NO
GITHUB_RELEASE_CREATED: NO
FINAL_RUN_URL: NOT_ATTACHED
TAGGING_STATUS: BLOCKED
LIVE_OPERATION: NO
```

`TAGGING_RUNBOOK: READY` means the procedure is documented. It does not mean the release itself is ready to tag.

## Preconditions

Before creating a tag or GitHub Release, confirm:

- [ ] latest `main` commit is the exact intended release commit;
- [ ] release identity is `1.0.0` consistently across `VERSION`, README, and public dashboard source;
- [ ] `RELEASE_TAG_TARGET` identifies the exact final intended commit;
- [ ] complete repository validation passed on that exact commit;
- [ ] final run URL or equivalent authoritative evidence is attached to release evidence;
- [ ] final public-status recheck is complete against that exact commit;
- [ ] required GitHub Pages runtime evidence is attached;
- [ ] `docs/RELEASE_NOTES_v1.0.0.md` matches the selected target;
- [ ] public dashboard still shows inactive operating status;
- [ ] no live receiving details are published;
- [ ] maintainer has explicitly approved the final tag.

## Local validation sequence

Run from the local clone after the release identity transition is committed:

```powershell
git checkout main
git pull origin main
git status --short
python -m compileall scripts tests
python scripts\validate_wallets.py wallets.example.json --allow-placeholders
python scripts\validate_campaigns.py campaigns\campaigns.example.json --allow-inactive-template
python scripts\validate_readiness.py .
python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --enforce-balance
python scripts\validate_ledger.py --donations examples\sample-ledger\donations.csv --disbursements examples\sample-ledger\disbursements.csv --enforce-balance
python scripts\validate_static_status.py .
python scripts\validate_release_consistency.py .
python scripts\validate_candidate.py .
python scripts\validate_rc1.py .
python scripts\validate_rc2.py .
python scripts\validate_rc3.py .
python scripts\check_public_safety.py .
python -m pytest -q
```

Only after every precondition is satisfied and the maintainer gives explicit final approval:

```powershell
git tag -a v1.0.0 -m "Open Aid Ledger v1.0.0"
git push origin v1.0.0
```

## GitHub Release checklist

- [ ] Open GitHub Releases.
- [ ] Draft a new release from tag `v1.0.0`.
- [ ] Use `docs/RELEASE_NOTES_v1.0.0.md` as the release text base.
- [ ] Link the final validation evidence file.
- [ ] Link the final public status recheck file.
- [ ] Confirm the release text says this is a repository/template release.
- [ ] Confirm the release text does not describe live operation.

## Release gate

```text
IF RELEASE_TAG_TARGET is NOT_SELECTED:
    DO_NOT_TAG_RELEASE
IF FINAL_RUN_URL is NOT_ATTACHED:
    DO_NOT_TAG_RELEASE
IF any precondition is unresolved:
    DO_NOT_TAG_RELEASE
```

## Final expected release identity

```text
TAG: v1.0.0
RELEASE_TYPE: repository-template-release
LIVE_OPERATION: NO
```
