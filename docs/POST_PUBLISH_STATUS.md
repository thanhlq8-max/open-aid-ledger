# Post-Publish Status

**Repository:** `thanhlq8-max/open-aid-ledger`  
**Status:** public repository published  
**Current version:** `0.1.1-post-publish-cleanup`  
**Donation status:** inactive  
**Wallet status:** no verified real wallet published  
**Last updated:** 2026-06-19

## Current lock

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Completed

- Public repository created.
- Initial README, policies, validators, campaign templates, and workflow committed.
- Six initial issues opened.
- Public labels added for documentation, enhancement, security, governance, and good-first-issue work.

## Initial issue backlog

| Issue | Purpose | Priority |
|---|---|---|
| #1 Harden wallet metadata schema | Prevent ambiguous or unsafe wallet publication | P0 |
| #2 Add unit tests for wallet and ledger validators | Prevent silent validator regressions | P0 |
| #3 Add sample transparency report | Make transparency output easy to review | P1 |
| #4 Add GitHub Pages static report design | Prepare shareable public transparency site | P1 |
| #5 Design read-only blockchain explorer importer | Plan future transaction import without custody risk | P1 |
| #6 Add maintainer governance checklist | Define operational controls before donation activation | P0 |

## Next milestone

```text
v0.2.0 â€” Ledger Safety & Public Report Foundation
```

Recommended order:

1. Complete issue #1.
2. Complete issue #2.
3. Complete issue #6.
4. Complete issue #3.
5. Confirm GitHub Actions passes.
6. Create/tag `v0.1.0-public-release-candidate` or `v0.1.1-post-publish-cleanup` depending on maintainer preference.

## Do not do yet

- Do not publish real donation wallets.
- Do not ask people to send funds.
- Do not create a token.
- Do not add transfer automation.
- Do not add exchange API access.
- Do not collect private beneficiary identity documents through GitHub.
- Do not describe crypto as legal tender or legal means of payment.

## Activation prerequisites

Before donations become active, maintainers should complete wallet schema hardening, wallet verification procedure, address-change review, governance checklist, privacy checklist, campaign-specific policy, first report template, tax/recordkeeping note, public safety scan, and maintainer approval note.