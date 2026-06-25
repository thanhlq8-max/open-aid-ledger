# Public Summary Checklist

This checklist helps maintainers prepare safe public summaries from internal review notes.

The checklist is documentation-only. It does not activate collection, publish live receiving details, automate custody, automate distribution, or replace qualified review.

## Purpose

A public summary should help readers understand what was reviewed, what was decided, and how the public ledger or report should describe the case without exposing a person or household.

Use this checklist before adding any case-related text to:

- ledger rows;
- transparency reports;
- release notes;
- public status pages;
- issue comments;
- pull request descriptions.

## Private review material

Keep the following material outside the public repository:

- full names;
- precise addresses;
- personal phone numbers;
- personal email addresses;
- identity documents;
- medical records;
- school records;
- employment records;
- exact workplace or school names;
- precise family composition;
- photos that identify a person, home, school, workplace, or vehicle;
- any unredacted partner notes;
- payment routing details;
- any screenshots that reveal private account information.

If any of the above is needed for review, store it in a private review location controlled by the maintainer or qualified partner. Do not commit it to this repository.

## Public summary fields

Prefer limited, non-identifying public fields:

| Field | Public-safe example |
|---|---|
| Case reference | `FAM-2026-001` |
| Region level | `province-level region` or `city-level region` |
| Support category | `rent support`, `food support`, `medical logistics support`, `school-cost support` |
| Review status | `reviewed`, `deferred`, `not approved`, `closed` |
| Evidence status | `partner-attested`, `maintainer-reviewed`, `insufficient evidence` |
| Decision date | `2026-06-25` |
| Amount band | optional; use only if approved by the publication policy |
| Public note | short, non-identifying explanation |

## Redaction checklist

Before publishing, confirm each item:

- [ ] No full personal names.
- [ ] No precise address or local landmark.
- [ ] No phone number or personal email.
- [ ] No identity document data.
- [ ] No photo metadata or image that can identify a person.
- [ ] No exact workplace, school, hospital, or shelter name unless already public and approved for publication.
- [ ] No private partner notes copied verbatim.
- [ ] No payment routing details.
- [ ] No raw screenshots from private chats, forms, bank apps, wallet apps, or exchange apps.
- [ ] No unsupported claim that a person has been verified by a legal authority.
- [ ] No promise that future support is guaranteed.
- [ ] No wording that implies investment return, yield, trading profit, or repayment obligation.
- [ ] No wording that implies the repository is a registered charity unless that status is separately documented by qualified counsel.
- [ ] Public text matches the current repository status: collection inactive, live receiving details unpublished, and activation not approved.

## Safe wording examples

### Good

```text
Case FAM-2026-001 was reviewed through maintainer notes and partner attestation. The public record only states the support category, review status, and decision reference. Private identifying details are not published.
```

```text
Decision: reviewed and approved for future ledger mapping after activation gates are separately completed. This record does not activate collection or distribution.
```

### Avoid

```text
A person at [exact address] needs help immediately. Here are their documents and contact details.
```

```text
Send funds now and we will distribute automatically.
```

```text
Donors will receive profit, yield, repayment, or trading benefits.
```

## Publication workflow

1. Prepare the internal review packet outside the public repository.
2. Create a case reference that does not reveal identity.
3. Draft a public summary using only public-safe fields.
4. Run the redaction checklist.
5. Have at least one maintainer or reviewer compare the public summary against the internal packet.
6. Add the public-safe summary to the appropriate ledger, report, or release artifact only after the relevant publication policy allows it.
7. Keep collection status, receiving-detail status, and activation status explicit.

## Stop conditions

Do not publish if:

- the case can be identified from the summary;
- evidence is not reviewed;
- consent or partner approval is unclear;
- the publication policy does not allow the field;
- the summary could create safety risk for the person, household, partner, or maintainer;
- the summary would imply activation before the activation gate is completed.

## Maintainer note

This checklist reduces obvious publication risk, but it is not legal, tax, compliance, security, or privacy advice. Use qualified review before any real public operation.
