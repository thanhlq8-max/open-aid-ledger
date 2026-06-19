# Campaign Status Schema

The canonical campaign metadata file is:

```text
campaigns/campaigns.example.json
```

Production projects may copy this file to a reviewed campaign metadata file, but must keep the same schema and guardrails.

## Top-level fields

| Field | Type | Required | Notes |
|---|---:|---:|---|
| `schema_version` | string | Yes | Must be `campaigns.v1.0`. |
| `project_id` | string | Yes | Repository or project identifier. |
| `donations_active` | boolean | Yes | Must remain false until activation gates pass. |
| `wallets_published` | boolean | Yes | Must not be true while wallets are placeholders. |
| `campaigns` | array | Yes | Campaign records. |

## Campaign fields

| Field | Type | Required | Notes |
|---|---:|---:|---|
| `campaign_id` | string | Yes | Lowercase slug, 3-81 characters. |
| `title` | string | Yes | Human-readable title. |
| `status` | enum | Yes | `proposed`, `review`, `approved_inactive`, `active`, `paused`, `closed`, `cancelled`. |
| `purpose` | string | Yes | Public explanation of campaign scope. |
| `beneficiary_privacy_level` | enum | Yes | Privacy disclosure mode. |
| `donation_activation_allowed` | boolean | Yes | Must be false until gates pass. |
| `wallets_required` | boolean | Yes | Whether campaign requires public wallet metadata. |
| `ledger_required` | boolean | Yes | Whether campaign requires ledger reporting. |
| `decision_record_path` | path | Yes | Governance decision reference. |
| `report_path` | path | Yes | Transparency report reference. |
| `created_utc` | date | Yes | `YYYY-MM-DD`. |
| `last_reviewed_utc` | date | Yes | `YYYY-MM-DD`. |
| `guardrails` | array | Yes | Must include required guardrails. |
| `notes` | string | No | Public operational note. |

## Required guardrails

Every campaign must include:

```text
NO_PRIVATE_KEYS
NO_SEED_PHRASES
NO_AUTO_TRANSFER
NO_CUSTODY_AUTOMATION
NO_TRADING_ACCOUNT_TOP_UP
NO_MARGIN_CALL_SUPPORT
NO_RETURN_PROMISE
NO_BENEFICIARY_DOXXING
```

## Validation

```powershell
python scripts\validate_campaigns.py campaigns\campaigns.example.json --allow-inactive-template
```

On CI/Linux:

```bash
python scripts/validate_campaigns.py campaigns/campaigns.example.json --allow-inactive-template
```
