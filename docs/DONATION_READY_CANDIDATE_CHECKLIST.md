# Donation-Ready Candidate Checklist

This checklist must be completed before the project can be treated as a donation-ready candidate.

## Repository status

- [ ] README states donation collection is inactive.
- [ ] `VERSION` matches the current release notes.
- [ ] CI passes on `main`.
- [ ] Public-safety scan passes.
- [ ] No helper patch artifacts are committed.

## Wallet controls

- [ ] `wallets.example.json` validates in placeholder mode.
- [ ] No real wallet address is required for this candidate.
- [ ] Wallet publication procedure is documented.
- [ ] Address-change procedure is documented.
- [ ] Custody model is documented without automation.

## Ledger controls

- [ ] Empty production ledger validates.
- [ ] Sample ledger validates.
- [ ] Balance enforcement passes on sample data.
- [ ] Duplicate transaction detection is covered by tests.

## Campaign controls

- [ ] `campaigns.example.json` validates as an inactive template.
- [ ] Campaign lifecycle states are documented.
- [ ] Review checklist exists for new campaigns.
- [ ] Campaign metadata does not imply active donation collection.

## Governance controls

- [ ] Maintainer governance checklist exists.
- [ ] Emergency freeze procedure exists.
- [ ] Conflict-of-interest template exists.
- [ ] Decision record template exists.

## Public communications

- [ ] Static public status page exists.
- [ ] Status page says donations are inactive.
- [ ] Release notes state the release is dry-run/candidate-only.
- [ ] No wording suggests investment, trading, return, or managed funds.

## Final candidate decision

```text
CANDIDATE_STATUS: PENDING_REVIEW
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
```
