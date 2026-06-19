# Emergency Freeze Procedure

This procedure defines how maintainers should respond to high-risk events.

## Freeze triggers

Freeze project donation activity if any of the following is suspected:

- wrong wallet address published;
- wallet compromise;
- private key or seed phrase disclosure;
- fake campaign impersonation;
- beneficiary privacy leak;
- unreconciled ledger discrepancy;
- scam report from community members;
- maintainer account compromise;
- platform policy risk;
- legal or tax uncertainty requiring review.

## Immediate action

1. Set `DONATIONS_ACTIVE` to `NO` in README and any public status pages.
2. Remove or mark affected wallet addresses as inactive.
3. Open a public incident issue unless disclosure would worsen security or privacy risk.
4. Preserve evidence: commits, tx hashes, issue links, timestamps, screenshots.
5. Stop all pending disbursements until review is complete.
6. Notify maintainers and reviewers.
7. Publish a short public status note.

## Freeze status block

Use this format:

```text
INCIDENT_STATUS: FROZEN
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: REVIEWING
DISBURSEMENTS_ACTIVE: NO
REASON: <short reason>
STARTED_UTC: <timestamp>
NEXT_REVIEW_UTC: <timestamp>
```

## Review process

- Identify affected assets, wallets, campaigns, and ledger rows.
- Determine whether donor funds or beneficiary privacy were affected.
- Check whether GitHub account security was affected.
- Check whether CI and safety scans still pass.
- Decide whether to reactivate, rotate addresses, or retire the campaign.

## Reactivation criteria

Do not reactivate until:

- root cause is documented;
- affected records are corrected or clearly annotated;
- wallet address integrity is verified;
- privacy issues are remediated;
- public status note is updated;
- at least one maintainer review is recorded.

## Non-goals

This procedure does not provide legal, tax, accounting, financial, or investment advice.
