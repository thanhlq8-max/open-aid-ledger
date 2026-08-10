# Release Validation Evidence: v1.0.0

This document records validation evidence for the planned `v1.0.0` repository/template release.

It does not create a release tag, create a GitHub Release, or change operating status.

## Current validation status

```text
RELEASE_TARGET: v1.0.0
VALIDATED_BASELINE_COMMIT: 95f6424
VALIDATED_BASELINE_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/77196823903
VALIDATED_BASELINE_RUN_LABEL: Validate #116
VALIDATED_BASELINE_STATUS: PASS
RELEASE_METADATA_COMMIT: RESOLVE_FROM_GIT_AT_RUNTIME
RELEASE_TAG_TARGET: NOT_SELECTED
RELEASE_TAG_CREATED: NO
GITHUB_RELEASE_CREATED: NO
```

`VALIDATED_BASELINE_COMMIT` records the historical commit that has attached validation evidence. It is not a moving claim about the future release tag target. `RELEASE_METADATA_COMMIT` and the final tag target must be resolved from Git after the last release-preparation mutation and freshly validated before tagging.

## Maintainer-provided evidence

- Screenshot evidence: GitHub Actions page showing `Validate #116` passed for commit `95f6424`.
- Log archive evidence: `logs_77196823903.zip`.
- Log check: `python -m pytest -q` completed with `81 passed in 0.53s`.
- Log check: public safety scan completed with `public safety scan OK`.
- Log check: compile step completed for scripts and tests.

## Required final checks

Before selecting a final tag target, run the complete repository validation on the final intended commit, including:

```powershell
python -m compileall scripts tests
python scripts\validate_release_consistency.py .
python scripts\check_public_safety.py .
python -m pytest -q
```

The GitHub Actions `Validate` workflow must also pass for the final intended commit. Tag-specific validation is configured for `v*` pushes, but creating the tag remains a separate maintainer-approved action.

## Release gate

```text
IF final intended commit has fresh validation evidence
AND release notes match the target
AND maintainer explicitly approves the tag:
    TAGGING_MAY_PROCEED
ELSE:
    TAGGING_BLOCKED
```

## Notes for final release

- Use this file as the historical and final-evidence index for `v1.0.0`.
- Do not update a file with a self-referential claim that its own commit is already the final tag target.
- Do not treat repository release evidence as an operating activation approval.
- Tagging and GitHub Release creation remain separate manual actions.
