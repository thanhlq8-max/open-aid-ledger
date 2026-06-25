# Receiving Account Protection Checklist

This checklist defines minimum protection expectations for any future account or address used to receive support.

Current status remains inactive:

```text
COLLECTION_ACTIVE: NO
LIVE_RECEIVING_DETAILS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

This document does not publish live receiving details and does not activate collection.

## Core rule

No single person should be able to receive, move, hide, or report support funds alone.

A future receiving setup must have:

- role separation;
- dual approval;
- clear records;
- periodic reconciliation;
- emergency freeze procedure;
- incident reporting;
- reviewer access to evidence.

## Roles

| Role | Responsibility |
|---|---|
| Channel owner | Maintains the approved receiving channel inventory. |
| Security reviewer | Reviews account hardening and access changes. |
| Ledger reviewer | Compares public records against source evidence. |
| Disbursement approver | Reviews outgoing support decisions. |
| Backup maintainer | Helps recover operations if a maintainer becomes unavailable. |

One person may temporarily hold more than one role during early development, but production operation should move toward separation of duties.

## Minimum controls before publication

Before any live receiving detail is published, confirm:

- [ ] Activation has been approved in a reviewed commit.
- [ ] The receiving channel is listed in an approved inventory file.
- [ ] The channel owner is documented.
- [ ] At least two maintainers or reviewers have approved publication.
- [ ] Access recovery process is documented.
- [ ] Account security settings have been reviewed.
- [ ] Withdrawal or outgoing movement requires dual approval where supported.
- [ ] Notification settings are enabled for sign-in, new device, account changes, and outgoing movement.
- [ ] A freeze procedure exists for suspected compromise or unexplained activity.
- [ ] Reconciliation procedure exists before and after every reporting cycle.
- [ ] Public status page clearly states whether collection is active.
- [ ] Donor guide clearly states the exact supported asset and network.

## Access protection

Future operators should use:

- hardware security keys or strong app-based two-factor authentication;
- password manager generated credentials;
- unique account email where appropriate;
- device lock and operating-system updates;
- access review after every maintainer change;
- removal of inactive maintainers;
- documented backup access process.

Do not use shared passwords in chat messages, issue comments, pull requests, spreadsheets, or public documents.

## Dual-control expectations

For any future live operation:

1. One person prepares the action record.
2. A second reviewer checks destination, amount, category, and supporting decision record.
3. A maintainer records the action reference.
4. A ledger reviewer reconciles the public ledger row against source evidence.
5. Any unexplained mismatch triggers freeze review before further operation.

## Reconciliation

Each reporting cycle should produce:

- opening balance;
- incoming support total;
- outgoing support total;
- fees if any;
- closing balance;
- unresolved differences;
- reviewer signoff date.

Unresolved differences must be documented before a report is marked final.

## Incident response

Trigger emergency freeze if any of these occur:

- unknown login or device alert;
- unknown account setting change;
- unexplained balance movement;
- mismatch between source evidence and ledger;
- suspected maintainer account compromise;
- donor report of sending to a different destination than the approved channel;
- reviewer cannot verify a reported transaction.

Freeze response:

1. Stop publication of new receiving details.
2. Mark public status as under review.
3. Preserve logs and evidence.
4. Reconcile known balances.
5. Rotate access where appropriate.
6. Publish a public-safe incident note after review.
7. Do not resume until reviewers approve.

## Prohibited shortcuts

Do not:

- publish a live receiving detail before activation approval;
- rely on one person as sole operator;
- use undocumented personal accounts for public collection;
- mix personal funds and support funds;
- delete or rewrite source evidence to hide a mismatch;
- promise instant support or guaranteed distribution;
- imply investment return, yield, repayment, or trading benefits;
- use automated outgoing movement without a separate reviewed design.

## Exchange-account caution

An exchange account may be convenient for some donors, but it adds custody, access, account freeze, network support, memo or tag, and reconciliation risks.

If an exchange account is ever used, it should be treated as an operational channel that requires stronger review, not as a shortcut around public accounting.

Prefer public on-chain receiving channels with explorer visibility when governance, review, and publication gates allow them.

## Maintainer note

This checklist is a baseline governance control. It is not legal, tax, security, privacy, or compliance advice. Use qualified review before any real operation.
