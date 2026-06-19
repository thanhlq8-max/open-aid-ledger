# Release Closeout

This document defines how Open Aid Ledger closes completed issues and prepares release notes.

## Purpose

The repository now has enough public infrastructure to close the initial seed issues without activating donations.

Release closeout records:

- which issue was completed;
- which version completed it;
- what files or tests prove completion;
- whether any follow-up scope remains;
- whether core safety guardrails changed.

## Closeout rules

An issue can be closed only when all of these are true:

1. The implemented scope maps directly to the issue objective.
2. The relevant docs, scripts, examples, or tests are merged into `main`.
3. GitHub Actions `Validate` passes on `main` after the merge.
4. The closure comment names the release version that completed the issue.
5. The closure comment states that donations remain inactive unless the issue explicitly concerns activation.

## Safety status

The following must remain true during issue closeout:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Release tags

Use annotated tags for release milestones:

```powershell
git tag -a v0.7.0 -m "v0.7.0 — Release closeout foundation"
git push origin v0.7.0
```

If using GitHub Desktop only, create the release manually in GitHub UI after the commit is pushed.

## GitHub Release

Use `docs/GITHUB_RELEASE_v0.7.0_DRAFT.md` as the release body.

## Follow-up after v0.7.0

Recommended next release:

```text
v0.8.0 — Donation readiness dry-run checklist
```

This should remain a dry run. It should not publish real wallet addresses or activate donation collection.
