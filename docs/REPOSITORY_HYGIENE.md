# Repository Hygiene

## Current status

```text
VERSION: 0.1.4-final-helper-cleanup
PUBLIC_REPOSITORY: YES
PATCH_HELPER_ARTIFACTS_ALLOWED_IN_ROOT: NO
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
```

## Rule

The repository root must not retain local patch helper files after a patch has been applied.

Do not commit files such as:

```text
PATCH_README.txt
README_PATCH.md
README_RESTORE.md
apply_v0.1.1_post_publish_cleanup.ps1
apply_v0.1.2_public_repo_hygiene.ps1
apply_v0.1.3_restore_readme_cleanup.ps1
apply_v*.ps1
```

## Allowed root files

Root files should be stable project files only, such as:

```text
README.md
LICENSE
CHANGELOG.md
VERSION
DONATION_POLICY.md
TRANSPARENCY_POLICY.md
BENEFICIARY_PRIVACY_POLICY.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md
RELEASE_CHECKLIST.md
wallets.example.json
```

## Patch workflow

1. Apply local patch scripts outside the repository root where possible.
2. If a patch script must be copied into the root, remove it before committing.
3. Review GitHub Desktop changed files before committing.
4. Do not commit local smoke reports unless they are intentionally promoted to reviewed sample reports.
5. Do not commit private wallet material, seed phrases, private keys, or beneficiary-identifying material.

## Release rule

Before cutting any release, confirm that the root does not contain local helper artifacts and that `DONATIONS_ACTIVE` remains `NO` unless a reviewed activation process has explicitly approved a transition to `YES`.