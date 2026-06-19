# Scam Prevention

## Threat model

Donation repositories are high-risk targets for:

- wallet address replacement;
- fake maintainer accounts;
- phishing links;
- private-key harvesting;
- impersonated beneficiaries;
- fake emergency campaigns;
- pressure tactics;
- token or airdrop scams.

## Hard rules

- Never ask donors or beneficiaries for seed phrases or private keys.
- Never ask donors to connect wallets to unknown websites.
- Never publish private beneficiary documents.
- Never promise returns, yield, signals, allocations, or trading benefits.
- Never change wallet addresses without a public review trail.
- Never accept direct messages as the only approval record for disbursement.

## Wallet-address change procedure

Use `docs/ADDRESS_CHANGE_PROCEDURE.md`.

## Incident response

If a suspicious wallet change, phishing attempt, privacy leak, or ledger manipulation is detected:

1. stop promoting donation addresses;
2. open a security advisory or private maintainer review if sensitive;
3. publish a redacted incident report;
4. rotate affected addresses only through the address-change procedure;
5. reconcile ledgers after review.
