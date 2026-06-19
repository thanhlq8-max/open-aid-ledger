# Governance Decision Record

Use this document as a lightweight template for important project decisions.

## Record template

```text
decision_id:
date_utc:
status: proposed | accepted | rejected | superseded
scope:
decision:
rationale:
risks:
alternatives_considered:
reviewers:
related_issues:
related_commits:
follow_up_actions:
```

## Decisions that should be recorded

- activating donations;
- publishing real wallet addresses;
- changing wallet addresses;
- changing custody or multisig governance;
- approving a campaign;
- approving emergency freeze or reactivation;
- changing beneficiary privacy policy;
- changing ledger schema;
- adding network-based importer implementation.

## Constraints

Decision records must preserve the project guardrails:

```text
NO_PRIVATE_KEYS
NO_SEED_PHRASES
NO_AUTO_TRANSFER
NO_EXCHANGE_WITHDRAWAL_API
NO_CUSTODY_AUTOMATION
NO_TRADING_ACCOUNT_TOP_UP
NO_MARGIN_CALL_SUPPORT
NO_RETURN_PROMISE
NO_BENEFICIARY_DOXXING
```
