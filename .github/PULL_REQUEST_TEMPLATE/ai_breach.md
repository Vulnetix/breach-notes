## AI Breach

Use this template for incidents involving AI models or AI-powered services (`category: ai`).

### File placement

- **Directory:** `ai/`
- **Filename:** `YYYY-MM_slug.yaml` (e.g., `2026-04_chatgpt-data-leak.yaml`)

### Pre-submission checklist

- [ ] YAML file placed in `ai/` directory
- [ ] File named `YYYY-MM_slug.yaml`
- [ ] All core fields filled in (`source_name`, `source_url`, `date_of_breach`, `date_of_disclosure`, `notes`)
- [ ] `ai_model_provider` filled in (**required** for AI breaches)
- [ ] `ai_model_name` filled in if known
- [ ] `ai_attack_vector` filled in if applicable
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
category: ai
notes: ""

# ── AI fields ──────────────────────────────────────────────────────────────────
ai_model_provider: ""                 # REQUIRED — e.g. "OpenAI", "Anthropic", "Google", "Microsoft", "Meta"
ai_model_name: ""                     # Recommended — e.g. "ChatGPT", "Claude", "Gemini", "GitHub Copilot"
ai_attack_vector: ""                  # Recommended — e.g. "prompt injection", "deepfake",
                                      #   "AI-generated malware", "model poisoning",
                                      #   "training data exposure", "jailbreak",
                                      #   "adversarial input", "AI-assisted cyberattack"

# ── Optional traditional fields ────────────────────────────────────────────────
initial_attack_vector: ""             # CWE-NNN description or free-text
cve: []                               # e.g. ["CVE-2024-1234"]
vendor_product: ""
software_package: ""
supply_chain_claimed: false
```

### Notes guidance

The `notes` field should be a narrative paragraph covering: what happened, when, who was affected, how the breach occurred, what the impact was, and any remediation or attribution details. See existing records in `ai/` for reference.
