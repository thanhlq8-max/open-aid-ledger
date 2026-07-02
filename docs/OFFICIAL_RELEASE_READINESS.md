# Official Release Readiness

This document prepares Open Aid Ledger for an official repository release.

This is release-preparation only. It does not publish receiving details, activate collection, or change operating status.

## Current release decision

```text
RELEASE_TARGET: v1.0.0
RELEASE_STATUS: READY_FOR_TAGGING_REVIEW
REPOSITORY_TEMPLATE_READY: YES
LIVE_OPERATION: NO
```

## Release scope

The official release should present the project as:

- a public repository template;
- a static dashboard and documentation workflow;
- a dry-run review system;
- a validation-gated public transparency template;
- an inactive operational baseline until separate review approves any future activation.

## Required release evidence

- [x] README front door is clear.
- [x] Public dashboard URL is visible.
- [x] Quick access guide is visible.
- [x] Share kit is visible.
- [x] Readiness packet is visible.
- [x] Governance model exists.
- [x] Account-protection review record exists.
- [x] Legal/tax review status record exists.
- [x] Scope review record exists.
- [x] Reconciliation dry-run review exists.
- [x] Freeze dry-run review exists.
- [x] Two-reviewer rule exists.
- [x] CI validation passes on the release commit.
- [x] Public-safety scan passes on the release commit.
- [x] No private keys, seed phrases, or credentials are present.
- [x] No live receiving details are published.

## Release blocker list

```text
RELEASE_NOTES: READY
RELEASE_TAG: NOT_CREATED
FINAL_CI_EVIDENCE: ATTACHED
PUBLIC_STATUS_RECHECK: PASS
```

## Release go/no-go rule

```text
IF maintainer approves final tag:
    TAGGING_MAY_PROCEED
```

## Next allowed step

Create or update final release notes for `v1.0.0`, then tag manually if maintainer approval is explicit.
