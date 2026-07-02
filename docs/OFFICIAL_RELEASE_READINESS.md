# Official Release Readiness

This document prepares Open Aid Ledger for an official repository release.

This is release-preparation only. It does not publish receiving details, activate collection, or change operating status.

## Current release decision

```text
RELEASE_TARGET: v1.0.0
RELEASE_STATUS: PREPARING
REPOSITORY_TEMPLATE_READY: REVIEW_REQUIRED
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

- [ ] README front door is clear.
- [ ] Public dashboard URL is visible.
- [ ] Quick access guide is visible.
- [ ] Share kit is visible.
- [ ] Readiness packet is visible.
- [ ] Governance model exists.
- [ ] Account-protection review record exists.
- [ ] Legal/tax review status record exists.
- [ ] Scope review record exists.
- [ ] Reconciliation dry-run review exists.
- [ ] Freeze dry-run review exists.
- [ ] Two-reviewer rule exists.
- [ ] CI validation passes on the release commit.
- [ ] Public-safety scan passes on the release commit.
- [ ] No private keys, seed phrases, or credentials are present.
- [ ] No live receiving details are published.

## Release blocker list

```text
RELEASE_NOTES: REQUIRED
RELEASE_TAG: NOT_CREATED
FINAL_CI_EVIDENCE: NOT_ATTACHED
PUBLIC_STATUS_RECHECK: REQUIRED
```

## Release go/no-go rule

```text
IF release evidence is incomplete:
    DO_NOT_TAG_RELEASE
```

## Next allowed step

Prepare release notes draft for `v1.0.0` and attach final validation evidence before creating a tag or GitHub Release.
