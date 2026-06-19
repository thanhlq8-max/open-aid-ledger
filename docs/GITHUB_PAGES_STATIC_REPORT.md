# GitHub Pages static report design

This document defines the first static-reporting path for Open Aid Ledger.

## Status

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
REPORTING_MODE: STATIC_ONLY
NETWORK_FETCHING: NO
CUSTODY_AUTOMATION: NO
```

The page is a public transparency surface, not a donation processor.

## Recommended Pages setup

Use GitHub Pages with one of these safe configurations:

1. Source branch: `main`
2. Source folder: `/docs`

The repository already keeps documentation in `docs/`, so the first public site can be static Markdown without a build system.

## Public site content

The initial static site should show:

- current project status;
- explicit donation inactive status;
- latest reviewed transparency report link;
- policy links;
- issue backlog links;
- safety guardrails;
- legal and tax disclaimer.

## Non-goals

The first static site must not include:

- wallet signing;
- transfer automation;
- exchange withdrawal integration;
- investment, yield, or trading language;
- raw beneficiary identity data;
- active donation address display unless `DONATIONS_ACTIVE` is explicitly changed through a reviewed commit.

## Future expansion

A later release may add generated HTML, but the first public version remains Markdown-first and static-only.
