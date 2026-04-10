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

## Automation Goals
This process should eventually be automated to reduce manual effort.

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