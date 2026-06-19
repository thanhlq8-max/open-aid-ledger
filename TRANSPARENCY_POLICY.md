# Transparency Policy

## Objective

The repository should let donors, maintainers, beneficiaries, and observers verify:

1. what came in;
2. what went out;
3. why support was sent;
4. what evidence exists;
5. whether privacy was protected.

## Public ledger files

Primary ledger files:

```text
ledger/donations.csv
ledger/disbursements.csv
reports/
```

## Minimum donation fields

`ledger/donations.csv` should include:

- date_utc
- campaign_id
- chain
- asset
- network
- amount
- tx_hash
- donor_label
- source_note
- status

`donor_label` may be anonymous.

## Minimum disbursement fields

`ledger/disbursements.csv` should include:

- date_utc
- campaign_id
- beneficiary_code
- category
- chain
- asset
- network
- amount
- tx_hash
- purpose
- evidence_ref
- approval_ref
- status
- privacy_level

## Evidence model

Allowed evidence references:

- redacted receipt;
- partner confirmation;
- internal case note;
- public proof with consent;
- tx hash;
- signed maintainer attestation.

Do not publish raw identity documents.

## Reporting cadence

Recommended:

- monthly report when active;
- immediate incident report for mistakes or suspicious transactions;
- annual summary if the project grows.

## Audit trail

Changes to wallet addresses, policies, and ledger records should be done through pull requests when possible.

Force-pushes and history rewrites should be avoided after public donations start.
