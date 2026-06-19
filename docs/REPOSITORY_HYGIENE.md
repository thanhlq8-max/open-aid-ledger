# Repository Hygiene

## Purpose

This document defines public-repository hygiene rules for Open Aid Ledger.

The repository is intended to be a transparency template. Its public tree should not contain temporary patch instructions, local apply scripts, generated smoke-test files, secrets, private beneficiary data, or maintainer-only operational clutter.

## Public tree rules

Allowed:

- source scripts under `scripts/`;
- policy files;
- documentation;
- issue and pull request templates;
- campaign templates;
- placeholder wallet metadata;
- reviewed sample reports.

Forbidden:

- private keys;
- seed phrases;
- API tokens;
- exchange credentials;
- unredacted beneficiary private data;
- temporary patch apply scripts;
- local-only smoke reports unless intentionally reviewed as samples;
- active donation wallet files before governance approval.

## Patch helper cleanup

Patch helper files should be used locally and removed before commit. Examples:

```text
README_PATCH.md
README_RESTORE.md
apply_v*_*.ps1
```

If a helper artifact is accidentally committed, create a cleanup patch that removes it and confirms the README still describes the actual project, not the patch procedure.

## README rule

`README.md` must describe the project and public status. It must not be used as a temporary patch instruction file.

## Current hygiene status

```text
LAST_REVIEWED_VERSION: 0.1.3-restore-readme-cleanup
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
PATCH_HELPERS_ALLOWED_IN_PUBLIC_TREE: NO
```