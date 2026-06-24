# Disbursement Decision Record Template

## Status

Review-only template.

Use this template to document why support was approved, paused, rejected, or closed while keeping donation collection inactive until a future activation gate is explicitly approved.

```text
DONATIONS_ACTIVE: NO
WALLETS_PUBLISHED: NO
CUSTODY_AUTOMATION: NO
TRANSFER_AUTOMATION: NO
```

## Public-safety rule

A public decision record must not include:

- real beneficiary identity;
- exact address;
- phone number;
- private message excerpts;
- unredacted receipts;
- bank details;
- wallet secrets;
- personal documents.

Use beneficiary codes and redacted summaries only.

## Decision metadata

```text
Decision ID: <DECISION_ID>
Campaign ID: <CAMPAIGN_ID>
Beneficiary code: <BENEFICIARY_CODE>
Decision status: <proposed | review | approved_inactive | paused | rejected | closed | cancelled>
Decision date: <YYYY-MM-DD>
Reviewer handles: <REVIEWER_HANDLES>
Privacy level: <redacted_public_summary | redacted_receipts | partner_attestation_only | public_project_summary>
Evidence level: <summary | redacted_receipts | partner_attestation | private_review>
Related attestation: <ATTESTATION_ID_OR_NONE>
Conflict disclosure path: <PATH_OR_NONE>
Campaign metadata path: <PATH>
Report path: <PATH>
```

## Need summary

```text
Need category: <FOOD | RENT | MEDICAL | EDUCATION | SHELTER | PUBLIC_GOOD | OTHER>
Public-safe summary: <REDACTED_SUMMARY>
Urgency: <low | medium | high | emergency_review>
Scope result: <in_scope | out_of_scope | needs_review>
```

Do not include details that can identify a person indirectly.

## Review findings

```text
Evidence reviewed: <yes | no | partner_attestation_only>
Evidence location: <private_review_storage | not_applicable>
Privacy review result: <pass | needs_redaction | fail>
Conflict review result: <pass | disclosed | fail>
Campaign scope result: <pass | needs_review | fail>
Safety review result: <pass | needs_review | fail>
```

## Support decision

```text
Decision: <approved_inactive | paused | rejected | closed | cancelled>
Approved support description: <PUBLIC_SAFE_DESCRIPTION>
Approved amount or category: <AMOUNT_OR_CATEGORY_IF_PUBLIC_SAFE>
Disbursement method: <manual | partner_mediated | pending_future_activation | not_applicable>
Disbursement details public: <redacted | not_applicable>
Ledger row required: <yes | no>
```

If donation collection is inactive, use `approved_inactive` or `pending_future_activation` rather than implying that funds are already collected or transferable.

## Required guardrail confirmation

- [ ] No beneficiary doxxing.
- [ ] No personal documents committed.
- [ ] No wallet secrets or private account details included.
- [ ] No automatic transfer path used.
- [ ] No exchange withdrawal path used.
- [ ] No trading account support.
- [ ] No margin-call or trading-loss support.
- [ ] No return promise.
- [ ] No charity-registration claim unless separately documented by qualified review.
- [ ] Donation activation status remains unchanged.

## Ledger mapping for future reporting

```text
ledger_date: <YYYY-MM-DD>
campaign_id: <CAMPAIGN_ID>
beneficiary_code: <BENEFICIARY_CODE>
support_purpose: <PUBLIC_SAFE_PURPOSE>
amount: <AMOUNT_IF_PUBLIC_SAFE>
asset_or_currency: <ASSET_OR_CURRENCY_IF_PUBLIC_SAFE>
reference: <REDACTED_REFERENCE_OR_NONE>
report_path: <PATH>
```

Do not include private account details or unredacted transaction screenshots.

## Closeout notes

```text
Closeout status: <not_started | partially_completed | completed | cancelled>
Public proof level: <summary | redacted_receipts | partner_attestation_only | none>
Follow-up needed: <yes | no>
Takedown risk reviewed: <yes | no>
```

## Related documents

```text
docs/BENEFICIARY_INTAKE_REVIEW.md
docs/PARTNER_ATTESTATION_TEMPLATE.md
BENEFICIARY_PRIVACY_POLICY.md
docs/CAMPAIGN_REVIEW_CHECKLIST.md
TRANSPARENCY_POLICY.md
```
