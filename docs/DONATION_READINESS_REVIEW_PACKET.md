# Donation Readiness Review Packet

This packet tracks whether Open Aid Ledger is ready for a future donation activation proposal.

It does not activate donations, publish receiving details, or change project status.

## Current decision

```text
DONATION_READINESS: NOT_READY
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
ACTIVATION_APPROVED: NO
GO_LIVE: NO
```

## Evidence index

| Area | Evidence | Current result |
|---|---|---:|
| Public dashboard | `docs/index.md` | READY |
| Quick access | `docs/QUICK_ACCESS.md` | READY |
| Share kit | `docs/SHARE_KIT.md` | READY |
| Governance model | `docs/DONATION_GOVERNANCE_MODEL.md` | DRAFT |
| Activation checklist | `docs/DONATION_ACTIVATION_CHECKLIST.md` | BLOCKED |
| Readiness matrix | `docs/OPERATIONAL_READINESS_MATRIX.md` | BLOCKED |
| Receiving channel policy | `docs/RECEIVING_CHANNEL_PUBLICATION_POLICY.md` | BLOCKED |
| Account protection | `docs/RECEIVING_ACCOUNT_PROTECTION.md` | REVIEW_REQUIRED |
| Legal and tax note | `docs/VN_LEGAL_AND_TAX_NOTE.md` | REVIEW_REQUIRED |
| Dry-run evidence loop | `examples/dry-run/README.md` | READY_FOR_DRY_RUN |
| Review packet template | `docs/REVIEW_PACKET_TEMPLATE.md` | READY |
| Wallet inventory | `wallets.example.json` | PLACEHOLDER_ONLY |
| CI validation | GitHub Actions Validate | REQUIRED_BEFORE_ANY_PROPOSAL |

## Required work before activation proposal

- [ ] Governance model is documented and reviewed.
- [ ] Account protection evidence is recorded.
- [ ] Legal and tax review status is recorded.
- [ ] Campaign or support scope is reviewed.
- [ ] Active-mode donor guide is drafted and reviewed.
- [ ] Reconciliation exercise is completed.
- [ ] Freeze exercise is completed.
- [ ] Two-reviewer approval rule is satisfied.
- [ ] Activation commit plan is prepared.
- [ ] Latest CI result is attached to the review packet.

## Current blockers

```text
RECEIVING_CHANNEL_PUBLICATION: BLOCKED
ACCOUNT_PROTECTION_REVIEW: REQUIRED
LEGAL_TAX_REVIEW: REQUIRED
WALLET_INVENTORY: PLACEHOLDER_ONLY
ACTIVATION_COMMIT: NOT_PREPARED
GO_LIVE: NO
```

## Go/no-go rule

```text
IF any blocker remains:
    GO_LIVE = NO
```

## Next allowed step

Prepare evidence for the blockers above. Keep all public status fields inactive until a separate reviewed activation proposal is ready.
