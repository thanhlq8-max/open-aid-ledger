# RC2 External Review and Activation Gate

## Purpose

This document defines the second release-candidate review gate before Open Aid Ledger can move toward any donation activation.

RC2 is not an activation release. It is a human-review checkpoint that keeps donation collection inactive while validating whether the project has enough governance, transparency, safety, and review evidence to proceed toward a later activation proposal.

## Current decision

```text
RC2_STATUS: REVIEW_GATE
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
CUSTODY_AUTOMATION: NO
TRANSFER_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Required review areas

RC2 review must cover:

1. public status accuracy;
2. wallet publication readiness;
3. campaign lifecycle controls;
4. ledger and report controls;
5. beneficiary privacy controls;
6. maintainer governance controls;
7. emergency freeze procedure;
8. conflict-of-interest review;
9. legal and tax note completeness;
10. external reviewer signoff.

## External review requirement

Before any later activation proposal, at least one reviewer outside the primary maintainer role should review the repository and record findings.

The review may be performed by a trusted community maintainer, an open-source reviewer, a legal or compliance reviewer, or an operations reviewer. The reviewer does not need to control funds.

## RC2 pass condition

RC2 passes only when:

- all validation scripts pass;
- public safety scan passes;
- the status page still says donations are inactive;
- no real wallet address is published;
- no transfer automation exists;
- external review documents are present;
- activation remains explicitly blocked pending later decision.

## Explicit non-activation

RC2 does not authorize:

- real donation collection;
- public wallet publication;
- custody operation;
- transfer automation;
- exchange account integration;
- trading activity;
- token issuance;
- return promises.

## Next allowed step

After RC2, the only allowed next step is a later activation proposal or another release-candidate review.

Any activation proposal must be separate, explicit, reviewed, and auditable.
