# Official Release Readiness

This document prepares Open Aid Ledger for an official repository release.

This is release-preparation only. It does not publish receiving details, activate collection, or change operating status.

## Current release decision

```text
RELEASE_TARGET: v1.0.0
RELEASE_STATUS: FINAL_VALIDATION_PENDING
REPOSITORY_TEMPLATE_READY: YES
CURRENT_RELEASE_IDENTITY: 1.0.0
RELEASE_IDENTITY_TRANSITION_COMPLETE: YES
RELEASE_TAG_TARGET: NOT_SELECTED
FINAL_CI_EVIDENCE: NOT_ATTACHED
FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PENDING_FINAL_TARGET
POST_MERGE_PAGES_RUNTIME: PENDING_AUTHORITATIVE_EVIDENCE
LIVE_OPERATION: NO
```

`REPOSITORY_TEMPLATE_READY: YES` describes the implemented template scope. It is not approval to tag or publish the repository release.

`RELEASE_IDENTITY_TRANSITION_COMPLETE: YES` records that the current repository identity is aligned to `1.0.0`. It does not select a final tag target or establish final CI, Pages, tag, GitHub Release, or operating-activation evidence.

## Release scope

The official release should present the project as:

- a public repository template;
- a static dashboard and documentation workflow;
- a dry-run review system;
- a validation-gated public transparency template;
- an inactive operational baseline until separate review approves any future activation.

## Completed release-preparation evidence

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
- [x] Public-safety scanner blind spot is fixed and regression-guarded.
- [x] Remote GitHub Actions are pinned to immutable commit SHAs and regression-guarded.
- [x] Release identity transition is complete across current public status files.
- [x] No live receiving details are published.

## Remaining release blockers

- [ ] Select the exact final intended release target.
- [ ] Run complete fresh validation on the exact final target.
- [ ] Attach authoritative final CI evidence for that target.
- [ ] Complete the final public-status recheck against that target.
- [ ] Obtain authoritative Pages runtime evidence required by the current project state.
- [ ] Confirm final release notes match the selected target.
- [ ] Receive explicit maintainer approval for the tag.

## Release blocker state

```text
RELEASE_NOTES: FINAL_VALIDATION_PENDING
RELEASE_TAG_TARGET: NOT_SELECTED
RELEASE_TAG: NOT_CREATED
FINAL_CI_EVIDENCE: NOT_ATTACHED
FINAL_RELEASE_PUBLIC_STATUS_RECHECK: PENDING_FINAL_TARGET
TAGGING_STATUS: BLOCKED
```

## Release go/no-go rule

Tagging remains blocked while any item in the remaining release blockers is unresolved. Repository release approval is separate from operating activation.

## Next allowed step

Select the exact final intended release candidate only after post-identity state sync is merged and read back, then run fresh complete validation and collect the required final CI, public-status and Pages evidence for that exact target.
