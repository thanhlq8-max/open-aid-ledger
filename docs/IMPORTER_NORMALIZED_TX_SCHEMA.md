# Importer Normalized Transaction Schema

## Purpose

This schema describes the review-only output of a future read-only blockchain explorer importer.

The schema is for staging and manual reconciliation. It is not a production donation ledger.

## Staging file

Suggested path:

```text
imports/incoming_transactions.review.csv
```

## Required columns

| Column | Required | Description |
|---|---:|---|
| `import_id` | yes | Stable importer-generated row ID. |
| `wallet_id` | yes | Internal wallet identifier from reviewed wallet metadata. |
| `network` | yes | Chain or network name, for example `bitcoin`, `ethereum`, `polygon`, `tron`. |
| `asset` | yes | Asset symbol, for example `BTC`, `ETH`, `USDT`. |
| `tx_hash` | yes | Public transaction hash. |
| `transfer_index` | yes | Event or output index to disambiguate multiple transfers in one transaction. |
| `direction` | yes | Must be `incoming` for donation imports. |
| `amount_decimal` | yes | Decimal amount as rendered after token decimals. |
| `token_contract` | no | Token contract address for contract-token transfers. Empty for native assets. |
| `block_number` | no | Block height or equivalent if available. |
| `block_time_utc` | no | Blockchain timestamp if available. |
| `confirmations` | no | Confirmation count if available. |
| `counterparty_address_hash` | no | Hashed or redacted counterparty address if retained. |
| `source_explorer` | yes | Explorer name or adapter ID. |
| `source_url` | no | Public explorer URL for manual verification. |
| `observed_at_utc` | yes | Time the importer observed the transaction. |
| `review_status` | yes | `pending_review`, `accepted`, `rejected`, or `duplicate`. |
| `review_note` | no | Maintainer note. |

## Constraints

- `direction` must be `incoming`.
- `amount_decimal` must be positive.
- `tx_hash` must be non-empty.
- `(network, tx_hash, transfer_index, wallet_id, asset)` should be unique.
- `review_status` must not default to `accepted`.
- Staging rows must not modify production ledgers automatically.

## Example

See:

```text
examples/importer/normalized_transactions.sample.csv
```

## Privacy rule

Do not publish donor identity claims. Do not infer real-world identity from a public transaction address.

If counterparty data is needed, prefer a hash or redacted form.

## Activation rule

A staging importer must not be used for active donation operations until:

- `wallets.json` is reviewed;
- placeholder wallets are removed;
- donation activation is explicitly approved;
- maintainer reconciliation procedure is documented;
- privacy controls are reviewed.
