# Publishing Guide

This guide publishes the repository to GitHub as a public transparency project.

## Requirements

- Git installed.
- GitHub CLI installed.
- GitHub CLI authenticated with an account that can create public repositories.

Check:

```powershell
git --version
gh auth status
```

If needed:

```powershell
gh auth login
```

## Recommended repository

```text
thanhlq8-max/open-aid-ledger
```

Suggested GitHub description:

```text
Transparency-first public ledger for voluntary digital-asset donations supporting hardship cases and open-source public goods.
```

Suggested topics:

```text
open-source, transparency, donations, crypto, charity, public-good, ledger, vietnam, community-support
```

## One-command publish

From the repository root:

```powershell
.\CREATE_REPO_AND_PUSH.ps1 -RepoName open-aid-ledger -Owner thanhlq8-max -Visibility public
```

The script initializes git, commits the files, creates the public GitHub repo, and pushes the initial commit.

The script uses `gh repo create --source . --push`, which is the GitHub CLI path for creating a remote repo from an existing local repo and pushing local commits.

## Manual publish

```powershell
git init
git branch -M main
git add .
git commit -m "Initialize Open Aid Ledger"
gh repo create thanhlq8-max/open-aid-ledger --public --source . --remote origin --push --description "Transparency-first public ledger for voluntary digital-asset donations supporting hardship cases and open-source public goods."
```

## After publish

1. Open the repository page.
2. Confirm GitHub Actions runs.
3. Confirm README renders correctly.
4. Confirm donation status still says inactive until wallets are filled.
5. Create labels listed in `docs/RECOMMENDED_LABELS.md`.
6. Open initial issues from `docs/INITIAL_ISSUES.md`.
7. Do not activate donations until `wallets.json` is ready and reviewed.
