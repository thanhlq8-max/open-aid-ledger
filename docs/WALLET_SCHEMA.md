# Wallet Metadata Schema v1.1

This document defines the wallet metadata contract for Open Aid Ledger.

## Scope

Wallet metadata is public, read-only address information. It must never contain:

- private keys;
- seed phrases;
- exchange API keys;
- signing instructions;
- withdrawal credentials;
- beneficiary private information.

## Top-level fields

| Field | Required | Description |
|---|---:|---|
| `schema_version` | Yes | Must be `1.1`. |
| `project_id` | Yes | Stable project identifier. |
| `last_updated` | Yes | `YYYY-MM-DD` or placeholder in example files. |
| `donations_active` | Yes | Boolean. Must remain `false` until launch criteria are met. |
| `wallets_published` | Yes | Boolean. Indicates whether real public wallet addresses are published. |
| `wallets` | Yes | Non-empty list of wallet metadata records. |
| `prohibited` | Yes | Public statement that private credentials are never stored. |

## Wallet fields

Each wallet entry must include:

| Field | Description |
|---|---|
| `wallet_id` | Stable wallet identifier. |
| `campaign_id` | Campaign that this wallet supports. |
| `chain` | Chain identifier, for example `bitcoin` or `ethereum`. |
| `asset` | Asset ticker, for example `BTC`, `ETH`, `USDT`. |
| `network` | Network identifier, for example `mainnet`, `erc20`, `trc20`. |
| `address` | Public receiving address only. |
| `controller_type` | One of the approved controller types. |
| `controller_disclosure` | Public governance/control disclosure. |
| `custody_model` | Must describe metadata-only, no private-key custody in repo. |
| `donation_use` | Approved use category. |
| `status` | `placeholder`, `proposed`, `verified`, or `retired`. |
| `purpose` | Plain-language campaign purpose. |
| `address_verification` | How the address was reviewed before publication. |
| `last_reviewed_utc` | `YYYY-MM-DD` or placeholder in example files. |
| `risk_note` | Network/asset risk warning. |

## Activation rule

`donations_active` and `wallets_published` must remain `false` until all wallet records are real, reviewed, non-placeholder, and `verified`.

## Validation

Template validation:

```powershell
python scripts
alidate_wallets.py wallets.example.json --allow-placeholders
```

Production validation:

```powershell
python scripts
alidate_wallets.py wallets.json
```

