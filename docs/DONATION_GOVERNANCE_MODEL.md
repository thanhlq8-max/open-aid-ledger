# Donation Governance Model

This document defines the minimum governance model required before any future donation activation proposal.

It is a draft control document. It does not activate donations, publish receiving details, or change project status.

## Current status

```text
GOVERNANCE_MODEL_STATUS: DRAFT
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
GO_LIVE: NO
```

## Governance principle

No single maintainer should be able to approve, operate, reconcile, and report a donation flow alone.

## Required roles

| Role | Responsibility | Required before activation |
|---|---|---:|
| Maintainer | Keeps repo docs, dashboard, and validation checks current. | YES |
| Governance reviewer | Reviews role separation and approval evidence. | YES |
| Account protection reviewer | Reviews account access, recovery, and freeze controls. | YES |
| Ledger reviewer | Checks ledger rows against source evidence. | YES |
| Public status reviewer | Checks dashboard status and donor-facing wording. | YES |
| Backup maintainer | Helps continuity if the primary maintainer is unavailable. | YES |

## Approval model

Before any activation proposal, the review packet must show:

- [ ] at least two named reviewer roles;
- [ ] documented role separation;
- [ ] public status review;
- [ ] account protection review;
- [ ] ledger and report review;
- [ ] freeze procedure review;
- [ ] legal and tax review status;
- [ ] latest CI evidence.

## Prohibited shortcuts

Do not use governance as a shortcut around readiness gates.

```text
IF any required role or review is missing:
    GO_LIVE = NO
```

## Evidence to attach later

A future activation proposal should attach:

- reviewer names or role identifiers;
- reviewed commit or pull request reference;
- account protection checklist result;
- legal and tax review status;
- reconciliation exercise result;
- freeze exercise result;
- latest validation result.

## Current decision

```text
GOVERNANCE_READY: NO
REASON: review evidence has not been attached yet
```
