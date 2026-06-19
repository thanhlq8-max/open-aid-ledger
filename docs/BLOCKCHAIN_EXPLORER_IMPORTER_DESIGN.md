# Read-only Blockchain Explorer Importer Design

## Status

```text
DESIGN_STATUS: APPROVED_FOR_REVIEW
IMPLEMENTATION_STATUS: NOT_IMPLEMENTED
NETWORK_FETCHING: NOT_INCLUDED
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
```

This document defines the design boundary for a future read-only importer that may collect public incoming transaction data from blockchain explorers into a review queue.

It is intentionally not a custody system and not a wallet system.

## Objective

The importer should help maintainers reconcile public incoming donation transactions without manually copying every transaction from block explorers.

The importer may eventually:

- read public wallet metadata;
- query public blockchain explorer APIs;
- normalize incoming transaction records;
- write review-only staging files;
- help detect duplicate transaction hashes;
- support manual reconciliation into `ledger/donations.csv`.

## Non-goals

The importer must not:

- handle private keys;
- handle seed phrases;
- sign transactions;
- transfer assets;
- withdraw from exchanges;
- connect to private exchange accounts;
- use mixer services;
- anonymize fund flows;
- bypass compliance checks;
- write directly to production donation ledgers without maintainer review;
- activate donations;
- publish real wallet addresses;
- make financial, legal, tax, or investment claims.

## Supported data sources

Initial design assumes public explorer APIs only.

Potential future adapters:

| Network family | Example data source type | Scope |
|---|---|---|
| BTC-like | public block explorer API | incoming transactions to public address |
| EVM-like | public explorer API | native token and contract-token transfer events |
| TRON-like | public explorer API | public transfer events only |

No private node keys, exchange credentials, or wallet-signing APIs are allowed.

## Inputs

A future importer may read:

```text
wallets.json
```

Required wallet metadata must already be reviewed and must not contain placeholders if imports are enabled.

The importer must reject active import mode when:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
wallet address is placeholder
wallet status is not active/reviewed
address verification is missing
```

## Outputs

A future importer must write staging data only, for example:

```text
imports/incoming_transactions.review.csv
```

It must not directly modify:

```text
ledger/donations.csv
ledger/disbursements.csv
```

Production ledger changes must remain explicit maintainer commits.

## Review workflow

```text
public explorer data
        ↓
normalized staging file
        ↓
maintainer review
        ↓
duplicate and privacy checks
        ↓
manual acceptance/rejection
        ↓
explicit commit to ledger/donations.csv
```

## Error handling

The importer should treat explorer data as untrusted.

It should record:

- source explorer;
- source URL;
- observed timestamp;
- block timestamp if available;
- API status;
- parsing warnings;
- duplicate warnings;
- confirmation count if available.

Failures should not mutate ledgers.

## Rate limits

A future implementation must include:

- configurable request delay;
- retry limits;
- timeout limits;
- clear user-agent string;
- no secret API key checked into the repo;
- cache or checkpoint option if needed.

## Privacy

Public blockchain data is public, but this project should still avoid unnecessary donor exposure.

Preferred behavior:

- store transaction hash;
- store network;
- store asset;
- store amount;
- store wallet identifier;
- store counterparty address only if required;
- prefer hashed or redacted counterparty address in public reports;
- never infer identity from wallet address;
- never publish beneficiary private details.

## Manual reconciliation

See:

```text
docs/IMPORTER_MANUAL_RECONCILIATION.md
```

## Normalized schema

See:

```text
docs/IMPORTER_NORMALIZED_TX_SCHEMA.md
```

## Safety invariant

The importer is a data-ingestion helper only. It must be safe to delete without affecting custody, wallets, or donation activation.
