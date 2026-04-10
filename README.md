# breach-notes

Structured YAML records of breach reports, advisories, and cyber incidents.

**Last updated:** 2026-04-10  **Total records:** 74

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total incidents | 74 |
| With CVE/GHSA references | 19 (26%) |
| Unique CVEs/GHSAs | 32 |
| With malware identified | 40 (54%) |
| Supply chain claimed | 16 (22%) |
| Unique vendor products | 71 |
| Median disclosure lag (days) | 24 |
| Max disclosure lag (days) | 1794 |

## Incidents by Category

| Category | Count | % |
|----------|-------|---|
| ransomware | 20 | 27% |
| data-leak | 19 | 26% |
| supply-chain | 11 | 15% |
| credential-theft | 14 | 19% |
| other | 10 | 14% |

## Incidents by Year

| Year | Count |
|------|-------|
| 2013 | 1 |
| 2014 | 1 |
| 2016 | 1 |
| 2017 | 1 |
| 2020 | 2 |
| 2021 | 7 |
| 2022 | 8 |
| 2023 | 18 |
| 2024 | 31 |
| 2025 | 4 |

## Top Malware Families

| Malware | Incidents |
|---------|----------|
| ALPHV/BlackCat | 3 |
| DragonForce | 2 |
| LEMURLOOT web shell | 2 |
| LockBit | 2 |
| LockBit 3.0 | 2 |
| REvil / Sodinokibi | 2 |
| RansomHub | 2 |
| Black Basta | 1 |
| BlackPOS / Kaptoxa | 1 |
| BlackSuit | 1 |
| BlogXX / REvil variant | 1 |
| China Chopper webshell / HAFNIUM custom tooling | 1 |
| Clop (Cl0p) | 1 |
| Conti (ransomware), various cryptominers, Orcus | 1 |
| DEWMODE webshell / FINTEAM | 1 |

## CVE / GHSA References

```
CVE-2017-5638
CVE-2020-10148
CVE-2020-5741
CVE-2021-26855
CVE-2021-26857
CVE-2021-26858
CVE-2021-27065
CVE-2021-27101
CVE-2021-27102
CVE-2021-27103
CVE-2021-27104
CVE-2021-27860
CVE-2021-30116
CVE-2021-40539
CVE-2021-44228
CVE-2021-45046
CVE-2021-45105
CVE-2023-0669
CVE-2023-29059
CVE-2023-34362
CVE-2023-35708
CVE-2023-46805
CVE-2023-4966
CVE-2024-21887
CVE-2024-21893
CVE-2024-3094
CVE-2024-3400
CVE-2024-50623
CVE-2024-55956
CVE-2025-0282
CVE-2025-0283
CVE-2025-22457
```

## Top Attack Vectors

| Attack Vector | Incidents |
|--------------|----------|
| CWE-307: Improper Restriction of Excessive Authentication Attempts (stolen credentials reused against Snowflake tenant with no MFA) | 5 |
| CWE-1021: Improper Restriction of Rendered UI (targeted spear-phishing with real-time TOTP relay against single employee) | 1 |
| CWE-1021: Improper Restriction of Rendered UI Layers (SMS phishing / smishing with real-time OTP relay to fake login page) | 1 |
| CWE-1104: Use of Unmaintained Third-Party Components (phishing of HVAC vendor Fazio Mechanical for network credentials, then lateral movement to POS environment) | 1 |
| CWE-121: Stack-based Buffer Overflow (CVE-2025-0282 — unauthenticated stack-based buffer overflow enabling RCE) | 1 |
| CWE-121: Stack-based Buffer Overflow (CVE-2025-22457 — stack buffer overflow in Ivanti Connect Secure enabling remote code execution) | 1 |
| CWE-1232: Improper Lock of Memory That Contains Resource (developer laptop compromise via malware; second stage via vulnerable Plex Media Server CVE-2020-5741) | 1 |
| CWE-1390: Weak Authentication (MFA push notification fatigue / bombing combined with social engineering via WhatsApp) | 1 |
| CWE-1390: Weak Authentication (vishing / voice phishing social engineering of outsourced IT vendor to bypass Okta MFA) | 1 |
| CWE-1391: Use of Weak Credentials (compromised credentials; exact initial vector not publicly disclosed) | 1 |
| CWE-1391: Use of Weak Credentials (exact vector not publicly disclosed) | 1 |
| CWE-1391: Use of Weak Credentials (social engineering via LinkedIn identity theft + vishing helpdesk to bypass Okta MFA) | 1 |
| CWE-1391: Use of Weak Credentials (social engineering; exact initial vector not fully disclosed) | 1 |
| CWE-1391: Use of Weak Credentials (third-party support contractor workstation compromise via RDP + credential harvesting) | 1 |
| CWE-200: Exposure of Sensitive Information (Citrix Bleed - memory disclosure of valid session tokens enabling auth bypass) | 1 |

## Incident Index

| File | Category | Breach Date | Malware | CVEs |
|------|----------|-------------|---------|------|
| [2025-04_coop-harrods-dragonforce.yaml](ransomware/2025-04_coop-harrods-dragonforce.yaml) | ransomware | 2025-04-01 | DragonForce ransomware |  |
| [2025-04_ivanti-connect-secure-cve-2025-22457.yaml](other/2025-04_ivanti-connect-secure-cve-2025-22457.yaml) | other | 2025-03-15 | TRAILBLAZE (in-memory dropper… | CVE-2025-22457 |
| [2025-04_marks-and-spencer.yaml](ransomware/2025-04_marks-and-spencer.yaml) | ransomware | 2025-02-01 | DragonForce ransomware |  |
| [2025-01_western-sydney-university.yaml](data-leak/2025-01_western-sydney-university.yaml) | data-leak | 2025-01-28 |  |  |
| [2024-12_powerschool-sis.yaml](supply-chain/2024-12_powerschool-sis.yaml) | supply-chain | 2024-12-19 |  |  |
| [2025-01_ivanti-connect-secure-cve-2025-0282.yaml](other/2025-01_ivanti-connect-secure-cve-2025-0282.yaml) | other | 2024-12-15 | SPAWN ecosystem (SPAWNANT ins… | CVE-2025-0282, CVE-2025-0283 |
| [2024-11_krispy-kreme-play.yaml](ransomware/2024-11_krispy-kreme-play.yaml) | ransomware | 2024-11-29 | Play ransomware |  |
| [2024-12_cleo-mft-clop.yaml](supply-chain/2024-12_cleo-mft-clop.yaml) | supply-chain | 2024-11-15 | Clop (Cl0p) ransomware | CVE-2024-50623, CVE-2024-55956 |
| [2024-10_hot-topic.yaml](data-leak/2024-10_hot-topic.yaml) | data-leak | 2024-10-01 | Infostealer malware (targetin… |  |
| [2024-10_internet-archive.yaml](data-leak/2024-10_internet-archive.yaml) | data-leak | 2024-09-28 |  |  |
| [2024-08_halliburton.yaml](ransomware/2024-08_halliburton.yaml) | ransomware | 2024-08-21 | RansomHub ransomware |  |
| [2024-08_mclaren-health.yaml](ransomware/2024-08_mclaren-health.yaml) | ransomware | 2024-07-17 | INC Ransom ransomware |  |
| [2024-06_cdk-global.yaml](ransomware/2024-06_cdk-global.yaml) | ransomware | 2024-06-18 | BlackSuit |  |
| [2024-06_synnovis-nhs.yaml](ransomware/2024-06_synnovis-nhs.yaml) | ransomware | 2024-06-03 | Qilin ransomware |  |
| [2024-06_patelco-credit-union.yaml](ransomware/2024-06_patelco-credit-union.yaml) | ransomware | 2024-05-23 | RansomHub ransomware |  |
| [2024-05_ascension-health.yaml](ransomware/2024-05_ascension-health.yaml) | ransomware | 2024-05-08 | Black Basta ransomware |  |
| [2024-05_dell-api-scrape.yaml](data-leak/2024-05_dell-api-scrape.yaml) | data-leak | 2024-04-28 |  |  |
| [2024-04_london-drugs-lockbit.yaml](ransomware/2024-04_london-drugs-lockbit.yaml) | ransomware | 2024-04-28 | LockBit ransomware |  |
| [2024-04_santander-snowflake.yaml](credential-theft/2024-04_santander-snowflake.yaml) | credential-theft | 2024-04-17 |  |  |
| [2024-04_att-snowflake.yaml](credential-theft/2024-04_att-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-04_advance-auto-parts-snowflake.yaml](credential-theft/2024-04_advance-auto-parts-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-05_lendingtree-quotewizard-snowflake.yaml](credential-theft/2024-05_lendingtree-quotewizard-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-04_ticketmaster-snowflake.yaml](credential-theft/2024-04_ticketmaster-snowflake.yaml) | credential-theft | 2024-04-14 | VIDAR, RISEPRO, REDLINE, RACO… |  |
| [2024-04_national-public-data.yaml](data-leak/2024-04_national-public-data.yaml) | data-leak | 2024-04-01 |  |  |
| [2024-04_snowflake-customers.yaml](credential-theft/2024-04_snowflake-customers.yaml) | credential-theft | 2024-04-01 | Redline Stealer / Lumma Steal… |  |
| [2024-05_neiman-marcus-snowflake.yaml](credential-theft/2024-05_neiman-marcus-snowflake.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-04_palo-alto-pan-os.yaml](other/2024-04_palo-alto-pan-os.yaml) | other | 2024-03-26 | UPSTYLE Python backdoor | CVE-2024-3400 |
| [2024-04_roku-credential-stuffing.yaml](credential-theft/2024-04_roku-credential-stuffing.yaml) | credential-theft | 2024-03-01 |  |  |
| [2024-03_xz-utils-backdoor.yaml](supply-chain/2024-03_xz-utils-backdoor.yaml) | supply-chain | 2024-02-24 |  | CVE-2024-3094 |
| [2024-02_cencora-pharma.yaml](data-leak/2024-02_cencora-pharma.yaml) | data-leak | 2024-02-21 |  |  |
| [2024-02_change-healthcare.yaml](ransomware/2024-02_change-healthcare.yaml) | ransomware | 2024-02-11 | ALPHV/BlackCat |  |
| [2024-02_prudential-financial.yaml](data-leak/2024-02_prudential-financial.yaml) | data-leak | 2024-02-04 | ALPHV/BlackCat ransomware |  |
| [2024-01_lurie-childrens-hospital.yaml](ransomware/2024-01_lurie-childrens-hospital.yaml) | ransomware | 2024-01-26 | Rhysida |  |
| [2024-01_trello-api-scrape.yaml](data-leak/2024-01_trello-api-scrape.yaml) | data-leak | 2024-01-16 |  |  |
| [2024-04_kaiser-permanente-tracker.yaml](data-leak/2024-04_kaiser-permanente-tracker.yaml) | data-leak | 2024-01-01 |  |  |
| [2024-01_ivanti-connect-secure.yaml](other/2024-01_ivanti-connect-secure.yaml) | other | 2023-12-01 | ZIPLINE backdoor / LIGHTWIRE … | CVE-2023-46805, CVE-2024-21887, CVE-202… |
| [2023-11_integris-health.yaml](ransomware/2023-11_integris-health.yaml) | ransomware | 2023-11-28 |  |  |
| [2024-01_cloudflare-midnight-blizzard.yaml](credential-theft/2024-01_cloudflare-midnight-blizzard.yaml) | credential-theft | 2023-11-14 |  |  |
| [2024-01_microsoft-midnight-blizzard.yaml](credential-theft/2024-01_microsoft-midnight-blizzard.yaml) | credential-theft | 2023-11-01 |  |  |
| [2023-10_infosys-mccamish-lockbit.yaml](supply-chain/2023-10_infosys-mccamish-lockbit.yaml) | supply-chain | 2023-10-29 | LockBit ransomware |  |
| [2023-10_boeing-citrixbleed.yaml](ransomware/2023-10_boeing-citrixbleed.yaml) | ransomware | 2023-10-01 | LockBit 3.0 | CVE-2023-4966 |
| [2023-10_okta-support-system.yaml](credential-theft/2023-10_okta-support-system.yaml) | credential-theft | 2023-09-28 |  |  |
| [2023-09_mgm-resorts.yaml](ransomware/2023-09_mgm-resorts.yaml) | ransomware | 2023-09-08 | ALPHV/BlackCat |  |
| [2023-08_caesars-entertainment.yaml](ransomware/2023-08_caesars-entertainment.yaml) | ransomware | 2023-08-18 | Scattered Spider ransomware |  |
| [2023-05_moveit-transfer-clop.yaml](supply-chain/2023-05_moveit-transfer-clop.yaml) | supply-chain | 2023-05-27 | LEMURLOOT web shell | CVE-2023-34362, CVE-2023-35708 |
| [2023-07_moveit-maximus.yaml](supply-chain/2023-07_moveit-maximus.yaml) | supply-chain | 2023-05-27 | LEMURLOOT web shell | CVE-2023-34362 |
| [2023-05_storm-0558-microsoft-exchange.yaml](other/2023-05_storm-0558-microsoft-exchange.yaml) | other | 2023-05-15 |  |  |
| [2023-03_3cx-desktop-app.yaml](supply-chain/2023-03_3cx-desktop-app.yaml) | supply-chain | 2023-03-16 | SUDDENICON downloader / ICONI… | CVE-2023-29059 |
| [2023-03_latitude-financial.yaml](data-leak/2023-03_latitude-financial.yaml) | data-leak | 2023-03-16 |  |  |
| [2023-02_reddit-blackcat.yaml](data-leak/2023-02_reddit-blackcat.yaml) | data-leak | 2023-02-05 |  |  |
| [2023-01_goanywhere-clop.yaml](supply-chain/2023-01_goanywhere-clop.yaml) | supply-chain | 2023-01-18 |  | CVE-2023-0669 |
| [2023-01_royal-mail-lockbit.yaml](ransomware/2023-01_royal-mail-lockbit.yaml) | ransomware | 2023-01-10 | LockBit 3.0 |  |
| [2024-10_salt-typhoon-telecoms.yaml](other/2024-10_salt-typhoon-telecoms.yaml) | other | 2023-01-01 |  |  |
| [2023-01_t-mobile-api.yaml](data-leak/2023-01_t-mobile-api.yaml) | data-leak | 2022-11-25 |  |  |
| [2022-09_optus.yaml](data-leak/2022-09_optus.yaml) | data-leak | 2022-09-19 |  |  |
| [2022-09_uber-mfa-fatigue.yaml](credential-theft/2022-09_uber-mfa-fatigue.yaml) | credential-theft | 2022-09-15 |  |  |
| [2022-10_medibank.yaml](ransomware/2022-10_medibank.yaml) | ransomware | 2022-08-25 | BlogXX / REvil variant |  |
| [2022-08_lastpass.yaml](data-leak/2022-08_lastpass.yaml) | data-leak | 2022-08-08 |  | CVE-2020-5741 |
| [2022-08_twilio-0ktapus.yaml](credential-theft/2022-08_twilio-0ktapus.yaml) | credential-theft | 2022-06-01 |  |  |
| [2022-03_samsung-lapsus.yaml](data-leak/2022-03_samsung-lapsus.yaml) | data-leak | 2022-03-04 |  |  |
| [2022-01_okta-lapsus.yaml](credential-theft/2022-01_okta-lapsus.yaml) | credential-theft | 2022-01-16 | Mimikatz |  |
| [2021-12_log4shell.yaml](other/2021-12_log4shell.yaml) | other | 2021-12-01 | Conti (ransomware), various c… | CVE-2021-44228, CVE-2021-45046, CVE-202… |
| [2021-07_kaseya-vsa-revil.yaml](supply-chain/2021-07_kaseya-vsa-revil.yaml) | supply-chain | 2021-07-02 | REvil / Sodinokibi | CVE-2021-30116 |
| [2023-01_twitter-api-scrape.yaml](data-leak/2023-01_twitter-api-scrape.yaml) | data-leak | 2021-06-01 |  |  |
| [2024-02_volt-typhoon-critical-infrastructure.yaml](other/2024-02_volt-typhoon-critical-infrastructure.yaml) | other | 2021-06-01 |  | CVE-2021-40539, CVE-2021-27860 |
| [2021-05_jbs-foods.yaml](ransomware/2021-05_jbs-foods.yaml) | ransomware | 2021-05-30 | REvil / Sodinokibi |  |
| [2021-05_colonial-pipeline.yaml](ransomware/2021-05_colonial-pipeline.yaml) | ransomware | 2021-05-07 | DarkSide |  |
| [2021-03_microsoft-exchange-proxylogon.yaml](other/2021-03_microsoft-exchange-proxylogon.yaml) | other | 2021-01-03 | China Chopper webshell / HAFN… | CVE-2021-26855, CVE-2021-26857, CVE-202… |
| [2021-01_accellion-fta-clop.yaml](supply-chain/2021-01_accellion-fta-clop.yaml) | supply-chain | 2020-12-25 | DEWMODE webshell / FINTEAM | CVE-2021-27101, CVE-2021-27102, CVE-202… |
| [2020-12_solarwinds-sunburst.yaml](supply-chain/2020-12_solarwinds-sunburst.yaml) | supply-chain | 2020-03-26 | SUNBURST / TEARDROP / SUNSPOT | CVE-2020-10148 |
| [2017-05_equifax.yaml](data-leak/2017-05_equifax.yaml) | data-leak | 2017-03-10 |  | CVE-2017-5638 |
| [2016-10_uber-cover-up.yaml](data-leak/2016-10_uber-cover-up.yaml) | data-leak | 2016-10-01 |  |  |
| [2018-11_marriott-starwood.yaml](data-leak/2018-11_marriott-starwood.yaml) | data-leak | 2014-01-01 | Remote Access Trojan (name un… |  |
| [2013-11_target-blackpos.yaml](other/2013-11_target-blackpos.yaml) | other | 2013-11-15 | BlackPOS / Kaptoxa |  |

## Schema

Each YAML file captures:

```yaml
source_name: "publication or organization name"
source_url: "direct URL to the report"
date_of_breach: "YYYY-MM-DD or YYYY-MM or YYYY"
date_of_disclosure: "YYYY-MM-DD or unknown"
date_of_customer_notification: "YYYY-MM-DD or unknown"
category: "ransomware | data-leak | supply-chain | credential-theft | other"
initial_attack_vector: "CWE-NNN: Description or free text"
cve: ["CVE-2021-44228"]  # list, empty if none
vendor_product: "Vendor Product Name"
software_package: "package-name"
malware: "MalwareName"
supply_chain_claimed: false
notes: "Additional context"
```

## Folders

- `ransomware/` — ransomware incidents
- `data-leak/` — customer data exposure
- `supply-chain/` — supply chain attacks
- `credential-theft/` — credential compromise
- `other/` — uncategorized or multi-category
