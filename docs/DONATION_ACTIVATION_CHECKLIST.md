# Donation Activation Checklist

Open Aid Ledger starts inactive by design. This checklist defines the minimum criteria for any future activation.

Activation is not a technical toggle only. It is a governance, legal, tax, privacy, and security decision.

## Current state

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
PRIVATE_KEYS_IN_REPO: FORBIDDEN
TRADING_USE: FORBIDDEN
RETURN_PROMISE: FORBIDDEN
```

## Activation requirements

Do not publish real donation addresses until all sections are complete.

### 1. Policy review

- [ ] `DONATION_POLICY.md` reviewed.
- [ ] `TRANSPARENCY_POLICY.md` reviewed.
- [ ] `BENEFICIARY_PRIVACY_POLICY.md` reviewed.
- [ ] `SECURITY.md` reviewed.
- [ ] `docs/VN_LEGAL_AND_TAX_NOTE.md` reviewed if operating in Vietnam context.

### 2. Wallet governance

- [ ] Wallet ownership model documented.
- [ ] Multisig or equivalent governance documented.
- [ ] Address-change procedure reviewed.
- [ ] Wallet metadata passes validator.
- [ ] No private keys or seed phrases are present in the repository.
- [ ] Wallet addresses are verified out-of-band by maintainers.

### 3. Campaign readiness

- [ ] Campaign scope documented.
- [ ] Beneficiary privacy model documented.
- [ ] Eligibility criteria documented.
- [ ] Disbursement review process documented.
- [ ] Conflict-of-interest disclosure completed.

### 4. Reporting readiness

- [ ] Sample transparency report reviewed.
- [ ] Ledger CSV schema reviewed.
- [ ] Manual reconciliation process reviewed.
- [ ] Monthly reporting schedule defined.
- [ ] Emergency freeze process documented.

### 5. CI and safety gates

- [ ] GitHub Actions validation passes.
- [ ] Wallet validator passes.
- [ ] Ledger validator passes.
- [ ] Public safety scan passes.
- [ ] Unit tests pass.

## Activation commit requirements

The activation commit must explicitly change:

```text
DONATIONS_ACTIVE: NO -> YES
WALLETS_PUBLISHED: NO -> YES
```

The activation commit must not include:

- private keys;
- seed phrases;
- wallet signing code;
- auto-transfer code;
- exchange withdrawal API credentials;
- trading logic;
- return promises.

## Deactivation criteria

Set `DONATIONS_ACTIVE` back to `NO` if any of the following occurs:

- wallet compromise suspected;
- incorrect address published;
- beneficiary privacy incident detected;
- scam impersonation risk appears;
- ledger cannot be reconciled;
- legal/tax/platform risk changes materially;
- maintainers cannot perform review duties.
