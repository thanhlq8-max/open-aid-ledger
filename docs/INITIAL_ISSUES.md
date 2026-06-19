# Initial Issues To Open After Publication

Open these manually after the public repository exists.

## 1. Activate repository labels

Title:

```text
Add initial governance and ledger labels
```

Body:

```text
Create labels from docs/RECOMMENDED_LABELS.md so audit, policy, privacy, wallet-change, and support-request issues are easier to triage.
```

Labels: `documentation`, `good first issue`

## 2. Prepare first real wallets.json

Title:

```text
Prepare first reviewed wallets.json before accepting donations
```

Body:

```text
Copy wallets.example.json to wallets.json, fill real wallet metadata, verify addresses out of band, and run scripts/validate_wallets.py wallets.json before any donation address is promoted.
```

Labels: `wallet-change`, `policy`, `security`

## 3. Draft first monthly transparency report template

Title:

```text
Create first monthly transparency report template
```

Body:

```text
Create reports/YYYY-MM.md using the generated report format and add human-readable campaign notes, privacy-safe beneficiary summary, and ledger reconciliation status.
```

Labels: `ledger`, `documentation`, `good first issue`

## 4. Review Vietnam legal/tax note

Title:

```text
Review Vietnam legal and tax wording before donation activation
```

Body:

```text
Review docs/VN_LEGAL_AND_TAX_NOTE.md and confirm the repo wording avoids legal-tender/payment-service claims. This is not a substitute for professional legal review.
```

Labels: `policy`, `help wanted`
