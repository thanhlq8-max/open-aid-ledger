# External Review Feedback Register

## Status

This register is a template. It contains no real reviewer data and no active donation approval.

## Register fields

Each review finding should include:

| Field | Meaning |
|---|---|
| ID | Stable finding identifier |
| Reviewer role | Reviewer category or role |
| Area | Reviewed area |
| Severity | low, medium, high, blocker |
| Finding | Concise issue description |
| Evidence | File or process evidence |
| Recommendation | Reviewer recommendation |
| Maintainer response | Accepted, rejected, deferred |
| Resolution status | open, mitigated, resolved, not applicable |
| Closure evidence | Link or note |

## Severity definitions

- `blocker`: prevents activation proposal.
- `high`: must be resolved before activation proposal.
- `medium`: should be resolved or explicitly accepted.
- `low`: may be deferred with rationale.

## Guardrails

Do not include private beneficiary information, wallet control secrets, unpublished wallet addresses, or personal identity data beyond what reviewers explicitly approve for public disclosure.
