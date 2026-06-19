# Maintainer Governance Checklist

This checklist defines the minimum maintainer controls required before Open Aid Ledger can be used for any active donation campaign.

Current state remains:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## 1. Maintainer roles

Before any campaign becomes active, maintainers should document role ownership.

| Role | Required before launch | Responsibility |
|---|---:|---|
| Repository maintainer | Yes | Reviews code, docs, issues, and release gates. |
| Wallet metadata reviewer | Yes | Reviews public wallet metadata only. Never handles private keys. |
| Ledger reviewer | Yes | Reviews donation and disbursement CSV entries. |
| Privacy reviewer | Yes | Checks that beneficiary records are redacted and non-identifying. |
| Campaign reviewer | Yes | Confirms campaign scope matches published policy. |
| Emergency contact | Yes | Coordinates freeze procedure if abuse, scam risk, or key-compromise suspicion appears. |

A single person may temporarily hold multiple roles during template development, but active donation operation should use independent review whenever possible.

## 2. Pre-launch governance gates

Donation activation must remain blocked until all items are complete.

- [ ] Donation policy reviewed.
- [ ] Transparency policy reviewed.
- [ ] Beneficiary privacy policy reviewed.
- [ ] Wallet metadata schema reviewed.
- [ ] Address-change procedure reviewed.
- [ ] Multisig or equivalent governance reviewed.
- [ ] Ledger validator tests pass in CI.
- [ ] Public safety scan passes in CI.
- [ ] Sample transparency report exists.
- [ ] Emergency freeze procedure exists.
- [ ] Conflict-of-interest disclosure template exists.
- [ ] Maintainer explicitly changes `DONATIONS_ACTIVE` from `NO` to `YES` in a reviewed commit.
- [ ] Maintainer explicitly changes `WALLETS_PUBLISHED` from `NO` to `YES` in a reviewed commit.

## 3. Monthly operating checklist

For active projects, run this at least monthly.

- [ ] Reconcile incoming donations against public transaction records.
- [ ] Reconcile outgoing disbursements against public reporting records.
- [ ] Confirm no private beneficiary data was published.
- [ ] Confirm no private key, seed phrase, or signing material was committed.
- [ ] Publish or update the monthly transparency report.
- [ ] Review open wallet-change requests.
- [ ] Review campaign proposal issues.
- [ ] Review conflict-of-interest disclosures.
- [ ] Confirm donation status remains accurate.

## 4. Release checklist

Before each release:

- [ ] `python -m compileall scripts tests` passes.
- [ ] Wallet validator passes.
- [ ] Ledger validator passes.
- [ ] Public safety scan passes.
- [ ] `pytest` passes.
- [ ] README status block is accurate.
- [ ] Release notes match the implemented scope.
- [ ] No local patch helper scripts are committed.

## 5. Guardrails

Maintainers must not merge changes that introduce:

- private key handling;
- seed phrase handling;
- wallet signing;
- automatic transfers;
- exchange withdrawal APIs;
- mixer/tumbler integration;
- trading account top-up;
- margin-call support;
- copy trading, managed accounts, or profit sharing;
- token issuance;
- return promises;
- beneficiary doxxing.

## 6. Review evidence

For each release or donation-activation decision, maintainers should record:

```text
review_date:
reviewer:
scope:
files_reviewed:
decision: approved | rejected | needs_changes
notes:
```

This can be posted in an issue, pull request, release note, or signed governance record.
