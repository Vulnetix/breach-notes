## Cloud / SaaS Breach

Use this template for incidents involving cloud infrastructure or SaaS platforms (`category: cloud`).

### File placement

- **Directory:** `cloud/`
- **Filename:** `YYYY-MM_slug.yaml` (e.g., `2026-04_acme-s3-exposure.yaml`)

### Pre-submission checklist

- [ ] YAML file placed in `cloud/` directory
- [ ] File named `YYYY-MM_slug.yaml`
- [ ] All core fields filled in (`source_name`, `source_url`, `date_of_breach`, `date_of_disclosure`, `notes`)
- [ ] `cloud_provider` filled in (**required** for cloud breaches)
- [ ] `cloud_resource_crit` filled in (**required** for cloud breaches)
- [ ] `cloud_shared_responsibility` set to one of: `vendor`, `customer`, `shared`, `unknown`
- [ ] `notes` contains a substantive narrative (timeline, scope, threat actor, impact)
- [ ] `source_url` links to an authoritative report

### Breach record

Fields marked **REQUIRED** must be filled in. Remove or leave blank any optional fields that don't apply.

```yaml
# ── Core fields (all required) ─────────────────────────────────────────────────
source_name: ""
source_url: ""
date_of_breach: "YYYY-MM-DD"
date_of_disclosure: ""                # YYYY-MM-DD or "" if unknown
category: cloud
notes: ""

# ── Cloud fields ───────────────────────────────────────────────────────────────
cloud_provider: ""                    # REQUIRED — e.g. "AWS", "Azure", "GCP", "Snowflake", "Dropbox"
cloud_resource_crit: ""               # REQUIRED — CRIT identifier, e.g. "arn:aws:s3:::{bucket}",
                                      #   "subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Storage/storageAccounts/{name}",
                                      #   "projects/{project}/buckets/{bucket}"
cloud_shared_responsibility: ""       # REQUIRED — "vendor" | "customer" | "shared" | "unknown"

# ── Optional traditional fields ────────────────────────────────────────────────
initial_attack_vector: ""             # CWE-NNN description or free-text
cve: []                               # e.g. ["CVE-2024-1234"]
vendor_product: ""
supply_chain_claimed: false
```

### Notes guidance

The `notes` field should be a narrative paragraph covering: what happened, when, who was affected, how the breach occurred, what the impact was, and any remediation or attribution details. See existing records in `cloud/` for reference.
