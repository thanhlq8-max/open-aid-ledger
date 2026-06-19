# Multisig Recommendation

Single-maintainer wallets are acceptable only for very small pilot campaigns and must be disclosed.

For serious campaigns, use multisig.

## Recommended patterns

```text
2-of-3: small team, low operational overhead
3-of-5: larger public campaign, stronger governance
```

## Signer roles

Suggested signer categories:

- technical maintainer;
- ledger/reporting maintainer;
- independent community reviewer;
- campaign coordinator;
- backup signer.

## Separation of duties

The same person should not unilaterally:

- control the wallet;
- approve beneficiaries;
- edit the ledger;
- publish final reports.

## Disclosure

Do not disclose operational security details that would increase attack risk. Do disclose:

- controller type;
- number of required signers;
- broad signer roles;
- campaign ownership;
- address activation and deactivation dates.
