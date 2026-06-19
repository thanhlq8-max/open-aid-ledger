# Dry-Run Wallet Publication Review

This review is a dry-run-only checklist for future wallet publication.

It must not be used to publish real donation addresses until the maintainer explicitly moves the project from inactive/template mode to a reviewed donation-ready release.

## Required status before this review

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
```

## Review checklist

Before any real wallet address is published, maintainers must verify:

- the wallet address is controlled by the intended maintainer or multisig;
- no private key, seed phrase, mnemonic, keystore, exchange API key, or recovery material is stored in the repository;
- the target chain, network, and asset are unambiguous;
- unsupported-chain transfer risk is documented;
- address-change procedure is documented;
- emergency freeze procedure is documented;
- donation activation checklist is complete;
- beneficiary privacy policy is reviewed;
- public reporting format is reviewed;
- conflict-of-interest disclosure is completed;
- legal/tax note is reviewed for the relevant jurisdiction.

## Required evidence

A future real wallet publication should have:

```text
wallet_id
campaign_id
chain
network
asset
public_address
controller_type
custody_model
verification_method
verification_date_utc
reviewer
status
```

## Forbidden evidence

Never publish:

```text
private_key
seed_phrase
mnemonic
keystore_json
exchange_api_key
exchange_api_secret
withdrawal_key
wallet_password
hardware_wallet_pin
recovery_shard
```

## Dry-run conclusion

Until every item above is reviewed and the maintainer intentionally updates `DONATIONS_ACTIVE`, this repository remains a public transparency template, not an active donation collection endpoint.
