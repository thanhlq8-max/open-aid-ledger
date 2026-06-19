# Issue and Release Mapping

This document maps the initial public backlog to releases. It is an operating aid, not an automatic issue closer.

| Issue | Title | Release coverage | Status guidance |
|---:|---|---|---|
| #1 | Harden wallet metadata schema | v0.2.0 | Close if wallet schema docs, validator, and tests are accepted. |
| #2 | Add unit tests for wallet and ledger validators | v0.2.0 | Close if CI includes pytest and validator regression tests. |
| #3 | Add sample transparency report | v0.3.0 | Close if sample report and sample ledger are accepted. |
| #4 | Add GitHub Pages static report design | v0.3.0 | Close if static status-page design is accepted. |
| #5 | Design read-only blockchain explorer importer | v0.4.0 | Close if importer design, schema, and reconciliation docs are accepted. |
| #6 | Add maintainer governance checklist | v0.5.0 | Close if governance, activation, freeze, and conflict docs are accepted. |
| N/A | Add campaign lifecycle validation | v0.6.0 | New foundation for future campaign status work. |

## Suggested issue closeout comment

```text
Implemented in <release/version>.

Scope completed:
- <short bullet>
- <short bullet>

Guardrails preserved:
- donations inactive;
- no wallet publication;
- no custody automation;
- no trading or return promise.

CI: Validate workflow passed on main.
```

Do not close an issue if CI is red or if the release only partially covers the acceptance criteria.
