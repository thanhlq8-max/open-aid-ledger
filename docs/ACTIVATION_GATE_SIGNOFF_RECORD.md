# Activation Gate Signoff Record

## Purpose

This file records the signoff structure required before any future activation proposal.

This is a template. It does not activate donations.

## Current status

```text
SIGNOFF_RECORD_STATUS: TEMPLATE_ONLY
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

## Signoff fields

For any later activation proposal, record:

```text
proposal_id:
proposal_date_utc:
target_release:
review_scope:
maintainer_signoff:
external_reviewer_signoff:
privacy_review_signoff:
governance_review_signoff:
emergency_freeze_reviewed:
wallet_publication_reviewed:
public_status_page_reviewed:
decision:
decision_notes:
```

## Valid decisions

Allowed decision values:

```text
blocked
deferred
approved_for_next_review
approved_for_activation_proposal
```

`approved_for_activation_proposal` is not the same as donation activation. It only permits a separate activation proposal to be prepared.

## Minimum evidence

The record should link to:

- candidate release notes;
- validation run;
- external review notes;
- wallet publication review;
- public status page review;
- risk register;
- emergency freeze procedure.
