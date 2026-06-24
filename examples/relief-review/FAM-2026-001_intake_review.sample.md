# Fictional Intake Review Sample — FAM-2026-001

## Status

Sample-only record.

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
SAMPLE_DATA_ONLY: YES
REAL_BENEFICIARY_DATA: NO
```

## Intake metadata

```text
Beneficiary code: FAM-2026-001
Campaign ID: 2026-community-hardship-support
Need category: RENT
Privacy level: redacted_public_summary
Evidence level: partner_attestation_only
Decision status: review
Public summary: Fictional family facing short-term rent pressure after temporary income interruption.
```

## Scope screening

| Check | Result |
|---|---|
| Public-interest or hardship purpose | pass |
| Trading account support | not applicable |
| Margin-call or trading-loss recovery | not applicable |
| Return promise | not applicable |
| Token or investment promotion | not applicable |
| Private account credential request | not applicable |
| Public identification risk | needs redaction |

## Privacy review

Public record may include:

- beneficiary code;
- broad need category;
- redacted public summary;
- partner attestation reference;
- campaign ID.

Public record must not include:

- real names;
- exact location;
- private messages;
- private documents;
- private account details.

## Evidence handling

```text
Evidence reviewed: partner_attestation_only
Evidence location: private_review_storage
Public proof level: summary only
Partner attestation sample: FAM-2026-001_partner_attestation.sample.md
```

## Intake result

```text
Review result: proceed_to_decision_review
Reason: Fictional case is in-scope and can be represented with redacted public summary plus partner attestation.
Next record: FAM-2026-001_disbursement_decision.sample.md
```

## Guardrail confirmation

- [x] No real beneficiary data used.
- [x] No personal documents included.
- [x] No wallet address included.
- [x] No donation activation implied.
- [x] No custody or transfer workflow included.
