# Changelog

## 0.8.0-donation-readiness-dry-run

- Added donation-readiness dry-run documentation.
- Added dry-run wallet publication review checklist.
- Added launch risk register and future launch runbook.
- Added `scripts/validate_readiness.py` and regression tests.
- Kept donations inactive and wallets unpublished.

## 0.7.0-release-closeout-foundation

- Added release closeout documentation.
- Added initial issue completion map for issues #1 through #6.
- Added copy-ready issue closeout comments.
- Added GitHub Release draft for v0.7.0.
- Added tests for release closeout documentation.
- Donations remain inactive; wallets remain unpublished.

## v0.6.0 — Campaign lifecycle foundation

- Added campaign lifecycle metadata template.
- Added `scripts/validate_campaigns.py`.
- Added campaign lifecycle, status schema, review checklist, and issue/release mapping docs.
- Added campaign validator tests.
- Updated CI validation to include campaign metadata.
- Preserved donation-inactive, no-wallet-publication, no-custody, no-trading, and no-return-promise boundaries.

## v0.5.0 — Maintainer Governance Checklist

- Added maintainer governance checklist.
- Added donation activation checklist.
- Added emergency freeze procedure.
- Added conflict-of-interest disclosure template.
- Added governance decision record template.
- Added governance documentation tests.
- Kept donations inactive, wallets unpublished, custody automation disabled, trading use forbidden, and return promises forbidden.


## v0.4.0 — Read-only Blockchain Explorer Importer Design

- Added design-only read-only blockchain explorer importer documentation.
- Added normalized incoming transaction schema.
- Added manual reconciliation workflow for importer staging rows.
- Added fictional normalized transaction sample CSV under `examples/importer/`.
- Added tests to lock importer design guardrails.
- Kept donations inactive, wallets unpublished, and all custody/trading/return-promise guardrails unchanged.

## v0.3.0 — Sample Transparency Report + GitHub Pages Foundation

- Added a sample transparency report with fictional records only.
- Added sample ledger CSV rows under `examples/sample-ledger/`.
- Added static GitHub Pages status-page design docs.
- Added report-generation tests.
- Extended CI to validate sample ledgers and generate a sample report.
- Kept donations inactive and wallets unpublished.

## v0.2.0 — Ledger Safety Foundation

- Hardened wallet metadata schema to v1.1.
- Added stronger wallet metadata validation.
- Added stronger ledger CSV validation, duplicate transaction checks, and optional balance enforcement.
- Added validator regression tests and CI test execution.
- Added wallet schema and ledger validation documentation.
- Improved transparency report output with net balance by asset.
- Kept donations inactive and wallets unpublished.

## v0.1.4 — Final Helper Cleanup

- Removed residual local patch helper artifacts from the public repository root.
- Preserved the restored project README.
- Updated `VERSION` to `0.1.4-final-helper-cleanup`.
- Added `RELEASE_NOTES_v0.1.4.md`.
- Updated repository hygiene and post-publish status documentation.
- Kept donations inactive and wallet publication disabled.

## v0.1.3 — Restore README Cleanup

- Restored `README.md` to the main Open Aid Ledger project overview.
- Removed local patch helper artifacts from the public repository tree.
- Added `RELEASE_NOTES_v0.1.3.md`.
- Updated repository hygiene documentation.
- Kept donation activation disabled and all custody/trading guardrails unchanged.

## v0.1.2 — Public Repository Hygiene

- Removed local patch helper artifacts from the public repository.
- Added repository hygiene documentation.
- Kept all donation, wallet, custody, trading, and return-promise guardrails unchanged.

## v0.1.1 — Post-publish Cleanup

- Added post-publish status document.
- Added release notes for v0.1.0 public-release candidate.
- Added README active backlog links for issues #1 through #6.
- Added explicit milestone marker for v0.1.1 / v0.2.0.
- No donation activation, wallet publication, custody automation, or trading-related behavior was added.

## v0.1.0 — Public Release Candidate

- Added transparency-first README.
- Added donation policy.
- Added transparency policy.
- Added beneficiary privacy policy.
- Added Vietnam legal/tax operational note.
- Added campaign templates.
- Added ledger CSV templates.
- Added wallet metadata example.
- Added report generator.
- Added wallet validator.
- Added ledger validator.
- Added public safety scanner.
- Added GitHub Actions validation workflow.
- Added issue templates.
- Added publishing guide.
- Added release checklist.
- Added scam prevention and address-change procedures.
