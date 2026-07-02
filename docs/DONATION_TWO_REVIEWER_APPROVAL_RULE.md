# Donation Two-Reviewer Approval Rule

This document defines the minimum reviewer rule required before any future donation activation proposal.

It does not activate donations, publish receiving details, or change project status.

## Current status

```text
TWO_REVIEWER_APPROVAL_RULE: DRAFT
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
GO_LIVE: NO
```

## Core rule

Any future activation proposal must show at least two independent review roles before status can change.

The two reviews must not be replaced by a documentation-only merge.

## Required review roles

| Review area | Required evidence | Current result |
|---|---|---:|
| Governance review | role separation and approval notes | NOT_ATTACHED |
| Account protection review | access, recovery, freeze controls | NOT_ATTACHED |
| Legal or tax review status | reviewer status or blocker note | NOT_ATTACHED |
| Public status review | dashboard and donor wording alignment | NOT_ATTACHED |
| Ledger review | reconciliation and report checks | NOT_ATTACHED |

## Minimum approval packet

A future approval packet should include:

- [ ] reviewer role 1;
- [ ] reviewer role 2;
- [ ] reviewed commit or pull request reference;
- [ ] review date;
- [ ] scope reviewed;
- [ ] decision;
- [ ] blockers;
- [ ] latest CI result.

## Current blockers

```text
REVIEWER_ROLE_1: NOT_ATTACHED
REVIEWER_ROLE_2: NOT_ATTACHED
REVIEWED_COMMIT: NOT_ATTACHED
REVIEW_DECISION: NOT_ATTACHED
TWO_REVIEWER_APPROVAL_READY: NO
```

## Go/no-go rule

```text
IF fewer than two required reviewer roles are attached:
    GO_LIVE = NO
```
