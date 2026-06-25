# Receiving Channel Publication Policy

This policy defines how future receiving channels may be prepared, reviewed, published, changed, or withdrawn.

Current status remains inactive:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

This document does not publish live receiving details and does not activate collection.

## Purpose

A future donor-facing page must have one clear source of truth for receiving information.

The goal is to reduce:

- copy-and-paste mistakes;
- wrong asset or network selection;
- private-message scams;
- outdated receiving details;
- unclear ownership;
- unclear freeze status;
- unreconciled records.

## Source of truth

Future receiving information must come from an approved repository source, not from private messages or screenshots.

A future publication source should include:

| Field | Requirement |
|---|---|
| channel_id | stable internal reference |
| status | inactive, active, frozen, retired |
| asset | exact asset symbol |
| network | exact network name |
| receiving_detail | published only after activation approval |
| explorer_template | optional public verification URL pattern |
| owner_role | responsible maintainer role |
| review_date | latest review date |
| approved_by | reviewer references, not private secrets |
| replaced_by | successor channel if retired |
| notes | public-safe operational notes |

## Publication gates

Do not publish a live receiving detail unless all gates are true:

- [ ] Donation activation has been approved in a dedicated reviewed commit.
- [ ] Wallet or account governance has been reviewed.
- [ ] Account protection checklist is complete.
- [ ] Public status page has been updated.
- [ ] Donor trust guide is linked from the public page.
- [ ] Asset and network are written exactly.
- [ ] Wrong-network risk note is visible.
- [ ] Ledger and reporting policy are linked.
- [ ] Emergency freeze procedure is linked.
- [ ] Beneficiary privacy controls are linked.
- [ ] At least two maintainers or reviewers approve publication.

## Donor-facing display rules

A future public page should show:

```text
Status: ACTIVE or INACTIVE
Asset: exact symbol
Network: exact network
Receiving detail: only if active and approved
Ledger: where records will appear
Report: where reconciliation will be published
Freeze status: normal, frozen, or retired
Last reviewed: date
```

If status is inactive, frozen, or retired, the page must say not to send.

## Change procedure

When changing a receiving channel:

1. Mark the old channel as retiring or frozen.
2. Open a reviewed change record.
3. Explain the reason using public-safe wording.
4. Add the new channel only after approval.
5. Keep the old reference visible as retired, not deleted.
6. Update the public status page.
7. Add a reconciliation note for the transition period.

## Freeze procedure

Freeze a channel if:

- access control is uncertain;
- an unexplained mismatch appears;
- a maintainer account may be compromised;
- a donor reports a mismatch with the public source;
- network or platform support changes unexpectedly;
- reviewers cannot verify source evidence.

When frozen:

- do not publish new receiving details;
- mark the channel as frozen;
- preserve evidence;
- reconcile known records;
- publish a public-safe status note after review;
- do not resume until reviewer approval is documented.

## Exchange-account caution

Exchange accounts may be convenient for some users, but they add operational risk.

If an exchange account is ever used as an operational channel, it must meet the same publication, protection, freeze, and reconciliation requirements as any other channel.

Do not present exchange support as guaranteed. Asset and network support can change.

Prefer channels that allow public verification when governance and review gates allow them.

## Prohibited publication patterns

Do not:

- publish receiving information only in chat;
- publish a screenshot as the source of truth;
- publish a channel with unclear asset or network;
- publish a channel without status;
- delete old channel history to hide a change;
- pressure donors to send before the public source is updated;
- imply collection is active while repository status says inactive;
- imply profit, yield, repayment, or special benefit.

## Maintainer note

This policy is a documentation baseline. It is not legal, tax, security, privacy, accounting, or financial advice. Use qualified review before any real public operation.
