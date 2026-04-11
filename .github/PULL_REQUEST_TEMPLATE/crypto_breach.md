## Cryptocurrency / Web3 Breach

Use this template for incidents involving cryptocurrency, DeFi protocols, or Web3 platforms (`category: cryptocurrency`).

### File placement

- **Directory:** `cryptocurrency/`
- **Filename:** `YYYY-MM_slug.yaml` (e.g., `2026-04_defi-bridge-exploit.yaml`)

### Pre-submission checklist

- [ ] YAML file placed in `cryptocurrency/` directory
- [ ] File named `YYYY-MM_slug.yaml`
- [ ] All core fields filled in (`source_name`, `source_url`, `date_of_breach`, `date_of_disclosure`, `notes`)
- [ ] `financial_loss_usd` filled in (**required** for crypto breaches)
- [ ] `blockchain` filled in if applicable
- [ ] `financial_recovered_usd` filled in if any recovery occurred
- [ ] `affected_count` filled in if known
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
category: cryptocurrency
notes: ""

# ── Crypto / Web3 fields ──────────────────────────────────────────────────────
financial_loss_usd: 0                 # REQUIRED — plain number, no $ or commas (e.g. 1500000)
blockchain: ""                        # Recommended — e.g. "ethereum", "solana", "bitcoin", "bsc"
financial_recovered_usd: 0            # Amount recovered, 0 if none
affected_count: 0                     # Number of affected wallets/users, 0 if unknown

# ── Optional traditional fields ────────────────────────────────────────────────
initial_attack_vector: ""             # e.g. "Smart contract exploit / hack", "Rug pull"
vendor_product: ""                    # Protocol or platform name
```

### Notes guidance

The `notes` field should be a narrative paragraph covering: what happened, when, which protocol/chain was affected, how the exploit worked, what the financial impact was, and whether any funds were recovered. See existing records in `cryptocurrency/` for reference.
