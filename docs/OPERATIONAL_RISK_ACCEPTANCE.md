# Operational Risk Acceptance

This document defines how maintainers record accepted, deferred, and blocking risks.

## Risk states

```text
OPEN
MITIGATED
ACCEPTED_WITH_LIMITS
DEFERRED
BLOCKING
```

## Current candidate risks

| Risk | Status | Required control |
|---|---:|---|
| Donation wording could be misunderstood | OPEN | Status page and README must say inactive |
| Wallet address publication could be spoofed | OPEN | Address-change procedure and review commit required |
| Campaign beneficiary privacy could be exposed | OPEN | Redacted beneficiary identifiers only |
| Maintainer conflict of interest | OPEN | Disclosure template before activation |
| Jurisdiction-specific tax treatment | OPEN | Legal/tax note and recordkeeping required |

## Acceptance rule

No risk marked `BLOCKING` may remain unresolved before a donation-ready release.

`ACCEPTED_WITH_LIMITS` requires a written decision record.
