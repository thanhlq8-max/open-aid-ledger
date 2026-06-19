# Importer Manual Reconciliation Workflow

## Purpose

This workflow defines how future read-only importer output should be reviewed before any row is copied into `ledger/donations.csv`.

The importer must be treated as an assistant, not an authority.

## Flow

```text
1. Run read-only importer
2. Write staging file
3. Review each row manually
4. Check duplicates
5. Check privacy
6. Mark accepted/rejected/duplicate
7. Copy accepted rows into donation ledger
8. Commit ledger changes with clear summary
9. Generate transparency report
```

## Staging file

Suggested path:

```text
imports/incoming_transactions.review.csv
```

The staging file is review-only. It may be regenerated.

## Acceptance checklist

Before accepting a transaction into `ledger/donations.csv`:

- transaction hash exists on the public explorer;
- transaction direction is incoming;
- receiving wallet matches reviewed wallet metadata;
- asset and network match expected values;
- amount is positive;
- row is not a duplicate;
- donor identity is not inferred or exposed;
- source URL is recorded where safe;
- maintainer review note is added if needed.

## Rejection reasons

Use explicit reasons:

```text
wrong_wallet
wrong_network
dust_or_spam
duplicate
not_confirmed
ambiguous_asset
privacy_risk
manual_review_failed
```

## Duplicate handling

A transaction may contain multiple transfers. Duplicate detection should consider:

```text
network
tx_hash
transfer_index
wallet_id
asset
```

Do not use `tx_hash` alone when one transaction can emit multiple transfer events.

## Ledger write policy

Only accepted rows should be manually copied into:

```text
ledger/donations.csv
```

The importer must never directly write production ledger rows.

## Audit trail

Each accepted batch should include:

- staging file reference or checksum;
- review date;
- reviewer handle;
- count accepted;
- count rejected;
- count duplicates;
- generated report path.

## Safety boundary

No part of this workflow requires:

- private keys;
- seed phrases;
- wallet signing;
- transfers;
- exchange account access;
- custody automation.
