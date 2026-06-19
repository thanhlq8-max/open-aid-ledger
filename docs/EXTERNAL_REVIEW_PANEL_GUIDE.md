# External Review Panel Guide

## Purpose

This guide explains how an external reviewer can inspect Open Aid Ledger before any donation activation is considered.

## Reviewer roles

Recommended review roles:

- governance reviewer;
- public transparency reviewer;
- privacy reviewer;
- operational safety reviewer;
- legal or tax context reviewer.

One person may cover multiple areas, but the review record should identify which areas were reviewed.

## Review checklist

Reviewers should inspect:

- `README.md`
- `DONATION_POLICY.md`
- `TRANSPARENCY_POLICY.md`
- `BENEFICIARY_PRIVACY_POLICY.md`
- `docs/DONATION_ACTIVATION_CHECKLIST.md`
- `docs/DONATION_READINESS_DRY_RUN.md`
- `docs/PUBLIC_STATUS_PAGE.md`
- `docs/WALLET_PUBLICATION_PRECHECK.md`
- `docs/RC2_EXTERNAL_REVIEW_ACTIVATION_GATE.md`

## Required findings

Each reviewer should record:

- scope reviewed;
- date reviewed;
- result: `approved`, `approved_with_notes`, or `blocked`;
- blocking issues, if any;
- non-blocking recommendations, if any;
- conflicts of interest, if any.

## Review boundaries

External review is not fund custody.

External reviewers do not approve asset transfers. They only review whether the public project controls are coherent enough for a later activation decision.

## Red flags

A reviewer should block activation if the repository:

- claims charity registration without verified basis;
- implies investment returns;
- implies trading-loss rescue support;
- exposes beneficiary identity data;
- contains signing material;
- contains transfer automation;
- lacks an emergency freeze procedure;
- lacks public reporting requirements.
