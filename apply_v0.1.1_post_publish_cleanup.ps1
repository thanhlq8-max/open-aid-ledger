param(
    [string]$RepoPath = "."
)

$ErrorActionPreference = "Stop"

function Write-Utf8NoBom {
    param([string]$Path, [string]$Content)
    $dir = Split-Path -Parent $Path
    if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    $full = Join-Path (Get-Location) $Path
    [System.IO.File]::WriteAllText($full, $Content, $utf8NoBom)
}

$root = Resolve-Path $RepoPath
Set-Location $root

if (-not (Test-Path "README.md")) { throw "README.md not found. Run from open-aid-ledger root." }
if (-not (Test-Path "scripts")) { throw "scripts directory not found. Run from open-aid-ledger root." }

$readme = Get-Content "README.md" -Raw

if ($readme -notmatch "\*\*Current milestone:\*\*") {
    $readme = $readme -replace "(\*\*Donation status:\*\* inactive until maintainers publish verified wallet addresses\s+)", "`$1**Current milestone:** v0.1.1 post-publish cleanup / v0.2.0 ledger-safety foundation  `r`n"
}

$backlog = @'
---

## Active public backlog

The first public backlog is intentionally focused on safety and transparency infrastructure:

- [#1 Harden wallet metadata schema](https://github.com/thanhlq8-max/open-aid-ledger/issues/1)
- [#2 Add unit tests for wallet and ledger validators](https://github.com/thanhlq8-max/open-aid-ledger/issues/2)
- [#3 Add sample transparency report](https://github.com/thanhlq8-max/open-aid-ledger/issues/3)
- [#4 Add GitHub Pages static report design](https://github.com/thanhlq8-max/open-aid-ledger/issues/4)
- [#5 Design read-only blockchain explorer importer](https://github.com/thanhlq8-max/open-aid-ledger/issues/5)
- [#6 Add maintainer governance checklist](https://github.com/thanhlq8-max/open-aid-ledger/issues/6)

The project should not move to active donations until the wallet schema, ledger validation, privacy policy, governance checklist, and reporting workflow have been reviewed.

'@

if ($readme -notmatch "## Active public backlog") {
    $needle = "Donations should not be sent until the maintainers create a real ``wallets.json``, publish the first transparency report, and make the policy files consistent with the active campaign."
    $replacement = $needle + "`r`n`r`nThe repository has been published publicly and the initial safety backlog is open. The current development focus is to harden the transparency infrastructure before any real wallet address is published.`r`n" + $backlog
    $readme = $readme.Replace($needle, $replacement)
}

$readme = $readme.Replace(
    "See [`docs/PUBLISHING.md`](docs/PUBLISHING.md) and [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md).",
    "See [`docs/PUBLISHING.md`](docs/PUBLISHING.md), [`docs/POST_PUBLISH_STATUS.md`](docs/POST_PUBLISH_STATUS.md), and [`RELEASE_CHECKLIST.md`](RELEASE_CHECKLIST.md)."
)

Write-Utf8NoBom -Path "README.md" -Content $readme

$changelogExisting = if (Test-Path "CHANGELOG.md") { Get-Content "CHANGELOG.md" -Raw } else { "# Changelog`r`n" }
if ($changelogExisting -notmatch "v0.1.1-post-publish-cleanup") {
    $entry = @'
## v0.1.1-post-publish-cleanup — 2026-06-19

Documentation-only post-publish cleanup.

Added:

- post-publish status document;
- release notes for v0.1.0 public-release candidate;
- README active backlog links for issues #1 through #6;
- explicit milestone marker for v0.1.1 / v0.2.0.

No donation activation, wallet publication, custody automation, or trading-related behavior was added.

'@
    $changelogExisting = $changelogExisting -replace "# Changelog\s*", "# Changelog`r`n`r`n$entry"
}
Write-Utf8NoBom -Path "CHANGELOG.md" -Content $changelogExisting

Write-Utf8NoBom -Path "VERSION" -Content "0.1.1-post-publish-cleanup`r`n"

$releaseNotes = @'
# Release Notes — v0.1.0 Public Release Candidate

**Release type:** public template / safety foundation  
**Donation status:** inactive  
**Wallet status:** no real wallet address published  
**Release date:** 2026-06-19

## Summary

This release publishes the initial Open Aid Ledger transparency template.

The repository is intended to provide a public, read-only framework for voluntary digital-asset donation transparency. It is designed to support hardship cases and open-source public-good work without becoming a trading fund, payment processor, exchange, broker, custody service, or charity-registration substitute.

## Included

- README with public guardrails.
- Donation policy.
- Transparency policy.
- Beneficiary privacy policy.
- Vietnam legal and tax operational note.
- Campaign templates.
- Wallet metadata example.
- Donation and disbursement ledger CSV templates.
- Markdown transparency report generator.
- Wallet validator.
- Ledger validator.
- Public safety scanner.
- GitHub Actions validation workflow.
- Issue templates.
- Publishing guide.
- Release checklist.
- Scam-prevention and address-change procedures.

## Explicit non-goals

This release does not activate donations, publish real wallet addresses, store private keys, automate custody, provide trading signals, fund trading accounts, rescue margin calls, issue tokens, promise returns, or claim charity registration.

## First public backlog

- #1 Harden wallet metadata schema
- #2 Add unit tests for wallet and ledger validators
- #3 Add sample transparency report
- #4 Add GitHub Pages static report design
- #5 Design read-only blockchain explorer importer
- #6 Add maintainer governance checklist

## Activation gate

Donations must remain inactive until wallet schema, validator tests, sample report, governance checklist, wallet procedure, legal/tax notes, public safety scan, and the first campaign policy are reviewed.
'@
Write-Utf8NoBom -Path "RELEASE_NOTES_v0.1.0.md" -Content $releaseNotes

$postPublish = @'
# Post-Publish Status

**Repository:** `thanhlq8-max/open-aid-ledger`  
**Status:** public repository published  
**Current version:** `0.1.1-post-publish-cleanup`  
**Donation status:** inactive  
**Wallet status:** no verified real wallet published  
**Last updated:** 2026-06-19

## Current lock

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Completed

- Public repository created.
- Initial README, policies, validators, campaign templates, and workflow committed.
- Six initial issues opened.
- Public labels added for documentation, enhancement, security, governance, and good-first-issue work.

## Initial issue backlog

| Issue | Purpose | Priority |
|---|---|---|
| #1 Harden wallet metadata schema | Prevent ambiguous or unsafe wallet publication | P0 |
| #2 Add unit tests for wallet and ledger validators | Prevent silent validator regressions | P0 |
| #3 Add sample transparency report | Make transparency output easy to review | P1 |
| #4 Add GitHub Pages static report design | Prepare shareable public transparency site | P1 |
| #5 Design read-only blockchain explorer importer | Plan future transaction import without custody risk | P1 |
| #6 Add maintainer governance checklist | Define operational controls before donation activation | P0 |

## Next milestone

```text
v0.2.0 — Ledger Safety & Public Report Foundation
```

Recommended order:

1. Complete issue #1.
2. Complete issue #2.
3. Complete issue #6.
4. Complete issue #3.
5. Confirm GitHub Actions passes.
6. Create/tag `v0.1.0-public-release-candidate` or `v0.1.1-post-publish-cleanup` depending on maintainer preference.

## Do not do yet

- Do not publish real donation wallets.
- Do not ask people to send funds.
- Do not create a token.
- Do not add transfer automation.
- Do not add exchange API access.
- Do not collect private beneficiary identity documents through GitHub.
- Do not describe crypto as legal tender or legal means of payment.

## Activation prerequisites

Before donations become active, maintainers should complete wallet schema hardening, wallet verification procedure, address-change review, governance checklist, privacy checklist, campaign-specific policy, first report template, tax/recordkeeping note, public safety scan, and maintainer approval note.
'@
Write-Utf8NoBom -Path "docs\POST_PUBLISH_STATUS.md" -Content $postPublish

Write-Host ""
Write-Host "Applied v0.1.1 post-publish cleanup."
Write-Host "Changed/added:"
Write-Host "- README.md"
Write-Host "- CHANGELOG.md"
Write-Host "- VERSION"
Write-Host "- RELEASE_NOTES_v0.1.0.md"
Write-Host "- docs\POST_PUBLISH_STATUS.md"
Write-Host ""
Write-Host "Run validation:"
Write-Host "python -m compileall scripts"
Write-Host "python scripts\validate_wallets.py wallets.example.json --allow-placeholders"
Write-Host "python scripts\validate_ledger.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv"
Write-Host "python scripts\check_public_safety.py ."
Write-Host "python scripts\generate_report.py --donations ledger\donations.csv --disbursements ledger\disbursements.csv --out reports\local-smoke-report.md"
Write-Host ""
Write-Host "Commit with GitHub Desktop:"
Write-Host "Summary: Document v0.1.1 post-publish cleanup"
