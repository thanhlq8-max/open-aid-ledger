# Donation Reconciliation Dry-Run Review

This document records the reconciliation exercise required before any future donation activation proposal.

It uses dry-run evidence only. It does not activate donations, publish receiving details, or change project status.

## Current status

```text
RECONCILIATION_REVIEW: DRY_RUN_ONLY
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
GO_LIVE: NO
```

## Review scope

| Area | Evidence | Current result |
|---|---|---:|
| Ledger schema | sample ledger files | BASELINE_EXISTS |
| Ledger validation | `scripts/validate_ledger.py` | BASELINE_EXISTS |
| Report generation | sample report generator | BASELINE_EXISTS |
| Dry-run packet | `examples/dry-run/DRY_RUN_001_REVIEW_PACKET.sample.md` | SAMPLE_ONLY |
| Source evidence | future review packet | NOT_ATTACHED |
| Reviewer signoff | future review packet | NOT_ATTACHED |
| Latest CI result | GitHub Actions Validate | REQUIRED |

## Reconciliation checklist

- [ ] Opening balance is recorded.
- [ ] Incoming total is recorded.
- [ ] Outgoing total is recorded.
- [ ] Fees are recorded.
- [ ] Closing balance is recorded.
- [ ] Source evidence is linked.
- [ ] Ledger rows are checked against evidence.
- [ ] Report totals match ledger totals.
- [ ] Unresolved differences are recorded.
- [ ] Reviewer signoff is attached.

## Current blockers

```text
SOURCE_EVIDENCE: NOT_ATTACHED
REPORT_TOTALS_REVIEW: NOT_ATTACHED
LEDGER_ROW_REVIEW: NOT_ATTACHED
UNRESOLVED_DIFFERENCE_REVIEW: NOT_ATTACHED
RECONCILIATION_READY: NO
```

## Go/no-go rule

```text
IF reconciliation evidence is incomplete:
    GO_LIVE = NO
```
