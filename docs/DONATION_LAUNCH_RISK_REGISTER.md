# Donation Launch Risk Register

This register captures risks that must be reviewed before any donation-ready release.

## Risk table

| Risk ID | Risk | Severity | Required control |
|---|---:|---:|---|
| RISK-001 | Donor sends unsupported asset/network | High | Clear wallet metadata and unsupported-transfer warning |
| RISK-002 | Address replacement attack | Critical | Address-change review and commit history audit |
| RISK-003 | Private key leaked into repository | Critical | Public safety scan and manual review |
| RISK-004 | Donation mistaken for investment | High | No-return-promise wording in README and policies |
| RISK-005 | Trader loss rescue misconception | High | Explicit no margin-call / no trading-account-top-up policy |
| RISK-006 | Beneficiary privacy exposure | High | Redacted beneficiary IDs and privacy review |
| RISK-007 | Maintainer conflict of interest | Medium | Conflict-of-interest disclosure |
| RISK-008 | Missing tax/legal documentation | Medium | Jurisdiction note and donor/maintainer responsibility note |
| RISK-009 | Manual ledger mismatch | Medium | Reconciliation checklist and immutable transaction references |
| RISK-010 | False charity registration implication | High | No charity-registration claim unless formally verified |

## Launch rule

Any unresolved critical or high risk blocks donation activation.

## Dry-run position

This register is for readiness review only. It does not authorize donation activation.
