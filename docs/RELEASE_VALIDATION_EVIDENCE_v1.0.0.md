# Release Validation Evidence: v1.0.0

This document records validation evidence for the planned `v1.0.0` repository/template release.

It does not create a release tag, create a GitHub Release, or change operating status.

## Current validation status

```text
RELEASE_TARGET: v1.0.0
VALIDATION_STATUS: MAINTAINER_REPORTED_PASS
FINAL_RUN_URL: NOT_ATTACHED
RELEASE_TAG_CREATED: NO
GITHUB_RELEASE_CREATED: NO
```

## Maintainer-reported evidence

The maintainer reported that validation passed after the latest release-preparation changes.

Before tagging, attach the final GitHub Actions run URL or screenshot reference in the release notes.

## Required final checks

```powershell
python -m compileall scripts tests
python scripts\check_public_safety.py .
python -m pytest -q
```

## Release gate

```text
IF final run evidence is not attached:
    DO_NOT_TAG_RELEASE
```

## Notes for final release

- Use this file as the evidence index for `v1.0.0`.
- Keep release notes in draft state until final run evidence is attached.
- Do not treat this file as an operating activation approval.
