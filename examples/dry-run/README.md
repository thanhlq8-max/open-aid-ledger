# Dry-Run Evidence Loop

This folder contains sample-only evidence for testing the Open Aid Ledger operating process.

Nothing in this folder activates donation collection, publishes live receiving details, approves go-live, or describes a real beneficiary case.

## Current status

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
GO_LIVE: NO
```

## Run the loop

Use this order:

```text
1. Read docs/DRY_RUN_OPERATIONS_RUNBOOK.md
2. Review DRY_RUN_001_OPERATION_REPORT.sample.md
3. Review DRY_RUN_001_REVIEW_PACKET.sample.md
4. Compare blockers with docs/OPERATIONAL_READINESS_MATRIX.md
5. Keep GO_LIVE as NO while blockers remain
6. Repeat after any material dashboard, validator, governance, or runbook change
```

## Evidence artifacts

| Artifact | Role | Status |
|---|---|---:|
| `DRY_RUN_001_OPERATION_REPORT.sample.md` | sample operation report | SAMPLE_ONLY |
| `DRY_RUN_001_REVIEW_PACKET.sample.md` | sample review packet | SAMPLE_ONLY |
| `candidate-review.example.json` | candidate review fixture | SAMPLE_ONLY |
| `rc1-candidate.example.json` | rc1 candidate fixture | SAMPLE_ONLY |
| `rc2-external-review.example.json` | rc2 external review fixture | SAMPLE_ONLY |
| `rc3-evidence-pack.example.json` | rc3 evidence fixture | SAMPLE_ONLY |

## Completion rule

```text
IF any production gate remains incomplete:
    GO_LIVE = NO
```

The sample evidence loop is complete only when:

- operation report is inspectable;
- review packet records findings and blockers;
- no live receiving details are present;
- no real beneficiary data is present;
- current status remains inactive;
- latest validation evidence is recorded or marked as required.

## Next real-work step

After this sample loop is stable, maintainers may prepare a reviewed dry-run packet using private or fictional data only. That packet still must not activate donation collection.
