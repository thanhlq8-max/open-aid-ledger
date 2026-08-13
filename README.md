# Open Aid Ledger

Open Aid Ledger is a reusable open-source template for showing where support came from, how funds were used, and what evidence supports each public record.

**This repository is a working template and demo. It is not currently collecting donations, and it does not publish a live receiving wallet.**

## What can I do here?

Choose the path that matches what you want to do:

- **See how it works:** open the [public dashboard](https://thanhlq8-max.github.io/open-aid-ledger/) or read the [5-minute sample walkthrough](docs/REPRODUCIBLE_SAMPLE_WALKTHROUGH.md).
- **Try it yourself:** validate the bundled fictional ledger and generate a sample transparency report locally.
- **Use the template:** follow [Start Here](docs/START_HERE.md) to understand the donor, maintainer, and reviewer paths.

## Why this exists

Public support projects often need to answer simple questions clearly:

- Is the project actually accepting support right now?
- Where did the recorded funds come from?
- How were they used?
- What can be shown publicly without exposing the people being helped?
- What should happen if a record cannot be verified?

This repository provides a structured starting point for answering those questions with a public status page, sample ledgers, validation tools, transparency reports, review records, and safety procedures.

## How it works

At a high level:

1. A maintainer publishes a clear public status.
2. Ledger records are stored in a simple, reviewable format.
3. Validators check the records and a transparency report can be generated.
4. Reviewers record blockers before any future live operation is considered.

The repository currently demonstrates that flow with fictional sample data only.

## Try the sample in about 5 minutes

The easiest way to understand the project is to run the bundled example:

[Open the reproducible sample walkthrough →](docs/REPRODUCIBLE_SAMPLE_WALKTHROUGH.md)

You will validate a fictional ledger, generate a Markdown transparency report, and compare the result with known expected totals. No blockchain connection, wallet, private account, or real funds are required.

## Who is this for?

**Maintainers** can use the repository as a starting point for a transparent support workflow.

**Reviewers** can inspect status, privacy controls, ledger evidence, reconciliation steps, and unresolved blockers.

**Donors or observers** can check whether support is active and where authoritative public information should come from.

If you only want the shortest route through the repository, use [Quick Access](docs/QUICK_ACCESS.md).

## Current human-readable status

Open Aid Ledger has a published `v1.0.0` repository release, but the support operation is still inactive.

**Do not send funds.** No live receiving details are published.

If this project is ever activated in the future, that must happen through a separate reviewed process and the public dashboard must clearly say that support is active.

## What this project does not do

Open Aid Ledger is not a payment processor, custody wallet, investment product, trading fund, token project, or promise of financial return.

It does not sign transactions, automate transfers, expose beneficiary private information, or turn a repository release into permission to collect funds.

## For maintainers and contributors

Useful operating documents include:

- [Start Here](docs/START_HERE.md)
- [Quick Access](docs/QUICK_ACCESS.md)
- [Dry-run operations runbook](docs/DRY_RUN_OPERATIONS_RUNBOOK.md)
- [Donation readiness review packet](docs/DONATION_READINESS_REVIEW_PACKET.md)
- [Review packet template](docs/REVIEW_PACKET_TEMPLATE.md)
- [Operational readiness matrix](docs/OPERATIONAL_READINESS_MATRIX.md)
- [Share kit](docs/SHARE_KIT.md)
- [Contributing guide](CONTRIBUTING.md)

The repository uses GitHub Actions to run compile checks, ledger validation, release/status consistency checks, public-safety checks, tests, and sample report generation.

For local development:

```powershell
python -m compileall scripts tests
python scripts\validate_release_consistency.py .
python scripts\check_public_safety.py .
python -m pytest -q
```

## Technical status

The block below is intentionally machine-readable so repository validators can detect status drift. Most users do not need to interpret it.

```text
PROJECT_STATUS: PUBLIC_TEMPLATE
VERSION: 1.0.0
RELEASE_TARGET: v1.0.0
RELEASE_TAG_CREATED: YES
GITHUB_RELEASE_CREATED: YES
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
CUSTODY_AUTOMATION: NO
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
GO_LIVE: NO
```

Safety guardrails:

```text
NO_PRIVATE_KEYS
NO_SEED_PHRASES
NO_AUTO_TRANSFER
NO_EXCHANGE_WITHDRAWAL_API
NO_CUSTODY_AUTOMATION
NO_RETURN_PROMISE
NO_BENEFICIARY_DOXXING
```

## License

See [LICENSE](LICENSE).
