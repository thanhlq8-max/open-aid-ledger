# Wallet Publication Precheck

## Purpose

This checklist must be completed before any real wallet address is proposed for publication.

It does not publish wallets. It defines the review gate only.

## Current status

```text
WALLET_PUBLICATION_STATUS: NOT_STARTED
WALLETS_PUBLISHED: NO
DONATIONS_ACTIVE: NO
```

## Precheck requirements

Before proposing wallet publication:

1. confirm donation activation remains inactive;
2. confirm wallet metadata schema validation passes;
3. confirm the address-change procedure is reviewed;
4. confirm multisig or equivalent governance is documented;
5. confirm emergency freeze procedure is reviewed;
6. confirm public status page can display inactive and active states;
7. confirm beneficiary privacy policy is reviewed;
8. confirm conflict-of-interest disclosure is reviewed;
9. confirm at least one external review has been recorded;
10. confirm release notes state whether donation collection is active.

## Publication proposal

A wallet publication proposal must include:

- asset;
- network;
- address owner or controller model;
- custody model;
- intended campaign scope;
- verification evidence;
- rollback procedure;
- public communication plan.

## Hard blocks

Wallet publication must be blocked if:

- any validation script fails;
- public safety scan fails;
- reviewer signoff is missing;
- emergency freeze procedure is unclear;
- beneficiary privacy controls are unclear;
- donation policy is stale;
- public status page does not match repository status.
