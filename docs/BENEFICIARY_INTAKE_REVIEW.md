# Beneficiary Intake and Relief Review Workflow

## Status

Review-only workflow.

This document helps maintainers review hardship-support cases without exposing vulnerable people or activating donation collection.

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
TRANSFER_AUTOMATION: NO
NO_BENEFICIARY_DOXXING
```

## Purpose

The workflow exists to answer four questions before any public campaign or future disbursement decision is considered:

1. Is the need real enough to review further?
2. Can the case be documented without public personal exposure?
3. Is there a conflict, safety risk, or unsupported purpose?
4. Can a public ledger entry later describe support without identifying the beneficiary?

## Operating boundaries

Maintainers must not commit or publish:

- full legal names;
- exact addresses;
- phone numbers;
- identity documents;
- unredacted medical records;
- child photos;
- private chat screenshots;
- bank account details;
- wallet screenshots or wallet secrets.

This workflow does not collect funds, publish wallets, move assets, or approve automated transfers.

## Roles

| Role | Responsibility |
|---|---|
| Intake reviewer | Receives a case through a private channel and assigns a beneficiary code. |
| Privacy reviewer | Confirms that public summaries are redacted and safe. |
| Evidence reviewer | Reviews proof material outside the public repository. |
| Decision reviewer | Records the support decision and links it to campaign metadata. |
| Maintainer | Ensures activation gates remain inactive unless explicitly reviewed later. |

A single maintainer may hold multiple roles only if the conflict-of-interest review is clean.

## Beneficiary code

Use a pseudonymous code, not a name.

Recommended format:

```text
CHD-YYYY-NNN
FAM-YYYY-NNN
MED-YYYY-NNN
HOM-YYYY-NNN
OSS-YYYY-NNN
```

Examples:

```text
FAM-2026-001
MED-2026-001
OSS-2026-001
```

## Review stages

### 1. Private intake

Record privately:

- beneficiary code;
- broad need category;
- broad location level if needed;
- requested support summary;
- evidence type received;
- consent and redaction preference;
- immediate safety concerns;
- reviewer name or handle.

Do not put private intake material in the public repository.

### 2. Scope screening

Reject or pause the case if it involves:

- trading account top-up;
- trading-loss recovery;
- margin-call support;
- return promise;
- token sale or investment pitch;
- private account credentials;
- coercion, unclear consent, or unsafe publication risk.

### 3. Evidence review

Acceptable evidence levels are:

| Level | Public handling |
|---|---|
| redacted_public_summary | Safe summary can be public. |
| redacted_receipts | Receipts may be public only after redaction. |
| partner_attestation_only | Public repo records partner confirmation only. |
| public_project_summary | Public project support can be described without personal data. |

Evidence review should produce a short public-safe summary, not raw evidence.

### 4. Privacy review

Before any public reference is created, confirm:

- beneficiary code is used instead of identity;
- exact location is removed;
- documents are not committed;
- photos are omitted unless safe and consented;
- public report wording cannot identify the person indirectly;
- takedown path is understood.

### 5. Decision record

Create a decision record from:

```text
docs/DISBURSEMENT_DECISION_RECORD_TEMPLATE.md
```

The record may be kept private during review. If a public version is committed, it must use redacted fields only.

### 6. Campaign mapping

Every reviewed case should map to a campaign record in:

```text
campaigns/campaigns.example.json
```

The campaign must remain inactive unless donation activation is explicitly reviewed later.

### 7. Ledger mapping

A future public ledger row should use:

- beneficiary code;
- campaign ID;
- date;
- amount category or amount if public-safe;
- support purpose;
- redacted transaction reference if any;
- report path.

Do not publish bank details, wallet secrets, personal documents, or private contact information.

## Minimum public-safe case summary

Use this format for public reports:

```text
Beneficiary code: <BENEFICIARY_CODE>
Campaign: <CAMPAIGN_ID>
Need category: <FOOD | RENT | MEDICAL | EDUCATION | SHELTER | PUBLIC_GOOD | OTHER>
Privacy level: <redacted_public_summary | redacted_receipts | partner_attestation_only | public_project_summary>
Evidence level: <summary only>
Decision status: <proposed | review | approved_inactive | paused | closed | cancelled>
Public summary: <short redacted summary>
```

## Stop conditions

Stop review if:

- identity exposure cannot be controlled;
- consent is unclear;
- evidence cannot be reviewed safely;
- the case creates legal, tax, safety, or platform-policy concerns that maintainers cannot resolve;
- the case conflicts with project guardrails.

## Maintainer checklist

- [ ] Beneficiary code assigned.
- [ ] No personal documents committed.
- [ ] Privacy level selected.
- [ ] Evidence level selected.
- [ ] Scope screening completed.
- [ ] Conflict-of-interest review completed.
- [ ] Partner attestation considered if direct evidence should not be public.
- [ ] Decision record drafted.
- [ ] Campaign mapping checked.
- [ ] Donation activation remains inactive.

## Related documents

```text
BENEFICIARY_PRIVACY_POLICY.md
docs/PARTNER_ATTESTATION_TEMPLATE.md
docs/DISBURSEMENT_DECISION_RECORD_TEMPLATE.md
docs/CAMPAIGN_REVIEW_CHECKLIST.md
docs/CONFLICT_OF_INTEREST_DISCLOSURE_TEMPLATE.md
```
