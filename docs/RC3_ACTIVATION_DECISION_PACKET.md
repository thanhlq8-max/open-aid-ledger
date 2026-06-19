# RC3 Activation Decision Packet

## Purpose

This packet explains what a future activation decision must include.

This document is not an activation decision.

## Required sections

A future activation decision must include:

1. release version under review;
2. evidence pack summary;
3. external review findings summary;
4. unresolved risks;
5. accepted risks;
6. beneficiary privacy review status;
7. wallet publication precheck status;
8. public status page review status;
9. maintainer signoff;
10. activation decision.

## Allowed decision values

```text
ACTIVATION_DECISION: BLOCKED
ACTIVATION_DECISION: DEFERRED
ACTIVATION_DECISION: APPROVED_FOR_SEPARATE_ACTIVATION_RELEASE
```

## Current RC3 decision

```text
ACTIVATION_DECISION: BLOCKED
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
```

## Rule

No real wallet publication or donation activation may occur through this RC3 release.
