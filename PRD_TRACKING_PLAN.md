# PRD Tracking Plan

This document outlines the process for populating breach data in the breach-notes repository.

## Objective
Continuously discover and document new cybersecurity breach incidents from public sources.

## Process
1. Monitor security news sources, breach databases, and threat intelligence feeds
2. Identify new breach incidents not already documented in the repository
3. For each new incident, create a YAML file following the schema in README.md
4. Place the file in the appropriate category directory (ransomware, data-leak, supply-chain, credential-theft, other)
5. Update README.md statistics if needed

## Sources to Monitor
- BleepingComputer
- The Hacker News
- Krebs on Security
- Dark Reading
- HaveIBeenPwned
- Various vendor advisories
- Regulatory filings (SEC, GDPR, etc.)

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