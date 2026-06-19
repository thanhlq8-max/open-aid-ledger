# Security Policy

## Never disclose

Do not submit:

- private keys;
- seed phrases;
- recovery phrases;
- exchange API keys;
- wallet screenshots containing secrets;
- identity documents;
- private beneficiary records.

## Supported security reports

Report privately if you find:

- exposed secrets;
- tampered wallet addresses;
- malicious pull requests;
- fake donation addresses;
- report-generation vulnerabilities;
- privacy leaks.

## Non-goals

This repository does not provide:

- wallet custody;
- smart contracts;
- signing systems;
- exchange integration;
- automated transfers.

## Emergency response

If a wallet address is suspected to be compromised:

1. stop displaying the affected address;
2. publish an incident note;
3. preserve audit trail;
4. move to multisig or a new address only after public disclosure;
5. never rewrite ledger history silently.
