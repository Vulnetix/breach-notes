# PRD Tracking Plan

This document outlines the process for populating breach data in the breach-notes repository.

## Objective
Continuously discover and document cybersecurity breach incidents from public sources, covering incidents from 1999 to the present day.

## Process
1. Monitor security news sources, breach databases, and threat intelligence feeds
2. Identify new breach incidents not already documented in the repository
3. For each new incident, create a YAML file following the schema in README.md
4. Place the file in the appropriate category directory (ransomware, data-leak, supply-chain, credential-theft, other)
5. Update README.md statistics if needed

## Sources to Monitor

### Security News
- BleepingComputer (bleepingcomputer.com)
- The Hacker News (thehackernews.com)
- The Record (therecord.media)
- Krebs on Security (krebsonsecurity.com)
- Dark Reading (darkreading.com)
- SecurityWeek (securityweek.com)
- Ars Technica Security (arstechnica.com/security)

### Breach Tracking
- HaveIBeenPwned (haveibeenpwned.com)
- DataBreaches.net
- Privacy Guides breach roundups (privacyguides.org)
- DataBreachToday (databreachtoday.com) — comprehensive breach news and analysis; sitemap at databreachtoday.com/sitemap.html covers incidents back to ~2010
- Breaches.cloud (breaches.cloud/incidents/) — cloud-specific breach incidents with technical root cause analysis; covers major cloud misconfigurations and credential theft incidents
- BlackKite Third-Party Breach List (blackkite.com/data-breaches-caused-by-third-parties) — supply chain and vendor-related breaches going back to 2013

### Regulatory & Mandatory Notification Registries

#### United States
- SEC Edgar cybersecurity incident filings (8-K, Item 1.05)
- HHS OCR HIPAA Breach Portal (ocrportal.hhs.gov) — healthcare breaches ≥500 individuals
- State AG notification databases (Maine AGO is most comprehensive; also CA, TX, NY)
- CISA Known Exploited Vulnerabilities (KEV) catalog

#### Australia
- OAIC Notifiable Data Breaches (NDB) scheme — oaic.gov.au/privacy/notifiable-data-breaches
  - Quarterly statistics reports; individual summaries for larger incidents
  - Covers entities under the Privacy Act (health, finance, govt agencies)

#### European Union / EEA
- ENISA Threat Landscape reports (enisa.europa.eu)
- National DPA enforcement decisions (typically published on DPA websites):
  - France: CNIL (cnil.fr/en) — decisions, sanctions, and notable breach cases
  - Germany: BSI (bsi.bund.de) and state-level DPAs (e.g., BayLDA, LfDI)
  - Netherlands: AP (autoriteitpersoonsgegevens.nl)
  - Ireland: DPC (dataprotection.ie) — major EU hub decisions under GDPR
  - Spain: AEPD (aepd.es)
  - Italy: Garante (garanteprivacy.it)
  - Denmark: Datatilsynet (datatilsynet.dk)
- EU CERT/CSIRT advisories: CERT-EU (cert.europa.eu)

#### United Kingdom
- ICO (ico.org.uk) — enforcement actions, fines, and notable breach decisions
- NCSC cyber incident reports (ncsc.gov.uk)

#### Canada
- OPC (priv.gc.ca) — Office of the Privacy Commissioner, PIPEDA breach reports

#### Other Asia-Pacific
- Singapore: PDPC (pdpc.gov.sg) — Personal Data Protection Commission decisions
- Japan: PPC (ppc.go.jp) — Personal Information Protection Commission
- South Korea: PIPC (pipc.go.kr) — Personal Information Protection Commission
- New Zealand: OPC (privacy.org.nz) — Office of the Privacy Commissioner

### Vendor Advisories
- Vendor security advisories (CVE disclosures linked to breach events)
- GitHub Advisory Database

## Quality Standards
- Verify information from multiple sources when possible
- Include direct URLs to primary sources
- Fill all applicable schema fields
- Use consistent date formats (YYYY-MM-DD)
- Categorize correctly based on primary attack type

## Automation Goals & Scripts
This process is being automated to reduce manual effort. We have developed Python scripts that fetch feeds from specific data sources and generate properly formatted YAML files.

- `scripts/import-breaches-cloud.py`: Scrapes the `breaches.cloud` RSS feed and automatically generates YAML files into the `data/` directory.

To run the import scripts, use `uv` to automatically handle dependencies:
```bash
uv run --with pyyaml python scripts/import-breaches-cloud.py
```

### Expanding Automation
Future scripts should be created for:
- DataBreachToday sitemap parsing (`https://www.databreachtoday.com/sitemap.html`)
- BlackKite Third-Party Breaches JSON API/DOM parsing
- Parsing mandatory notification registries (e.g. OAIC NDB exports)

## Commit & Push Workflow
After each batch of new YAML files and README updates:
1. Run the analyzer: `./analyze/analyze` (updates README.md stats)
2. Stage all new YAML files and README.md: `git add README.md <category>/<filename>.yaml ...`
3. Commit with a descriptive message — **no co-author lines**
4. Push: `git push`

Example commit message format:
```
Add breach batch N: X new incidents (summary of categories/themes)
```
## Sources Confirmed Working Well

These sources have been validated to yield high-quality, verifiable breach data:

- **KrebsOnSecurity** (krebsonsecurity.com) — excellent detail on financial, retail POS, credential breaches
- **UpGuard Blog** (upguard.com/breaches) — cloud misconfiguration and S3 bucket exposures
- **Wiz.io Blog** (wiz.io/blog) — cloud-native vulnerability research (ChaosDB, Power Apps, etc.)
- **HHS OCR HIPAA Breach Portal** (ocrportal.hhs.gov) — authoritative US healthcare breaches ≥500 individuals ("Wall of Shame")
- **OAIC NDB Register** (oaic.gov.au/privacy/notifiable-data-breaches) — Australia mandatory; quarterly reports name major incidents
- **SafetyDetectives Blog** (safetydetectives.com/blog) — unprotected database discoveries
- **vpnMentor Research** (vpnmentor.com/blog) — Elasticsearch and S3 exposure research
- **Troy Hunt / Have I Been Pwned** (haveibeenpwned.com) — authoritative credential dump catalogue
- **UK ICO enforcement** (ico.org.uk/action-weve-taken/enforcement/) — GDPR fines with attached breach details
- **SEC EDGAR 8-K filings** — post-December 2023 material cybersecurity disclosures; pre-2023 voluntary disclosures
- **Australian ACSC advisories** (cyber.gov.au) — Australian government cyber incident alerts
- **Bob Diachenko / Cyble** — prolific discoverers of exposed databases

## Gaps Still to Fill — Next Priority

- **HHS OCR 2013-2016 period**: Many hospital/insurer HIPAA breaches ≥500K records not yet documented
- **PDPC Singapore decisions** (pdpc.gov.sg/all-commissions-decisions) — decisions dating back to 2012
- **OPC Canada PIPEDA reports** (priv.gc.ca) — Canadian mandatory breach summaries
- **ICO UK enforcement actions pre-2018** — breach decisions with fine amounts
- **DataBreachToday.com archives 2013-2018** — retail, healthcare, financial breaches
- **Retail POS malware wave 2013-2015** — many smaller retailers not yet documented
- **Australia NDB quarterly statistics 2018-present** — individual large incidents named in OAIC reports
- **State AG breach notification databases** — Maine AGO most comprehensive; NY, CA, TX also useful
- **ENISA Threat Landscape reports** — European incident data including GDPR notification summaries

## Do Not Include

- Incidents with no verifiable public source
- Purely speculative or unconfirmed breach claims
- Breaches where the only source is a threat actor claim with no corroboration
- Duplicate entries for the same incident (consolidate into the richer record)

## Current Repository Status (Updated 2026-04-10)

- **Total records**: 1,221 breach incidents documented
- **Coverage**: 1996–2026, all major categories
- **By category**: data-leak (263+), supply-chain (750+), ransomware (95+), credential-theft (64+), other (46+)
- **Sources used**: BlackKite third-party breach timeline (687 supply-chain stubs via automated import), manually curated comprehensive records for major incidents, OAIC NDB, PDPC Singapore, ICO UK, HHS OCR, OPC Canada, SEC 8-K filings, KrebsOnSecurity, UpGuard, Wiz.io, vpnMentor, SafetyDetectives

## Analyzer Usage

Run from repo root to update README.md with correct stats:
```bash
./analyze/analyze data
cp data/README.md README.md
```

## Quality Tiers

Records fall into two quality tiers:

**Tier 1 — Comprehensive** (manually curated, ~530 records):
- Full narrative notes (300–600 words)
- Verified attack vector, impact, and regulatory response
- Cross-referenced with primary sources

**Tier 2 — Stub** (automated BlackKite import, ~687 records):
- Brief notes from BlackKite's third-party breach timeline
- Basic metadata (date, category, vendor, data type)
- Suitable for coverage; may lack regulatory/legal details

**Promotion path**: Tier 2 stubs for high-impact incidents should be promoted to Tier 1 by adding comprehensive notes from primary sources.

## Next Priorities for Tier 1 Promotion

1. All BlackKite healthcare provider stubs (multiple hospitals and health plans)
2. All BlackKite financial sector stubs (banks, insurance, payment processors)
3. Government/critical infrastructure stubs
4. Any stubs where the source_url returns a 404 or paywalled article — find a better primary source
