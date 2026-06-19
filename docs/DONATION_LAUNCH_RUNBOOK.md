# Donation Launch Runbook

This runbook describes a future donation launch flow. It is not an authorization to activate donations.

## Phase 0 — Dry run

Required state:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
```

Actions:

1. run all validators;
2. run all tests;
3. review wallet publication checklist;
4. review risk register;
5. review governance checklist;
6. review emergency freeze procedure;
7. review sample transparency report;
8. confirm no private key material exists in the repository.

## Phase 1 — Candidate review

Actions:

1. create a reviewed branch or pull request;
2. add real public wallet metadata only if policy allows it;
3. keep private material outside the repository;
4. obtain maintainer review;
5. verify address display and network warnings.

## Phase 2 — Activation commit

Only after all launch gates pass, maintainers may change:

```text
DONATIONS_ACTIVE: YES
WALLETS_PUBLISHED: YES
```

This must be a reviewed commit with release notes.

## Phase 3 — Public reporting

Actions:

1. reconcile incoming donations manually or through an approved read-only importer;
2. publish transparency reports;
3. disclose unresolved review items;
4. keep beneficiary information redacted;
5. maintain emergency freeze readiness.

## Emergency stop

Any suspected address compromise, private-key exposure, false claim, beneficiary privacy incident, or ledger mismatch triggers the emergency freeze procedure.
