# Dry-Run Operations Runbook

This runbook lets maintainers test the operating model without accepting real support, publishing live receiving details, or exposing real people.

Current status remains inactive:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

## Purpose

Use this runbook to test whether the repository workflow is understandable, auditable, and safe before any production proposal.

The dry run should prove that maintainers can:

- read public status;
- prepare a fictional support case;
- review a fictional partner attestation;
- prepare a public-safe summary;
- record sample ledger rows;
- generate a sample report;
- reconcile balances;
- simulate a freeze;
- document unresolved findings.

## Inputs

Use only repository sample files or private fictional records:

- `examples/sample-ledger/donations.csv`
- `examples/sample-ledger/disbursements.csv`
- `examples/relief-review/README.md`
- `examples/relief-review/FAM-2026-001_intake_review.sample.md`
- `examples/relief-review/FAM-2026-001_partner_attestation.sample.md`
- `examples/relief-review/FAM-2026-001_disbursement_decision.sample.md`
- `docs/PUBLIC_SUMMARY_CHECKLIST.md`
- `docs/RECEIVING_CHANNEL_PUBLICATION_POLICY.md`
- `docs/RECEIVING_ACCOUNT_PROTECTION.md`
- `docs/OPERATIONAL_READINESS_MATRIX.md`

Do not use real case records, real receiving details, private account information, or private credentials in the dry run.

## Roles for the exercise

At minimum, assign these roles for the exercise:

| Role | Dry-run task |
|---|---|
| Operator | Prepares the fictional packet and sample ledger rows. |
| Reviewer | Checks privacy, status, and evidence consistency. |
| Reconciler | Compares ledger totals and report output. |
| Safety lead | Runs the freeze scenario and records blockers. |

The same person may simulate multiple roles during early testing, but the test report should still name which role was simulated.

## Step 1: Status check

Confirm public status says inactive:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

If public status does not match, stop and fix documentation drift before continuing.

## Step 2: Fictional case review

Review the fictional relief example and confirm:

- [ ] no real personal data is present;
- [ ] case reference does not identify a person;
- [ ] public summary omits private evidence;
- [ ] decision record does not imply real transfer;
- [ ] partner attestation is sample-only.

## Step 3: Public summary review

Use `docs/PUBLIC_SUMMARY_CHECKLIST.md` to confirm that the public-facing summary does not expose protected details.

Record findings as:

```text
PUBLIC_SUMMARY_REVIEW: PASS | FAIL
FINDINGS:
- item 1
- item 2
```

## Step 4: Ledger and report dry run

Run the local validation commands from README.

Expected result:

```text
compile: PASS
wallet example: PASS
campaign metadata: PASS
readiness dry run: PASS
ledger validation: PASS
sample ledger validation: PASS
static public status: PASS
candidate review: PASS
rc1: PASS
rc2: PASS
rc3: PASS
public safety: PASS
tests: PASS
sample report generation: PASS
```

If any step fails, fix only the failing scope.

## Step 5: Reconciliation exercise

Confirm:

- [ ] opening balance is known;
- [ ] incoming sample rows are totaled;
- [ ] outgoing sample rows are totaled;
- [ ] fees are recorded if present;
- [ ] closing balance matches expected value;
- [ ] unresolved differences are listed.

Record:

```text
RECONCILIATION_STATUS: PASS | FAIL
OPENING_BALANCE:
INCOMING_TOTAL:
OUTGOING_TOTAL:
FEES:
CLOSING_BALANCE:
UNRESOLVED_DIFFERENCES:
```

## Step 6: Freeze exercise

Simulate one issue:

```text
SCENARIO: reviewer cannot verify one ledger row
```

Expected response:

1. mark the dry-run channel or report as under review;
2. stop publication of any new receiving detail;
3. preserve evidence;
4. reconcile known records;
5. document the unresolved finding;
6. do not resume until reviewer approval is recorded.

## Step 7: Go/no-go review

Use `docs/OPERATIONAL_READINESS_MATRIX.md`.

Expected current decision:

```text
GO_LIVE: NO
REASON: production gates remain incomplete
NEXT_MODE: dry-run and external review only
```

## Dry-run report template

```text
DRY_RUN_ID:
DATE:
REPOSITORY_VERSION:
OPERATOR:
REVIEWER:
RECONCILER:
SAFETY_LEAD:

STATUS_CHECK: PASS | FAIL
FICTIONAL_CASE_REVIEW: PASS | FAIL
PUBLIC_SUMMARY_REVIEW: PASS | FAIL
VALIDATION_RUN: PASS | FAIL
RECONCILIATION: PASS | FAIL
FREEZE_EXERCISE: PASS | FAIL
GO_LIVE_DECISION: NO

FINDINGS:
- 

BLOCKERS:
- 

NEXT_ACTIONS:
- 
```

## Stop conditions

Stop the dry run if:

- real personal data appears;
- live receiving details appear;
- public status suggests activation;
- private credentials appear;
- ledger totals do not reconcile;
- a reviewer cannot explain a finding.

## Maintainer note

This runbook is for dry-run testing only. It is not legal, tax, security, privacy, accounting, or financial advice. Use qualified review before any real public operation.
