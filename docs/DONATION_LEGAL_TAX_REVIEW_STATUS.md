# Donation Legal and Tax Review Status

This document records legal and tax review status required before any future donation activation proposal.

It is an operational tracking record only. It is not legal advice, tax advice, accounting advice, or regulatory advice.

## Current status

```text
LEGAL_TAX_REVIEW: REQUIRED
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
GO_LIVE: NO
```

## Review scope

| Area | Evidence | Current result |
|---|---|---:|
| Vietnam note | `docs/VN_LEGAL_AND_TAX_NOTE.md` | BASELINE_EXISTS |
| Donation policy | `DONATION_POLICY.md` | NEEDS_REVIEW |
| Transparency policy | `TRANSPARENCY_POLICY.md` | NEEDS_REVIEW |
| Privacy policy | `BENEFICIARY_PRIVACY_POLICY.md` | NEEDS_REVIEW |
| Receiving policy | `docs/RECEIVING_CHANNEL_PUBLICATION_POLICY.md` | NEEDS_REVIEW |
| Qualified reviewer note | future review packet | NOT_ATTACHED |
| Latest CI result | GitHub Actions Validate | REQUIRED |

## Review checklist

- [ ] Operating jurisdiction is recorded.
- [ ] Qualified legal reviewer status is recorded.
- [ ] Qualified tax/accounting reviewer status is recorded.
- [ ] Donation wording is reviewed.
- [ ] Public dashboard wording is reviewed.
- [ ] Reporting and recordkeeping obligations are reviewed.
- [ ] Conversion or withdrawal recordkeeping plan is reviewed.
- [ ] Charity/nonprofit status wording is reviewed.
- [ ] Reviewer notes are attached to the review packet.

## Current blockers

```text
LEGAL_REVIEW_STATUS: NOT_ATTACHED
TAX_REVIEW_STATUS: NOT_ATTACHED
JURISDICTION_RECORD: NOT_FINAL
REPORTING_OBLIGATIONS_REVIEW: NOT_ATTACHED
PUBLIC_WORDING_REVIEW: NOT_ATTACHED
LEGAL_TAX_READY: NO
```

## Go/no-go rule

```text
IF legal or tax review evidence is incomplete:
    GO_LIVE = NO
```
