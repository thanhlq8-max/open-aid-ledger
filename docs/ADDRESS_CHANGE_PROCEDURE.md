# Address Change Procedure

Wallet addresses must be treated as security-critical public infrastructure.

## Required process

1. Open a pull request changing `wallets.json`.
2. State the reason for the address change.
3. Include the old wallet ID and new wallet ID.
4. Include the campaign ID.
5. Include the controller type.
6. Include the activation date.
7. Get review from at least two maintainers where possible.
8. Merge only after out-of-band verification.
9. Publish a report entry under `reports/`.
10. Keep the old address in historical records as inactive; do not delete history.

## Emergency address freeze

If compromise is suspected, publish:

```text
DONATION_STATUS: FROZEN
REASON: wallet compromise suspected
NEXT_UPDATE: pending maintainer review
```

Do not silently replace wallet addresses.
