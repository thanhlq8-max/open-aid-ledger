# Release Tagging Runbook: v1.0.0

This runbook prepares the final manual steps for the `v1.0.0` repository/template release.

It does not create a release tag, create a GitHub Release, publish receiving details, or change operating status.

## Current status

```text
RELEASE_TARGET: v1.0.0
TAGGING_RUNBOOK: READY
RELEASE_TAG_CREATED: NO
GITHUB_RELEASE_CREATED: NO
FINAL_RUN_URL: NOT_ATTACHED
LIVE_OPERATION: NO
```

## Preconditions

Before creating a tag or GitHub Release, confirm:

- [ ] latest `main` commit is the intended release commit;
- [ ] GitHub Actions passed on the intended release commit;
- [ ] final run URL or screenshot reference is attached to release evidence;
- [ ] release notes are no longer draft;
- [ ] public status recheck is complete;
- [ ] public dashboard still shows inactive operating status;
- [ ] no live receiving details are published.

## Local command sequence

Run from the local clone:

```powershell
git checkout main
git pull origin main
git status --short
python -m compileall scripts tests
python scripts\check_public_safety.py .
python -m pytest -q
```

Only after the evidence files are updated and committed:

```powershell
git tag -a v1.0.0 -m "Open Aid Ledger v1.0.0"
git push origin v1.0.0
```

## GitHub Release checklist

- [ ] Open GitHub Releases.
- [ ] Draft a new release from tag `v1.0.0`.
- [ ] Use `docs/RELEASE_NOTES_DRAFT_v1.0.0.md` as the base.
- [ ] Link the final validation evidence file.
- [ ] Link the public status recheck file.
- [ ] Confirm the release text says this is a repository/template release.
- [ ] Confirm the release text does not describe live operation.

## Release gate

```text
IF final run evidence is not attached:
    DO_NOT_TAG_RELEASE
```

## Final expected release identity

```text
TAG: v1.0.0
RELEASE_TYPE: repository-template-release
LIVE_OPERATION: NO
```
