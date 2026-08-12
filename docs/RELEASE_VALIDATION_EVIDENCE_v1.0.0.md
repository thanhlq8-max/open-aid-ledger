# Release Validation Evidence: v1.0.0

This document records historical and final validation evidence for the published `v1.0.0` repository/template release.

Repository release evidence does not change operating status.

## Published release evidence

```text
RELEASE_TARGET: v1.0.0
RELEASE_STATUS: RELEASED
RELEASE_TAG_TARGET: 21b341c50d8e2277eda4134c66bd2ea3155a816e
FINAL_TARGET_VALIDATE: VALIDATE_147_ATTEMPT_2_PASS
FINAL_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/31373591930
PAGES_RUNTIME: PAGES_62_PASS
PAGES_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/31373591958
RELEASE_TAG_CREATED: YES
GITHUB_RELEASE_CREATED: YES
TAG_VALIDATE: VALIDATE_148_PASS
TAG_VALIDATE_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/31565722944
GITHUB_RELEASE_ID: 369005821
LIVE_OPERATION: NO
```

The `v1.0.0` tag points to exact commit `21b341c50d8e2277eda4134c66bd2ea3155a816e`. Validate #147 attempt 2 passed on that exact target after maintainer approval. GitHub Pages #62 built and deployed successfully on the same target. After tag publication, Validate #148 passed on `v1.0.0`.

## Historical validation baseline

```text
VALIDATED_BASELINE_COMMIT: 95f6424
VALIDATED_BASELINE_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/77196823903
VALIDATED_BASELINE_RUN_LABEL: Validate #116
VALIDATED_BASELINE_STATUS: PASS
```

The historical baseline is retained for traceability. It is not the final release target.

## Historical maintainer-provided evidence

- Screenshot evidence: GitHub Actions page showing `Validate #116` passed for commit `95f6424`.
- Log archive evidence: `logs_77196823903.zip`.
- Log check: `python -m pytest -q` completed with `81 passed in 0.53s`.
- Log check: public safety scan completed with `public safety scan OK`.
- Log check: compile step completed for scripts and tests.

## Final release checks completed

- Exact release target selected and read back.
- Complete repository validation passed on that target.
- Public-safety scan and full tests passed in Validate #147 attempt 2.
- GitHub Pages exact-target build/deploy passed in Pages #62.
- Final public-status recheck passed while all inactive operating locks remained unchanged.
- Maintainer explicitly approved the repository release gate.
- Tag `v1.0.0` was created on the selected target.
- GitHub Release was published.
- Tag-triggered Validate #148 passed.

## Evidence semantics

- Do not use a later post-release `main` commit as the historical `v1.0.0` tag target.
- Do not add a self-referential `FINAL_COMMIT` field to a commit that describes itself.
- Do not treat repository release evidence as operating activation approval.
- Keep later post-release state synchronization separate from the immutable release-target record.
