# breach-notes

Structured YAML records of breach reports, advisories, and cyber incidents.

## Schema

Each YAML file captures:
- `source_name`: publication or organization name
- `source_url`: direct URL to the report
- `date_of_breach`: when the breach occurred (best estimate)
- `date_of_disclosure`: when publicly disclosed
- `date_of_customer_notification`: when affected parties were notified
- `category`: impact category (ransomware, data-leak, supply-chain, credential-theft, other)
- `initial_attack_vector`: CWE or description
- `cve`: list of CVE/GHSA/etc IDs mentioned
- `vendor_product`: vendor product involved
- `software_package`: software package involved
- `malware`: malware name/family if mentioned
- `supply_chain_claimed`: boolean
- `notes`: free-form additional context

## Folders

- `ransomware/` — ransomware incidents
- `data-leak/` — customer data exposure
- `supply-chain/` — supply chain attacks
- `credential-theft/` — credential compromise
- `other/` — uncategorized or multi-category

