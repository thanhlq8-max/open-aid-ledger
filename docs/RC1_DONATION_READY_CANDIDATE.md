# v1.0.0-rc1 Donation-Ready Candidate

This document defines the first release-candidate checkpoint for Open Aid Ledger.

## Candidate status

```text
RELEASE: v1.0.0-rc1
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
TRANSFER_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

The repository is not collecting donations in this release candidate. The purpose of this checkpoint is to verify that policy, ledger, campaign, static status, readiness, and candidate review controls are present before any real wallet publication is considered.

## Required foundations

The candidate is valid only when all of the following foundations exist and pass CI:

- wallet metadata schema validation;
- ledger validation and duplicate transaction guards;
- public safety scan;
- sample transparency report;
- static public status page design;
- read-only importer design;
- maintainer governance checklist;
- campaign lifecycle metadata validation;
- donation readiness dry run;
- pre-1.0 candidate review.

## Non-activation rule

This release candidate does not activate donation intake. A later release may only activate donations after a separate reviewed commit changes the status fields and links to a completed approval record.

## Review result

Use `docs/RC1_SIGNOFF_RECORD.md` to record reviewer decisions. A missing signoff means the candidate remains documentation-only.
