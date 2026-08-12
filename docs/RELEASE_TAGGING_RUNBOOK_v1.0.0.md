# Release Tagging Runbook: v1.0.0

This runbook is now a completed release record for the published `v1.0.0` repository/template release.

It does not publish receiving details or change operating status.

## Completed status

```text
RELEASE_TARGET: v1.0.0
TAGGING_RUNBOOK: COMPLETE
RELEASE_TAG_TARGET: 21b341c50d8e2277eda4134c66bd2ea3155a816e
RELEASE_TAG_CREATED: YES
GITHUB_RELEASE_CREATED: YES
FINAL_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/31373591930
PAGES_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/31373591958
TAG_VALIDATE: VALIDATE_148_PASS
TAG_VALIDATE_RUN_URL: https://github.com/thanhlq8-max/open-aid-ledger/actions/runs/31565722944
TAGGING_STATUS: COMPLETE
LIVE_OPERATION: NO
```

## Preconditions completed

- [x] final `main` release target selected as `21b341c50d8e2277eda4134c66bd2ea3155a816e`;
- [x] release identity is `1.0.0` consistently across `VERSION`, README, and public dashboard source;
- [x] complete repository validation passed on that exact target in Validate #147 attempt 2;
- [x] final public-status recheck completed against that target;
- [x] GitHub Pages #62 built and deployed on that target;
- [x] final release notes matched the repository/template release scope;
- [x] public dashboard remained inactive for donation operation;
- [x] no live receiving details were published;
- [x] maintainer explicitly approved the final repository release gate;
- [x] tag `v1.0.0` was created on the exact target;
- [x] GitHub Release was published;
- [x] tag-triggered Validate #148 passed.

## Historical local validation sequence

The release-preparation validation sequence was:

```powershell
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

## Published release identity

```text
TAG: v1.0.0
TAG_TARGET: 21b341c50d8e2277eda4134c66bd2ea3155a816e
RELEASE_TYPE: repository-template-release
GITHUB_RELEASE_ID: 369005821
LIVE_OPERATION: NO
```

The published tag is retained as historical release evidence. Do not delete, recreate, or move it merely to follow later `main` commits.

## Post-release follow-up

- Use `docs/RELEASE_NOTES_v1.0.0.md` as the canonical corrected release text if GitHub Release metadata needs manual correction.
- Keep post-release documentation commits distinct from the immutable release target.
- Preserve all inactive operating locks unless a separate activation proposal is explicitly approved.
