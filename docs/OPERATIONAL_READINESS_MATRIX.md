# Operational Readiness Matrix

This matrix shows whether Open Aid Ledger is ready for real operation.

Current status remains inactive:

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
```

This document does not activate collection, publish live receiving details, or approve production operation.

## Readiness definitions

| Status | Meaning |
|---|---|
| READY | The repository contains reviewed documentation or validation for this area. |
| READY_FOR_DRY_RUN | The area can be tested with fictional or placeholder data only. |
| BLOCKED | The area cannot be used for real operation yet. |
| EXTERNAL_REVIEW_REQUIRED | The area needs qualified external review before activation. |
| FORBIDDEN | The repository must not implement this behavior. |

## Current readiness summary

| Area | Status | Evidence | Next required action |
|---|---:|---|---|
| Public template | READY | README and public status page | Keep status aligned across docs. |
| Ledger shape | READY | Ledger validators and sample ledgers | Keep CI passing. |
| Sample reporting | READY | Sample report generation | Keep sample data fictional. |
| Campaign metadata | READY_FOR_DRY_RUN | Campaign lifecycle and validator | Keep campaigns inactive until activation. |
| Beneficiary review | READY_FOR_DRY_RUN | Intake, attestation, decision records | Test only with fictional or private review data. |
| Public case summary | READY_FOR_DRY_RUN | Public summary checklist | Use only redacted public-safe fields. |
| Donor trust guidance | READY_FOR_DRY_RUN | Donor trust guide | Keep donor-facing language simple and inactive. |
| Receiving-channel publication | BLOCKED | Publication policy exists | Do not publish live receiving details until gates pass. |
| Receiving-account protection | EXTERNAL_REVIEW_REQUIRED | Account protection checklist exists | Review governance, access, recovery, and freeze process. |
| Legal and tax review | EXTERNAL_REVIEW_REQUIRED | Legal/tax notes exist | Obtain qualified review before real operation. |
| Wallet or account governance | EXTERNAL_REVIEW_REQUIRED | Dry-run wallet review exists | Define approved governance and signoff process. |
| Read-only importer | READY_FOR_DRY_RUN | Importer design and normalized schema | Keep manual reconciliation before any ledger use. |
| Activation | BLOCKED | Activation checklist exists | Requires dedicated reviewed commit. |
| Custody automation | FORBIDDEN | Core guardrails | Do not implement. |
| Outgoing automation | FORBIDDEN | Core guardrails | Do not implement. |
| Trading or return promise | FORBIDDEN | Core guardrails | Do not imply. |

## Minimum production-readiness gate

The system is not production-ready until all of these are true:

- [ ] External review evidence has been collected and assessed.
- [ ] Legal and tax blockers are documented and resolved.
- [ ] Receiving-channel governance is approved.
- [ ] Receiving-account protection is reviewed.
- [ ] Public status page is updated.
- [ ] Donor trust guide is updated for the active release.
- [ ] Campaign or support category is active and reviewed.
- [ ] Public ledger publication process is reviewed.
- [ ] Reconciliation process is tested.
- [ ] Emergency freeze process is tested.
- [ ] Beneficiary privacy controls are reviewed.
- [ ] A dedicated activation commit changes status intentionally.

If any item is incomplete, keep operation inactive.

## Dry-run readiness gate

The system can be dry-run tested when:

- [ ] CI passes.
- [ ] No live receiving details are published.
- [ ] All case examples are fictional or private.
- [ ] Public status remains inactive.
- [ ] Ledger examples balance.
- [ ] Reports are generated from fictional data.
- [ ] Freeze and reconciliation steps are walked through manually.

## Operational risk register

| Risk | Current control | Residual status |
|---|---|---:|
| Donor follows private message | Donor trust guide and public status warning | Needs public-page visibility |
| Wrong network or asset | Receiving-channel policy | Blocked until active guide is reviewed |
| Single-person control | Account protection checklist | Needs external/governance review |
| Case exposure | Privacy policy and public summary checklist | Needs real-case reviewer discipline |
| Unexplained mismatch | Reconciliation and freeze docs | Needs dry-run exercise |
| Outdated public status | Static page validator and README alignment | Needs release checklist discipline |
| Legal/tax uncertainty | Legal/tax note | External review required |

## Go/no-go rule

Use this rule for every future release:

```text
IF any production gate is incomplete:
    GO_LIVE = NO
ELSE:
    prepare a dedicated reviewed activation proposal
```

No maintainer should treat a documentation-only merge as activation.

## Maintainer note

This matrix is an operating-control document. It is not legal, tax, security, privacy, accounting, or financial advice. Use qualified review before any real public operation.
