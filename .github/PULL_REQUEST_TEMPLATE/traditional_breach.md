## Traditional Breach

Use this template for ransomware, data leaks, supply-chain compromises, credential theft, and other incidents that don't fall under cloud, AI, or crypto categories.

### File placement

- **Directory:** one of `ransomware/`, `data-leak/`, `supply-chain/`, `credential-theft/`, or `other/`
- **Filename:** `YYYY-MM_slug.yaml` (e.g., `2026-04_acme-corp-ransomware.yaml`)
- The file **must** be placed in the directory matching its `category` value.

### Pre-submission checklist

- [ ] YAML file placed in the correct category directory
- [ ] File named `YYYY-MM_slug.yaml`
- [ ] `category` set to one of: `ransomware`, `data-leak`, `supply-chain`, `credential-theft`, `other`
- [ ] All core fields filled in (`source_name`, `source_url`, `date_of_breach`, `date_of_disclosure`, `notes`)
- [ ] `notes` contains a substantive narrative (timeline, scope, threat actor, impact)
- [ ] `source_url` links to an authoritative report
- [ ] Relevant optional fields filled in where information is available

### Breach record

All fields below the core section are optional. Fill in whichever are relevant to the incident.

```yaml
# ── Core fields (all required) ─────────────────────────────────────────────────
source_name: ""
source_url: ""
date_of_breach: "YYYY-MM-DD"
date_of_disclosure: ""                # YYYY-MM-DD or "" if unknown
category: ""                          # ransomware | data-leak | supply-chain | credential-theft | other
notes: ""

# ── Traditional breach fields (all optional) ──────────────────────────────────
date_of_customer_notification: ""     # YYYY-MM-DD or "" if unknown
initial_attack_vector: ""             # CWE-NNN description or free-text
cve: []                               # e.g. ["CVE-2024-1234", "GHSA-xxxx-xxxx-xxxx"]
vendor_product: ""                    # Affected vendor and/or product
software_package: ""                  # Package name for supply-chain incidents
malware: ""                           # Malware family name if identified
supply_chain_claimed: false           # true if a third-party vendor was the attack vector
```

### Notes guidance

The `notes` field should be a narrative paragraph covering: what happened, when, who was affected, how the breach occurred, what the impact was, and any remediation or attribution details. See existing records in the relevant category directory for reference.
