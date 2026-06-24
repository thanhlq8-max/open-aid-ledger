# Partner Attestation Template

## Status

Review-only template.

Use this when a trusted partner can confirm a hardship-support case without requiring the public repository to expose personal documents or identifying details.

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
NO_BENEFICIARY_DOXXING
```

## Use case

Partner attestation is appropriate when:

- direct public evidence would expose a vulnerable person;
- a local helper, school, clinic, shelter, community organizer, or open-source project maintainer can confirm the need;
- public reporting should show that review occurred without publishing raw evidence.

This template does not authorize donation activation, custody, payment processing, or automatic transfer.

## Private review fields

Keep this section private unless every field is redacted.

```text
Attestation ID: <ATTESTATION_ID>
Campaign ID: <CAMPAIGN_ID>
Beneficiary code: <BENEFICIARY_CODE>
Partner type: <community | school | clinic | shelter | OSS maintainer | other>
Partner public name: <PUBLIC_SAFE_NAME_OR_REDACTED>
Partner private contact: <PRIVATE_REVIEW_ONLY>
Reviewer: <MAINTAINER_HANDLE>
Review date: <YYYY-MM-DD>
Privacy level: <redacted_public_summary | redacted_receipts | partner_attestation_only | public_project_summary>
Evidence reviewed privately: <yes | no | not applicable>
Conflict disclosed: <yes | no | needs review>
Decision record path: <PATH>
```

Do not commit private contact details, personal documents, or unredacted proof material.

## Partner statement

```text
I confirm that I reviewed the case identified by <BENEFICIARY_CODE> for <CAMPAIGN_ID>.

Based on my review, the support need is:
<SHORT_PRIVATE_SUMMARY>

The public repository may describe this case only as:
<PUBLIC_SAFE_SUMMARY>

I understand that the public repository should not publish identifying personal details or raw private evidence.
```

## Maintainer review checklist

- [ ] Partner identity was reviewed through a private channel.
- [ ] Partner role is relevant to the case.
- [ ] Beneficiary code is used instead of real identity.
- [ ] Public summary is redacted.
- [ ] No personal documents will be committed.
- [ ] No private contact information will be committed.
- [ ] Conflict-of-interest disclosure is clean or documented.
- [ ] Campaign remains inactive unless a future activation gate is explicitly approved.

## Public-safe attestation summary

Use this format if a public report needs to reference the attestation:

```text
Attestation ID: <ATTESTATION_ID>
Campaign ID: <CAMPAIGN_ID>
Beneficiary code: <BENEFICIARY_CODE>
Partner type: <community | school | clinic | shelter | OSS maintainer | other>
Privacy level: <partner_attestation_only>
Public summary: <REDACTED_SUMMARY>
Review date: <YYYY-MM-DD>
```

## Rejection or pause reasons

Pause or reject the attestation if:

- the partner cannot be reviewed safely;
- the partner has an unresolved conflict of interest;
- the public summary would identify the beneficiary;
- the case is outside campaign scope;
- the case conflicts with project guardrails;
- legal, tax, safety, or platform-policy questions cannot be resolved by maintainers.

## Related documents

```text
docs/BENEFICIARY_INTAKE_REVIEW.md
docs/DISBURSEMENT_DECISION_RECORD_TEMPLATE.md
BENEFICIARY_PRIVACY_POLICY.md
docs/CAMPAIGN_REVIEW_CHECKLIST.md
```
