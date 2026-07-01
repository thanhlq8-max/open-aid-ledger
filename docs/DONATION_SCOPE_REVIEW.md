# Donation Scope Review

This document records the campaign or support scope required before any future donation activation proposal.

It does not activate donations, publish receiving details, or change project status.

## Current status

```text
DONATION_SCOPE_REVIEW: REQUIRED
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
GO_LIVE: NO
```

## Review scope

| Area | Evidence | Current result |
|---|---|---:|
| Public goal | `README.md` | BASELINE_EXISTS |
| Dashboard goal | `docs/index.md` | BASELINE_EXISTS |
| Campaign metadata | `campaigns/campaigns.example.json` | PLACEHOLDER_OR_INACTIVE |
| Public summary checklist | `docs/PUBLIC_SUMMARY_CHECKLIST.md` | BASELINE_EXISTS |
| Beneficiary privacy | `BENEFICIARY_PRIVACY_POLICY.md` | NEEDS_REVIEW |
| Donation policy | `DONATION_POLICY.md` | NEEDS_REVIEW |
| Review packet | future review packet | NOT_ATTACHED |
| Latest CI result | GitHub Actions Validate | REQUIRED |

## Scope checklist

- [ ] Supported purpose is recorded.
- [ ] Excluded purpose is recorded.
- [ ] Beneficiary privacy model is reviewed.
- [ ] Public summary fields are reviewed.
- [ ] Eligibility criteria are reviewed.
- [ ] Conflict-of-interest process is reviewed.
- [ ] Reporting cadence is reviewed.
- [ ] Reviewer notes are attached to the review packet.

## Current blockers

```text
SUPPORTED_SCOPE: NOT_FINAL
EXCLUDED_SCOPE: NOT_FINAL
ELIGIBILITY_REVIEW: NOT_ATTACHED
PRIVACY_REVIEW: NOT_ATTACHED
REPORTING_CADENCE: NOT_FINAL
DONATION_SCOPE_READY: NO
```

## Go/no-go rule

```text
IF donation scope evidence is incomplete:
    GO_LIVE = NO
```
