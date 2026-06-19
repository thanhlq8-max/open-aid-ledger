# Campaign Lifecycle

Open Aid Ledger campaigns must move through explicit, reviewable states. Campaign status tracking is documentation-only until donation activation is separately approved.

## Status model

```text
proposed -> review -> approved_inactive -> active -> paused -> closed
                         |             |       |
                         |             |       -> cancelled
                         |             -> cancelled
                         -> cancelled
```

## Status definitions

| Status | Meaning | Donation collection allowed? |
|---|---|---|
| `proposed` | Idea has been opened but not reviewed. | No |
| `review` | Maintainers are reviewing scope, privacy, and safety. | No |
| `approved_inactive` | Approved as a campaign concept, but not collecting donations. | No |
| `active` | Donation collection has been explicitly activated. | Only after all activation gates pass |
| `paused` | Temporarily halted because of incident, review, or stale governance. | No new donation request |
| `closed` | Campaign is complete and final report is published. | No |
| `cancelled` | Campaign was rejected or withdrawn. | No |

## Required gates before `active`

A campaign must not become `active` unless all of the following are true:

1. `DONATIONS_ACTIVE` is explicitly changed from `NO` to `YES` in a reviewed commit.
2. `wallets_published` is true in the approved wallet metadata.
3. Wallet metadata passes validation without placeholders.
4. Campaign metadata passes `scripts/validate_campaigns.py`.
5. Donation policy and transparency policy are still current.
6. Beneficiary privacy review is complete.
7. Conflict-of-interest disclosures are reviewed.
8. Emergency freeze procedure is acknowledged by maintainers.
9. A public transparency report path is defined.
10. Any blockchain-importer workflow remains read-only and manually reconciled.

## Prohibited campaign types

Campaigns must not support:

- trading account top-up;
- margin-call rescue;
- trading-loss recovery;
- copy trading;
- managed account activity;
- profit sharing;
- investment products;
- token issuance;
- private key handling;
- automatic transfer or withdrawal workflows.

## Closeout

Every closed campaign should include:

- final donation ledger snapshot;
- final disbursement ledger snapshot;
- public report path;
- unresolved item list;
- privacy review confirmation;
- maintainer sign-off.

Closed campaigns must not be reopened by editing historical records. Open a new campaign record instead.
