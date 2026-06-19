param(
  [Parameter(Mandatory=$true)]
  [string]$RepoName,

  [string]$Owner = "thanhlq8-max",

  [ValidateSet("public", "private", "internal")]
  [string]$Visibility = "public",

  [string]$Description = "Transparency-first public ledger for voluntary digital-asset donations supporting hardship cases and open-source public goods.",

  [switch]$SkipValidation
)

$ErrorActionPreference = "Stop"

function Require-Command($Name) {
  if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
    throw "Required command not found: $Name"
  }
}

Require-Command git
Require-Command gh
Require-Command python

Write-Host "Checking GitHub CLI authentication..."
gh auth status | Out-Host

if (-not $SkipValidation) {
  Write-Host "Running local validation..."
  python -m compileall scripts
  python scripts/validate_wallets.py wallets.example.json --allow-placeholders
  python scripts/validate_ledger.py --donations ledger/donations.csv --disbursements ledger/disbursements.csv
  python scripts/check_public_safety.py .
  python scripts/generate_report.py --donations ledger/donations.csv --disbursements ledger/disbursements.csv --out reports/local-smoke-report.md
}

if (-not (Test-Path .git)) {
  Write-Host "Initializing local git repository..."
  git init
}

git branch -M main

Write-Host "Staging files..."
git add .

$HasChanges = git status --porcelain
if ($HasChanges) {
  git commit -m "Initialize Open Aid Ledger transparency template"
} else {
  Write-Host "No local changes to commit."
}

$FullName = "$Owner/$RepoName"
Write-Host "Checking whether GitHub repository already exists: $FullName"
$RepoExists = $false
try {
  gh repo view $FullName | Out-Null
  $RepoExists = $true
} catch {
  $RepoExists = $false
}

if ($RepoExists) {
  Write-Host "Repository already exists. Ensuring remote origin and pushing main..."
  $RemoteUrl = "https://github.com/$FullName.git"
  $ExistingOrigin = git remote get-url origin 2>$null
  if ($LASTEXITCODE -ne 0) {
    git remote add origin $RemoteUrl
  } elseif ($ExistingOrigin -ne $RemoteUrl) {
    git remote set-url origin $RemoteUrl
  }
  git push -u origin main
} else {
  Write-Host "Creating GitHub repository with GitHub CLI..."
  $VisibilityFlag = "--$Visibility"
  gh repo create $FullName $VisibilityFlag --source . --remote origin --push --description $Description --disable-wiki
}

Write-Host "Done."
Write-Host "Repository: https://github.com/$FullName"
Write-Host "Next: open GitHub Actions and verify workflow status."
