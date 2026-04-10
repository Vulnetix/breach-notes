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
- `scripts/import-web3isgoinggreat.py`: Scrapes the `web3isgoinggreat.com` Next.js API/DOM and follows pagination to generate YAML files for all incidents.

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
## Source Status Matrix (what works now)

### Confirmed Working (automated)

- `scripts/import-web3isgoinggreat.py`
  - Source: `https://www.web3isgoinggreat.com/web1`
  - Method: parse `__NEXT_DATA__` JSON (Next.js SSR), follow cursor pagination (`?cursor=YYYY-MM-DD-N&direction=next`) until `hasNext: false`
  - Result: full site archive of crypto/DeFi/NFT/blockchain hacks, scams, rug-pulls, collapses — 2,200+ incidents from 2021–2026
  - Run: `uv run --with pyyaml --with requests --with beautifulsoup4 python scripts/import-web3isgoinggreat.py`

- `scripts/import-breaches-cloud.py`
  - Source: `https://www.breaches.cloud/incidents/index.xml`
  - Method: RSS/XML parse
  - Result: creates incident YAML directly in `data/`

- `scripts/import-blackkite.py`
  - Source: `https://blackkite.com/data-breaches-caused-by-third-parties/`
  - Method: parse embedded Next.js Flight payload (`yearSections`) and normalize timeline rows
  - Result: creates/updates supply-chain incidents from BlackKite's third-party timeline

- `scripts/import-databreachtoday.py`
  - Source: `https://www.databreachtoday.com/sitemap.html` + `articles-sitemap*.html`
  - Method: parse sitemap article links, filter incident-like titles, fetch article metadata (title/description/byline date)
  - Result: creates incident YAML from DataBreachToday archive coverage

### Mandatory Notification Sources (checked)

- **OAIC NDB (Australia)**
  - URL: `https://www.oaic.gov.au/privacy/notifiable-data-breaches/notifiable-data-breaches-publications`
  - Status: accessible; primarily quarterly/aggregate publications
  - Action: use OAIC as corroboration + major case enrichment; not yet a clean bulk per-incident feed

- **HHS OCR HIPAA (US)**
  - URL: `https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf`
  - Status: accessible but JSF portal flow is stateful; bulk export path still needs scripted form navigation
  - Action: keep as priority for dedicated parser/export workflow

## Current Rules

- Do not add incidents without at least one verifiable public source URL
- Prefer primary source links (regulator, victim org, vendor advisory)
- Avoid duplicate records for the same incident; enrich existing records instead
- Use `YYYY-MM-DD` dates; if day unknown use first day of month and document uncertainty in notes

## Analyzer Usage

Run from repo root to update README.md with correct stats after import batches:
```bash
./analyze/analyze
```

## Repository Status (Updated 2026-04-10)

- **Total records**: 3,425 breach incidents
- **By category**: data-leak (1,078), other (1,333), supply-chain (769), ransomware (129), credential-theft (116)
- **Coverage**: 1996–2026
- **Sources ingested**: BlackKite third-party timeline (687 supply-chain stubs), Web3 Is Going Great full archive (2,200+ crypto/DeFi incidents via paginated scraper), DataBreachToday sitemap, breaches.cloud RSS, manually curated major incidents

## Confirmed Working Automation Sources

- `scripts/import-web3isgoinggreat.py`
  - Source: `https://www.web3isgoinggreat.com/web1` (Next.js SSP endpoint, paginated with cursor)
  - Method: parse `__NEXT_DATA__` JSON from page HTML; follow `cursor` pagination via `?cursor=YYYY-MM-DD-N&direction=next`; create YAML per entry skipping already-existing files
  - Result: 2,200+ crypto/DeFi/NFT/blockchain incidents ingested across data-leak, supply-chain, and other categories
  - Run: `uv run --with pyyaml --with requests --with beautifulsoup4 python scripts/import-web3isgoinggreat.py`

## Immediate Next Automation Priorities

1. Build a robust HHS OCR HIPAA parser/export path (JSF form flow)
2. Add parser for regulator decision feeds where structured pagination exists (ICO, PDPC, OPC)
3. Continue DataBreachToday ingestion in batches until new sitemap coverage yields no new incidents
4. Promote high-impact stub entries to richer notes with additional primary references
