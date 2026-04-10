# breach-notes

Structured YAML records of breach reports, advisories, and cyber incidents.

**Last updated:** 2026-04-10  **Total records:** 1253

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total incidents | 1253 |
| With CVE/GHSA references | 48 (4%) |
| Unique CVEs/GHSAs | 61 |
| With malware identified | 158 (13%) |
| Supply chain claimed | 790 (63%) |
| Unique vendor products | 825 |
| Median disclosure lag (days) | 0 |
| Max disclosure lag (days) | 3474 |

## Incidents by Category

| Category | Count | % |
|----------|-------|---|
| ransomware | 105 | 8% |
| data-leak | 268 | 21% |
| supply-chain | 746 | 60% |
| credential-theft | 77 | 6% |
| other | 57 | 5% |

## Incidents by Year

| Year | Count |
|------|-------|
| 2000 | 1 |
| 2001 | 3 |
| 2002 | 1 |
| 2003 | 1 |
| 2004 | 3 |
| 2005 | 1 |
| 2006 | 2 |
| 2007 | 2 |
| 2008 | 1 |
| 2009 | 2 |
| 2011 | 2 |
| 2012 | 6 |
| 2013 | 14 |
| 2014 | 22 |
| 2015 | 12 |
| 2016 | 20 |
| 2017 | 31 |
| 2018 | 75 |
| 2019 | 78 |
| 2020 | 104 |
| 2021 | 138 |
| 2022 | 93 |
| 2023 | 169 |
| 2024 | 202 |
| 2025 | 208 |
| 2026 | 57 |

## Top Malware Families

| Malware | Incidents |
|---------|----------|
| ALPHV/BlackCat | 7 |
| Qilin | 5 |
| RansomHub | 5 |
| Black Basta | 4 |
| DragonForce | 4 |
| Hunters International | 4 |
| Interlock | 4 |
| LockBit | 4 |
| POS RAM-scraping | 4 |
| TeamPCP Cloud Stealer | 4 |
| BlackSuit | 3 |
| INC Ransom | 3 |
| Medusa | 3 |
| SafePay | 3 |
| Akira | 2 |

## CVE / GHSA References

```
CVE-2001-0333
CVE-2001-0500
CVE-2001-0507
CVE-2002-0649
CVE-2011-0609
CVE-2014-0160
CVE-2017-0143
CVE-2017-0144
CVE-2017-0145
CVE-2017-5638
CVE-2019-19781
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
CVE-2021-31207
CVE-2021-34473
CVE-2021-34523
CVE-2021-35587
CVE-2021-40539
CVE-2021-44228
CVE-2021-45046
CVE-2021-45105
CVE-2022-24521
CVE-2022-41080
CVE-2022-41082
CVE-2023-0669
CVE-2023-2868
CVE-2023-29059
CVE-2023-34362
CVE-2023-35708
CVE-2023-46805
CVE-2023-4966
CVE-2023-6448
CVE-2024-21887
CVE-2024-21893
CVE-2024-3094
CVE-2024-3400
CVE-2024-40766
CVE-2024-50623
CVE-2024-55956
CVE-2024-57726
CVE-2024-57727
CVE-2024-57728
CVE-2025-0282
CVE-2025-0283
CVE-2025-0994
CVE-2025-22457
CVE-2025-30154
CVE-2025-5777
CVE-2025-61882
CVE-2025-61884
CVE-2026-33634
```

## Top Attack Vectors

| Attack Vector | Incidents |
|--------------|----------|
| Compromise of third-party service provider / vendor relationship | 686 |
| CWE-284: Improper Access Control | 15 |
| Unauthorized access / data exposure | 6 |
| CWE-307: Improper Restriction of Excessive Authentication Attempts (stolen credentials reused against Snowflake tenant with no MFA) | 5 |
| Credential theft or account compromise | 3 |
| Ransomware intrusion | 3 |
| CWE-522: Insufficiently Protected Credentials (infostealer-harvested credentials, no MFA on Snowflake) | 2 |
| A Dropbox employee reused their LinkedIn password for their Dropbox work account; when the 2012 LinkedIn breach exposed that password, attackers used it to log into the employee's Dropbox work account, which contained a document with hashed Dropbox user passwords | 1 |
| A First Republic Bank employee with legitimate AWS access used their credentials to exfiltrate customer data from AWS-hosted banking systems | 1 |
| A Mercedes-Benz employee inadvertently included a GitHub API token in a public GitHub repository; the token provided unrestricted read access (with no expiration date) to the entire Mercedes-Benz Enterprise GitHub organization, allowing access to all private repositories | 1 |
| A VA data analyst took home a VA-issued laptop and external hard drive containing 26.5 million veterans' PII without authorization; the equipment was stolen from his home in a burglary | 1 |
| A contract worker with knowledge of the credentials used Chegg's AWS root account credentials and shared access keys to access an S3 bucket containing user data, exfiltrating records for 40 million users | 1 |
| A disgruntled Morrisons senior internal IT auditor (Andrew Skelton) with legitimate access to payroll data deliberately copied and leaked the personal and financial data of 99,998 Morrisons employees to newspaper outlets and multiple file sharing websites, motivated by a personal grievance over a disciplinary matter | 1 |
| A faulty content configuration update (Channel File 291) for the CrowdStrike Falcon sensor on Windows hosts caused a logic error in the sensor's Content Interpreter, triggering an out-of-bounds memory read that led to an exception handling failure and Windows BSOD (Blue Screen of Death) | 1 |
| A file containing Ambulance Victoria staff personal data was inadvertently uploaded to a publicly accessible part of Ambulance Victoria's website, where it was accessible without authentication | 1 |

## Incident Index

| File | Category | Breach Date | Malware | CVEs |
|------|----------|-------------|---------|------|
| [2026-04_chipsoft-netherlands-hospitals.yaml](ransomware/2026-04_chipsoft-netherlands-hospitals.yaml) | ransomware | 2026-04-07 |  |  |
| [2026-04_massachusetts-hospital-ambulance-diversion.yaml](ransomware/2026-04_massachusetts-hospital-ambulance-diversion.yaml) | ransomware | 2026-04-07 |  |  |
| [2026-04_cisco-trivy-teamPCP-source-code.yaml](supply-chain/2026-04_cisco-trivy-teamPCP-source-code.yaml) | supply-chain | 2026-04-03 | TeamPCP Cloud Stealer |  |
| [2026-04_drift-protocol-dprk-285m.yaml](other/2026-04_drift-protocol-dprk-285m.yaml) | other | 2026-04-01 |  |  |
| [2026-03_axios-npm-sapphire-sleet-dprk.yaml](supply-chain/2026-03_axios-npm-sapphire-sleet-dprk.yaml) | supply-chain | 2026-03-31 | Sapphire Sleet RAT |  |
| [2026-03_teamPCP-telnyx-pypi.yaml](supply-chain/2026-03_teamPCP-telnyx-pypi.yaml) | supply-chain | 2026-03-27 | TeamPCP Cloud Stealer |  |
| [2026-03_litellm-pypi-mercor-teamPCP.yaml](supply-chain/2026-03_litellm-pypi-mercor-teamPCP.yaml) | supply-chain | 2026-03-27 |  |  |
| [2026-03_ai-is-fueling-a-new-wave-of-credential-attacks.yaml](ransomware/2026-03_ai-is-fueling-a-new-wave-of-credential-attacks.yaml) | ransomware | 2026-03-26 |  |  |
| [2026-03_litellm-hit-in-cascading-supply-chain-attack.yaml](credential-theft/2026-03_litellm-hit-in-cascading-supply-chain-attack.yaml) | credential-theft | 2026-03-26 |  |  |
| [2026-03_die-linke-qilin-germany.yaml](ransomware/2026-03_die-linke-qilin-germany.yaml) | ransomware | 2026-03-26 | Qilin |  |
| [2026-03_nyc-health-notifying-patients-of-2-third-party-hacks.yaml](supply-chain/2026-03_nyc-health-notifying-patients-of-2-third-party-hacks.yaml) | supply-chain | 2026-03-26 |  |  |
| [2026-03_handala-iran-fbi-director-kash-patel-email.yaml](credential-theft/2026-03_handala-iran-fbi-director-kash-patel-email.yaml) | credential-theft | 2026-03-25 |  |  |
| [2026-04_hasbro-it-systems-breach.yaml](data-leak/2026-04_hasbro-it-systems-breach.yaml) | data-leak | 2026-03-25 |  |  |
| [2026-03_resolv-protocol-24m-defi-exploit.yaml](other/2026-03_resolv-protocol-24m-defi-exploit.yaml) | other | 2026-03-22 |  |  |
| [2026-03_teamPCP-checkmarx-kics.yaml](supply-chain/2026-03_teamPCP-checkmarx-kics.yaml) | supply-chain | 2026-03-21 | TeamPCP Cloud Stealer |  |
| [2026-03_bitcoin-depot-crypto-theft.yaml](other/2026-03_bitcoin-depot-crypto-theft.yaml) | other | 2026-03-20 |  |  |
| [2026-03_lapd-city-attorney-worldleaks.yaml](data-leak/2026-03_lapd-city-attorney-worldleaks.yaml) | data-leak | 2026-03-20 |  |  |
| [2026-03_multi-month-cyberespionage-campaign-hits-libyan-oil-refinery.yaml](credential-theft/2026-03_multi-month-cyberespionage-campaign-hits-libyan-oil-refinery.yaml) | credential-theft | 2026-03-20 |  |  |
| [2026-03_cryptohack-roundup-appsflyer-sdk-breach-enabled-theft.yaml](data-leak/2026-03_cryptohack-roundup-appsflyer-sdk-breach-enabled-theft.yaml) | data-leak | 2026-03-19 |  |  |
| [2026-03_teamPCP-trivy-github-actions.yaml](supply-chain/2026-03_teamPCP-trivy-github-actions.yaml) | supply-chain | 2026-03-19 | TeamPCP Cloud Stealer | CVE-2026-33634 |
| [2026-03_breach-roundup-fancy-bear-in-schmancy-opsec-failure.yaml](data-leak/2026-03_breach-roundup-fancy-bear-in-schmancy-opsec-failure.yaml) | data-leak | 2026-03-19 |  |  |
| [2026-03_worker-benefits-administrator-notifying-2-7m-of-hack.yaml](data-leak/2026-03_worker-benefits-administrator-notifying-2-7m-of-hack.yaml) | data-leak | 2026-03-19 |  |  |
| [2026-03_microsoft-intune-mdm-gains-notoriety-after-stryker-hack.yaml](data-leak/2026-03_microsoft-intune-mdm-gains-notoriety-after-stryker-hack.yaml) | data-leak | 2026-03-19 |  |  |
| [2026-03_european-commission-shinyhunters-aws.yaml](data-leak/2026-03_european-commission-shinyhunters-aws.yaml) | data-leak | 2026-03-19 |  |  |
| [2026-03_xbow-raises-120m-series-c-to-scale-autonomous-ai-hacking.yaml](data-leak/2026-03_xbow-raises-120m-series-c-to-scale-autonomous-ai-hacking.yaml) | data-leak | 2026-03-19 |  |  |
| [2026-03_claudy-day-forecast-chat-data-theft.yaml](credential-theft/2026-03_claudy-day-forecast-chat-data-theft.yaml) | credential-theft | 2026-03-18 |  |  |
| [2026-03_stryker-wiper-attack-hackers-boast-as-lawsuits-pile-up.yaml](ransomware/2026-03_stryker-wiper-attack-hackers-boast-as-lawsuits-pile-up.yaml) | ransomware | 2026-03-18 |  |  |
| [2026-03_interlock-ransomware-exploited-cisco-firewall-flaw-for-weeks.yaml](ransomware/2026-03_interlock-ransomware-exploited-cisco-firewall-flaw-for-weeks.yaml) | ransomware | 2026-03-18 |  |  |
| [2026-03_eu-belatedly-sanctions-chinese-and-iranian-hackers.yaml](data-leak/2026-03_eu-belatedly-sanctions-chinese-and-iranian-hackers.yaml) | data-leak | 2026-03-17 |  |  |
| [2026-03_aura-identity-shinyhunters-vishing.yaml](data-leak/2026-03_aura-identity-shinyhunters-vishing.yaml) | data-leak | 2026-03-17 |  |  |
| [2026-03_carecloud-ehr-breach.yaml](data-leak/2026-03_carecloud-ehr-breach.yaml) | data-leak | 2026-03-16 |  |  |
| [2026-03_crunchyroll-bpo-okta-breach.yaml](data-leak/2026-03_crunchyroll-bpo-okta-breach.yaml) | data-leak | 2026-03-12 | infostealer (unspecified) |  |
| [2026-03_stryker-handala-intune-wiper.yaml](other/2026-03_stryker-handala-intune-wiper.yaml) | other | 2026-03-11 |  |  |
| [2026-04_anodot-shinyhunters-snowflake-tokens.yaml](credential-theft/2026-04_anodot-shinyhunters-snowflake-tokens.yaml) | credential-theft | 2026-03-01 |  |  |
| [2026-03_california-orthopedic-device-maker-hack.yaml](data-leak/2026-03_california-orthopedic-device-maker-hack.yaml) | data-leak | 2026-03-01 |  |  |
| [2026-03_unc6426-nx-npm-aws-takeover.yaml](supply-chain/2026-03_unc6426-nx-npm-aws-takeover.yaml) | supply-chain | 2026-03-01 |  |  |
| [2026-03_fbi-seizes-handala-iranian-leak-domains.yaml](other/2026-03_fbi-seizes-handala-iranian-leak-domains.yaml) | other | 2026-03-01 |  |  |
| [2026-03_bithumb-exchange-hack-recovery.yaml](other/2026-03_bithumb-exchange-hack-recovery.yaml) | other | 2026-03-01 |  |  |
| [2026-03_dutch-ministry-finance-breach.yaml](data-leak/2026-03_dutch-ministry-finance-breach.yaml) | data-leak | 2026-03-01 |  |  |
| [2026-03_lloyds-banking-group-450k-leak.yaml](data-leak/2026-03_lloyds-banking-group-450k-leak.yaml) | data-leak | 2026-03-01 |  |  |
| [2026-02_malaysia-airlines-qilin.yaml](ransomware/2026-02_malaysia-airlines-qilin.yaml) | ransomware | 2026-02-26 | Qilin |  |
| [2026-02_ummc-medusa-ransomware.yaml](ransomware/2026-02_ummc-medusa-ransomware.yaml) | ransomware | 2026-02-19 | Medusa |  |
| [2026-02_fbi-dcsnet-china-surveillance.yaml](other/2026-02_fbi-dcsnet-china-surveillance.yaml) | other | 2026-02-17 |  |  |
| [2026-02_odido-dutch-telecom-shinyhunters.yaml](data-leak/2026-02_odido-dutch-telecom-shinyhunters.yaml) | data-leak | 2026-02-07 |  |  |
| [2026-02_bridgepay-ransomware-outage.yaml](ransomware/2026-02_bridgepay-ransomware-outage.yaml) | ransomware | 2026-02-06 |  |  |
| [2026-02_hims-hers-zendesk-shinyhunters.yaml](data-leak/2026-02_hims-hers-zendesk-shinyhunters.yaml) | data-leak | 2026-02-04 |  |  |
| [2026-02_sears-home-services-chatbot-exposure.yaml](data-leak/2026-02_sears-home-services-chatbot-exposure.yaml) | data-leak | 2026-02-03 |  |  |
| [2026-02_cargurus-shinyhunters-social-engineering.yaml](data-leak/2026-02_cargurus-shinyhunters-social-engineering.yaml) | data-leak | 2026-02-01 |  |  |
| [2026-03_lexisnexis-law-firm-breach.yaml](data-leak/2026-03_lexisnexis-law-firm-breach.yaml) | data-leak | 2026-02-01 |  |  |
| [2026-01_glassworm-open-vsx-extensions.yaml](supply-chain/2026-01_glassworm-open-vsx-extensions.yaml) | supply-chain | 2026-01-30 | GlassWorm |  |
| [2026-01_starbucks-partner-central-phishing.yaml](credential-theft/2026-01_starbucks-partner-central-phishing.yaml) | credential-theft | 2026-01-19 |  |  |
| [2026-01_crunchbase-shinyhunters-vishing.yaml](data-leak/2026-01_crunchbase-shinyhunters-vishing.yaml) | data-leak | 2026-01-09 |  |  |
| [2026-01_betterment-shinyhunters-vishing.yaml](data-leak/2026-01_betterment-shinyhunters-vishing.yaml) | data-leak | 2026-01-09 |  |  |
| [2026-01_bumble-match-shinyhunters-vishing.yaml](data-leak/2026-01_bumble-match-shinyhunters-vishing.yaml) | data-leak | 2026-01-01 |  |  |
| [2026-03_telus-digital-shinyhunters.yaml](data-leak/2026-03_telus-digital-shinyhunters.yaml) | data-leak | 2026-01-01 |  |  |
| [2026-04_gru-apt28-soho-router-dns-hijacking.yaml](other/2026-04_gru-apt28-soho-router-dns-hijacking.yaml) | other | 2026-01-01 | MooBot (Mirai variant), custo… |  |
| [2026-01_figure-fintech-shinyhunters-vishing.yaml](data-leak/2026-01_figure-fintech-shinyhunters-vishing.yaml) | data-leak | 2026-01-01 |  |  |
| [2025-12_sedgwick-government-tridentlocker.yaml](ransomware/2025-12_sedgwick-government-tridentlocker.yaml) | ransomware | 2025-12-31 | TridentLocker |  |
| [2025-12_eurail-aws-s3-passport-breach.yaml](data-leak/2025-12_eurail-aws-s3-passport-breach.yaml) | data-leak | 2025-12-26 |  |  |
| [2026-01_navia-benefit-solutions-bola.yaml](data-leak/2026-01_navia-benefit-solutions-bola.yaml) | data-leak | 2025-12-22 |  |  |
| [2025-12_conde-nast-wired-idor-breach.yaml](data-leak/2025-12_conde-nast-wired-idor-breach.yaml) | data-leak | 2025-12-20 |  |  |
| [2025-12_soundcloud-shinyhunters-vishing.yaml](data-leak/2025-12_soundcloud-shinyhunters-vishing.yaml) | data-leak | 2025-12-15 |  |  |
| [2026-01_brightspeed-crimson-collective.yaml](data-leak/2026-01_brightspeed-crimson-collective.yaml) | data-leak | 2025-12-01 |  |  |
| [2026-01_ledger-global-e-third-party.yaml](data-leak/2026-01_ledger-global-e-third-party.yaml) | data-leak | 2025-12-01 |  |  |
| [2025-12_customers-of-74-banks-and-credit-unions-served-by-marquis-software-solutions-marquis-software-solutions.yaml](supply-chain/2025-12_customers-of-74-banks-and-credit-unions-served-by-marquis-software-solutions-marquis-software-solutions.yaml) | supply-chain | 2025-12-01 |  |  |
| [2025-12_freedom-mobile-third-party-vendor.yaml](supply-chain/2025-12_freedom-mobile-third-party-vendor.yaml) | supply-chain | 2025-12-01 |  |  |
| [2025-12_pornhub-mixpanel.yaml](supply-chain/2025-12_pornhub-mixpanel.yaml) | supply-chain | 2025-12-01 |  |  |
| [2025-12_shuffles-pinterest-app-mixpanel.yaml](supply-chain/2025-12_shuffles-pinterest-app-mixpanel.yaml) | supply-chain | 2025-12-01 |  |  |
| [2026-02_cegedim-sante-monlogicielmedical.yaml](data-leak/2026-02_cegedim-sante-monlogicielmedical.yaml) | data-leak | 2025-12-01 |  |  |
| [2025-11_openai-mixpanel-vendor.yaml](other/2025-11_openai-mixpanel-vendor.yaml) | other | 2025-11-26 |  |  |
| [2025-11_situsamc-banks-breach.yaml](data-leak/2025-11_situsamc-banks-breach.yaml) | data-leak | 2025-11-12 |  |  |
| [2025-11_idmerit-mongodb-kyc-exposure.yaml](data-leak/2025-11_idmerit-mongodb-kyc-exposure.yaml) | data-leak | 2025-11-11 |  |  |
| [2025-11_coupang-insider-33m-korea.yaml](data-leak/2025-11_coupang-insider-33m-korea.yaml) | data-leak | 2025-11-08 |  |  |
| [2025-11_openai-mixpanel.yaml](supply-chain/2025-11_openai-mixpanel.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-11_terminalen-a-s-docubizz.yaml](supply-chain/2025-11_terminalen-a-s-docubizz.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-11_cbo-china-hack.yaml](other/2025-11_cbo-china-hack.yaml) | other | 2025-11-01 |  |  |
| [2025-11_the-washington-post-oracle-e-business-suite.yaml](supply-chain/2025-11_the-washington-post-oracle-e-business-suite.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-12_marquis-software-74-banks.yaml](data-leak/2025-12_marquis-software-74-banks.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-12_freedom-mobile-third-party.yaml](data-leak/2025-12_freedom-mobile-third-party.yaml) | data-leak | 2025-11-01 |  |  |
| [2025-11_logitech-third-party-vendor.yaml](supply-chain/2025-11_logitech-third-party-vendor.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-11_iberia-international-airlines-group-third-party-vendor.yaml](supply-chain/2025-11_iberia-international-airlines-group-third-party-vendor.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-11_under-armour-everest-ransomware.yaml](ransomware/2025-11_under-armour-everest-ransomware.yaml) | ransomware | 2025-11-01 | Everest |  |
| [2025-11_checkout-com-third-party-vendor.yaml](supply-chain/2025-11_checkout-com-third-party-vendor.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-10_doordash-social-engineering.yaml](data-leak/2025-10_doordash-social-engineering.yaml) | data-leak | 2025-10-25 |  |  |
| [2025-11_iberia-iag-loyalty-breach.yaml](data-leak/2025-11_iberia-iag-loyalty-breach.yaml) | data-leak | 2025-10-15 |  |  |
| [2025-11_mixpanel-analytics-multi-company.yaml](supply-chain/2025-11_mixpanel-analytics-multi-company.yaml) | supply-chain | 2025-10-15 |  |  |
| [2025-11_washington-post-oracle-ebs-breach.yaml](data-leak/2025-11_washington-post-oracle-ebs-breach.yaml) | data-leak | 2025-10-01 |  | CVE-2025-61882 |
| [2025-10_renault-and-dacia-uk-third-party-vendor.yaml](supply-chain/2025-10_renault-and-dacia-uk-third-party-vendor.yaml) | supply-chain | 2025-10-01 |  |  |
| [2025-10_redhat-gitlab-crimson-collective.yaml](supply-chain/2025-10_redhat-gitlab-crimson-collective.yaml) | supply-chain | 2025-10-01 |  |  |
| [2025-10_mango-third-party-vendor.yaml](supply-chain/2025-10_mango-third-party-vendor.yaml) | supply-chain | 2025-10-01 |  |  |
| [2025-10_discord-third-party-vendor.yaml](supply-chain/2025-10_discord-third-party-vendor.yaml) | supply-chain | 2025-10-01 |  |  |
| [2025-11_openai-mixpanel-analytics-leak.yaml](data-leak/2025-11_openai-mixpanel-analytics-leak.yaml) | data-leak | 2025-10-01 |  |  |
| [2025-10_discord-third-party-customer-service-55m.yaml](data-leak/2025-10_discord-third-party-customer-service-55m.yaml) | data-leak | 2025-10-01 |  |  |
| [2025-10_docketwise-credential-immigration.yaml](data-leak/2025-10_docketwise-credential-immigration.yaml) | data-leak | 2025-10-01 |  |  |
| [2025-09_insightin-health-goanywhere-medusa.yaml](ransomware/2025-09_insightin-health-goanywhere-medusa.yaml) | ransomware | 2025-09-17 | Medusa |  |
| [2025-10_mango-marketing-provider-breach.yaml](data-leak/2025-10_mango-marketing-provider-breach.yaml) | data-leak | 2025-09-15 |  |  |
| [2025-09_shai-hulud-npm-worm.yaml](supply-chain/2025-09_shai-hulud-npm-worm.yaml) | supply-chain | 2025-09-14 | Shai-Hulud |  |
| [2025-09_npm-chalk-debug-phishing.yaml](supply-chain/2025-09_npm-chalk-debug-phishing.yaml) | supply-chain | 2025-09-08 | Browser crypto wallet stealer… |  |
| [2025-09_dynatrace-llc-drift-salesloft.yaml](supply-chain/2025-09_dynatrace-llc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_palo-alto-networks-drift-salesloft.yaml](supply-chain/2025-09_palo-alto-networks-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-10_renault-dacia-uk-third-party.yaml](data-leak/2025-10_renault-dacia-uk-third-party.yaml) | data-leak | 2025-09-01 |  |  |
| [2025-09_wynn-resorts-oracle-shinyhunters.yaml](data-leak/2025-09_wynn-resorts-oracle-shinyhunters.yaml) | data-leak | 2025-09-01 |  |  |
| [2025-09_327-unknown-users-github-workflows.yaml](supply-chain/2025-09_327-unknown-users-github-workflows.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_swissborg-kiln-staking-41m-sol.yaml](data-leak/2025-09_swissborg-kiln-staking-41m-sol.yaml) | other | 2025-09-01 |  |  |
| [2025-09_agility-pr-solutions-drift-salesloft.yaml](supply-chain/2025-09_agility-pr-solutions-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_beyondtrust-drift-salesloft.yaml](supply-chain/2025-09_beyondtrust-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_black-duck-software-inc-drift-salesloft.yaml](supply-chain/2025-09_black-duck-software-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_bugcrowd-drift-salesloft.yaml](supply-chain/2025-09_bugcrowd-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_cato-networks-drift-salesloft.yaml](supply-chain/2025-09_cato-networks-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_workiva-drift-salesloft.yaml](supply-chain/2025-09_workiva-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_workday-drift-salesloft.yaml](supply-chain/2025-09_workday-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_wealthsimple-third-party-vendor.yaml](supply-chain/2025-09_wealthsimple-third-party-vendor.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_tenable-inc-drift-salesloft.yaml](supply-chain/2025-09_tenable-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_swissborg-kiln.yaml](supply-chain/2025-09_swissborg-kiln.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_stellantis-salesforce.yaml](supply-chain/2025-09_stellantis-salesforce.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_spycloud-inc-drift-salesloft.yaml](supply-chain/2025-09_spycloud-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_sprout-social-inc-drift-salesloft.yaml](supply-chain/2025-09_sprout-social-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_sophos-ltd-drift-salesloft.yaml](supply-chain/2025-09_sophos-ltd-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_sigma-computing-drift-salesloft.yaml](supply-chain/2025-09_sigma-computing-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_chess-com-third-party-vendor.yaml](supply-chain/2025-09_chess-com-third-party-vendor.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_qualys-inc-drift-salesloft.yaml](supply-chain/2025-09_qualys-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_proofpoint-drift-salesloft.yaml](supply-chain/2025-09_proofpoint-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_pantheon-drift-salesloft.yaml](supply-chain/2025-09_pantheon-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_cloudflare-drift-salesloft.yaml](supply-chain/2025-09_cloudflare-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_onespan-drift-salesloft.yaml](supply-chain/2025-09_onespan-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_omada-drift-salesloft.yaml](supply-chain/2025-09_omada-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_contentsquare-drift-salesloft.yaml](supply-chain/2025-09_contentsquare-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_london-north-eastern-railway-lner-third-party-vendor.yaml](supply-chain/2025-09_london-north-eastern-railway-lner-third-party-vendor.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_liveramp-drift-salesloft.yaml](supply-chain/2025-09_liveramp-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_harrods-third-party-vendor.yaml](supply-chain/2025-09_harrods-third-party-vendor.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_hackerone-drift-salesloft.yaml](supply-chain/2025-09_hackerone-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_fastly-drift-salesloft.yaml](supply-chain/2025-09_fastly-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_esker-drift-salesloft.yaml](supply-chain/2025-09_esker-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_ericom-software-drift-salesloft.yaml](supply-chain/2025-09_ericom-software-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_employment-and-social-development-canada-esdc-2keys-corporation.yaml](supply-chain/2025-09_employment-and-social-development-canada-esdc-2keys-corporation.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_elasticsearch-b-v-drift-salesloft.yaml](supply-chain/2025-09_elasticsearch-b-v-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_cyberark-software-ltd-drift-salesloft.yaml](supply-chain/2025-09_cyberark-software-ltd-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-08_university-hawaii-cancer-center.yaml](ransomware/2025-08_university-hawaii-cancer-center.yaml) | ransomware | 2025-08-31 |  |  |
| [2025-09_jaguar-land-rover-scattered-lapsus.yaml](ransomware/2025-09_jaguar-land-rover-scattered-lapsus.yaml) | ransomware | 2025-08-31 |  |  |
| [2025-08_minnesota-dhs-fei-systems-insider.yaml](data-leak/2025-08_minnesota-dhs-fei-systems-insider.yaml) | data-leak | 2025-08-28 |  |  |
| [2025-08_insight-hospital-chicago-termite.yaml](ransomware/2025-08_insight-hospital-chicago-termite.yaml) | ransomware | 2025-08-22 | Termite |  |
| [2025-09_lner-third-party-vendor.yaml](data-leak/2025-09_lner-third-party-vendor.yaml) | data-leak | 2025-08-15 |  |  |
| [2025-09_wealthsimple-third-party-breach.yaml](data-leak/2025-09_wealthsimple-third-party-breach.yaml) | data-leak | 2025-08-15 |  |  |
| [2025-08_marquis-software-akira-banks.yaml](ransomware/2025-08_marquis-software-akira-banks.yaml) | ransomware | 2025-08-14 | Akira | CVE-2024-40766 |
| [2025-08_pennsylvania-ag-inc-ransom.yaml](ransomware/2025-08_pennsylvania-ag-inc-ransom.yaml) | ransomware | 2025-08-09 | INC Ransom | CVE-2025-5777 |
| [2025-08_clop-oracle-ebs-education.yaml](supply-chain/2025-08_clop-oracle-ebs-education.yaml) | supply-chain | 2025-08-09 |  | CVE-2025-61882, CVE-2025-61884 |
| [2025-08_salesloft-drift-oauth-salesforce.yaml](supply-chain/2025-08_salesloft-drift-oauth-salesforce.yaml) | supply-chain | 2025-08-08 |  |  |
| [2025-08_bouygues-telecom-france-6m.yaml](data-leak/2025-08_bouygues-telecom-france-6m.yaml) | data-leak | 2025-08-04 |  |  |
| [2025-08_transunion-salesforce.yaml](supply-chain/2025-08_transunion-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_farmers-insurance-salesforce.yaml](supply-chain/2025-08_farmers-insurance-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_tanium-drift-salesloft.yaml](supply-chain/2025-08_tanium-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_swedish-municipalities-milj-data.yaml](supply-chain/2025-08_swedish-municipalities-milj-data.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_uk-s-defence-ministry-and-the-cabinet-office-inflite-the-jet-centre-ltd.yaml](supply-chain/2025-08_uk-s-defence-ministry-and-the-cabinet-office-inflite-the-jet-centre-ltd.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_rubrik-drift-salesloft.yaml](supply-chain/2025-08_rubrik-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_pi-hole-givewp-wordpress.yaml](supply-chain/2025-08_pi-hole-givewp-wordpress.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_pandora-salesforce.yaml](supply-chain/2025-08_pandora-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_pagerduty-drift-salesloft.yaml](supply-chain/2025-08_pagerduty-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_miami-plastic-surgery-keys-dermatology-and-more-dermcare-management.yaml](supply-chain/2025-08_miami-plastic-surgery-keys-dermatology-and-more-dermcare-management.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_megaport-drift-salesloft.yaml](supply-chain/2025-08_megaport-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_lucid-software-inc-drift-salesloft.yaml](supply-chain/2025-08_lucid-software-inc-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_jfrog-drift-salesloft.yaml](supply-chain/2025-08_jfrog-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-09_canada-2keys-government-accounts.yaml](data-leak/2025-09_canada-2keys-government-accounts.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_zscaler-drift-salesloft.yaml](supply-chain/2025-08_zscaler-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_cisco-salesforce.yaml](supply-chain/2025-08_cisco-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_chanel-salesforce.yaml](supply-chain/2025-08_chanel-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_air-france-klm-group-salesforce.yaml](supply-chain/2025-08_air-france-klm-group-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_access-personal-checking-services-apcs-intradev.yaml](supply-chain/2025-08_access-personal-checking-services-apcs-intradev.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_university-phoenix-oracle-ebs-clop.yaml](data-leak/2025-08_university-phoenix-oracle-ebs-clop.yaml) | data-leak | 2025-08-01 |  | CVE-2025-61882 |
| [2025-09_harrods-third-party-breach.yaml](data-leak/2025-09_harrods-third-party-breach.yaml) | data-leak | 2025-08-01 |  |  |
| [2025-09_chess-com-file-transfer-breach.yaml](data-leak/2025-09_chess-com-file-transfer-breach.yaml) | data-leak | 2025-08-01 |  |  |
| [2025-07_transunion-salesforce-unc6395.yaml](data-leak/2025-07_transunion-salesforce-unc6395.yaml) | data-leak | 2025-07-28 |  |  |
| [2025-07_st-paul-minnesota-interlock.yaml](ransomware/2025-07_st-paul-minnesota-interlock.yaml) | ransomware | 2025-07-25 | Interlock ransomware |  |
| [2025-07_allianz-life-shiny-hunters.yaml](data-leak/2025-07_allianz-life-shiny-hunters.yaml) | data-leak | 2025-07-16 |  |  |
| [2025-07_ingram-micro-safepay.yaml](ransomware/2025-07_ingram-micro-safepay.yaml) | ransomware | 2025-07-02 | SafePay |  |
| [2025-08_cisco-salesforce-shinyhunters.yaml](data-leak/2025-08_cisco-salesforce-shinyhunters.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_louis-vuitton-third-party-vendor.yaml](supply-chain/2025-07_louis-vuitton-third-party-vendor.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_united-healthcare-aetna-life-insurance-company-cvs-health-and-46-more-kelly-associates-insurance-g.yaml](supply-chain/2025-07_united-healthcare-aetna-life-insurance-company-cvs-health-and-46-more-kelly-associates-insurance-g.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_texas-centers-for-infectious-disease-associates-third-party-vendor.yaml](supply-chain/2025-07_texas-centers-for-infectious-disease-associates-third-party-vendor.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_qantas-airways-limited-third-party-vendor.yaml](supply-chain/2025-07_qantas-airways-limited-third-party-vendor.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_700credit-api-automotive-dealers.yaml](data-leak/2025-07_700credit-api-automotive-dealers.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-08_transunion-salesforce-44m.yaml](data-leak/2025-08_transunion-salesforce-44m.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-08_pandora-chanel-salesforce-shinyhunters.yaml](data-leak/2025-08_pandora-chanel-salesforce-shinyhunters.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-09_stellantis-salesforce-shinyhunters.yaml](data-leak/2025-09_stellantis-salesforce-shinyhunters.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_mcdonald-s-paradox-inc.yaml](supply-chain/2025-07_mcdonald-s-paradox-inc.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_mcdonalds-paradox-ai-chatbot-64m.yaml](data-leak/2025-07_mcdonalds-paradox-ai-chatbot-64m.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_allianz-life-third-party-vendor.yaml](supply-chain/2025-07_allianz-life-third-party-vendor.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-08_air-france-klm-salesforce.yaml](data-leak/2025-08_air-france-klm-salesforce.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_paypal-working-capital-code-error.yaml](data-leak/2025-07_paypal-working-capital-code-error.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_qantas-salesforce-shinyhunters-vishing.yaml](data-leak/2025-07_qantas-salesforce-shinyhunters-vishing.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-06_aflac-scattered-spider.yaml](data-leak/2025-06_aflac-scattered-spider.yaml) | data-leak | 2025-06-12 |  |  |
| [2025-06_sharp-healthcare-episource.yaml](supply-chain/2025-06_sharp-healthcare-episource.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-10_vietnam-airlines-salesforce-scattered-lapsus.yaml](data-leak/2025-10_vietnam-airlines-salesforce-scattered-lapsus.yaml) | data-leak | 2025-06-01 |  |  |
| [2025-06_switzerland-government-radix-zurich-based-and-non-p.yaml](supply-chain/2025-06_switzerland-government-radix-zurich-based-and-non-p.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-06_prosper-marketplace-credential-17m.yaml](data-leak/2025-06_prosper-marketplace-credential-17m.yaml) | data-leak | 2025-06-01 |  |  |
| [2025-06_coinbase-taskus.yaml](supply-chain/2025-06_coinbase-taskus.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-06_glasgow-city-council-third-party-vendor.yaml](supply-chain/2025-06_glasgow-city-council-third-party-vendor.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-06_mainstreet-bank-third-party-vendor.yaml](supply-chain/2025-06_mainstreet-bank-third-party-vendor.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-05_farmers-insurance-salesforce-shinyhunters.yaml](data-leak/2025-05_farmers-insurance-salesforce-shinyhunters.yaml) | data-leak | 2025-05-29 |  |  |
| [2025-05_kettering-health-interlock.yaml](ransomware/2025-05_kettering-health-interlock.yaml) | ransomware | 2025-05-20 | Interlock ransomware |  |
| [2025-05_covenant-health-qilin.yaml](ransomware/2025-05_covenant-health-qilin.yaml) | ransomware | 2025-05-18 | Qilin |  |
| [2025-05_marks-spencer-tata-consultancy-services-tc.yaml](supply-chain/2025-05_marks-spencer-tata-consultancy-services-tc.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_500-1-000-e-commerce-stores-tigren-meetanshi-and-mgs.yaml](supply-chain/2025-05_500-1-000-e-commerce-stores-tigren-meetanshi-and-mgs.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_2-000-providers-including-barristers-solicitor-firms-and-non-profit-organizations-legal-aid-agency-laa.yaml](supply-chain/2025-05_2-000-providers-including-barristers-solicitor-firms-and-non-profit-organizations-legal-aid-agency-laa.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-06_sharp-healthcare-episource-breach.yaml](supply-chain/2025-06_sharp-healthcare-episource-breach.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_trg-medical-imaging-nationwide-recovery-services.yaml](supply-chain/2025-05_trg-medical-imaging-nationwide-recovery-services.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_adidas-third-party-vendor.yaml](supply-chain/2025-05_adidas-third-party-vendor.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_catholic-health-serviceaide.yaml](supply-chain/2025-05_catholic-health-serviceaide.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_multiple-local-governing-bodies-across-the-united-states-trimble-cityworks.yaml](supply-chain/2025-05_multiple-local-governing-bodies-across-the-united-states-trimble-cityworks.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_dragonforce-simplehelp-msp.yaml](supply-chain/2025-05_dragonforce-simplehelp-msp.yaml) | supply-chain | 2025-05-01 | DragonForce ransomware | CVE-2024-57726, CVE-2024-57727, CVE-202… |
| [2025-05_marks-spencer-tcs-breach.yaml](data-leak/2025-05_marks-spencer-tcs-breach.yaml) | data-leak | 2025-04-22 | DragonForce ransomware |  |
| [2025-04_sk-telecom-bpfdoor-sim-data.yaml](other/2025-04_sk-telecom-bpfdoor-sim-data.yaml) | other | 2025-04-18 | BPFDoor; Tiny Shell |  |
| [2025-04_ericsson-us-third-party-breach.yaml](data-leak/2025-04_ericsson-us-third-party-breach.yaml) | data-leak | 2025-04-17 |  |  |
| [2025-04_coop-harrods-dragonforce.yaml](ransomware/2025-04_coop-harrods-dragonforce.yaml) | ransomware | 2025-04-01 | DragonForce ransomware |  |
| [2025-04_ascension-former-business-partner.yaml](supply-chain/2025-04_ascension-former-business-partner.yaml) | supply-chain | 2025-04-01 |  |  |
| [2025-05_legal-aid-agency-uk-2000-providers.yaml](data-leak/2025-05_legal-aid-agency-uk-2000-providers.yaml) | data-leak | 2025-04-01 |  |  |
| [2025-05_nationwide-recovery-services-healthcare-cluster.yaml](supply-chain/2025-05_nationwide-recovery-services-healthcare-cluster.yaml) | supply-chain | 2025-04-01 |  |  |
| [2025-04_12-insurance-company-landmark-admin.yaml](supply-chain/2025-04_12-insurance-company-landmark-admin.yaml) | supply-chain | 2025-04-01 |  |  |
| [2025-05_adidas-customer-service-breach.yaml](data-leak/2025-05_adidas-customer-service-breach.yaml) | data-leak | 2025-04-01 |  |  |
| [2025-04_royal-mail-spectos-gmbh.yaml](supply-chain/2025-04_royal-mail-spectos-gmbh.yaml) | supply-chain | 2025-04-01 |  |  |
| [2025-04_royal-mail-spectos-breach.yaml](data-leak/2025-04_royal-mail-spectos-breach.yaml) | data-leak | 2025-03-29 |  |  |
| [2025-04_davita-interlock.yaml](ransomware/2025-04_davita-interlock.yaml) | ransomware | 2025-03-24 | Interlock ransomware |  |
| [2025-04_ivanti-connect-secure-cve-2025-22457.yaml](other/2025-04_ivanti-connect-secure-cve-2025-22457.yaml) | other | 2025-03-15 | TRAILBLAZE (in-memory dropper… | CVE-2025-22457 |
| [2025-03_yale-new-haven-health.yaml](ransomware/2025-03_yale-new-haven-health.yaml) | ransomware | 2025-03-08 |  |  |
| [2025-03_dozens-of-public-schools-across-the-usa-carruth-compliance-consultin.yaml](supply-chain/2025-03_dozens-of-public-schools-across-the-usa-carruth-compliance-consultin.yaml) | supply-chain | 2025-03-01 |  |  |
| [2025-03_17-891-corporate-customers-companies-ntt-communications-corporati.yaml](supply-chain/2025-03_17-891-corporate-customers-companies-ntt-communications-corporati.yaml) | supply-chain | 2025-03-01 |  |  |
| [2025-03_streamelements-gooten.yaml](supply-chain/2025-03_streamelements-gooten.yaml) | supply-chain | 2025-03-01 |  |  |
| [2025-03_multiple-us-healthcare-organizations-and-hospitals-oracle-health-formerly-cerne.yaml](supply-chain/2025-03_multiple-us-healthcare-organizations-and-hospitals-oracle-health-formerly-cerne.yaml) | supply-chain | 2025-03-01 |  |  |
| [2025-03_berkeley-research-group-chaos.yaml](ransomware/2025-03_berkeley-research-group-chaos.yaml) | ransomware | 2025-02-28 | Chaos ransomware |  |
| [2025-02_bybit-safe-wallet-lazarus.yaml](supply-chain/2025-02_bybit-safe-wallet-lazarus.yaml) | supply-chain | 2025-02-21 |  |  |
| [2025-02_opexus-insider-federal.yaml](other/2025-02_opexus-insider-federal.yaml) | other | 2025-02-18 |  |  |
| [2025-03_streamelements-gooten-breach.yaml](supply-chain/2025-03_streamelements-gooten-breach.yaml) | supply-chain | 2025-02-15 |  |  |
| [2025-02_anne-arundel-dermatology-breach.yaml](data-leak/2025-02_anne-arundel-dermatology-breach.yaml) | data-leak | 2025-02-14 |  |  |
| [2025-02_current-former-and-prospective-employees-of-its-customers-disa-global-solutions.yaml](supply-chain/2025-02_current-former-and-prospective-employees-of-its-customers-disa-global-solutions.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-02_grubhub-third-party-vendor.yaml](supply-chain/2025-02_grubhub-third-party-vendor.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-02_moses-weitzman-health-system-community-health-center.yaml](supply-chain/2025-02_moses-weitzman-health-system-community-health-center.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-04_marks-and-spencer.yaml](ransomware/2025-04_marks-and-spencer.yaml) | ransomware | 2025-02-01 | DragonForce ransomware |  |
| [2025-02_local-credit-and-financial-businesses-lanit-group.yaml](supply-chain/2025-02_local-credit-and-financial-businesses-lanit-group.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-02_river-region-cardiology-third-party-vendor.yaml](supply-chain/2025-02_river-region-cardiology-third-party-vendor.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-02_17-banks-and-5-other-organizations-bankers-cooperative-group.yaml](supply-chain/2025-02_17-banks-and-5-other-organizations-bankers-cooperative-group.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-01_western-sydney-university.yaml](data-leak/2025-01_western-sydney-university.yaml) | data-leak | 2025-01-28 |  |  |
| [2025-01_frederick-health-ransomware.yaml](ransomware/2025-01_frederick-health-ransomware.yaml) | ransomware | 2025-01-27 |  |  |
| [2025-02_episource-optum-unitedhealth.yaml](ransomware/2025-02_episource-optum-unitedhealth.yaml) | ransomware | 2025-01-27 |  |  |
| [2025-01_oracle-health-cerner-hospitals.yaml](supply-chain/2025-01_oracle-health-cerner-hospitals.yaml) | supply-chain | 2025-01-22 |  | CVE-2025-30154 |
| [2025-01_simonmed-imaging-medusa.yaml](ransomware/2025-01_simonmed-imaging-medusa.yaml) | ransomware | 2025-01-21 | Medusa |  |
| [2025-06_heritage-foundation-doge.yaml](data-leak/2025-06_heritage-foundation-doge.yaml) | other | 2025-01-20 |  |  |
| [2025-02_grubhub-third-party-vendor.yaml](data-leak/2025-02_grubhub-third-party-vendor.yaml) | data-leak | 2025-01-01 |  |  |
| [2025-01_allegheny-health-network-intrasystems-llc.yaml](supply-chain/2025-01_allegheny-health-network-intrasystems-llc.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-05_magento-tigren-meetanshi-extensions.yaml](supply-chain/2025-05_magento-tigren-meetanshi-extensions.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-05_trimble-cityworks-us-local-govts.yaml](supply-chain/2025-05_trimble-cityworks-us-local-govts.yaml) | supply-chain | 2025-01-01 |  | CVE-2025-0994 |
| [2025-05_coinbase-insider-bribery.yaml](credential-theft/2025-05_coinbase-insider-bribery.yaml) | credential-theft | 2025-01-01 |  |  |
| [2025-01_ai-accelerating-cyberattack-timelines.yaml](other/2025-01_ai-accelerating-cyberattack-timelines.yaml) | other | 2025-01-01 |  |  |
| [2025-01_ai-powered-identity-theft-wave.yaml](other/2025-01_ai-powered-identity-theft-wave.yaml) | other | 2025-01-01 |  |  |
| [2025-01_rostelecom-third-party-vendor.yaml](supply-chain/2025-01_rostelecom-third-party-vendor.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_machine-speed-attacks-ai-automation.yaml](other/2025-01_machine-speed-attacks-ai-automation.yaml) | other | 2025-01-01 |  |  |
| [2025-01_khalil-foundation-transform-studios.yaml](supply-chain/2025-01_khalil-foundation-transform-studios.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_94-k-12-schools-powerschool.yaml](supply-chain/2025-01_94-k-12-schools-powerschool.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_wyndham-otelier.yaml](supply-chain/2025-01_wyndham-otelier.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_centerpoint-energy-third-party-vendor.yaml](supply-chain/2025-01_centerpoint-energy-third-party-vendor.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-06_coinbase-taskus-customer-support.yaml](data-leak/2025-06_coinbase-taskus-customer-support.yaml) | data-leak | 2025-01-01 |  |  |
| [2025-01_talktalk-csg-ascendon.yaml](supply-chain/2025-01_talktalk-csg-ascendon.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_stiiizy-third-party-vendor.yaml](supply-chain/2025-01_stiiizy-third-party-vendor.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_tata-technologies-hunters-intl.yaml](ransomware/2025-01_tata-technologies-hunters-intl.yaml) | ransomware | 2025-01-01 | Hunters International ransomw… |  |
| [2025-01_talktalk-csg-ascendon-subscriber.yaml](supply-chain/2025-01_talktalk-csg-ascendon-subscriber.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_oracle-cloud-sso-breach.yaml](data-leak/2025-01_oracle-cloud-sso-breach.yaml) | data-leak | 2025-01-01 |  | CVE-2021-35587 |
| [2025-01_square-medical-group-third-party-vendor.yaml](supply-chain/2025-01_square-medical-group-third-party-vendor.yaml) | supply-chain | 2025-01-01 |  |  |
| [2024-12_powerschool-sis.yaml](supply-chain/2024-12_powerschool-sis.yaml) | supply-chain | 2024-12-19 |  |  |
| [2024-12_powerschool-extortion-followon.yaml](data-leak/2024-12_powerschool-extortion-followon.yaml) | data-leak | 2024-12-19 |  |  |
| [2025-01_ivanti-connect-secure-cve-2025-0282.yaml](other/2025-01_ivanti-connect-secure-cve-2025-0282.yaml) | other | 2024-12-15 | SPAWN ecosystem (SPAWNANT ins… | CVE-2025-0282, CVE-2025-0283 |
| [2024-12_monroe-university.yaml](data-leak/2024-12_monroe-university.yaml) | data-leak | 2024-12-09 |  |  |
| [2024-12_ultralytics-pypi-github-actions-cryptominer.yaml](supply-chain/2024-12_ultralytics-pypi-github-actions-cryptominer.yaml) | supply-chain | 2024-12-04 | XMRig (Monero cryptominer) |  |
| [2025-04_ascension-former-partner-ehr.yaml](supply-chain/2025-04_ascension-former-partner-ehr.yaml) | supply-chain | 2024-12-01 |  |  |
| [2025-04_hertz-cleo-clop-breach.yaml](data-leak/2025-04_hertz-cleo-clop-breach.yaml) | data-leak | 2024-12-01 |  | CVE-2024-50623, CVE-2024-55956 |
| [2025-01_orange-romania-hellcat-jira.yaml](data-leak/2025-01_orange-romania-hellcat-jira.yaml) | data-leak | 2024-12-01 |  |  |
| [2024-12_monument-health-change-healthcare.yaml](supply-chain/2024-12_monument-health-change-healthcare.yaml) | supply-chain | 2024-12-01 |  |  |
| [2024-12_whittier-hospital-pih-health.yaml](supply-chain/2024-12_whittier-hospital-pih-health.yaml) | supply-chain | 2024-12-01 |  |  |
| [2024-12_ribridges-system-deloitte.yaml](supply-chain/2024-12_ribridges-system-deloitte.yaml) | supply-chain | 2024-12-01 |  |  |
| [2024-12_pavilion-of-bridgeview-pointclickcare.yaml](supply-chain/2024-12_pavilion-of-bridgeview-pointclickcare.yaml) | supply-chain | 2024-12-01 |  |  |
| [2024-12_veterans-health-administration-dbp-inc.yaml](supply-chain/2024-12_veterans-health-administration-dbp-inc.yaml) | supply-chain | 2024-12-01 |  |  |
| [2024-11_krispy-kreme-play.yaml](ransomware/2024-11_krispy-kreme-play.yaml) | ransomware | 2024-11-29 | Play ransomware |  |
| [2024-11_lockton-companies-southeast-breach.yaml](data-leak/2024-11_lockton-companies-southeast-breach.yaml) | data-leak | 2024-11-20 |  |  |
| [2024-12_cleo-mft-clop.yaml](supply-chain/2024-12_cleo-mft-clop.yaml) | supply-chain | 2024-11-15 | Clop (Cl0p) ransomware | CVE-2024-50623, CVE-2024-55956 |
| [2024-11_legends-international.yaml](data-leak/2024-11_legends-international.yaml) | data-leak | 2024-11-09 |  |  |
| [2024-11_ahold-delhaize-inc-ransom.yaml](ransomware/2024-11_ahold-delhaize-inc-ransom.yaml) | ransomware | 2024-11-05 | INC Ransom |  |
| [2024-11_minist-re-du-travail-et-de-l-emploi-third-party-vendor.yaml](supply-chain/2024-11_minist-re-du-travail-et-de-l-emploi-third-party-vendor.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_nokia-third-party-vendor.yaml](supply-chain/2024-11_nokia-third-party-vendor.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_bologna-fc-ransomhub.yaml](ransomware/2024-11_bologna-fc-ransomhub.yaml) | ransomware | 2024-11-01 | RansomHub ransomware |  |
| [2024-11_sainsbury-s-blue-yonder.yaml](supply-chain/2024-11_sainsbury-s-blue-yonder.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_schneider-electric-hellcat.yaml](ransomware/2024-11_schneider-electric-hellcat.yaml) | ransomware | 2024-11-01 | Hellcat |  |
| [2024-12_arc-community-services.yaml](ransomware/2024-12_arc-community-services.yaml) | ransomware | 2024-11-01 |  |  |
| [2024-11_mid-minnesota-management-services-central-resources-third-party-vendor.yaml](supply-chain/2024-11_mid-minnesota-management-services-central-resources-third-party-vendor.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_presbyterian-healthcare-services-thompson-coburn.yaml](supply-chain/2024-11_presbyterian-healthcare-services-thompson-coburn.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_trihealth-physician-partners-trihealth-third-party-vendor.yaml](supply-chain/2024-11_trihealth-physician-partners-trihealth-third-party-vendor.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_schneider-electric-atlassian-s-jira-server.yaml](supply-chain/2024-11_schneider-electric-atlassian-s-jira-server.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_finastra-sftp-banking-software.yaml](data-leak/2024-11_finastra-sftp-banking-software.yaml) | data-leak | 2024-10-31 |  |  |
| [2024-10_midnight-blizzard-rdp-spearphish.yaml](other/2024-10_midnight-blizzard-rdp-spearphish.yaml) | other | 2024-10-22 |  |  |
| [2025-01_conduent-safepay-state-benefits.yaml](ransomware/2025-01_conduent-safepay-state-benefits.yaml) | ransomware | 2024-10-21 | SafePay |  |
| [2024-10_conduent-safepay.yaml](ransomware/2024-10_conduent-safepay.yaml) | ransomware | 2024-10-21 | SafePay ransomware |  |
| [2024-10_radiant-capital-defi-lazarus.yaml](credential-theft/2024-10_radiant-capital-defi-lazarus.yaml) | credential-theft | 2024-10-16 | InletDrift |  |
| [2024-10_mut8694-npm-pypi-roblox.yaml](supply-chain/2024-10_mut8694-npm-pypi-roblox.yaml) | supply-chain | 2024-10-10 | Blank Grabber infostealer; Sk… |  |
| [2024-10_casio-underground.yaml](ransomware/2024-10_casio-underground.yaml) | ransomware | 2024-10-05 | Underground ransomware |  |
| [2024-10_american-water-works.yaml](other/2024-10_american-water-works.yaml) | other | 2024-10-03 |  |  |
| [2025-01_stiiizy-cannabis-pos-breach-380k.yaml](data-leak/2025-01_stiiizy-cannabis-pos-breach-380k.yaml) | data-leak | 2024-10-01 |  |  |
| [2024-10_hot-topic.yaml](data-leak/2024-10_hot-topic.yaml) | data-leak | 2024-10-01 | Infostealer malware (targetin… |  |
| [2024-10_adt-third-party-business-partner.yaml](supply-chain/2024-10_adt-third-party-business-partner.yaml) | supply-chain | 2024-10-01 |  |  |
| [2024-10_smile-design-management-third-party-vendor.yaml](supply-chain/2024-10_smile-design-management-third-party-vendor.yaml) | supply-chain | 2024-10-01 |  |  |
| [2024-10_rackspace-sciencelogic.yaml](supply-chain/2024-10_rackspace-sciencelogic.yaml) | supply-chain | 2024-10-01 |  |  |
| [2024-10_cf-medical-financial-business-and-consu.yaml](supply-chain/2024-10_cf-medical-financial-business-and-consu.yaml) | supply-chain | 2024-10-01 |  |  |
| [2024-10_boston-children-s-health-physicians-axispoint-technology-solutio.yaml](supply-chain/2024-10_boston-children-s-health-physicians-axispoint-technology-solutio.yaml) | supply-chain | 2024-10-01 |  |  |
| [2024-11_byte-federal-bitcoin-atm-gitlab.yaml](data-leak/2024-11_byte-federal-bitcoin-atm-gitlab.yaml) | data-leak | 2024-09-30 |  |  |
| [2024-10_free-mobile-france-vpn-24m.yaml](data-leak/2024-10_free-mobile-france-vpn-24m.yaml) | data-leak | 2024-09-28 |  |  |
| [2024-10_internet-archive.yaml](data-leak/2024-10_internet-archive.yaml) | data-leak | 2024-09-28 |  |  |
| [2024-09_moneygram-social-engineering.yaml](data-leak/2024-09_moneygram-social-engineering.yaml) | data-leak | 2024-09-20 |  |  |
| [2024-09_serviceaide-catholic-health-elasticsearch.yaml](data-leak/2024-09_serviceaide-catholic-health-elasticsearch.yaml) | data-leak | 2024-09-19 |  |  |
| [2024-09_texas-tech-health-interlock.yaml](ransomware/2024-09_texas-tech-health-interlock.yaml) | ransomware | 2024-09-17 | Interlock ransomware |  |
| [2024-09_nhs-england-synnovis.yaml](supply-chain/2024-09_nhs-england-synnovis.yaml) | supply-chain | 2024-09-01 |  |  |
| [2024-09_t-mobile-capgemini.yaml](supply-chain/2024-09_t-mobile-capgemini.yaml) | supply-chain | 2024-09-01 |  |  |
| [2024-11_icbc-london-hunters-intl.yaml](other/2024-11_icbc-london-hunters-intl.yaml) | ransomware | 2024-09-01 | Hunters International ransomw… |  |
| [2024-09_cultura-third-party-vendor.yaml](supply-chain/2024-09_cultura-third-party-vendor.yaml) | supply-chain | 2024-09-01 |  |  |
| [2024-09_centers-for-medicare-medicaid-services-cms-wisconsin-physicians-service.yaml](supply-chain/2024-09_centers-for-medicare-medicaid-services-cms-wisconsin-physicians-service.yaml) | supply-chain | 2024-09-01 |  |  |
| [2024-09_transport-for-london-scattered-spider.yaml](other/2024-09_transport-for-london-scattered-spider.yaml) | credential-theft | 2024-08-31 |  |  |
| [2024-08_halliburton.yaml](ransomware/2024-08_halliburton.yaml) | ransomware | 2024-08-21 | RansomHub ransomware |  |
| [2024-08_fidelity-investments-account-abuse.yaml](data-leak/2024-08_fidelity-investments-account-abuse.yaml) | data-leak | 2024-08-17 |  |  |
| [2023-03_royal-mail-lockbit-v2.yaml](ransomware/2023-03_royal-mail-lockbit-v2.yaml) | ransomware | 2024-08-11 | Hunters International ransomw… |  |
| [2024-08_toyota-third-party-vendor.yaml](supply-chain/2024-08_toyota-third-party-vendor.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_surgery-center-of-mid-florida-third-party-vendor.yaml](supply-chain/2024-08_surgery-center-of-mid-florida-third-party-vendor.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_hah-group-holding-company-third-party-vendor.yaml](supply-chain/2024-08_hah-group-holding-company-third-party-vendor.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_blue-shield-of-california-young-consulting.yaml](supply-chain/2024-08_blue-shield-of-california-young-consulting.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_13-000-students-in-singapore-mobile-guardian.yaml](supply-chain/2024-08_13-000-students-in-singapore-mobile-guardian.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_national-payments-corporation-of-india-npci-c-edge-technologies-ltd.yaml](supply-chain/2024-08_national-payments-corporation-of-india-npci-c-edge-technologies-ltd.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-07_crowdstrike-falcon-global-bsod.yaml](other/2024-07_crowdstrike-falcon-global-bsod.yaml) | other | 2024-07-19 |  |  |
| [2024-07_wazirx-lazarus-multisig.yaml](credential-theft/2024-07_wazirx-lazarus-multisig.yaml) | credential-theft | 2024-07-18 | Safe Wallet front-end manipul… |  |
| [2024-08_mclaren-health.yaml](ransomware/2024-08_mclaren-health.yaml) | ransomware | 2024-07-17 | INC Ransom ransomware |  |
| [2025-01_otelier-hotel-reservation-platform.yaml](supply-chain/2025-01_otelier-hotel-reservation-platform.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_bilt-evolve-bank-trust.yaml](supply-chain/2024-07_bilt-evolve-bank-trust.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_autonation-cdk-global.yaml](supply-chain/2024-07_autonation-cdk-global.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_at-t-snowflake.yaml](supply-chain/2024-07_at-t-snowflake.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_300-small-indian-banks-c-edge-technologies-ltd.yaml](supply-chain/2024-07_300-small-indian-banks-c-edge-technologies-ltd.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_gemini-not-disclosed-automated-clea.yaml](supply-chain/2024-07_gemini-not-disclosed-automated-clea.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_clear-spring-health-change-healthcare.yaml](supply-chain/2024-07_clear-spring-health-change-healthcare.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_kairos-health-arizona-a-third-party-vendor.yaml](supply-chain/2024-07_kairos-health-arizona-a-third-party-vendor.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_mobile-medical-response-cbm-services.yaml](supply-chain/2024-07_mobile-medical-response-cbm-services.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_roblox-fntech.yaml](supply-chain/2024-07_roblox-fntech.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_wisconsin-department-of-health-services-disability-rights-wisconsin.yaml](supply-chain/2024-07_wisconsin-department-of-health-services-disability-rights-wisconsin.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-11_trizetto-cognizant-healthcare-3m.yaml](supply-chain/2024-11_trizetto-cognizant-healthcare-3m.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-06_polyfill-io-cdn-attack.yaml](supply-chain/2024-06_polyfill-io-cdn-attack.yaml) | supply-chain | 2024-06-25 |  |  |
| [2024-06_acadian-ambulance-daixin.yaml](ransomware/2024-06_acadian-ambulance-daixin.yaml) | ransomware | 2024-06-19 | Daixin Team ransomware |  |
| [2024-06_cdk-global.yaml](ransomware/2024-06_cdk-global.yaml) | ransomware | 2024-06-18 | BlackSuit |  |
| [2024-06_globe-life-insurance-extortion.yaml](data-leak/2024-06_globe-life-insurance-extortion.yaml) | data-leak | 2024-06-13 |  |  |
| [2024-06_kadokawa-niconico-blacksuit.yaml](ransomware/2024-06_kadokawa-niconico-blacksuit.yaml) | ransomware | 2024-06-08 | BlackSuit |  |
| [2024-06_rite-aid-ransomhub.yaml](ransomware/2024-06_rite-aid-ransomhub.yaml) | ransomware | 2024-06-06 | RansomHub |  |
| [2024-06_synnovis-nhs.yaml](ransomware/2024-06_synnovis-nhs.yaml) | ransomware | 2024-06-03 | Qilin ransomware |  |
| [2024-06_cbiz-benefits-insurance-breach.yaml](data-leak/2024-06_cbiz-benefits-insurance-breach.yaml) | data-leak | 2024-06-02 |  |  |
| [2024-06_iact-health-advarra.yaml](supply-chain/2024-06_iact-health-advarra.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_king-s-college-hospital-guy-s-hospital-st-thomas-hospital-and-more-synnovis.yaml](supply-chain/2024-06_king-s-college-hospital-guy-s-hospital-st-thomas-hospital-and-more-synnovis.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_adventist-health-tulare-signature-performance.yaml](supply-chain/2024-06_adventist-health-tulare-signature-performance.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_aptihealth-sisense.yaml](supply-chain/2024-06_aptihealth-sisense.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_t-mobile-third-party-vendor.yaml](supply-chain/2024-06_t-mobile-third-party-vendor.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_newton-centre-dental-affinity-dental-management.yaml](supply-chain/2024-06_newton-centre-dental-affinity-dental-management.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_geisinger-nuance-communications.yaml](supply-chain/2024-06_geisinger-nuance-communications.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_tile-life360-extortion.yaml](data-leak/2024-06_tile-life360-extortion.yaml) | data-leak | 2024-06-01 |  |  |
| [2024-06_lithia-motors-sonic-automotive-penske-automotive-group-inc-and-more-cdk-global.yaml](supply-chain/2024-06_lithia-motors-sonic-automotive-penske-automotive-group-inc-and-more-cdk-global.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-05_dmm-bitcoin-tradertraitor.yaml](credential-theft/2024-05_dmm-bitcoin-tradertraitor.yaml) | credential-theft | 2024-05-31 |  |  |
| [2024-05_evolve-bank-lockbit.yaml](ransomware/2024-05_evolve-bank-lockbit.yaml) | ransomware | 2024-05-29 | LockBit ransomware |  |
| [2024-06_patelco-credit-union.yaml](ransomware/2024-06_patelco-credit-union.yaml) | ransomware | 2024-05-23 | RansomHub ransomware |  |
| [2024-05_landmark-admin-insurance.yaml](ransomware/2024-05_landmark-admin-insurance.yaml) | ransomware | 2024-05-13 |  |  |
| [2024-05_ascension-health.yaml](ransomware/2024-05_ascension-health.yaml) | ransomware | 2024-05-08 | Black Basta ransomware |  |
| [2024-05_keytronic-black-basta.yaml](ransomware/2024-05_keytronic-black-basta.yaml) | ransomware | 2024-05-06 | Black Basta ransomware |  |
| [2024-05_hsbc-baton-systems.yaml](supply-chain/2024-05_hsbc-baton-systems.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_medisecure-third-party-vendor.yaml](supply-chain/2024-05_medisecure-third-party-vendor.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_advance-auto-parts-snowflake.yaml](supply-chain/2024-05_advance-auto-parts-snowflake.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_alexion-pharmaceuticals-trade-limited-eclinical-solutions-llc.yaml](supply-chain/2024-05_alexion-pharmaceuticals-trade-limited-eclinical-solutions-llc.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_bym-fashion-lizay-kuyumculuk-aker-magazac-l-k-and-more-tekrom-technology-a-s-t-soft.yaml](supply-chain/2024-05_bym-fashion-lizay-kuyumculuk-aker-magazac-l-k-and-more-tekrom-technology-a-s-t-soft.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_continuum-health-alliance-consensus-medical-group.yaml](supply-chain/2024-05_continuum-health-alliance-consensus-medical-group.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_gerber-life-insurance-webtpa.yaml](supply-chain/2024-05_gerber-life-insurance-webtpa.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_acrotech-biopharma-inc-cencora-inc.yaml](supply-chain/2024-05_acrotech-biopharma-inc-cencora-inc.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-07_snowflake-bausch-health-pharma.yaml](credential-theft/2024-07_snowflake-bausch-health-pharma.yaml) | credential-theft | 2024-05-01 |  |  |
| [2024-06_pure-storage-snowflake.yaml](credential-theft/2024-06_pure-storage-snowflake.yaml) | credential-theft | 2024-05-01 |  |  |
| [2024-05_ticketmaster-snowflake.yaml](supply-chain/2024-05_ticketmaster-snowflake.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_dell-api-scrape.yaml](data-leak/2024-05_dell-api-scrape.yaml) | data-leak | 2024-04-28 |  |  |
| [2024-04_london-drugs-lockbit.yaml](ransomware/2024-04_london-drugs-lockbit.yaml) | ransomware | 2024-04-28 | LockBit ransomware |  |
| [2024-04_dropbox-sign-mfa-seeds.yaml](credential-theft/2024-04_dropbox-sign-mfa-seeds.yaml) | credential-theft | 2024-04-24 |  |  |
| [2024-04_santander-snowflake.yaml](credential-theft/2024-04_santander-snowflake.yaml) | credential-theft | 2024-04-17 |  |  |
| [2024-04_ticketmaster-snowflake.yaml](credential-theft/2024-04_ticketmaster-snowflake.yaml) | credential-theft | 2024-04-14 | VIDAR, RISEPRO, REDLINE, RACO… |  |
| [2024-05_lendingtree-quotewizard-snowflake.yaml](credential-theft/2024-05_lendingtree-quotewizard-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-05_neiman-marcus-snowflake-31m-email.yaml](credential-theft/2024-05_neiman-marcus-snowflake-31m-email.yaml) | credential-theft | 2024-04-14 | VIDAR/RISEPRO/REDLINE infoste… |  |
| [2024-04_att-snowflake.yaml](credential-theft/2024-04_att-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-04_advance-auto-parts-snowflake.yaml](credential-theft/2024-04_advance-auto-parts-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-07_att-snowflake-110million-metadata.yaml](data-leak/2024-07_att-snowflake-110million-metadata.yaml) | data-leak | 2024-04-14 | Lumma/Vidar/RedLine infosteal… |  |
| [2024-04_frontier-communications-ransomhub.yaml](ransomware/2024-04_frontier-communications-ransomhub.yaml) | ransomware | 2024-04-14 | RansomHub |  |
| [2024-04_young-consulting-blacksuit.yaml](ransomware/2024-04_young-consulting-blacksuit.yaml) | ransomware | 2024-04-10 | BlackSuit ransomware |  |
| [2024-04_department-of-justice-greylock-mckinnon-associates.yaml](supply-chain/2024-04_department-of-justice-greylock-mckinnon-associates.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-05_neiman-marcus-snowflake.yaml](credential-theft/2024-05_neiman-marcus-snowflake.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-04_national-public-data.yaml](data-leak/2024-04_national-public-data.yaml) | data-leak | 2024-04-01 |  |  |
| [2024-04_heilbronn-city-library-genios.yaml](supply-chain/2024-04_heilbronn-city-library-genios.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-07_disney-slack-nullbulge.yaml](data-leak/2024-07_disney-slack-nullbulge.yaml) | data-leak | 2024-04-01 |  |  |
| [2024-04_snowflake-customers.yaml](credential-theft/2024-04_snowflake-customers.yaml) | credential-theft | 2024-04-01 | Redline Stealer / Lumma Steal… |  |
| [2024-04_snowflake-cylance-blackberry.yaml](credential-theft/2024-04_snowflake-cylance-blackberry.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-04_amg-healthcare-management-services-marshall-medical-center-south-coast-er-medical-group-and-more-designed-receivable-solution.yaml](supply-chain/2024-04_amg-healthcare-management-services-marshall-medical-center-south-coast-er-medical-group-and-more-designed-receivable-solution.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_d-c-department-of-insurance-securities-and-banking-disb-tyler-technologies.yaml](supply-chain/2024-04_d-c-department-of-insurance-securities-and-banking-disb-tyler-technologies.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_cisco-duo-unknown-telephony-provider.yaml](supply-chain/2024-04_cisco-duo-unknown-telephony-provider.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_medisecure-australia.yaml](ransomware/2024-04_medisecure-australia.yaml) | ransomware | 2024-04-01 |  |  |
| [2024-05_ticketek-australia-teg-cloud.yaml](credential-theft/2024-05_ticketek-australia-teg-cloud.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-04_moffitt-cancer-center-advarra.yaml](supply-chain/2024-04_moffitt-cancer-center-advarra.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_moffitt-cancer-center-gunster-yoakley-and-stewart.yaml](supply-chain/2024-04_moffitt-cancer-center-gunster-yoakley-and-stewart.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_multiple-u-s-agencies-acuity-consulting.yaml](supply-chain/2024-04_multiple-u-s-agencies-acuity-consulting.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_snowflake-unc5537-165-customers.yaml](supply-chain/2024-04_snowflake-unc5537-165-customers.yaml) | credential-theft | 2024-04-01 | Lumma; Vidar; RedLine; RisePr… |  |
| [2024-04_catholic-medical-center-cmc-lamont-hanley-associates.yaml](supply-chain/2024-04_catholic-medical-center-cmc-lamont-hanley-associates.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-06_lausd-snowflake.yaml](credential-theft/2024-06_lausd-snowflake.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-04_palo-alto-pan-os.yaml](other/2024-04_palo-alto-pan-os.yaml) | other | 2024-03-26 | UPSTYLE Python backdoor | CVE-2024-3400 |
| [2024-03_healthequity-vendor-breach.yaml](data-leak/2024-03_healthequity-vendor-breach.yaml) | data-leak | 2024-03-09 |  |  |
| [2024-03_wacks-law-group-qilin.yaml](ransomware/2024-03_wacks-law-group-qilin.yaml) | ransomware | 2024-03-09 | Qilin ransomware |  |
| [2024-03_acuity-federal-contractor-github.yaml](data-leak/2024-03_acuity-federal-contractor-github.yaml) | data-leak | 2024-03-07 |  |  |
| [2024-03_baylor-college-of-medicine-advarra.yaml](supply-chain/2024-03_baylor-college-of-medicine-advarra.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_swiss-goverment-xplain.yaml](supply-chain/2024-03_swiss-goverment-xplain.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_the-hanoi-stock-exchange-hnx-vndirect.yaml](supply-chain/2024-03_the-hanoi-stock-exchange-hnx-vndirect.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-04_roku-credential-stuffing.yaml](credential-theft/2024-04_roku-credential-stuffing.yaml) | credential-theft | 2024-03-01 |  |  |
| [2024-03_fidelity-infosys-mccamish-systems-ims.yaml](supply-chain/2024-03_fidelity-infosys-mccamish-systems-ims.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_university-of-tennessee-health-science-center-kmj-health-solutions.yaml](supply-chain/2024-03_university-of-tennessee-health-science-center-kmj-health-solutions.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_american-express-a-merchant-processor.yaml](supply-chain/2024-03_american-express-a-merchant-processor.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_santa-clarita-community-college-keenan-associates.yaml](supply-chain/2024-03_santa-clarita-community-college-keenan-associates.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_bay-area-anesthesia-bowden-barlow-law-p-a.yaml](supply-chain/2024-03_bay-area-anesthesia-bowden-barlow-law-p-a.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_health-plan-intermediaries-holdings-benefytt-multiplan-inc.yaml](supply-chain/2024-03_health-plan-intermediaries-holdings-benefytt-multiplan-inc.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_mintlify-github-tokens.yaml](supply-chain/2024-03_mintlify-github-tokens.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_virginia-farm-bureau-service-corporation-employee-benefits-corporatio.yaml](supply-chain/2024-03_virginia-farm-bureau-service-corporation-employee-benefits-corporatio.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-02_verisource-hr-benefits-breach.yaml](data-leak/2024-02_verisource-hr-benefits-breach.yaml) | data-leak | 2024-02-27 |  |  |
| [2024-03_xz-utils-backdoor.yaml](supply-chain/2024-03_xz-utils-backdoor.yaml) | supply-chain | 2024-02-24 |  | CVE-2024-3094 |
| [2024-02_cencora-pharma.yaml](data-leak/2024-02_cencora-pharma.yaml) | data-leak | 2024-02-21 |  |  |
| [2024-09_comcast-xfinity-fcc-fine.yaml](data-leak/2024-09_comcast-xfinity-fcc-fine.yaml) | data-leak | 2024-02-14 |  |  |
| [2024-02_fbcs-comcast-truist.yaml](data-leak/2024-02_fbcs-comcast-truist.yaml) | data-leak | 2024-02-14 |  |  |
| [2026-04_iowa-ag-sues-unitedhealth-change-healthcare.yaml](ransomware/2026-04_iowa-ag-sues-unitedhealth-change-healthcare.yaml) | ransomware | 2024-02-12 | ALPHV/BlackCat ransomware (or… |  |
| [2024-02_change-healthcare.yaml](ransomware/2024-02_change-healthcare.yaml) | ransomware | 2024-02-11 | ALPHV/BlackCat |  |
| [2024-02_disa-global-employment-screening.yaml](data-leak/2024-02_disa-global-employment-screening.yaml) | data-leak | 2024-02-09 |  |  |
| [2024-02_prudential-financial.yaml](data-leak/2024-02_prudential-financial.yaml) | data-leak | 2024-02-04 | ALPHV/BlackCat ransomware |  |
| [2024-02_prudential-financial-alphv.yaml](ransomware/2024-02_prudential-financial-alphv.yaml) | ransomware | 2024-02-04 | ALPHV/BlackCat |  |
| [2024-02_rotech-healthcare-philips-respironics.yaml](supply-chain/2024-02_rotech-healthcare-philips-respironics.yaml) | supply-chain | 2024-02-01 |  |  |
| [2025-03_ntt-communications-corporate-customers.yaml](data-leak/2025-03_ntt-communications-corporate-customers.yaml) | data-leak | 2024-02-01 |  |  |
| [2024-02_forward-healthcare-philips-respironics.yaml](supply-chain/2024-02_forward-healthcare-philips-respironics.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_bay-area-heart-center-bowden-barlow-law-p-a.yaml](supply-chain/2024-02_bay-area-heart-center-bowden-barlow-law-p-a.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_hawaii-medical-service-association-hmsa-navvis-company.yaml](supply-chain/2024-02_hawaii-medical-service-association-hmsa-navvis-company.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_the-u-s-government-accountability-office-cgi-federal.yaml](supply-chain/2024-02_the-u-s-government-accountability-office-cgi-federal.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_nabholz-construction-cadence-bank.yaml](supply-chain/2024-02_nabholz-construction-cadence-bank.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_audiens-viamedis.yaml](supply-chain/2024-02_audiens-viamedis.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_prime-healthcare-keenan-associates.yaml](supply-chain/2024-02_prime-healthcare-keenan-associates.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_100-romanian-hospitals-hipocrate-information-system.yaml](supply-chain/2024-02_100-romanian-hospitals-hipocrate-information-system.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_qualcomm-incorporated-unknown-third-party-vendor.yaml](supply-chain/2024-02_qualcomm-incorporated-unknown-third-party-vendor.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-01_lurie-childrens-hospital.yaml](ransomware/2024-01_lurie-childrens-hospital.yaml) | ransomware | 2024-01-26 | Rhysida |  |
| [2024-01_anydesk-source-code-breach.yaml](data-leak/2024-01_anydesk-source-code-breach.yaml) | data-leak | 2024-01-20 |  |  |
| [2024-01_tietoevry-ransomware-swedish-orgs.yaml](supply-chain/2024-01_tietoevry-ransomware-swedish-orgs.yaml) | ransomware | 2024-01-19 | Akira ransomware |  |
| [2024-02_sandworm-texas-water-muleshoe.yaml](other/2024-02_sandworm-texas-water-muleshoe.yaml) | other | 2024-01-18 |  |  |
| [2024-01_trello-api-scrape.yaml](data-leak/2024-01_trello-api-scrape.yaml) | data-leak | 2024-01-16 |  |  |
| [2024-01_loandepot-alphv.yaml](ransomware/2024-01_loandepot-alphv.yaml) | ransomware | 2024-01-04 | ALPHV/BlackCat ransomware |  |
| [2024-01_family-healthcare-brady-martz-associates.yaml](supply-chain/2024-01_family-healthcare-brady-martz-associates.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-12_volkswagen-cariad-aws-location.yaml](data-leak/2024-12_volkswagen-cariad-aws-location.yaml) | data-leak | 2024-01-01 |  |  |
| [2024-01_uppsala-county-tietoevry.yaml](supply-chain/2024-01_uppsala-county-tietoevry.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_tycoon2fa-phishing-as-a-service-aitm.yaml](credential-theft/2024-01_tycoon2fa-phishing-as-a-service-aitm.yaml) | credential-theft | 2024-01-01 | Tycoon2FA phishing kit |  |
| [2024-01_woundcare-innovations-of-golf-land-consensiohealth.yaml](supply-chain/2024-01_woundcare-innovations-of-golf-land-consensiohealth.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_healthcare-vendor-supply-chain-systemic-risk.yaml](other/2024-01_healthcare-vendor-supply-chain-systemic-risk.yaml) | other | 2024-01-01 |  |  |
| [2024-01_upstate-family-health-center-inc-healthec-llc.yaml](supply-chain/2024-01_upstate-family-health-center-inc-healthec-llc.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_primula-tietoevry.yaml](supply-chain/2024-01_primula-tietoevry.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-04_sisense-analytics-cisa-advisory.yaml](other/2024-04_sisense-analytics-cisa-advisory.yaml) | other | 2024-01-01 |  |  |
| [2024-01_meritas-health-corporation-perry-johnson-associates-inc.yaml](supply-chain/2024-01_meritas-health-corporation-perry-johnson-associates-inc.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_us-small-business-administration-orrick-herrington-sutcliffe.yaml](supply-chain/2024-01_us-small-business-administration-orrick-herrington-sutcliffe.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-05_outabox-biometric-australia.yaml](data-leak/2024-05_outabox-biometric-australia.yaml) | data-leak | 2024-01-01 |  |  |
| [2024-01_framework-computer-keating-consulting-group.yaml](supply-chain/2024-01_framework-computer-keating-consulting-group.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_ransomware-law-enforcement-disruption-wave.yaml](other/2024-01_ransomware-law-enforcement-disruption-wave.yaml) | other | 2024-01-01 | LockBit, ALPHV/BlackCat, Hive… |  |
| [2024-01_40-affiliated-nursing-facilities-in-texas-and-kansas-hmg-healthcare.yaml](supply-chain/2024-01_40-affiliated-nursing-facilities-in-texas-and-kansas-hmg-healthcare.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-04_kaiser-permanente-tracker.yaml](data-leak/2024-04_kaiser-permanente-tracker.yaml) | data-leak | 2024-01-01 |  |  |
| [2023-12_anna-jaques-hospital-money-message.yaml](ransomware/2023-12_anna-jaques-hospital-money-message.yaml) | ransomware | 2023-12-25 | Money Message |  |
| [2023-12_first-american-financial-ransomware.yaml](ransomware/2023-12_first-american-financial-ransomware.yaml) | ransomware | 2023-12-20 |  |  |
| [2023-12_st-vincents-health-australia.yaml](data-leak/2023-12_st-vincents-health-australia.yaml) | data-leak | 2023-12-19 |  |  |
| [2023-12_60-credit-unions-trellance.yaml](supply-chain/2023-12_60-credit-unions-trellance.yaml) | supply-chain | 2023-12-01 |  |  |
| [2023-12_valley-health-system-eso-solutions-inc.yaml](supply-chain/2023-12_valley-health-system-eso-solutions-inc.yaml) | supply-chain | 2023-12-01 |  |  |
| [2024-01_ivanti-connect-secure.yaml](other/2024-01_ivanti-connect-secure.yaml) | other | 2023-12-01 | ZIPLINE backdoor / LIGHTWIRE … | CVE-2023-46805, CVE-2024-21887, CVE-202… |
| [2023-12_40-healthcare-companies-asper-biogene.yaml](supply-chain/2023-12_40-healthcare-companies-asper-biogene.yaml) | supply-chain | 2023-12-01 |  |  |
| [2023-11_integris-health.yaml](ransomware/2023-11_integris-health.yaml) | ransomware | 2023-11-28 |  |  |
| [2023-11_geisinger-nuance-insider-breach.yaml](data-leak/2023-11_geisinger-nuance-insider-breach.yaml) | data-leak | 2023-11-27 |  |  |
| [2023-11_iran-irgc-cyberav3ngers-water-utilities.yaml](other/2023-11_iran-irgc-cyberav3ngers-water-utilities.yaml) | other | 2023-11-22 |  | CVE-2023-6448 |
| [2024-01_cloudflare-midnight-blizzard.yaml](credential-theft/2024-01_cloudflare-midnight-blizzard.yaml) | credential-theft | 2023-11-14 |  |  |
| [2023-11_fred-hutch-hunters-intl.yaml](ransomware/2023-11_fred-hutch-hunters-intl.yaml) | ransomware | 2023-11-10 | Hunters International ransomw… |  |
| [2023-11_dp-world-australia-port-attack.yaml](ransomware/2023-11_dp-world-australia-port-attack.yaml) | ransomware | 2023-11-10 |  |  |
| [2023-11_icbc-us-lockbit-treasury.yaml](other/2023-11_icbc-us-lockbit-treasury.yaml) | ransomware | 2023-11-08 | LockBit ransomware | CVE-2023-4966 |
| [2023-11_sumo-logic-aws-access-key.yaml](credential-theft/2023-11_sumo-logic-aws-access-key.yaml) | credential-theft | 2023-11-03 |  |  |
| [2023-11_the-canadian-government-sirva-worldwide-inc.yaml](supply-chain/2023-11_the-canadian-government-sirva-worldwide-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_blue-cross-and-blue-shield-of-minnesota-and-blue-plus-welltok.yaml](supply-chain/2023-11_blue-cross-and-blue-shield-of-minnesota-and-blue-plus-welltok.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_1password-okta.yaml](supply-chain/2023-11_1password-okta.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_northwell-health-perry-johnson-associates-inc.yaml](supply-chain/2023-11_northwell-health-perry-johnson-associates-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_crouse-health-in-syracuse-perry-johnson-associates-inc.yaml](supply-chain/2023-11_crouse-health-in-syracuse-perry-johnson-associates-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_sutter-health-virgin-pulse.yaml](supply-chain/2023-11_sutter-health-virgin-pulse.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_samsung-electronics-unknown.yaml](supply-chain/2023-11_samsung-electronics-unknown.yaml) | supply-chain | 2023-11-01 |  |  |
| [2024-01_microsoft-midnight-blizzard.yaml](credential-theft/2024-01_microsoft-midnight-blizzard.yaml) | credential-theft | 2023-11-01 |  |  |
| [2023-11_dollar-tree-zeroed-in-technologies.yaml](supply-chain/2023-11_dollar-tree-zeroed-in-technologies.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_westat-inc-nuance-communications-inc.yaml](supply-chain/2023-11_westat-inc-nuance-communications-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_taylor-rose-cts.yaml](supply-chain/2023-11_taylor-rose-cts.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_california-physicians-service-d-b-a-blue-shield-of-california-medical-eye-services-inc.yaml](supply-chain/2023-11_california-physicians-service-d-b-a-blue-shield-of-california-medical-eye-services-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-10_infosys-mccamish-lockbit.yaml](supply-chain/2023-10_infosys-mccamish-lockbit.yaml) | supply-chain | 2023-10-29 | LockBit ransomware |  |
| [2024-06_truist-bank-sp1d3r-dark-web.yaml](data-leak/2024-06_truist-bank-sp1d3r-dark-web.yaml) | data-leak | 2023-10-27 |  |  |
| [2023-10_marina-bay-sands-singapore-pdpc.yaml](data-leak/2023-10_marina-bay-sands-singapore-pdpc.yaml) | data-leak | 2023-10-19 |  |  |
| [2023-10_cook-county-health-perry-johnson-associates-inc.yaml](supply-chain/2023-10_cook-county-health-perry-johnson-associates-inc.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_virginia-dept-of-medical-assistance-services-maximus.yaml](supply-chain/2023-10_virginia-dept-of-medical-assistance-services-maximus.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_super-sa-former-external-service-prov.yaml](supply-chain/2023-10_super-sa-former-external-service-prov.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_sony-ipswitch-inc.yaml](supply-chain/2023-10_sony-ipswitch-inc.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_sa-health-personify-care.yaml](supply-chain/2023-10_sa-health-personify-care.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_northstar-anesthesia-arietis-health.yaml](supply-chain/2023-10_northstar-anesthesia-arietis-health.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_humana-inc-pnc-bank.yaml](supply-chain/2023-10_humana-inc-pnc-bank.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_flagstar-bank-fiserv.yaml](supply-chain/2023-10_flagstar-bank-fiserv.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_united-states-department-of-justice-ipswitch-inc.yaml](supply-chain/2023-10_united-states-department-of-justice-ipswitch-inc.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_chatham-kent-health-alliance-transform.yaml](supply-chain/2023-10_chatham-kent-health-alliance-transform.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_boeing-citrixbleed.yaml](ransomware/2023-10_boeing-citrixbleed.yaml) | ransomware | 2023-10-01 | LockBit 3.0 | CVE-2023-4966 |
| [2023-10_arietis-health-ipswitch-inc.yaml](supply-chain/2023-10_arietis-health-ipswitch-inc.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_truist-bank-dark-web.yaml](data-leak/2023-10_truist-bank-dark-web.yaml) | data-leak | 2023-10-01 |  |  |
| [2023-09_mercedes-benz-github-token.yaml](credential-theft/2023-09_mercedes-benz-github-token.yaml) | credential-theft | 2023-09-29 |  |  |
| [2023-09_okta-support-system-breach.yaml](credential-theft/2023-09_okta-support-system-breach.yaml) | credential-theft | 2023-09-28 |  |  |
| [2023-09_johnson-controls-dark-angels.yaml](ransomware/2023-09_johnson-controls-dark-angels.yaml) | ransomware | 2023-09-25 | Dark Angels ransomware |  |
| [2023-09_mgm-resorts.yaml](ransomware/2023-09_mgm-resorts.yaml) | ransomware | 2023-09-08 | ALPHV/BlackCat |  |
| [2023-09_university-of-sydney-unknown.yaml](supply-chain/2023-09_university-of-sydney-unknown.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_airbus-turkish-airlines.yaml](supply-chain/2023-09_airbus-turkish-airlines.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_sutter-north-surgery-center-patients-sightpath-medical.yaml](supply-chain/2023-09_sutter-north-surgery-center-patients-sightpath-medical.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_judiciary-branch-ifx-networks-colombia.yaml](supply-chain/2023-09_judiciary-branch-ifx-networks-colombia.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_ftx-kroll-inc.yaml](supply-chain/2023-09_ftx-kroll-inc.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_born-ontario-ipswitch-inc.yaml](supply-chain/2023-09_born-ontario-ipswitch-inc.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_amerita-pharmerica.yaml](supply-chain/2023-09_amerita-pharmerica.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_890-schools-national-student-clearinghou.yaml](supply-chain/2023-09_890-schools-national-student-clearinghou.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-08_retool-mfa-google-cloud-phishing.yaml](other/2023-08_retool-mfa-google-cloud-phishing.yaml) | other | 2023-08-27 |  |  |
| [2023-08_caesars-entertainment.yaml](ransomware/2023-08_caesars-entertainment.yaml) | ransomware | 2023-08-18 | Scattered Spider ransomware |  |
| [2024-09_slim-cd-payment-processor.yaml](data-leak/2024-09_slim-cd-payment-processor.yaml) | data-leak | 2023-08-17 |  |  |
| [2023-08_clorox-scattered-spider.yaml](ransomware/2023-08_clorox-scattered-spider.yaml) | ransomware | 2023-08-11 | ALPHV/BlackCat ransomware |  |
| [2023-08_rapattoni-mls-ransomware.yaml](ransomware/2023-08_rapattoni-mls-ransomware.yaml) | ransomware | 2023-08-09 |  |  |
| [2023-08_zillow-rapattoni-corporation.yaml](supply-chain/2023-08_zillow-rapattoni-corporation.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_serco-inc-group-health-plan-ipswitch-inc.yaml](supply-chain/2023-08_serco-inc-group-health-plan-ipswitch-inc.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_dagi-clothing-industry-and-trade-as-vodatech-it.yaml](supply-chain/2023-08_dagi-clothing-industry-and-trade-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_child-health-plan-plus-chp-ibm.yaml](supply-chain/2023-08_child-health-plan-plus-chp-ibm.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_be-ikta-sportive-products-industry-and-trade-as-vodatech-it.yaml](supply-chain/2023-08_be-ikta-sportive-products-industry-and-trade-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_automobile-plan-operational-vehicle-rental-trade-vodatech-it.yaml](supply-chain/2023-08_automobile-plan-operational-vehicle-rental-trade-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_agesalife-and-retirement-as-vodatech-it.yaml](supply-chain/2023-08_agesalife-and-retirement-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_yoyo-information-technologies-and-tourism-trade-as-vodatech-it.yaml](supply-chain/2023-08_yoyo-information-technologies-and-tourism-trade-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_ups-cargo-vodatech-it.yaml](supply-chain/2023-08_ups-cargo-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_eversource-energy-clearesult.yaml](supply-chain/2023-08_eversource-energy-clearesult.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_puma-sportswear-industry-and-trade-vodatech-it.yaml](supply-chain/2023-08_puma-sportswear-industry-and-trade-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_nuance-communications-ipswitch-inc.yaml](supply-chain/2023-08_nuance-communications-ipswitch-inc.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_janssen-healthcare-platform-ibm.yaml](supply-chain/2023-08_janssen-healthcare-platform-ibm.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_gulf-insurance-as-vodatech-it.yaml](supply-chain/2023-08_gulf-insurance-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_do-an-trend-automotive-trade-service-and-technology-joint-stock-company-vodatech-it.yaml](supply-chain/2023-08_do-an-trend-automotive-trade-service-and-technology-joint-stock-company-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_derimod-leather-garment-marketing-industry-and-trade-as-vodatech-it.yaml](supply-chain/2023-08_derimod-leather-garment-marketing-industry-and-trade-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-07_hca-healthcare-11m-patients.yaml](data-leak/2023-07_hca-healthcare-11m-patients.yaml) | data-leak | 2023-07-05 |  |  |
| [2023-07_vodafone-turkey-mivento-it-services.yaml](supply-chain/2023-07_vodafone-turkey-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_vestel-mivento-it-services.yaml](supply-chain/2023-07_vestel-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_anadolu-isuzu-automotive-industry-and-trade-inc-mivento-it-services.yaml](supply-chain/2023-07_anadolu-isuzu-automotive-industry-and-trade-inc-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_blue-cross-blue-shield-of-arizona-az-blue-cognizant-technology-solutio.yaml](supply-chain/2023-07_blue-cross-blue-shield-of-arizona-az-blue-cognizant-technology-solutio.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_dymocks-australia-836k.yaml](data-leak/2023-07_dymocks-australia-836k.yaml) | data-leak | 2023-07-01 |  |  |
| [2023-07_toyota-turkey-marketing-and-sales-joint-stock-company-mivento-it-services.yaml](supply-chain/2023-07_toyota-turkey-marketing-and-sales-joint-stock-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_schneider-electric-industry-and-trade-joint-stock-company-mivento-it-services.yaml](supply-chain/2023-07_schneider-electric-industry-and-trade-joint-stock-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_postbank-majorel.yaml](supply-chain/2023-07_postbank-majorel.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_mais-motor-vehicles-manufacturing-and-sales-joint-stock-company-mivento-it-services.yaml](supply-chain/2023-07_mais-motor-vehicles-manufacturing-and-sales-joint-stock-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_lenders-choice-escrow-cashcall-inc.yaml](supply-chain/2023-07_lenders-choice-escrow-cashcall-inc.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_henrietta-johnson-medical-center-delaware-health-network.yaml](supply-chain/2023-07_henrietta-johnson-medical-center-delaware-health-network.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_celik-motor-trade-joint-stock-company-mivento-it-services.yaml](supply-chain/2023-07_celik-motor-trade-joint-stock-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_geberit-installation-systems-trade-limited-company-mivento-it-services.yaml](supply-chain/2023-07_geberit-installation-systems-trade-limited-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-06_vecino-health-centers-tx-ipswitch-inc.yaml](supply-chain/2023-06_vecino-health-centers-tx-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_intellihartx-llc-goanywhere-mft.yaml](supply-chain/2023-06_intellihartx-llc-goanywhere-mft.yaml) | supply-chain | 2023-06-01 |  |  |
| [2024-02_flax-typhoon-taiwan-botnet.yaml](other/2024-02_flax-typhoon-taiwan-botnet.yaml) | other | 2023-06-01 | Flax Typhoon botnet (Raptor T… |  |
| [2023-06_australian-information-commissioner-oaic-hwl-ebsworth-lawyers.yaml](supply-chain/2023-06_australian-information-commissioner-oaic-hwl-ebsworth-lawyers.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_calpers-california-public-employees-retirement-system-pbi-research-services-pbi.yaml](supply-chain/2023-06_calpers-california-public-employees-retirement-system-pbi-research-services-pbi.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_coxhealth-intellihartx-llc.yaml](supply-chain/2023-06_coxhealth-intellihartx-llc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_dhl-ipswitch-inc.yaml](supply-chain/2023-06_dhl-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_dublin-airport-aon.yaml](supply-chain/2023-06_dublin-airport-aon.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_exeter-finance-ncb-management-services-inc.yaml](supply-chain/2023-06_exeter-finance-ncb-management-services-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_tj-maxx-ipswitch-inc.yaml](supply-chain/2023-06_tj-maxx-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_majorel-ipswitch-inc.yaml](supply-chain/2023-06_majorel-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_oregon-driver-motor-vehicle-services-ipswitch-inc.yaml](supply-chain/2023-06_oregon-driver-motor-vehicle-services-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_pbi-research-services-pbi-ipswitch-inc.yaml](supply-chain/2023-06_pbi-research-services-pbi-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_southwest-airlines-pilot-credentials.yaml](supply-chain/2023-06_southwest-airlines-pilot-credentials.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_the-new-york-city-department-of-education-nyc-doe-ipswitch-inc.yaml](supply-chain/2023-06_the-new-york-city-department-of-education-nyc-doe-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-05_moveit-transfer-clop.yaml](supply-chain/2023-05_moveit-transfer-clop.yaml) | supply-chain | 2023-05-27 | LEMURLOOT web shell | CVE-2023-34362, CVE-2023-35708 |
| [2023-05_welltok-moveit-8-5m-patients.yaml](supply-chain/2023-05_welltok-moveit-8-5m-patients.yaml) | supply-chain | 2023-05-27 | Cl0p ransomware | CVE-2023-34362 |
| [2023-07_moveit-maximus.yaml](supply-chain/2023-07_moveit-maximus.yaml) | supply-chain | 2023-05-27 | LEMURLOOT web shell | CVE-2023-34362 |
| [2023-05_storm-0558-microsoft-exchange.yaml](other/2023-05_storm-0558-microsoft-exchange.yaml) | other | 2023-05-15 |  |  |
| [2023-05_fermanagh-and-omagh-district-council-evide-impact-limited.yaml](supply-chain/2023-05_fermanagh-and-omagh-district-council-evide-impact-limited.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_paramount-health-care-nationsbenefits-holding-llc.yaml](supply-chain/2023-05_paramount-health-care-nationsbenefits-holding-llc.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_vcu-health-system-credit-control-corporation.yaml](supply-chain/2023-05_vcu-health-system-credit-control-corporation.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_webster-bank-guardian-analytics-inc.yaml](supply-chain/2023-05_webster-bank-guardian-analytics-inc.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_whitman-college-brightline-health.yaml](supply-chain/2023-05_whitman-college-brightline-health.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_coles-latitude-financial-services.yaml](supply-chain/2023-05_coles-latitude-financial-services.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_cornerstone-home-lending-unknown.yaml](supply-chain/2023-05_cornerstone-home-lending-unknown.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_south-baldwin-regional-medical-center-community-health-systems.yaml](supply-chain/2023-05_south-baldwin-regional-medical-center-community-health-systems.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_queensway-carleton-hospital-aetonix-systems-inc.yaml](supply-chain/2023-05_queensway-carleton-hospital-aetonix-systems-inc.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_medicare-medicaid-services-cms-palmetto-gba.yaml](supply-chain/2023-05_medicare-medicaid-services-cms-palmetto-gba.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_discord-zendesk.yaml](supply-chain/2023-05_discord-zendesk.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_stanford-university-brightline-health.yaml](supply-chain/2023-05_stanford-university-brightline-health.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_intel-micro-star-international-msi.yaml](supply-chain/2023-05_intel-micro-star-international-msi.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_kibble-equipment-razor-consulting-solutions.yaml](supply-chain/2023-05_kibble-equipment-razor-consulting-solutions.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_iowa-medicaid-telligen-inc.yaml](supply-chain/2023-05_iowa-medicaid-telligen-inc.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-10_23andme-credential-stuffing.yaml](data-leak/2023-10_23andme-credential-stuffing.yaml) | credential-theft | 2023-04-29 |  |  |
| [2023-04_hwl-ebsworth-alphv-blackcat.yaml](ransomware/2023-04_hwl-ebsworth-alphv-blackcat.yaml) | ransomware | 2023-04-28 | ALPHV/BlackCat ransomware |  |
| [2024-04_webtpa-health-insurance.yaml](data-leak/2024-04_webtpa-health-insurance.yaml) | data-leak | 2023-04-18 |  |  |
| [2023-04_ncb-management-services.yaml](data-leak/2023-04_ncb-management-services.yaml) | data-leak | 2023-04-04 |  |  |
| [2023-04_brightline-health-goanywhere-mft.yaml](supply-chain/2023-04_brightline-health-goanywhere-mft.yaml) | supply-chain | 2023-04-01 |  |  |
| [2023-04_nationsbenefits-holding-llc-goanywhere-mft.yaml](supply-chain/2023-04_nationsbenefits-holding-llc-goanywhere-mft.yaml) | supply-chain | 2023-04-01 |  |  |
| [2023-04_santa-clara-family-health-plan-goanywhere-mft.yaml](supply-chain/2023-04_santa-clara-family-health-plan-goanywhere-mft.yaml) | supply-chain | 2023-04-01 |  |  |
| [2023-04_iowa-department-of-health-and-human-services-iowa-medicaid-enterprise-iowa-hhs-ime-independent-living-systems.yaml](supply-chain/2023-04_iowa-department-of-health-and-human-services-iowa-medicaid-enterprise-iowa-hhs-ime-independent-living-systems.yaml) | supply-chain | 2023-04-01 |  |  |
| [2023-02_pja-concentra-healthcare.yaml](data-leak/2023-02_pja-concentra-healthcare.yaml) | data-leak | 2023-03-27 |  |  |
| [2023-03_capita-black-basta.yaml](ransomware/2023-03_capita-black-basta.yaml) | ransomware | 2023-03-22 | Black Basta ransomware |  |
| [2023-03_3cx-desktop-app.yaml](supply-chain/2023-03_3cx-desktop-app.yaml) | supply-chain | 2023-03-16 | SUDDENICON downloader / ICONI… | CVE-2023-29059 |
| [2023-03_latitude-financial.yaml](data-leak/2023-03_latitude-financial.yaml) | data-leak | 2023-03-16 |  |  |
| [2023-03_pharmerica-money-message.yaml](ransomware/2023-03_pharmerica-money-message.yaml) | ransomware | 2023-03-12 | Money Message ransomware |  |
| [2023-03_dc-health-link-congress-breach.yaml](data-leak/2023-03_dc-health-link-congress-breach.yaml) | data-leak | 2023-03-08 |  |  |
| [2023-03_national-basketball-association-unknown.yaml](supply-chain/2023-03_national-basketball-association-unknown.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_ferrari-customer-data-breach.yaml](data-leak/2023-03_ferrari-customer-data-breach.yaml) | data-leak | 2023-03-01 |  |  |
| [2023-03_at-t-unknown.yaml](supply-chain/2023-03_at-t-unknown.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_blue-shield-of-california-goanywhere-mft.yaml](supply-chain/2023-03_blue-shield-of-california-goanywhere-mft.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_cornell-university-ithaca-college-virginia-tech-university-suny-oswego-colorado-state-university-loyola-university-chicago-and-mcmaster-university-audienceview.yaml](supply-chain/2023-03_cornell-university-ithaca-college-virginia-tech-university-suny-oswego-colorado-state-university-loyola-university-chicago-and-mcmaster-university-audienceview.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_hatch-bank-goanywhere-mft.yaml](supply-chain/2023-03_hatch-bank-goanywhere-mft.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_spacex-maximum-industries.yaml](supply-chain/2023-03_spacex-maximum-industries.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_netherlands-enterprise-agency-rvo-nebu-bv.yaml](supply-chain/2023-03_netherlands-enterprise-agency-rvo-nebu-bv.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_uber-genova-burns.yaml](supply-chain/2023-03_uber-genova-burns.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_orrick-herrington-law-firm.yaml](data-leak/2023-03_orrick-herrington-law-firm.yaml) | data-leak | 2023-02-28 | SilentRansom/Luna Moth |  |
| [2023-02_dish-network-black-basta.yaml](ransomware/2023-02_dish-network-black-basta.yaml) | ransomware | 2023-02-23 | Black Basta ransomware |  |
| [2023-02_reddit-blackcat.yaml](data-leak/2023-02_reddit-blackcat.yaml) | data-leak | 2023-02-05 |  |  |
| [2023-02_applied-materials-rise-interactive.yaml](supply-chain/2023-02_applied-materials-rise-interactive.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_atlassian-envoy.yaml](supply-chain/2023-02_atlassian-envoy.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_boost-mobile-dish-network-corporation.yaml](supply-chain/2023-02_boost-mobile-dish-network-corporation.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_community-health-systems-goanywhere-mft.yaml](supply-chain/2023-02_community-health-systems-goanywhere-mft.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_sharp-healthcare-unknown.yaml](supply-chain/2023-02_sharp-healthcare-unknown.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_sling-tv-dish-network-corporation.yaml](supply-chain/2023-02_sling-tv-dish-network-corporation.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_volt-typhoon-lelwd-utility.yaml](other/2023-02_volt-typhoon-lelwd-utility.yaml) | other | 2023-02-01 |  |  |
| [2023-01_goanywhere-clop.yaml](supply-chain/2023-01_goanywhere-clop.yaml) | supply-chain | 2023-01-18 |  | CVE-2023-0669 |
| [2023-01_western-sydney-uni-m365.yaml](data-leak/2023-01_western-sydney-uni-m365.yaml) | data-leak | 2023-01-17 |  |  |
| [2023-01_royal-mail-lockbit.yaml](ransomware/2023-01_royal-mail-lockbit.yaml) | ransomware | 2023-01-10 | LockBit 3.0 |  |
| [2023-03_forever21-employee-breach.yaml](data-leak/2023-03_forever21-employee-breach.yaml) | data-leak | 2023-01-05 |  |  |
| [2023-01_datadog-circleci.yaml](supply-chain/2023-01_datadog-circleci.yaml) | supply-chain | 2023-01-01 |  |  |
| [2024-10_salt-typhoon-telecoms.yaml](other/2024-10_salt-typhoon-telecoms.yaml) | other | 2023-01-01 |  |  |
| [2023-01_fanduels-mailchimp.yaml](supply-chain/2023-01_fanduels-mailchimp.yaml) | supply-chain | 2023-01-01 |  |  |
| [2023-01_klm-flying-blue.yaml](supply-chain/2023-01_klm-flying-blue.yaml) | supply-chain | 2023-01-01 |  |  |
| [2023-01_nissan-north-america-unknown.yaml](supply-chain/2023-01_nissan-north-america-unknown.yaml) | supply-chain | 2023-01-01 |  |  |
| [2023-01_solana-foundation-mailchimp.yaml](supply-chain/2023-01_solana-foundation-mailchimp.yaml) | supply-chain | 2023-01-01 |  |  |
| [2023-01_university-of-colorado-hospital-authority-diligent-corporation.yaml](supply-chain/2023-01_university-of-colorado-hospital-authority-diligent-corporation.yaml) | supply-chain | 2023-01-01 |  |  |
| [2024-10_salt-typhoon-lumen-verizon-att-telecom.yaml](other/2024-10_salt-typhoon-lumen-verizon-att-telecom.yaml) | other | 2023-01-01 | Demodex (kernel-mode rootkit) |  |
| [2024-08_toyota-240gb-dark-web.yaml](data-leak/2024-08_toyota-240gb-dark-web.yaml) | data-leak | 2022-12-25 |  |  |
| [2022-12_circleci-secrets-breach.yaml](credential-theft/2022-12_circleci-secrets-breach.yaml) | credential-theft | 2022-12-16 |  |  |
| [2022-12_rackspace-play-ransomware.yaml](ransomware/2022-12_rackspace-play-ransomware.yaml) | ransomware | 2022-12-02 | Play ransomware | CVE-2022-41080, CVE-2022-41082 |
| [2023-01_commuteair-jenkins-aws-s3.yaml](credential-theft/2023-01_commuteair-jenkins-aws-s3.yaml) | credential-theft | 2022-12-01 |  |  |
| [2022-12_st-luke-s-health-adelanto-healthcare-ventures.yaml](supply-chain/2022-12_st-luke-s-health-adelanto-healthcare-ventures.yaml) | supply-chain | 2022-12-01 |  |  |
| [2022-12_sobeys-empire-co.yaml](supply-chain/2022-12_sobeys-empire-co.yaml) | supply-chain | 2022-12-01 |  |  |
| [2022-11_lastpass-devops-keylogger.yaml](credential-theft/2022-11_lastpass-devops-keylogger.yaml) | credential-theft | 2022-11-30 | Keylogger (via vulnerable Ple… |  |
| [2023-01_t-mobile-api.yaml](data-leak/2023-01_t-mobile-api.yaml) | data-leak | 2022-11-25 |  |  |
| [2022-11_ftx-aws-secrets-compromise.yaml](credential-theft/2022-11_ftx-aws-secrets-compromise.yaml) | credential-theft | 2022-11-11 |  |  |
| [2022-10_advocate-aurora-health-meta-pixel.yaml](supply-chain/2022-10_advocate-aurora-health-meta-pixel.yaml) | data-leak | 2022-10-14 |  |  |
| [2022-10_mydeal-australia-2-2m.yaml](credential-theft/2022-10_mydeal-australia-2-2m.yaml) | credential-theft | 2022-10-09 |  |  |
| [2022-10_commonspirit-health-hive.yaml](ransomware/2022-10_commonspirit-health-hive.yaml) | ransomware | 2022-10-03 | Hive ransomware |  |
| [2022-10_somnia-pain-management-of-kentucky-not-disclosed.yaml](supply-chain/2022-10_somnia-pain-management-of-kentucky-not-disclosed.yaml) | supply-chain | 2022-10-01 |  |  |
| [2022-10_barracuda-esg-cve-2023-2868.yaml](supply-chain/2022-10_barracuda-esg-cve-2023-2868.yaml) | supply-chain | 2022-10-01 | SALTWATER, SEASPY, SEASIDE, S… | CVE-2023-2868 |
| [2022-09_optus.yaml](data-leak/2022-09_optus.yaml) | data-leak | 2022-09-19 |  |  |
| [2022-09_rockstar-games-gta6-leak.yaml](data-leak/2022-09_rockstar-games-gta6-leak.yaml) | data-leak | 2022-09-17 |  |  |
| [2022-09_uber-mfa-fatigue.yaml](credential-theft/2022-09_uber-mfa-fatigue.yaml) | credential-theft | 2022-09-15 |  |  |
| [2022-09_revolut-social-engineering.yaml](credential-theft/2022-09_revolut-social-engineering.yaml) | credential-theft | 2022-09-11 |  |  |
| [2022-09_lausd-vice-society.yaml](ransomware/2022-09_lausd-vice-society.yaml) | ransomware | 2022-09-03 | Vice Society ransomware |  |
| [2022-09_magento-fishpig.yaml](supply-chain/2022-09_magento-fishpig.yaml) | supply-chain | 2022-09-01 |  |  |
| [2022-09_anthem-mainehealth-alight-com-choice-health-pre.yaml](supply-chain/2022-09_anthem-mainehealth-alight-com-choice-health-pre.yaml) | supply-chain | 2022-09-01 |  |  |
| [2022-09_humana-alight-com-choice-health-pre.yaml](supply-chain/2022-09_humana-alight-com-choice-health-pre.yaml) | supply-chain | 2022-09-01 |  |  |
| [2022-10_medibank.yaml](ransomware/2022-10_medibank.yaml) | ransomware | 2022-08-25 | BlogXX / REvil variant |  |
| [2022-08_plex-15m-user-breach.yaml](data-leak/2022-08_plex-15m-user-breach.yaml) | data-leak | 2022-08-23 |  |  |
| [2022-08_lastpass.yaml](data-leak/2022-08_lastpass.yaml) | data-leak | 2022-08-08 |  | CVE-2020-5741 |
| [2022-08_signal-twilio.yaml](supply-chain/2022-08_signal-twilio.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_syracuse-pediatrics-tully-physical-therapy-st-joseph-s-medical-salvation-army-and-24-organizations-practice-resources-llc.yaml](supply-chain/2022-08_syracuse-pediatrics-tully-physical-therapy-st-joseph-s-medical-salvation-army-and-24-organizations-practice-resources-llc.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_sturm-ruger-company-freestyle-solutions.yaml](supply-chain/2022-08_sturm-ruger-company-freestyle-solutions.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_orange-business-services-orange-silicon-valley.yaml](supply-chain/2022-08_orange-business-services-orange-silicon-valley.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_nhs-advanced.yaml](supply-chain/2022-08_nhs-advanced.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_municipalities-of-eijsden-margraten-gulpen-wittem-kerkrade-meerssen-and-vaals-not-disclosed.yaml](supply-chain/2022-08_municipalities-of-eijsden-margraten-gulpen-wittem-kerkrade-meerssen-and-vaals-not-disclosed.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_lee-county-emergency-medical-services-intermedix-corporation.yaml](supply-chain/2022-08_lee-county-emergency-medical-services-intermedix-corporation.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_lastpass-doordash-okta-and-authy-twilio.yaml](supply-chain/2022-08_lastpass-doordash-okta-and-authy-twilio.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_kiplepay-sdn-bhd-not-disclosed.yaml](supply-chain/2022-08_kiplepay-sdn-bhd-not-disclosed.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_digitalocean-edge-messari-decrypt-mailchimp.yaml](supply-chain/2022-08_digitalocean-edge-messari-decrypt-mailchimp.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_anesthesia-associates-of-el-paso-pa-not-disclosed.yaml](supply-chain/2022-08_anesthesia-associates-of-el-paso-pa-not-disclosed.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-07_rogers-communications-network-outage.yaml](other/2022-07_rogers-communications-network-outage.yaml) | other | 2022-07-08 |  |  |
| [2022-07_mid-westchester-anesthesia-services-not-disclosed.yaml](supply-chain/2022-07_mid-westchester-anesthesia-services-not-disclosed.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_toronto-symphony-orchestra-wordfly.yaml](supply-chain/2022-07_toronto-symphony-orchestra-wordfly.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_american-health-imaging-banner-medical-group-belle-point-dental-duck-creek-family-dental-partners-in-periodontics-and-652-organizations-professional-finance-company.yaml](supply-chain/2022-07_american-health-imaging-banner-medical-group-belle-point-dental-duck-creek-family-dental-partners-in-periodontics-and-652-organizations-professional-finance-company.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_arlington-skin-virtual-private-network-solu.yaml](supply-chain/2022-07_arlington-skin-virtual-private-network-solu.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_boeing-employees-credit-union-not-disclosed.yaml](supply-chain/2022-07_boeing-employees-credit-union-not-disclosed.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_celsius-customer-io.yaml](supply-chain/2022-07_celsius-customer-io.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_edfinancial-and-oklahoma-student-loan-authority-nelnet-servicing.yaml](supply-chain/2022-07_edfinancial-and-oklahoma-student-loan-authority-nelnet-servicing.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_sound-health-and-wellness-trust-zenith-american-solutions.yaml](supply-chain/2022-07_sound-health-and-wellness-trust-zenith-american-solutions.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-06_baptist-health-system-resolute-health-hospital-the-hospitals-of-providence-memorial-campus-valley-baptist-medical-center-brownsville-valley-baptist-medical-center-harlingen-conifer-revenue-cycle-soluti.yaml](supply-chain/2022-06_baptist-health-system-resolute-health-hospital-the-hospitals-of-providence-memorial-campus-valley-baptist-medical-center-brownsville-valley-baptist-medical-center-harlingen-conifer-revenue-cycle-soluti.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-06_priority-health-warner-norcross-judd.yaml](supply-chain/2022-06_priority-health-warner-norcross-judd.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-08_twilio-0ktapus.yaml](credential-theft/2022-08_twilio-0ktapus.yaml) | credential-theft | 2022-06-01 |  |  |
| [2022-06_marriott-social-engineering-20gb.yaml](credential-theft/2022-06_marriott-social-engineering-20gb.yaml) | credential-theft | 2022-06-01 |  |  |
| [2022-06_blue-cross-and-blue-shield-of-massachusetts-lifeworks-us.yaml](supply-chain/2022-06_blue-cross-and-blue-shield-of-massachusetts-lifeworks-us.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-06_burman-zuckerbrod-ophthalmology-associates-fishman-vision-eyecare-leaders.yaml](supply-chain/2022-06_burman-zuckerbrod-ophthalmology-associates-fishman-vision-eyecare-leaders.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-06_colorado-springs-utilities-not-disclosed.yaml](supply-chain/2022-06_colorado-springs-utilities-not-disclosed.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-06_opensea-customer-io.yaml](supply-chain/2022-06_opensea-customer-io.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-05_cisco-yanluowang-mfa-fatigue.yaml](credential-theft/2022-05_cisco-yanluowang-mfa-fatigue.yaml) | credential-theft | 2022-05-24 |  |  |
| [2022-05_hospitals-in-northern-california-partnership-healthplan-of-ca.yaml](supply-chain/2022-05_hospitals-in-northern-california-partnership-healthplan-of-ca.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-05_st-luke-s-kaye-smith.yaml](supply-chain/2022-05_st-luke-s-kaye-smith.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-05_evergreenhealth-mycare.yaml](supply-chain/2022-05_evergreenhealth-mycare.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-05_k12-schools-in-ny-illuminate-education.yaml](supply-chain/2022-05_k12-schools-in-ny-illuminate-education.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-05_mangatoon-elasticsearch.yaml](supply-chain/2022-05_mangatoon-elasticsearch.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-04_heroku-travis-oauth-token-theft.yaml](supply-chain/2022-04_heroku-travis-oauth-token-theft.yaml) | supply-chain | 2022-04-07 |  |  |
| [2022-04_blue-cross-blue-shield-of-arizona-clover-health-kaiser-permanente-point32health-upmc-health-plan-and-33-healthcare-organizations-onetouchpoint.yaml](supply-chain/2022-04_blue-cross-blue-shield-of-arizona-clover-health-kaiser-permanente-point32health-upmc-health-plan-and-33-healthcare-organizations-onetouchpoint.yaml) | supply-chain | 2022-04-01 |  |  |
| [2022-04_sunwing-airlines-airline-choice.yaml](supply-chain/2022-04_sunwing-airlines-airline-choice.yaml) | supply-chain | 2022-04-01 |  |  |
| [2022-04_dis-chem-not-disclosed.yaml](supply-chain/2022-04_dis-chem-not-disclosed.yaml) | supply-chain | 2022-04-01 |  |  |
| [2022-03_mcg-health-1-1m-patients.yaml](supply-chain/2022-03_mcg-health-1-1m-patients.yaml) | data-leak | 2022-03-25 |  |  |
| [2022-03_samsung-lapsus.yaml](data-leak/2022-03_samsung-lapsus.yaml) | data-leak | 2022-03-04 |  |  |
| [2022-03_samsung-qualcomm-nvidia.yaml](supply-chain/2022-03_samsung-qualcomm-nvidia.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_acro-not-disclosed.yaml](supply-chain/2022-03_acro-not-disclosed.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_oklahoma-s-department-of-human-services-okdhs-liberty-of-oklahoma.yaml](supply-chain/2022-03_oklahoma-s-department-of-human-services-okdhs-liberty-of-oklahoma.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_highmark-quantum-group.yaml](supply-chain/2022-03_highmark-quantum-group.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_datahealth-not-disclosed.yaml](supply-chain/2022-03_datahealth-not-disclosed.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_unc-lenoir-health-care-avera-health-chi-health-phelps-health-and-4-organizations-mcg-health.yaml](supply-chain/2022-03_unc-lenoir-health-care-avera-health-chi-health-phelps-health-and-4-organizations-mcg-health.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_okta-sykes-enterprises.yaml](supply-chain/2022-03_okta-sykes-enterprises.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_rennline-freestyle-solutions.yaml](supply-chain/2022-03_rennline-freestyle-solutions.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_central-maine-medical-center-shields-health-care-group-in.yaml](supply-chain/2022-03_central-maine-medical-center-shields-health-care-group-in.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-02_cyberattacks-modern-armed-conflicts.yaml](other/2022-02_cyberattacks-modern-armed-conflicts.yaml) | other | 2022-02-24 | HermeticWiper, WhisperGate, C… | CVE-2022-24521 |
| [2022-02_nvidia-lapsus.yaml](data-leak/2022-02_nvidia-lapsus.yaml) | data-leak | 2022-02-23 |  |  |
| [2022-02_internet-society-not-disclosed.yaml](supply-chain/2022-02_internet-society-not-disclosed.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-02_memorial-health-system-advent-health-partners.yaml](supply-chain/2022-02_memorial-health-system-advent-health-partners.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-02_not-disclosed-comprehensive-health-service.yaml](supply-chain/2022-02_not-disclosed-comprehensive-health-service.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-02_oklahoma-city-police-department-dna-solutions-inc.yaml](supply-chain/2022-02_oklahoma-city-police-department-dna-solutions-inc.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-02_australian-clinical-labs-medlab.yaml](data-leak/2022-02_australian-clinical-labs-medlab.yaml) | ransomware | 2022-02-01 |  |  |
| [2022-02_fortune-500-companies-morley-companies.yaml](supply-chain/2022-02_fortune-500-companies-morley-companies.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-01_red-cross-icrc-515k-vulnerable.yaml](data-leak/2022-01_red-cross-icrc-515k-vulnerable.yaml) | data-leak | 2022-01-18 | BEACON, GLASSTOKEN (custom ma… | CVE-2021-40539 |
| [2022-01_okta-lapsus.yaml](credential-theft/2022-01_okta-lapsus.yaml) | credential-theft | 2022-01-16 | Mimikatz |  |
| [2022-01_baptist-memorial-health-care-butler-health-systems-children-s-healthcare-of-atlanta-hoag-health-system-and-28-organizations-ciox-health.yaml](supply-chain/2022-01_baptist-memorial-health-care-butler-health-systems-children-s-healthcare-of-atlanta-hoag-health-system-and-28-organizations-ciox-health.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-01_red-cross-not-disclosed.yaml](supply-chain/2022-01_red-cross-not-disclosed.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-01_government-of-south-australia-frontier-software.yaml](supply-chain/2022-01_government-of-south-australia-frontier-software.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-01_good-samaritan-society-mission-healthcare-at-renton-prestige-care-rockwood-south-hill-kin-on-health-care-center-and-63-organizations-infinity-rehab.yaml](supply-chain/2022-01_good-samaritan-society-mission-healthcare-at-renton-prestige-care-rockwood-south-hill-kin-on-health-care-center-and-63-organizations-infinity-rehab.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-01_entira-family-clinics-netgain.yaml](supply-chain/2022-01_entira-family-clinics-netgain.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-11_whatsapp-487m-phone-scrape.yaml](data-leak/2022-11_whatsapp-487m-phone-scrape.yaml) | data-leak | 2022-01-01 |  |  |
| [2022-01_a-one-home-health-services-bend-transitional-care-infinity-rehab-salem-transitional-care-the-arbor-at-avamere-court-and-75-organizations-avamere-health-services.yaml](supply-chain/2022-01_a-one-home-health-services-bend-transitional-care-infinity-rehab-salem-transitional-care-the-arbor-at-avamere-court-and-75-organizations-avamere-health-services.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-01_pegasus-airlines-s3-65tb.yaml](data-leak/2022-01_pegasus-airlines-s3-65tb.yaml) | data-leak | 2022-01-01 |  |  |
| [2022-10_football-australia-aws-s3-keys.yaml](credential-theft/2022-10_football-australia-aws-s3-keys.yaml) | credential-theft | 2022-01-01 |  |  |
| [2021-12_ukg-kronos-ransomware.yaml](ransomware/2021-12_ukg-kronos-ransomware.yaml) | ransomware | 2021-12-11 |  |  |
| [2021-12_cash-app-former-employee.yaml](data-leak/2021-12_cash-app-former-employee.yaml) | data-leak | 2021-12-10 |  |  |
| [2021-12_eye-care-leaders-ehr-3-6m.yaml](ransomware/2021-12_eye-care-leaders-ehr-3-6m.yaml) | ransomware | 2021-12-04 |  |  |
| [2021-12_twitter-api-5-4m-scrape.yaml](data-leak/2021-12_twitter-api-5-4m-scrape.yaml) | data-leak | 2021-12-01 |  |  |
| [2021-12_log4shell.yaml](other/2021-12_log4shell.yaml) | other | 2021-12-01 | Conti (ransomware), various c… | CVE-2021-44228, CVE-2021-45046, CVE-202… |
| [2021-11_qrs-clients-qrs.yaml](supply-chain/2021-11_qrs-clients-qrs.yaml) | supply-chain | 2021-11-01 |  |  |
| [2021-11_uber-eats-third-party-820k.yaml](supply-chain/2021-11_uber-eats-third-party-820k.yaml) | supply-chain | 2021-11-01 |  |  |
| [2021-10_twitch-source-code-leak.yaml](data-leak/2021-10_twitch-source-code-leak.yaml) | data-leak | 2021-10-06 |  |  |
| [2021-10_fullerton-health-agape-connecting-people.yaml](supply-chain/2021-10_fullerton-health-agape-connecting-people.yaml) | supply-chain | 2021-10-01 |  |  |
| [2021-10_anthem-humana-practicemax.yaml](supply-chain/2021-10_anthem-humana-practicemax.yaml) | supply-chain | 2021-10-01 |  |  |
| [2021-10_durham-regional-government-not-disclosed.yaml](supply-chain/2021-10_durham-regional-government-not-disclosed.yaml) | supply-chain | 2021-10-01 |  |  |
| [2021-09_ambulance-victoria-2241-staff.yaml](data-leak/2021-09_ambulance-victoria-2241-staff.yaml) | data-leak | 2021-09-07 |  |  |
| [2021-09_godaddy-wordpress-1-2m.yaml](data-leak/2021-09_godaddy-wordpress-1-2m.yaml) | data-leak | 2021-09-06 |  |  |
| [2021-09_nrs-dotty-s.yaml](supply-chain/2021-09_nrs-dotty-s.yaml) | supply-chain | 2021-09-01 |  |  |
| [2021-08_apria-healthcare-1-87m.yaml](data-leak/2021-08_apria-healthcare-1-87m.yaml) | data-leak | 2021-08-22 |  |  |
| [2021-08_microsoft-exchange-proxyshell.yaml](other/2021-08_microsoft-exchange-proxyshell.yaml) | other | 2021-08-13 | LockFile ransomware, Babuk ra… | CVE-2021-34473, CVE-2021-34523, CVE-202… |
| [2021-08_azure-cosmos-db-chaosdb.yaml](other/2021-08_azure-cosmos-db-chaosdb.yaml) | other | 2021-08-09 |  |  |
| [2021-08_eskenazi-health-vice-society.yaml](ransomware/2021-08_eskenazi-health-vice-society.yaml) | ransomware | 2021-08-04 | Vice Society ransomware |  |
| [2021-08_first-horizon-bank-not-disclosed.yaml](supply-chain/2021-08_first-horizon-bank-not-disclosed.yaml) | supply-chain | 2021-08-01 |  |  |
| [2021-08_renaissance-life-health-insurance-secure-administrative-so.yaml](supply-chain/2021-08_renaissance-life-health-insurance-secure-administrative-so.yaml) | supply-chain | 2021-08-01 |  |  |
| [2021-08_catholic-health-capturerx.yaml](supply-chain/2021-08_catholic-health-capturerx.yaml) | supply-chain | 2021-08-01 |  |  |
| [2021-08_american-airlines-ford-maryland-depa-microsoft.yaml](supply-chain/2021-08_american-airlines-ford-maryland-depa-microsoft.yaml) | supply-chain | 2021-08-01 |  |  |
| [2024-09_tmobile-fcc-settlement.yaml](data-leak/2024-09_tmobile-fcc-settlement.yaml) | data-leak | 2021-08-01 |  |  |
| [2021-08_tmobile-john-binns-54m.yaml](data-leak/2021-08_tmobile-john-binns-54m.yaml) | data-leak | 2021-08-01 |  |  |
| [2021-07_kaseya-vsa-revil.yaml](supply-chain/2021-07_kaseya-vsa-revil.yaml) | supply-chain | 2021-07-02 | REvil / Sodinokibi | CVE-2021-30116 |
| [2021-07_memorial-health-system-guidehouse.yaml](supply-chain/2021-07_memorial-health-system-guidehouse.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_hospitals-clearbalance.yaml](supply-chain/2021-07_hospitals-clearbalance.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_hospitals-practicefirst.yaml](supply-chain/2021-07_hospitals-practicefirst.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_jefferson-s-kimmel-cancer-center-elekta.yaml](supply-chain/2021-07_jefferson-s-kimmel-cancer-center-elekta.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_morgan-stanley-guidehouse-accellion.yaml](supply-chain/2021-07_morgan-stanley-guidehouse-accellion.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_msps-and-clients-including-visma-ess-kaseya.yaml](supply-chain/2021-07_msps-and-clients-including-visma-ess-kaseya.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_saudi-aramco-not-disclosed.yaml](supply-chain/2021-07_saudi-aramco-not-disclosed.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_spreadgroup-customers-spreadshirt-spreadshop-a.yaml](supply-chain/2021-07_spreadgroup-customers-spreadshirt-spreadshop-a.yaml) | supply-chain | 2021-07-01 |  |  |
| [2022-06_unc2903-imdsv1-aws-metadata.yaml](credential-theft/2022-06_unc2903-imdsv1-aws-metadata.yaml) | credential-theft | 2021-06-21 |  |  |
| [2021-06_ea-games-lapsus-source-code.yaml](data-leak/2021-06_ea-games-lapsus-source-code.yaml) | data-leak | 2021-06-06 |  |  |
| [2021-06_amerigas-j-j-keller.yaml](supply-chain/2021-06_amerigas-j-j-keller.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_blue-cross-blue-shield-of-kansas-cit-logicgate.yaml](supply-chain/2021-06_blue-cross-blue-shield-of-kansas-cit-logicgate.yaml) | supply-chain | 2021-06-01 |  |  |
| [2024-02_volt-typhoon-critical-infrastructure.yaml](other/2024-02_volt-typhoon-critical-infrastructure.yaml) | other | 2021-06-01 |  | CVE-2021-40539, CVE-2021-27860 |
| [2021-06_harbor-regional-health-capturerx.yaml](supply-chain/2021-06_harbor-regional-health-capturerx.yaml) | supply-chain | 2021-06-01 |  |  |
| [2023-01_twitter-api-scrape.yaml](data-leak/2023-01_twitter-api-scrape.yaml) | data-leak | 2021-06-01 |  |  |
| [2021-06_latitude-financial-oaic-pre-breach.yaml](data-leak/2021-06_latitude-financial-oaic-pre-breach.yaml) | data-leak | 2021-06-01 |  |  |
| [2021-06_u-s-lawmakers-house-legislators-iconstituent.yaml](supply-chain/2021-06_u-s-lawmakers-house-legislators-iconstituent.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_cvs-health-not-disclosed.yaml](supply-chain/2021-06_cvs-health-not-disclosed.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_ohio-medicaid-program-maximus.yaml](supply-chain/2021-06_ohio-medicaid-program-maximus.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_mercedes-benz-usa-not-disclosed.yaml](supply-chain/2021-06_mercedes-benz-usa-not-disclosed.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_volkswagen-group-of-america-shift-digital.yaml](supply-chain/2021-06_volkswagen-group-of-america-shift-digital.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_cancer-centers-of-southwest-oklahoma-elekta.yaml](supply-chain/2021-06_cancer-centers-of-southwest-oklahoma-elekta.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-05_jbs-foods-revil.yaml](ransomware/2021-05_jbs-foods-revil.yaml) | ransomware | 2021-05-30 | REvil (Sodinokibi) |  |
| [2021-05_ireland-hse-conti-ransomware.yaml](ransomware/2021-05_ireland-hse-conti-ransomware.yaml) | ransomware | 2021-05-14 | Conti ransomware; Cobalt Stri… |  |
| [2021-05_colonial-pipeline.yaml](ransomware/2021-05_colonial-pipeline.yaml) | ransomware | 2021-05-07 | DarkSide |  |
| [2021-05_canada-post-commport-communications.yaml](supply-chain/2021-05_canada-post-commport-communications.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-08_microsoft-power-apps-misconfiguration.yaml](data-leak/2021-08_microsoft-power-apps-misconfiguration.yaml) | data-leak | 2021-05-01 |  |  |
| [2021-05_fasttrack-customers-fasttrack-recruitment.yaml](supply-chain/2021-05_fasttrack-customers-fasttrack-recruitment.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_fox-s-clinic-the-alpine-center-for-diabetes-endocrinology-and-metabolism-aprima.yaml](supply-chain/2021-05_fox-s-clinic-the-alpine-center-for-diabetes-endocrinology-and-metabolism-aprima.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_upmc-cole-hidalgo-medical-services-t-capturerx.yaml](supply-chain/2021-05_upmc-cole-hidalgo-medical-services-t-capturerx.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_university-of-houston-herff-jones.yaml](supply-chain/2021-05_university-of-houston-herff-jones.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_u-s-government-blueforce.yaml](supply-chain/2021-05_u-s-government-blueforce.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_u-s-department-of-energy-fermilab.yaml](supply-chain/2021-05_u-s-department-of-energy-fermilab.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_monday-com-rapid7-twilio-mercari-codecov.yaml](supply-chain/2021-05_monday-com-rapid7-twilio-mercari-codecov.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-06_linkedin-700m-api-scrape.yaml](data-leak/2021-06_linkedin-700m-api-scrape.yaml) | data-leak | 2021-05-01 |  |  |
| [2021-05_ardagh-clients-ardagh.yaml](supply-chain/2021-05_ardagh-clients-ardagh.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_japanese-government-the-ministry-of-land-infrastructure-transport-and-tourism-fujitsu.yaml](supply-chain/2021-05_japanese-government-the-ministry-of-land-infrastructure-transport-and-tourism-fujitsu.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_ac-health-systems-and-san-diego-family-care-sdfc-caresouth-carolina-health-center-partners-of-southern-california-netgain.yaml](supply-chain/2021-05_ac-health-systems-and-san-diego-family-care-sdfc-caresouth-carolina-health-center-partners-of-southern-california-netgain.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-04_uranium-finance-bsc-50m-exploit.yaml](other/2021-04_uranium-finance-bsc-50m-exploit.yaml) | other | 2021-04-28 |  |  |
| [2021-04_apple-quanta.yaml](supply-chain/2021-04_apple-quanta.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_doctors-medical-center-medifie.yaml](supply-chain/2021-04_doctors-medical-center-medifie.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_wiener-kennedy-perkins-co-netgain-4th-party.yaml](supply-chain/2021-04_wiener-kennedy-perkins-co-netgain-4th-party.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_illinois-dhs-medicaid-misconfiguration.yaml](data-leak/2021-04_illinois-dhs-medicaid-misconfiguration.yaml) | data-leak | 2021-04-01 |  |  |
| [2021-04_amazon-flipkart-myntra-swiggy-and-zomato-bizongo.yaml](supply-chain/2021-04_amazon-flipkart-myntra-swiggy-and-zomato-bizongo.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_upstox-not-disclosed.yaml](supply-chain/2021-04_upstox-not-disclosed.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_tata-communications-bharti-airtel-and-dbs-bank-route-mobil.yaml](supply-chain/2021-04_tata-communications-bharti-airtel-and-dbs-bank-route-mobil.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_subsidiaries-of-personal-touch-personal-touch-retirement-solutions-personal-touch-mortgage-administration-services-personal-touch-holding-corp.yaml](supply-chain/2021-04_subsidiaries-of-personal-touch-personal-touch-retirement-solutions-personal-touch-mortgage-administration-services-personal-touch-holding-corp.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_stanford-university-the-university-of-maryland-baltimore-and-the-university-of-california-at-berkeley-accellion.yaml](supply-chain/2021-04_stanford-university-the-university-of-maryland-baltimore-and-the-university-of-california-at-berkeley-accellion.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_peach-aviation-zipair-tokyo-air-belgium-sky-airlines-air-transat-vietravel-aero-k-airlines-salam-air-flysafair-air-india-express-wingo-radixx-subsidiary-of-sabre-c.yaml](supply-chain/2021-04_peach-aviation-zipair-tokyo-air-belgium-sky-airlines-air-transat-vietravel-aero-k-airlines-salam-air-flysafair-air-india-express-wingo-radixx-subsidiary-of-sabre-c.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_park-mobile-not-disclosed.yaml](supply-chain/2021-04_park-mobile-not-disclosed.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_japanese-prime-minister-s-cabinet-office-soliton-filezen-application.yaml](supply-chain/2021-04_japanese-prime-minister-s-cabinet-office-soliton-filezen-application.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_ei2-i-vic-international.yaml](supply-chain/2021-04_ei2-i-vic-international.yaml) | supply-chain | 2021-04-01 |  |  |
| [2025-04_blue-shield-california-google-analytics.yaml](data-leak/2025-04_blue-shield-california-google-analytics.yaml) | data-leak | 2021-04-01 |  |  |
| [2021-04_department-of-health-and-human-services-uchicago-king-s-daughters-health-system-osf-healthcare-aspirus-uchicago-medicine-and-memorial-hermann-health-system-meddata.yaml](supply-chain/2021-04_department-of-health-and-human-services-uchicago-king-s-daughters-health-system-osf-healthcare-aspirus-uchicago-medicine-and-memorial-hermann-health-system-meddata.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_click-studios-customers-click-studios.yaml](supply-chain/2021-04_click-studios-customers-click-studios.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_centene-subsidiaries-healthnet-chw-accellion.yaml](supply-chain/2021-04_centene-subsidiaries-healthnet-chw-accellion.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_celcius-not-disclosed.yaml](supply-chain/2021-04_celcius-not-disclosed.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_callx-customers-possibly-lendingtree-liberty-mutual-insurance-and-vivint-among-the-clients-callx.yaml](supply-chain/2021-04_callx-customers-possibly-lendingtree-liberty-mutual-insurance-and-vivint-among-the-clients-callx.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_biotel-heart-not-disclosed.yaml](supply-chain/2021-04_biotel-heart-not-disclosed.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_atlassian-procter-gamble-godaddy-the-washington-post-codecov.yaml](supply-chain/2021-04_atlassian-procter-gamble-godaddy-the-washington-post-codecov.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_apple-valley-clinic-netgain.yaml](supply-chain/2021-04_apple-valley-clinic-netgain.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-03_nine-entertainment-conti.yaml](ransomware/2021-03_nine-entertainment-conti.yaml) | ransomware | 2021-03-28 | Conti ransomware |  |
| [2021-03_cna-financial-phoenix-cryptolocker.yaml](ransomware/2021-03_cna-financial-phoenix-cryptolocker.yaml) | ransomware | 2021-03-21 | Phoenix CryptoLocker (Evil Co… |  |
| [2021-03_luxottica-eyecare-70m.yaml](data-leak/2021-03_luxottica-eyecare-70m.yaml) | data-leak | 2021-03-16 |  |  |
| [2021-03_calviva-health-health-net-community-solutio.yaml](supply-chain/2021-03_calviva-health-health-net-community-solutio.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_wake-forest-baptist-health-lexington-medical-center-healthgrades.yaml](supply-chain/2021-03_wake-forest-baptist-health-lexington-medical-center-healthgrades.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_university-of-miami-health-accellion.yaml](supply-chain/2021-03_university-of-miami-health-accellion.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_trillium-community-health-plan-southern-illinois-university-school-of-medicine-accellion.yaml](supply-chain/2021-03_trillium-community-health-plan-southern-illinois-university-school-of-medicine-accellion.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_singapore-airlines-air-new-zealand-british-airways-american-airlines-lufthansa-malaysia-airlines-finnair-japan-airlines-united-airlines-sas-cathay-pacific-and-south-korean-airline-juju-air-star-alliance-sita.yaml](supply-chain/2021-03_singapore-airlines-air-new-zealand-british-airways-american-airlines-lufthansa-malaysia-airlines-finnair-japan-airlines-united-airlines-sas-cathay-pacific-and-south-korean-airline-juju-air-star-alliance-sita.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_schools-jail-cells-hospital-icus-and-major-companies-like-tesla-nissan-equinox-cloudflare-verkada.yaml](supply-chain/2021-03_schools-jail-cells-hospital-icus-and-major-companies-like-tesla-nissan-equinox-cloudflare-verkada.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_royal-dutch-shell-accellion.yaml](supply-chain/2021-03_royal-dutch-shell-accellion.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_qualys-accellion.yaml](supply-chain/2021-03_qualys-accellion.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_poll-county-schools-pcs-revenue-systems.yaml](supply-chain/2021-03_poll-county-schools-pcs-revenue-systems.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_piedmont-health-services-peaktpa.yaml](supply-chain/2021-03_piedmont-health-services-peaktpa.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_multicare-health-services-netgain.yaml](supply-chain/2021-03_multicare-health-services-netgain.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_israeli-likud-party-elector-software.yaml](supply-chain/2021-03_israeli-likud-party-elector-software.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_flagstar-bank-accellion.yaml](supply-chain/2021-03_flagstar-bank-accellion.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_european-banking-authority-microsoft.yaml](supply-chain/2021-03_european-banking-authority-microsoft.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_armed-forces-communications-electronics-association-and-the-us-geospatial-intelligence-foundation-spargo.yaml](supply-chain/2021-03_armed-forces-communications-electronics-association-and-the-us-geospatial-intelligence-foundation-spargo.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_austin-isd-not-disclosed.yaml](supply-chain/2021-03_austin-isd-not-disclosed.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-02_singapore-airlines-sita-580k.yaml](supply-chain/2021-02_singapore-airlines-sita-580k.yaml) | supply-chain | 2021-02-26 |  |  |
| [2021-02_air-india-sita-pss-breach.yaml](supply-chain/2021-02_air-india-sita-pss-breach.yaml) | supply-chain | 2021-02-26 |  |  |
| [2021-02_florida-healthy-kids-corporation-fhkc-jelly-bean-communications-de.yaml](supply-chain/2021-02_florida-healthy-kids-corporation-fhkc-jelly-bean-communications-de.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_fertility-clinics-incl-shady-grove-fertility-reproductive-science-center-san-francisco-ivf-florida-and-fertility-center-of-illinois-usf.yaml](supply-chain/2021-02_fertility-clinics-incl-shady-grove-fertility-reproductive-science-center-san-francisco-ivf-florida-and-fertility-center-of-illinois-usf.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_ubiquiti-networks-not-disclosed.yaml](supply-chain/2021-02_ubiquiti-networks-not-disclosed.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_ramsey-county-minnesota-family-health-division-netgain.yaml](supply-chain/2021-02_ramsey-county-minnesota-family-health-division-netgain.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_microsoft-365-exchange-infrastructure-mimecast.yaml](supply-chain/2021-02_microsoft-365-exchange-infrastructure-mimecast.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_jamaican-government-amber-group.yaml](supply-chain/2021-02_jamaican-government-amber-group.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_goodwin-procter-qimr-berghofer-medical-research-institute-allens-jones-day-accellion.yaml](supply-chain/2021-02_goodwin-procter-qimr-berghofer-medical-research-institute-allens-jones-day-accellion.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_french-government-stormshield.yaml](supply-chain/2021-02_french-government-stormshield.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_sitepoint-teespring-waydev.yaml](supply-chain/2021-02_sitepoint-teespring-waydev.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_washington-state-auditor-singtel-university-of-colorado-bombardier-accellion.yaml](supply-chain/2021-02_washington-state-auditor-singtel-university-of-colorado-bombardier-accellion.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_airbus-air-cara-bes-arcelormittal-bt-luxottica-kuehne-nagel-minist-re-de-la-justice-fran-ais-new-zealand-police-pwc-russia-salomon-sanofi-and-sephora-possibly-centreon.yaml](supply-chain/2021-02_airbus-air-cara-bes-arcelormittal-bt-luxottica-kuehne-nagel-minist-re-de-la-justice-fran-ais-new-zealand-police-pwc-russia-salomon-sanofi-and-sephora-possibly-centreon.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_defense-industry-wind-river-customers-wind-river-systems.yaml](supply-chain/2021-02_defense-industry-wind-river-customers-wind-river-systems.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_city-of-monroe-kirkland-redmond-automatic-funds-transfer-ser.yaml](supply-chain/2021-02_city-of-monroe-kirkland-redmond-automatic-funds-transfer-ser.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_city-of-kirkland-monroe-redmonde-seattle-lakewood-water-district-afts.yaml](supply-chain/2021-02_city-of-kirkland-monroe-redmonde-seattle-lakewood-water-district-afts.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_beaumont-health-epic-software.yaml](supply-chain/2021-02_beaumont-health-epic-software.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-01_codecov-bash-uploader.yaml](supply-chain/2021-01_codecov-bash-uploader.yaml) | supply-chain | 2021-01-31 |  |  |
| [2021-01_asic-accellion-fta-australia.yaml](supply-chain/2021-01_asic-accellion-fta-australia.yaml) | supply-chain | 2021-01-15 | Cl0p / DEWMODE web shell | CVE-2021-27101, CVE-2021-27102, CVE-202… |
| [2021-01_2020-eye-care-network-3-25m.yaml](data-leak/2021-01_2020-eye-care-network-3-25m.yaml) | data-leak | 2021-01-11 |  |  |
| [2021-03_microsoft-exchange-proxylogon.yaml](other/2021-03_microsoft-exchange-proxylogon.yaml) | other | 2021-01-03 | China Chopper webshell / HAFN… | CVE-2021-26855, CVE-2021-26857, CVE-202… |
| [2021-01_new-zeland-reserve-bank-australian-securities-and-investments-commission-asic-acellion-software.yaml](supply-chain/2021-01_new-zeland-reserve-bank-australian-securities-and-investments-commission-asic-acellion-software.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_defence-forces-para-military-forces-and-intelligence-agencies-of-india-elcom-innovations.yaml](supply-chain/2021-01_defence-forces-para-military-forces-and-intelligence-agencies-of-india-elcom-innovations.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_saskatchewan-hal-system-aspira.yaml](supply-chain/2021-01_saskatchewan-hal-system-aspira.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_sonicwall-customers-sonicwall.yaml](supply-chain/2021-01_sonicwall-customers-sonicwall.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_supply-chain-for-audi-bmw-mercedes-porsche-saab-volkswagen-and-volvo-across-north-america-namesouth.yaml](supply-chain/2021-01_supply-chain-for-audi-bmw-mercedes-porsche-saab-volkswagen-and-volvo-across-north-america-namesouth.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_north-korean-stock-investment-firms-not-disclosed.yaml](supply-chain/2021-01_north-korean-stock-investment-firms-not-disclosed.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_united-parcel-service-ups-and-norfolk-southern-railroad-taylor-made-diagnostics-tmd.yaml](supply-chain/2021-01_united-parcel-service-ups-and-norfolk-southern-railroad-taylor-made-diagnostics-tmd.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_neopets-69m-live-access.yaml](data-leak/2021-01_neopets-69m-live-access.yaml) | data-leak | 2021-01-01 |  |  |
| [2021-01_socialarks-214m-profiles.yaml](data-leak/2021-01_socialarks-214m-profiles.yaml) | data-leak | 2021-01-01 |  |  |
| [2021-01_bonobos-not-disclosed.yaml](supply-chain/2021-01_bonobos-not-disclosed.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_facebook-instagram-linkedin-socialark.yaml](supply-chain/2021-01_facebook-instagram-linkedin-socialark.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_omnitrax-broe-group.yaml](supply-chain/2021-01_omnitrax-broe-group.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_accellion-fta-clop.yaml](supply-chain/2021-01_accellion-fta-clop.yaml) | supply-chain | 2020-12-25 | DEWMODE webshell / FINTEAM | CVE-2021-27101, CVE-2021-27102, CVE-202… |
| [2021-01_ubiquiti-insider-threat.yaml](data-leak/2021-01_ubiquiti-insider-threat.yaml) | data-leak | 2020-12-10 |  |  |
| [2020-12_private-and-government-organizations-vietnam-certification-au.yaml](supply-chain/2020-12_private-and-government-organizations-vietnam-certification-au.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_now-pensions-not-disclosed.yaml](supply-chain/2020-12_now-pensions-not-disclosed.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_mongolian-government-agencies-able-software.yaml](supply-chain/2020-12_mongolian-government-agencies-able-software.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_microsoft-not-disclosed.yaml](supply-chain/2020-12_microsoft-not-disclosed.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_fireeye-customers-fireeye.yaml](supply-chain/2020-12_fireeye-customers-fireeye.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_department-of-treasury-and-commerce--solarwinds.yaml](supply-chain/2020-12_department-of-treasury-and-commerce--solarwinds.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_dental-practices-dental-care-alliance-dca.yaml](supply-chain/2020-12_dental-practices-dental-care-alliance-dca.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-11_first-federal-community-bank-rio-ban-abs.yaml](supply-chain/2020-11_first-federal-community-bank-rio-ban-abs.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-11_wildworks-not-disclosed.yaml](supply-chain/2020-11_wildworks-not-disclosed.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-11_lenscrafters-target-optical-eyemed-a-luxottica.yaml](supply-chain/2020-11_lenscrafters-target-optical-eyemed-a-luxottica.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-11_insurance-carriers-in-texas-colarodo-vertafore.yaml](supply-chain/2020-11_insurance-carriers-in-texas-colarodo-vertafore.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-11_hotels-customers-of-prestige-softwar-prestige-software.yaml](supply-chain/2020-11_hotels-customers-of-prestige-softwar-prestige-software.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-11_great-heart-academies-blackbaud.yaml](supply-chain/2020-11_great-heart-academies-blackbaud.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-11_customers-of-belden-belden.yaml](supply-chain/2020-11_customers-of-belden-belden.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-10_uvm-health-network-doppelpaymer.yaml](ransomware/2020-10_uvm-health-network-doppelpaymer.yaml) | ransomware | 2020-10-28 | DoppelPaymer ransomware |  |
| [2020-10_nitro-pdf-77m-users.yaml](data-leak/2020-10_nitro-pdf-77m-users.yaml) | data-leak | 2020-10-21 |  |  |
| [2020-10_kylie-cosmetics-shopify.yaml](supply-chain/2020-10_kylie-cosmetics-shopify.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_jm-bullion-not-disclosed.yaml](supply-chain/2020-10_jm-bullion-not-disclosed.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_government-departments-and-the-austr-isentia.yaml](supply-chain/2020-10_government-departments-and-the-austr-isentia.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_google-fragomen-del-rey-bernsen.yaml](supply-chain/2020-10_google-fragomen-del-rey-bernsen.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_dickey-s-barbecue-pit-not-disclosed.yaml](supply-chain/2020-10_dickey-s-barbecue-pit-not-disclosed.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_city-of-odessa-click2gov.yaml](supply-chain/2020-10_city-of-odessa-click2gov.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_broadvoice-customers-broadvoice.yaml](supply-chain/2020-10_broadvoice-customers-broadvoice.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_apple-google-amazon-citibank-nitro.yaml](supply-chain/2020-10_apple-google-amazon-citibank-nitro.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_lazada-redmart-app-not-disclosed.yaml](supply-chain/2020-10_lazada-redmart-app-not-disclosed.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_rady-children-hospital-sonoma-valley-blackbaud.yaml](supply-chain/2020-10_rady-children-hospital-sonoma-valley-blackbaud.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-09_universal-health-services-ryuk.yaml](ransomware/2020-09_universal-health-services-ryuk.yaml) | ransomware | 2020-09-27 | Ryuk ransomware; TrickBot; Em… |  |
| [2021-09_cisco-webex-iam-compromise.yaml](credential-theft/2021-09_cisco-webex-iam-compromise.yaml) | credential-theft | 2020-09-24 |  |  |
| [2020-09_dusseldorf-hospital-patient-death.yaml](ransomware/2020-09_dusseldorf-hospital-patient-death.yaml) | ransomware | 2020-09-09 | DoppelPaymer ransomware | CVE-2019-19781 |
| [2020-09_pell-city-valley-bank-not-disclosed.yaml](supply-chain/2020-09_pell-city-valley-bank-not-disclosed.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-09_buffalo-n-y-area-hospitals-innova-he-blackbaud.yaml](supply-chain/2020-09_buffalo-n-y-area-hospitals-innova-he-blackbaud.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-09_tribune-media-times-media-grup-view-media.yaml](supply-chain/2020-09_tribune-media-times-media-grup-view-media.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-09_e-commerce-stores-adobe-magento-1.yaml](supply-chain/2020-09_e-commerce-stores-adobe-magento-1.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-09_phipps-conservatory-blackbaud.yaml](supply-chain/2020-09_phipps-conservatory-blackbaud.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-08_jack-daniel-s-brown-forman.yaml](supply-chain/2020-08_jack-daniel-s-brown-forman.yaml) | supply-chain | 2020-08-01 |  |  |
| [2020-08_razer-elasticsearch-100k.yaml](data-leak/2020-08_razer-elasticsearch-100k.yaml) | data-leak | 2020-08-01 |  |  |
| [2020-08_department-of-health-not-disclosed.yaml](supply-chain/2020-08_department-of-health-not-disclosed.yaml) | supply-chain | 2020-08-01 |  |  |
| [2020-08_rochester-ymca-not-disclosed.yaml](supply-chain/2020-08_rochester-ymca-not-disclosed.yaml) | supply-chain | 2020-08-01 |  |  |
| [2020-07_garmin-wastedlocker-evil-corp.yaml](ransomware/2020-07_garmin-wastedlocker-evil-corp.yaml) | ransomware | 2020-07-23 | WastedLocker ransomware; Fake… |  |
| [2020-07_gedmatch-dna-privacy-attack.yaml](other/2020-07_gedmatch-dna-privacy-attack.yaml) | other | 2020-07-19 |  |  |
| [2020-07_twitter-bitcoin-scam-vishing.yaml](credential-theft/2020-07_twitter-bitcoin-scam-vishing.yaml) | credential-theft | 2020-07-15 |  |  |
| [2020-07_university-of-manitoba-university-of-blackbaud.yaml](supply-chain/2020-07_university-of-manitoba-university-of-blackbaud.yaml) | supply-chain | 2020-07-01 |  |  |
| [2020-07_digital-bank-app-dave-waydev.yaml](supply-chain/2020-07_digital-bank-app-dave-waydev.yaml) | supply-chain | 2020-07-01 |  |  |
| [2020-07_promo-com-not-disclosed.yaml](supply-chain/2020-07_promo-com-not-disclosed.yaml) | supply-chain | 2020-07-01 |  |  |
| [2020-07_microsoft-ai-38tb-sas-token.yaml](data-leak/2020-07_microsoft-ai-38tb-sas-token.yaml) | data-leak | 2020-07-01 |  |  |
| [2020-07_freepik-flaticon-8-3m.yaml](data-leak/2020-07_freepik-flaticon-8-3m.yaml) | data-leak | 2020-07-01 |  |  |
| [2020-07_citrix-not-disclosed.yaml](supply-chain/2020-07_citrix-not-disclosed.yaml) | supply-chain | 2020-07-01 |  |  |
| [2020-07_angelo-gordon-co-graham-capital-mana-m-j-brunner.yaml](supply-chain/2020-07_angelo-gordon-co-graham-capital-mana-m-j-brunner.yaml) | supply-chain | 2020-07-01 |  |  |
| [2020-06_mednax-office365-phishing-1-3m.yaml](credential-theft/2020-06_mednax-office365-phishing-1-3m.yaml) | credential-theft | 2020-06-17 |  |  |
| [2020-06_drizly-github-rds-breach.yaml](credential-theft/2020-06_drizly-github-rds-breach.yaml) | credential-theft | 2020-06-12 |  |  |
| [2020-06_wattpad-breach.yaml](data-leak/2020-06_wattpad-breach.yaml) | data-leak | 2020-06-01 |  |  |
| [2020-06_san-francisco-employees-retirement-s-10up-inc.yaml](supply-chain/2020-06_san-francisco-employees-retirement-s-10up-inc.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-06_joomla-open-source-matters.yaml](supply-chain/2020-06_joomla-open-source-matters.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-06_keepnet-not-disclosed.yaml](supply-chain/2020-06_keepnet-not-disclosed.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-06_police-departments-netsentiel.yaml](supply-chain/2020-06_police-departments-netsentiel.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-06_mu-health-not-disclosed.yaml](supply-chain/2020-06_mu-health-not-disclosed.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-05_mns-healthcare-clients-management-and-network-s.yaml](supply-chain/2020-05_mns-healthcare-clients-management-and-network-s.yaml) | supply-chain | 2020-05-01 |  |  |
| [2020-05_truecaller-not-disclosed.yaml](supply-chain/2020-05_truecaller-not-disclosed.yaml) | supply-chain | 2020-05-01 |  |  |
| [2020-05_florida-department-of-economic-oppor-not-disclosed.yaml](supply-chain/2020-05_florida-department-of-economic-oppor-not-disclosed.yaml) | supply-chain | 2020-05-01 |  |  |
| [2020-05_bhim-wallet-app-csc-e-governance-service.yaml](supply-chain/2020-05_bhim-wallet-app-csc-e-governance-service.yaml) | supply-chain | 2020-05-01 |  |  |
| [2020-05_bank-of-america-not-disclosed.yaml](supply-chain/2020-05_bank-of-america-not-disclosed.yaml) | supply-chain | 2020-05-01 |  |  |
| [2020-04_magellan-health-ransomware.yaml](ransomware/2020-04_magellan-health-ransomware.yaml) | ransomware | 2020-04-11 |  |  |
| [2020-04_service-nsw-phishing-186k.yaml](credential-theft/2020-04_service-nsw-phishing-186k.yaml) | credential-theft | 2020-04-04 |  |  |
| [2020-04_cognizant-s-clients-cognizant.yaml](supply-chain/2020-04_cognizant-s-clients-cognizant.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-04_nintendo-credential-stuffing-160k.yaml](credential-theft/2020-04_nintendo-credential-stuffing-160k.yaml) | credential-theft | 2020-04-01 |  |  |
| [2020-04_usenext-usenet-nl-not-disclosed.yaml](supply-chain/2020-04_usenext-usenet-nl-not-disclosed.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-04_zoom-credential-stuffing-530k.yaml](credential-theft/2020-04_zoom-credential-stuffing-530k.yaml) | credential-theft | 2020-04-01 |  |  |
| [2020-04_rigup-s-energy-sector-clients-rigup.yaml](supply-chain/2020-04_rigup-s-energy-sector-clients-rigup.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-04_michigan-state-university-volusion.yaml](supply-chain/2020-04_michigan-state-university-volusion.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-04_mariott-not-disclosed.yaml](supply-chain/2020-04_mariott-not-disclosed.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-03_first-republic-bank-aws-insider.yaml](data-leak/2020-03_first-republic-bank-aws-insider.yaml) | data-leak | 2020-03-11 |  |  |
| [2020-03_radio-com-not-disclosed.yaml](supply-chain/2020-03_radio-com-not-disclosed.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_spacex-tesla-boeing-lockheed-martin-visser.yaml](supply-chain/2020-03_spacex-tesla-boeing-lockheed-martin-visser.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_amazon-ebay-shopify-stripe-paypal-not-disclosed.yaml](supply-chain/2020-03_amazon-ebay-shopify-stripe-paypal-not-disclosed.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_general-electric-canon-business-services.yaml](supply-chain/2020-03_general-electric-canon-business-services.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_t-mobile-not-disclosed.yaml](supply-chain/2020-03_t-mobile-not-disclosed.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_chubb-not-disclosed.yaml](supply-chain/2020-03_chubb-not-disclosed.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_cam4-elasticsearch-10bn-records.yaml](data-leak/2020-03_cam4-elasticsearch-10bn-records.yaml) | data-leak | 2020-03-01 |  |  |
| [2020-02_blackbaud-crm-ransomware.yaml](ransomware/2020-02_blackbaud-crm-ransomware.yaml) | ransomware | 2020-02-07 |  |  |
| [2020-02_health-share-of-oregon-gridworks.yaml](supply-chain/2020-02_health-share-of-oregon-gridworks.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_rutters-store-not-disclosed.yaml](supply-chain/2020-02_rutters-store-not-disclosed.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_tql-carriers-tql.yaml](supply-chain/2020-02_tql-carriers-tql.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_idaho-central-credit-union-not-disclosed.yaml](supply-chain/2020-02_idaho-central-credit-union-not-disclosed.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_nedbank-computer-facilities-pty.yaml](supply-chain/2020-02_nedbank-computer-facilities-pty.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_carson-city-click2gov.yaml](supply-chain/2020-02_carson-city-click2gov.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_brunswick-county-schools-interactive-medical-syst.yaml](supply-chain/2020-02_brunswick-county-schools-interactive-medical-syst.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_community-care-physicians-bst.yaml](supply-chain/2020-02_community-care-physicians-bst.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_clearview-ai-client-list.yaml](data-leak/2020-02_clearview-ai-client-list.yaml) | data-leak | 2020-02-01 |  |  |
| [2020-01_instagram-social-captain.yaml](supply-chain/2020-01_instagram-social-captain.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_mitsubishi-not-disclosed.yaml](supply-chain/2020-01_mitsubishi-not-disclosed.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_estee-lauder-440m-elasticsearch.yaml](data-leak/2020-01_estee-lauder-440m-elasticsearch.yaml) | data-leak | 2020-01-01 |  |  |
| [2020-01_marijuana-dispensaries-amedicanna-di-thsuite.yaml](supply-chain/2020-01_marijuana-dispensaries-amedicanna-di-thsuite.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_amazon-customers-amazon.yaml](supply-chain/2020-01_amazon-customers-amazon.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_medical-facilities-isofh.yaml](supply-chain/2020-01_medical-facilities-isofh.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_mercy-health-lorain-rcm-enterprise-services.yaml](supply-chain/2020-01_mercy-health-lorain-rcm-enterprise-services.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_easyjet-breach.yaml](data-leak/2020-01_easyjet-breach.yaml) | data-leak | 2020-01-01 |  |  |
| [2020-01_regus-applause.yaml](supply-chain/2020-01_regus-applause.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_schools-active-network.yaml](supply-chain/2020-01_schools-active-network.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_state-governments-of-u-s-not-disclosed.yaml](supply-chain/2020-01_state-governments-of-u-s-not-disclosed.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_the-australian-p-n-bank-not-disclosed.yaml](supply-chain/2020-01_the-australian-p-n-bank-not-disclosed.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-09_national-general-allstate-insurance.yaml](data-leak/2020-09_national-general-allstate-insurance.yaml) | data-leak | 2020-01-01 |  |  |
| [2020-01_marriott-employee-credentials-5-2m.yaml](credential-theft/2020-01_marriott-employee-credentials-5-2m.yaml) | credential-theft | 2020-01-01 |  |  |
| [2019-12_city-of-sioux-click2gov.yaml](supply-chain/2019-12_city-of-sioux-click2gov.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_xerox-centurylink-nasdaq-general-ele-ipr-software.yaml](supply-chain/2019-12_xerox-centurylink-nasdaq-general-ele-ipr-software.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_wyze-customer-wyze.yaml](supply-chain/2019-12_wyze-customer-wyze.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_singapore-armed-forces-saf-hmi-institute-of-health.yaml](supply-chain/2019-12_singapore-armed-forces-saf-hmi-institute-of-health.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_nypd-fingerprint-database-not-disclosed.yaml](supply-chain/2019-12_nypd-fingerprint-database-not-disclosed.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_city-of-marietta-click2gov.yaml](supply-chain/2019-12_city-of-marietta-click2gov.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-11_t-mobile-prepaid-breach.yaml](data-leak/2019-11_t-mobile-prepaid-breach.yaml) | data-leak | 2019-11-22 |  |  |
| [2019-11_the-city-of-charlottesville-not-disclosed.yaml](supply-chain/2019-11_the-city-of-charlottesville-not-disclosed.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_tenncare-magellan-health-system.yaml](supply-chain/2019-11_tenncare-magellan-health-system.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_pompano-beach-city-click2gov.yaml](supply-chain/2019-11_pompano-beach-city-click2gov.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_palo-alto-networks-not-disclosed.yaml](supply-chain/2019-11_palo-alto-networks-not-disclosed.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_macy-s-not-disclosed.yaml](supply-chain/2019-11_macy-s-not-disclosed.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_city-of-san-angelo-click2gov.yaml](supply-chain/2019-11_city-of-san-angelo-click2gov.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_florida-blue-magellan-health-inc.yaml](supply-chain/2019-11_florida-blue-magellan-health-inc.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_facebook-and-twitter-one-audience.yaml](supply-chain/2019-11_facebook-and-twitter-one-audience.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-10_uber-slack-and-fcc-zendesk.yaml](supply-chain/2019-10_uber-slack-and-fcc-zendesk.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-10_centurylink-not-disclosed.yaml](supply-chain/2019-10_centurylink-not-disclosed.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-10_nordvpn-not-disclosed.yaml](supply-chain/2019-10_nordvpn-not-disclosed.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-10_the-clark-county-school-district-pearson-clinical-assessm.yaml](supply-chain/2019-10_the-clark-county-school-district-pearson-clinical-assessm.yaml) | supply-chain | 2019-10-01 |  |  |
| [2020-12_solarwinds-sunburst.yaml](supply-chain/2020-12_solarwinds-sunburst.yaml) | supply-chain | 2019-10-01 | SUNBURST / TEARDROP / SUNSPOT | CVE-2020-10148 |
| [2019-10_unicredit-not-disclosed.yaml](supply-chain/2019-10_unicredit-not-disclosed.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-10_gw-community-members-chegg.yaml](supply-chain/2019-10_gw-community-members-chegg.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-10_geisinger-health-plan-magellan-national-imagin.yaml](supply-chain/2019-10_geisinger-health-plan-magellan-national-imagin.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-09_yves-rocher-aliznet.yaml](supply-chain/2019-09_yves-rocher-aliznet.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_ames-parking-ticket-payments-click2gov.yaml](supply-chain/2019-09_ames-parking-ticket-payments-click2gov.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_city-of-broken-arrow-deerfield-beach-click2gov.yaml](supply-chain/2019-09_city-of-broken-arrow-deerfield-beach-click2gov.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_doordash-not-disclosed.yaml](supply-chain/2019-09_doordash-not-disclosed.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_malinda-air-not-disclosed.yaml](supply-chain/2019-09_malinda-air-not-disclosed.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_github-and-bitbucket-circlci.yaml](supply-chain/2019-09_github-and-bitbucket-circlci.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-08_mastercard-not-disclosed.yaml](supply-chain/2019-08_mastercard-not-disclosed.yaml) | supply-chain | 2019-08-01 |  |  |
| [2019-08_cable-one-not-disclosed.yaml](supply-chain/2019-08_cable-one-not-disclosed.yaml) | supply-chain | 2019-08-01 |  |  |
| [2019-08_dekalb-school-district-428-wilmette--pearson-clinical-assessm.yaml](supply-chain/2019-08_dekalb-school-district-428-wilmette--pearson-clinical-assessm.yaml) | supply-chain | 2019-08-01 |  |  |
| [2019-08_biostar2-biometric-27m.yaml](data-leak/2019-08_biostar2-biometric-27m.yaml) | data-leak | 2019-08-01 |  |  |
| [2019-08_naperville-unit-district-203-indian--pearson-clinical-assessm.yaml](supply-chain/2019-08_naperville-unit-district-203-indian--pearson-clinical-assessm.yaml) | supply-chain | 2019-08-01 |  |  |
| [2019-07_clinical-pathology-laboratories-american-medical-collect.yaml](supply-chain/2019-07_clinical-pathology-laboratories-american-medical-collect.yaml) | supply-chain | 2019-07-01 |  |  |
| [2019-07_american-esoteric-laboratories-sunri-american-medical-collect.yaml](supply-chain/2019-07_american-esoteric-laboratories-sunri-american-medical-collect.yaml) | supply-chain | 2019-07-01 |  |  |
| [2019-07_mgm-resorts-cloud-10-6m.yaml](data-leak/2019-07_mgm-resorts-cloud-10-6m.yaml) | data-leak | 2019-07-01 |  |  |
| [2019-06_bulgarian-nra-5m-taxpayers.yaml](data-leak/2019-06_bulgarian-nra-5m-taxpayers.yaml) | data-leak | 2019-06-01 |  |  |
| [2019-06_westpac-bank-payid.yaml](supply-chain/2019-06_westpac-bank-payid.yaml) | supply-chain | 2019-06-01 |  |  |
| [2019-06_quest-diagnostics-laboratory-corpora-american-medical-collect.yaml](supply-chain/2019-06_quest-diagnostics-laboratory-corpora-american-medical-collect.yaml) | supply-chain | 2019-06-01 |  |  |
| [2019-06_opko-health-american-medical-collect.yaml](supply-chain/2019-06_opko-health-american-medical-collect.yaml) | supply-chain | 2019-06-01 |  |  |
| [2019-06_komodo-not-disclosed.yaml](supply-chain/2019-06_komodo-not-disclosed.yaml) | supply-chain | 2019-06-01 |  |  |
| [2019-05_canva-gnosticplayers.yaml](data-leak/2019-05_canva-gnosticplayers.yaml) | data-leak | 2019-05-24 |  |  |
| [2019-05_u-s-customs-and-border-protection-not-disclosed.yaml](supply-chain/2019-05_u-s-customs-and-border-protection-not-disclosed.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_vag-ericsson-leica-man-toshiba-unicr-citycomp.yaml](supply-chain/2019-05_vag-ericsson-leica-man-toshiba-unicr-citycomp.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_uniqlo-not.yaml](supply-chain/2019-05_uniqlo-not.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_stockx-sneaker-6-8m.yaml](data-leak/2019-05_stockx-sneaker-6-8m.yaml) | data-leak | 2019-05-01 |  |  |
| [2019-05_truecaller-not-disclosed.yaml](supply-chain/2019-05_truecaller-not-disclosed.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_instagram-chtrbox.yaml](supply-chain/2019-05_instagram-chtrbox.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_forbes-not-disclosed.yaml](supply-chain/2019-05_forbes-not-disclosed.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_4-600-websites-picreel-and-alpaca-forms.yaml](supply-chain/2019-05_4-600-websites-picreel-and-alpaca-forms.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_webstorage-users-asus-webstorage.yaml](supply-chain/2019-05_webstorage-users-asus-webstorage.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_bank-axis-icici-indusind-rbl-not-disclosed.yaml](supply-chain/2019-05_bank-axis-icici-indusind-rbl-not-disclosed.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-04_docker-hub-oauth-tokens.yaml](data-leak/2019-04_docker-hub-oauth-tokens.yaml) | data-leak | 2019-04-25 |  |  |
| [2019-04_176-colleges-and-universities-prismrbs.yaml](supply-chain/2019-04_176-colleges-and-universities-prismrbs.yaml) | supply-chain | 2019-04-01 |  |  |
| [2019-04_freedom-mobile-apptium-technologies.yaml](supply-chain/2019-04_freedom-mobile-apptium-technologies.yaml) | supply-chain | 2019-04-01 |  |  |
| [2019-07_capital-one-ssrf-imdsv1-106m.yaml](data-leak/2019-07_capital-one-ssrf-imdsv1-106m.yaml) | credential-theft | 2019-03-22 |  |  |
| [2019-03_the-bank-of-queensland-landmark-white-limited.yaml](supply-chain/2019-03_the-bank-of-queensland-landmark-white-limited.yaml) | supply-chain | 2019-03-01 |  |  |
| [2019-03_healthcare-institutions-including-bl-wolverine-solutions-grou.yaml](supply-chain/2019-03_healthcare-institutions-including-bl-wolverine-solutions-grou.yaml) | supply-chain | 2019-03-01 |  |  |
| [2019-03_rush-system-for-health-miramed.yaml](supply-chain/2019-03_rush-system-for-health-miramed.yaml) | supply-chain | 2019-03-01 |  |  |
| [2019-02_equifax-experian-and-transunion-image-i-nation-technolog.yaml](supply-chain/2019-02_equifax-experian-and-transunion-image-i-nation-technolog.yaml) | supply-chain | 2019-02-01 |  |  |
| [2019-02_huddle-house-not-disclosed.yaml](supply-chain/2019-02_huddle-house-not-disclosed.yaml) | supply-chain | 2019-02-01 |  |  |
| [2019-02_china-railway-not-disclosed.yaml](supply-chain/2019-02_china-railway-not-disclosed.yaml) | supply-chain | 2019-02-01 |  |  |
| [2019-02_verifications-io-763m-emails.yaml](data-leak/2019-02_verifications-io-763m-emails.yaml) | data-leak | 2019-02-01 |  |  |
| [2019-02_medibank-third-party-pre-breach.yaml](supply-chain/2019-02_medibank-third-party-pre-breach.yaml) | data-leak | 2019-02-01 |  |  |
| [2019-02_houzz-not-disclosed.yaml](supply-chain/2019-02_houzz-not-disclosed.yaml) | supply-chain | 2019-02-01 |  |  |
| [2019-01_141-airlines-that-partner-with-amade-amadeus.yaml](supply-chain/2019-01_141-airlines-that-partner-with-amade-amadeus.yaml) | supply-chain | 2019-01-01 |  |  |
| [2021-04_facebook-533m-phone-scrape.yaml](data-leak/2021-04_facebook-533m-phone-scrape.yaml) | data-leak | 2019-01-01 |  |  |
| [2019-01_highmark-bcbs-aetna-emblem-health-hu-benefitmall.yaml](supply-chain/2019-01_highmark-bcbs-aetna-emblem-health-hu-benefitmall.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_tim-hortons-covert-location-tracking.yaml](data-leak/2019-01_tim-hortons-covert-location-tracking.yaml) | data-leak | 2019-01-01 |  |  |
| [2019-01_humana-lcp-corp.yaml](supply-chain/2019-01_humana-lcp-corp.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_localbitcoins-not-disclosed.yaml](supply-chain/2019-01_localbitcoins-not-disclosed.yaml) | supply-chain | 2019-01-01 |  |  |
| [2024-03_att-dark-web-73million.yaml](data-leak/2024-03_att-dark-web-73million.yaml) | data-leak | 2019-01-01 |  |  |
| [2019-01_hanover-county-click2gov.yaml](supply-chain/2019-01_hanover-county-click2gov.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_e-commerce-sites-that-partner-with-a-adverline.yaml](supply-chain/2019-01_e-commerce-sites-that-partner-with-a-adverline.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_city-of-saint-john-nb-click2gov.yaml](supply-chain/2019-01_city-of-saint-john-nb-click2gov.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_ascension-opticsml.yaml](supply-chain/2019-01_ascension-opticsml.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_all-sites-that-use-php-pear-and-down-php-pear.yaml](supply-chain/2019-01_all-sites-that-use-php-pear-and-down-php-pear.yaml) | supply-chain | 2019-01-01 |  |  |
| [2018-12_quora-100m-users.yaml](data-leak/2018-12_quora-100m-users.yaml) | data-leak | 2018-12-03 |  |  |
| [2018-12_taobao-tmall-alipay-baidu-cloud-163--easy-programming-languag.yaml](supply-chain/2018-12_taobao-tmall-alipay-baidu-cloud-163--easy-programming-languag.yaml) | supply-chain | 2018-12-01 |  |  |
| [2018-12_redwood-eye-center-it-lighthouse.yaml](supply-chain/2018-12_redwood-eye-center-it-lighthouse.yaml) | supply-chain | 2018-12-01 |  |  |
| [2018-12_managed-health-services-of-indiana-lcp-corp.yaml](supply-chain/2018-12_managed-health-services-of-indiana-lcp-corp.yaml) | supply-chain | 2018-12-01 |  |  |
| [2018-12_city-of-saint-john-click2gov.yaml](supply-chain/2018-12_city-of-saint-john-click2gov.yaml) | supply-chain | 2018-12-01 |  |  |
| [2018-12_bevmo-ncr-corp.yaml](supply-chain/2018-12_bevmo-ncr-corp.yaml) | supply-chain | 2018-12-01 |  |  |
| [2018-12_baylor-scott-white-medical-center-fr-not-disclosed.yaml](supply-chain/2018-12_baylor-scott-white-medical-center-fr-not-disclosed.yaml) | supply-chain | 2018-12-01 |  |  |
| [2018-11_atrium-health-accudoc-solutions-inc.yaml](supply-chain/2018-11_atrium-health-accudoc-solutions-inc.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_the-australian-defence-department-not-disclosed.yaml](supply-chain/2018-11_the-australian-defence-department-not-disclosed.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_bitpay-right9ctrl.yaml](supply-chain/2018-11_bitpay-right9ctrl.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_city-of-bakersfield-click2gov.yaml](supply-chain/2018-11_city-of-bakersfield-click2gov.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_city-of-york-council-appware.yaml](supply-chain/2018-11_city-of-york-council-appware.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_el-centro-regional-medical-center-jobscience-inc.yaml](supply-chain/2018-11_el-centro-regional-medical-center-jobscience-inc.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_gate-io-cryptocurrency-exchange-statcounter.yaml](supply-chain/2018-11_gate-io-cryptocurrency-exchange-statcounter.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_huntsville-hospital-in-alabama-jobscience-inc.yaml](supply-chain/2018-11_huntsville-hospital-in-alabama-jobscience-inc.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_marriott-starwood.yaml](supply-chain/2018-11_marriott-starwood.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_nordstrom-not-disclosed.yaml](supply-chain/2018-11_nordstrom-not-disclosed.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_ontario-cannabis-store-canada-post.yaml](supply-chain/2018-11_ontario-cannabis-store-canada-post.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-10_dunkin-donuts-credential-stuffing.yaml](credential-theft/2018-10_dunkin-donuts-credential-stuffing.yaml) | credential-theft | 2018-10-31 |  |  |
| [2018-10_vestacp-not-disclosed.yaml](supply-chain/2018-10_vestacp-not-disclosed.yaml) | supply-chain | 2018-10-01 |  |  |
| [2018-10_a-few-e-commerce-sites-customers-of--shopper-approved.yaml](supply-chain/2018-10_a-few-e-commerce-sites-customers-of--shopper-approved.yaml) | supply-chain | 2018-10-01 |  |  |
| [2018-10_the-indio-water-authority-click2gov.yaml](supply-chain/2018-10_the-indio-water-authority-click2gov.yaml) | supply-chain | 2018-10-01 |  |  |
| [2018-10_many-major-companies-including-amazo-supermicro.yaml](supply-chain/2018-10_many-major-companies-including-amazo-supermicro.yaml) | supply-chain | 2018-10-01 |  |  |
| [2018-10_department-of-defense-pentagon-not-disclosed.yaml](supply-chain/2018-10_department-of-defense-pentagon-not-disclosed.yaml) | supply-chain | 2018-10-01 |  |  |
| [2018-09_foosackly-not-disclosed.yaml](supply-chain/2018-09_foosackly-not-disclosed.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_perth-mint-not-disclosed.yaml](supply-chain/2018-09_perth-mint-not-disclosed.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_blue-cross-blue-shield-of-rhode-isla-not-disclosed.yaml](supply-chain/2018-09_blue-cross-blue-shield-of-rhode-isla-not-disclosed.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_british-airways-still-in-investigation.yaml](supply-chain/2018-09_british-airways-still-in-investigation.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_e-commerce-sites-of-feedify-feedify.yaml](supply-chain/2018-09_e-commerce-sites-of-feedify-feedify.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_all-platfroms-that-use-facebook-logi-facebook.yaml](supply-chain/2018-09_all-platfroms-that-use-facebook-logi-facebook.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_the-conservative-party-uk-crowdcomms.yaml](supply-chain/2018-09_the-conservative-party-uk-crowdcomms.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_university-of-lousville-health-fitness-corp.yaml](supply-chain/2018-09_university-of-lousville-health-fitness-corp.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_the-washoe-county-school-district-edmodo.yaml](supply-chain/2018-09_the-washoe-county-school-district-edmodo.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_wegmans-invermar.yaml](supply-chain/2018-09_wegmans-invermar.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-08_british-airways-magecart.yaml](data-leak/2018-08_british-airways-magecart.yaml) | data-leak | 2018-08-21 | Magecart skimmer |  |
| [2018-08_t-mobile-api-2m.yaml](data-leak/2018-08_t-mobile-api-2m.yaml) | data-leak | 2018-08-20 |  |  |
| [2019-05_amca-quest-labcorp-breach.yaml](supply-chain/2019-05_amca-quest-labcorp-breach.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-08_150-businesses-including-those-in-tr-medcall-healthcare-advis.yaml](supply-chain/2018-08_150-businesses-including-those-in-tr-medcall-healthcare-advis.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-08_a-probably-mexican-government-healt--hova-health.yaml](supply-chain/2018-08_a-probably-mexican-government-healt--hova-health.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-08_air-canada-not-disclosed.yaml](supply-chain/2018-08_air-canada-not-disclosed.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-08_fiserv-affiliated-financial-institut-fiserv.yaml](supply-chain/2018-08_fiserv-affiliated-financial-institut-fiserv.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-08_godaddy-amazon-s3-bucket.yaml](supply-chain/2018-08_godaddy-amazon-s3-bucket.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-08_mention-not-disclosed.yaml](supply-chain/2018-08_mention-not-disclosed.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-08_south-korean-organizations-remote-support-solution.yaml](supply-chain/2018-08_south-korean-organizations-remote-support-solution.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-07_labcorp-samsam-ransomware.yaml](ransomware/2018-07_labcorp-samsam-ransomware.yaml) | ransomware | 2018-07-14 | SamSam ransomware |  |
| [2018-07_timehop-21m-social-tokens.yaml](credential-theft/2018-07_timehop-21m-social-tokens.yaml) | credential-theft | 2018-07-04 |  |  |
| [2018-06_singhealth-apt-breach.yaml](data-leak/2018-06_singhealth-apt-breach.yaml) | data-leak | 2018-06-27 | Custom RAT (remote access tro… |  |
| [2018-06_flipboard-145m-users.yaml](data-leak/2018-06_flipboard-145m-users.yaml) | data-leak | 2018-06-02 |  |  |
| [2018-06_more-than-a-dozen-us-cities-click2gov.yaml](supply-chain/2018-06_more-than-a-dozen-us-cities-click2gov.yaml) | supply-chain | 2018-06-01 |  |  |
| [2018-06_klook-sociaplus.yaml](supply-chain/2018-06_klook-sociaplus.yaml) | supply-chain | 2018-06-01 |  |  |
| [2018-06_exactis-elasticsearch-340m.yaml](data-leak/2018-06_exactis-elasticsearch-340m.yaml) | data-leak | 2018-06-01 |  |  |
| [2018-06_the-central-bank-of-the-bahamas-not-disclosed.yaml](supply-chain/2018-06_the-central-bank-of-the-bahamas-not-disclosed.yaml) | supply-chain | 2018-06-01 |  |  |
| [2018-06_uc-san-diego-health-nuance-communications.yaml](supply-chain/2018-06_uc-san-diego-health-nuance-communications.yaml) | supply-chain | 2018-06-01 |  |  |
| [2018-06_ticketmaster-inbenta.yaml](supply-chain/2018-06_ticketmaster-inbenta.yaml) | supply-chain | 2018-06-01 |  |  |
| [2018-06_reddit-not-disclosed.yaml](supply-chain/2018-06_reddit-not-disclosed.yaml) | supply-chain | 2018-06-01 |  |  |
| [2018-06_whitbread-costa-coffee-premier-inn-pageup.yaml](supply-chain/2018-06_whitbread-costa-coffee-premier-inn-pageup.yaml) | supply-chain | 2018-06-01 |  |  |
| [2018-05_pageup-hr-platform-breach.yaml](supply-chain/2018-05_pageup-hr-platform-breach.yaml) | data-leak | 2018-05-23 |  |  |
| [2018-05_some-fortune-500-firms-corporation-service-comp.yaml](supply-chain/2018-05_some-fortune-500-firms-corporation-service-comp.yaml) | supply-chain | 2018-05-01 |  |  |
| [2018-05_universal-music-group-agilisium.yaml](supply-chain/2018-05_universal-music-group-agilisium.yaml) | supply-chain | 2018-05-01 |  |  |
| [2018-05_chili-s-grill-bar-not-disclosed.yaml](supply-chain/2018-05_chili-s-grill-bar-not-disclosed.yaml) | supply-chain | 2018-05-01 |  |  |
| [2018-04_bestbuy-sears-kmart-delta-not-disclosed.yaml](supply-chain/2018-04_bestbuy-sears-kmart-delta-not-disclosed.yaml) | supply-chain | 2018-04-01 |  |  |
| [2018-09_chegg-s3-root-credentials.yaml](data-leak/2018-09_chegg-s3-root-credentials.yaml) | credential-theft | 2018-04-01 |  |  |
| [2018-03_unitypoint-health-bec-1-4m.yaml](credential-theft/2018-03_unitypoint-health-bec-1-4m.yaml) | credential-theft | 2018-03-14 |  |  |
| [2018-03_cathay-pacific-9-4m-passengers.yaml](data-leak/2018-03_cathay-pacific-9-4m-passengers.yaml) | data-leak | 2018-03-01 |  |  |
| [2018-02_la-times-s3-cryptomining.yaml](other/2018-02_la-times-s3-cryptomining.yaml) | other | 2018-02-09 |  |  |
| [2018-02_under-armour-myfitnesspal.yaml](data-leak/2018-02_under-armour-myfitnesspal.yaml) | data-leak | 2018-02-01 |  |  |
| [2018-02_ticketmaster-inbenta-magecart.yaml](supply-chain/2018-02_ticketmaster-inbenta-magecart.yaml) | supply-chain | 2018-02-01 | Magecart skimmer |  |
| [2018-02_orlando-orthopaedic-center-not-disclosed.yaml](supply-chain/2018-02_orlando-orthopaedic-center-not-disclosed.yaml) | supply-chain | 2018-02-01 |  |  |
| [2018-02_applebee-s-not-disclosed.yaml](supply-chain/2018-02_applebee-s-not-disclosed.yaml) | supply-chain | 2018-02-01 |  |  |
| [2018-01_allscripts-samsam-ehr-outage.yaml](ransomware/2018-01_allscripts-samsam-ehr-outage.yaml) | ransomware | 2018-01-18 | SamSam ransomware |  |
| [2018-01_reddit-mailgun.yaml](supply-chain/2018-01_reddit-mailgun.yaml) | supply-chain | 2018-01-01 |  |  |
| [2026-04_german-bka-revil-gandcrab-leader-unmasked.yaml](ransomware/2026-04_german-bka-revil-gandcrab-leader-unmasked.yaml) | ransomware | 2018-01-01 | REvil (Sodinokibi), GandCrab |  |
| [2019-01_collection1-773m-credential-dump.yaml](credential-theft/2019-01_collection1-773m-credential-dump.yaml) | credential-theft | 2018-01-01 |  |  |
| [2018-01_western-union-not-disclosed.yaml](supply-chain/2018-01_western-union-not-disclosed.yaml) | supply-chain | 2018-01-01 |  |  |
| [2018-01_healthengine-patient-data-lawyers.yaml](data-leak/2018-01_healthengine-patient-data-lawyers.yaml) | data-leak | 2018-01-01 |  |  |
| [2017-11_forever-21-not-disclosed.yaml](supply-chain/2017-11_forever-21-not-disclosed.yaml) | supply-chain | 2017-11-01 |  |  |
| [2017-10_domino-s-australia-a-former-supplier.yaml](supply-chain/2017-10_domino-s-australia-a-former-supplier.yaml) | supply-chain | 2017-10-01 |  |  |
| [2019-08_imperva-rds-snapshot-exposure.yaml](data-leak/2019-08_imperva-rds-snapshot-exposure.yaml) | credential-theft | 2017-10-01 |  |  |
| [2017-10_uber-github.yaml](supply-chain/2017-10_uber-github.yaml) | supply-chain | 2017-10-01 |  |  |
| [2017-10_hyatt-hotels-not-disclosed.yaml](supply-chain/2017-10_hyatt-hotels-not-disclosed.yaml) | supply-chain | 2017-10-01 |  |  |
| [2017-09_samsung-sony-asus-intel-vmware-o2-si-ccleaner.yaml](supply-chain/2017-09_samsung-sony-asus-intel-vmware-o2-si-ccleaner.yaml) | supply-chain | 2017-09-01 |  |  |
| [2017-08_panera-bread-plaintext-api.yaml](data-leak/2017-08_panera-bread-plaintext-api.yaml) | data-leak | 2017-08-01 |  |  |
| [2017-07_hbo-game-of-thrones-15tb.yaml](data-leak/2017-07_hbo-game-of-thrones-15tb.yaml) | data-leak | 2017-07-31 |  |  |
| [2017-07_hard-rock-hotels-casinos-sabre-corp-synxis.yaml](supply-chain/2017-07_hard-rock-hotels-casinos-sabre-corp-synxis.yaml) | supply-chain | 2017-07-01 |  |  |
| [2017-07_verizon-nice-systems.yaml](supply-chain/2017-07_verizon-nice-systems.yaml) | supply-chain | 2017-07-01 |  |  |
| [2017-07_hundreds-of-large-companies-around-t-netsarang.yaml](supply-chain/2017-07_hundreds-of-large-companies-around-t-netsarang.yaml) | supply-chain | 2017-07-01 |  |  |
| [2017-07_equifax-not-disclosed.yaml](supply-chain/2017-07_equifax-not-disclosed.yaml) | supply-chain | 2017-07-01 |  |  |
| [2017-06_notpetya-medoc-maersk-10b.yaml](supply-chain/2017-06_notpetya-medoc-maersk-10b.yaml) | supply-chain | 2017-06-27 | NotPetya (Petya variant / wip… | CVE-2017-0144 |
| [2017-06_deep-root-analytics-198m-voters.yaml](data-leak/2017-06_deep-root-analytics-198m-voters.yaml) | data-leak | 2017-06-01 |  |  |
| [2017-06_many-ukrainen-companies-and-everal-g-medoc.yaml](supply-chain/2017-06_many-ukrainen-companies-and-everal-g-medoc.yaml) | supply-chain | 2017-06-01 |  |  |
| [2017-06_republican-national-committee-deep-root.yaml](supply-chain/2017-06_republican-national-committee-deep-root.yaml) | supply-chain | 2017-06-01 |  |  |
| [2017-06_verizon-nice-systems-s3-14m.yaml](supply-chain/2017-06_verizon-nice-systems-s3-14m.yaml) | data-leak | 2017-06-01 |  |  |
| [2017-05_onelogin-aws-decryption-breach.yaml](credential-theft/2017-05_onelogin-aws-decryption-breach.yaml) | credential-theft | 2017-05-31 |  |  |
| [2017-05_zomato-17m-users.yaml](data-leak/2017-05_zomato-17m-users.yaml) | data-leak | 2017-05-17 |  |  |
| [2017-05_wannacry-nhs-attack.yaml](ransomware/2017-05_wannacry-nhs-attack.yaml) | ransomware | 2017-05-12 | WannaCry ransomware | CVE-2017-0144, CVE-2017-0145 |
| [2017-05_wannacry-eternalblue-global.yaml](ransomware/2017-05_wannacry-eternalblue-global.yaml) | ransomware | 2017-05-12 | WannaCry (WannaCrypt, WannaCr… | CVE-2017-0144, CVE-2017-0145, CVE-2017-… |
| [2017-05_saks-lord-taylor-fin7-pos.yaml](data-leak/2017-05_saks-lord-taylor-fin7-pos.yaml) | data-leak | 2017-05-01 | Carbanak POS RAM-scraping mal… |  |
| [2017-05_bronx-lebanon-hospital-center-in-new-ihealth-innovations.yaml](supply-chain/2017-05_bronx-lebanon-hospital-center-in-new-ihealth-innovations.yaml) | supply-chain | 2017-05-01 |  |  |
| [2017-05_companies-with-mac-user-employees-wh-handbrake.yaml](supply-chain/2017-05_companies-with-mac-user-employees-wh-handbrake.yaml) | supply-chain | 2017-05-01 |  |  |
| [2017-04_wonga-payday-loans-270k.yaml](data-leak/2017-04_wonga-payday-loans-270k.yaml) | data-leak | 2017-04-01 |  |  |
| [2017-03_chipotle-pos-malware.yaml](data-leak/2017-03_chipotle-pos-malware.yaml) | data-leak | 2017-03-24 | POS RAM scraping malware |  |
| [2017-05_equifax.yaml](data-leak/2017-05_equifax.yaml) | data-leak | 2017-03-10 |  | CVE-2017-5638 |
| [2017-03_brand-new-day-not-disclosed.yaml](supply-chain/2017-03_brand-new-day-not-disclosed.yaml) | supply-chain | 2017-03-01 |  |  |
| [2017-02_new-jersey-diamond-institute-for-fer-not-disclosed.yaml](supply-chain/2017-02_new-jersey-diamond-institute-for-fer-not-disclosed.yaml) | supply-chain | 2017-02-01 |  |  |
| [2019-01_desjardins-insider-breach.yaml](data-leak/2019-01_desjardins-insider-breach.yaml) | data-leak | 2017-01-01 |  |  |
| [2018-01_aadhaar-india-1-billion-exposed.yaml](data-leak/2018-01_aadhaar-india-1-billion-exposed.yaml) | data-leak | 2017-01-01 |  |  |
| [2016-11_three-mobile-uk-133k.yaml](data-leak/2016-11_three-mobile-uk-133k.yaml) | data-leak | 2016-11-01 |  |  |
| [2016-10_australian-red-cross-donor-data.yaml](data-leak/2016-10_australian-red-cross-donor-data.yaml) | data-leak | 2016-10-25 |  |  |
| [2016-10_uber-cover-up.yaml](data-leak/2016-10_uber-cover-up.yaml) | data-leak | 2016-10-01 |  |  |
| [2016-10_uber-github-aws-credentials.yaml](credential-theft/2016-10_uber-github-aws-credentials.yaml) | credential-theft | 2016-10-01 |  |  |
| [2016-10_deloitte-email-breach.yaml](data-leak/2016-10_deloitte-email-breach.yaml) | data-leak | 2016-10-01 |  |  |
| [2016-10_adult-friendfinder-lfi-412m.yaml](data-leak/2016-10_adult-friendfinder-lfi-412m.yaml) | data-leak | 2016-10-01 |  |  |
| [2016-08_sabre-synxis-hotel-breach.yaml](supply-chain/2016-08_sabre-synxis-hotel-breach.yaml) | data-leak | 2016-08-10 |  |  |
| [2016-07_datadog-aws-access-keys.yaml](credential-theft/2016-07_datadog-aws-access-keys.yaml) | credential-theft | 2016-07-07 |  |  |
| [2016-07_dark-overlord-healthcare-extortion.yaml](data-leak/2016-07_dark-overlord-healthcare-extortion.yaml) | data-leak | 2016-07-01 |  |  |
| [2016-07_oracle-micros-carbanak.yaml](supply-chain/2016-07_oracle-micros-carbanak.yaml) | supply-chain | 2016-07-01 | Carbanak malware |  |
| [2016-06_banner-health-pos-pivot.yaml](data-leak/2016-06_banner-health-pos-pivot.yaml) | data-leak | 2016-06-17 | POS RAM-scraping malware |  |
| [2016-05_newkirk-products-health-id-cards.yaml](supply-chain/2016-05_newkirk-products-health-id-cards.yaml) | supply-chain | 2016-05-11 |  |  |
| [2016-03_comelec-philippines-55m-voters.yaml](data-leak/2016-03_comelec-philippines-55m-voters.yaml) | data-leak | 2016-03-27 |  |  |
| [2016-03_gru-dnc-podesta-election-hack.yaml](credential-theft/2016-03_gru-dnc-podesta-election-hack.yaml) | credential-theft | 2016-03-19 | X-Agent, X-Tunnel, Mimikatz, … |  |
| [2016-02_snapchat-ceo-fraud-payroll.yaml](credential-theft/2016-02_snapchat-ceo-fraud-payroll.yaml) | credential-theft | 2016-02-26 |  |  |
| [2016-02_bangladesh-bank-swift-heist-81m.yaml](other/2016-02_bangladesh-bank-swift-heist-81m.yaml) | other | 2016-02-04 | EVTDIAG, MSOUTC, MSOUTC (Laza… |  |
| [2016-02_weebly-43m-users.yaml](data-leak/2016-02_weebly-43m-users.yaml) | data-leak | 2016-02-01 |  |  |
| [2016-01_lifeboat-minecraft-7m.yaml](data-leak/2016-01_lifeboat-minecraft-7m.yaml) | data-leak | 2016-01-01 |  |  |
| [2016-01_verizon-enterprise-1-5m.yaml](data-leak/2016-01_verizon-enterprise-1-5m.yaml) | data-leak | 2016-01-01 |  |  |
| [2016-07_vitagene-s3-unprotected-buckets.yaml](credential-theft/2016-07_vitagene-s3-unprotected-buckets.yaml) | data-leak | 2016-01-01 |  |  |
| [2015-11_vtech-children-learning-tablets.yaml](data-leak/2015-11_vtech-children-learning-tablets.yaml) | data-leak | 2015-11-14 |  |  |
| [2015-10_talktalk-sql-injection-157k.yaml](data-leak/2015-10_talktalk-sql-injection-157k.yaml) | data-leak | 2015-10-21 |  |  |
| [2015-10_21st-century-oncology-fbi.yaml](data-leak/2015-10_21st-century-oncology-fbi.yaml) | data-leak | 2015-10-03 |  |  |
| [2015-10_wendys-pos-malware-1025-locations.yaml](supply-chain/2015-10_wendys-pos-malware-1025-locations.yaml) | supply-chain | 2015-10-01 | Carbanak variant POS malware |  |
| [2015-09_experian-t-mobile-15m.yaml](supply-chain/2015-09_experian-t-mobile-15m.yaml) | supply-chain | 2015-09-01 |  |  |
| [2015-09_t-mobile-experian.yaml](supply-chain/2015-09_t-mobile-experian.yaml) | supply-chain | 2015-09-01 |  |  |
| [2015-09_sam-s-club-costco-cvs-riteaid-walmar-pni-digital-media.yaml](supply-chain/2015-09_sam-s-club-costco-cvs-riteaid-walmar-pni-digital-media.yaml) | supply-chain | 2015-09-01 |  |  |
| [2015-07_ashley-madison-impact-team.yaml](data-leak/2015-07_ashley-madison-impact-team.yaml) | data-leak | 2015-07-12 |  |  |
| [2015-07_hacking-team-400gb-dump.yaml](data-leak/2015-07_hacking-team-400gb-dump.yaml) | data-leak | 2015-07-05 |  |  |
| [2015-06_lastpass-first-breach.yaml](data-leak/2015-06_lastpass-first-breach.yaml) | data-leak | 2015-06-12 |  |  |
| [2015-05_medical-informatics-engineering-webchart.yaml](supply-chain/2015-05_medical-informatics-engineering-webchart.yaml) | data-leak | 2015-05-07 |  |  |
| [2015-01_irs-get-transcript-100k.yaml](credential-theft/2015-01_irs-get-transcript-100k.yaml) | credential-theft | 2015-01-01 |  |  |
| [2015-02_anthem-health-insurance-78m.yaml](data-leak/2015-02_anthem-health-insurance-78m.yaml) | data-leak | 2014-12-10 |  |  |
| [2014-11_sony-pictures-wiper-lazarus.yaml](other/2014-11_sony-pictures-wiper-lazarus.yaml) | other | 2014-11-24 | Destover (wiper/backdoor) |  |
| [2014-11_browserstack-aws-access-key-forgotten.yaml](credential-theft/2014-11_browserstack-aws-access-key-forgotten.yaml) | credential-theft | 2014-11-09 |  |  |
| [2014-10_jpmorgan-chase-co-not-disclosed.yaml](supply-chain/2014-10_jpmorgan-chase-co-not-disclosed.yaml) | supply-chain | 2014-10-01 |  |  |
| [2014-09_ucla-health-4-5m-apt.yaml](data-leak/2014-09_ucla-health-4-5m-apt.yaml) | data-leak | 2014-09-01 |  |  |
| [2014-07_lowe-s-safetyfirst-e-driver-fil.yaml](supply-chain/2014-07_lowe-s-safetyfirst-e-driver-fil.yaml) | supply-chain | 2014-07-01 |  |  |
| [2014-07_kbox-singapore-317k-pdpc.yaml](data-leak/2014-07_kbox-singapore-317k-pdpc.yaml) | data-leak | 2014-07-01 |  |  |
| [2015-06_opm-security-clearance-breach.yaml](data-leak/2015-06_opm-security-clearance-breach.yaml) | data-leak | 2014-07-01 |  |  |
| [2014-06_codespaces-aws-ransomware.yaml](other/2014-06_codespaces-aws-ransomware.yaml) | other | 2014-06-17 |  |  |
| [2014-06_jpmorgan-chase-76m-households.yaml](data-leak/2014-06_jpmorgan-chase-76m-households.yaml) | data-leak | 2014-06-01 |  |  |
| [2014-06_dominos-pizza-france-belgium.yaml](data-leak/2014-06_dominos-pizza-france-belgium.yaml) | data-leak | 2014-06-01 |  |  |
| [2014-06_carefirst-bcbs-china-apt.yaml](data-leak/2014-06_carefirst-bcbs-china-apt.yaml) | data-leak | 2014-06-01 |  |  |
| [2014-05_uber-github-aws-50k-drivers.yaml](credential-theft/2014-05_uber-github-aws-50k-drivers.yaml) | credential-theft | 2014-05-12 |  |  |
| [2014-05_premera-blue-cross-apt.yaml](data-leak/2014-05_premera-blue-cross-apt.yaml) | data-leak | 2014-05-05 |  |  |
| [2014-04_heartbleed-openssl-cve-2014-0160.yaml](other/2014-04_heartbleed-openssl-cve-2014-0160.yaml) | other | 2014-04-07 |  | CVE-2014-0160 |
| [2014-04_boston-medical-mdf-transcription-servic.yaml](supply-chain/2014-04_boston-medical-mdf-transcription-servic.yaml) | supply-chain | 2014-04-01 |  |  |
| [2014-09_home-depot-blackpos-56m.yaml](data-leak/2014-09_home-depot-blackpos-56m.yaml) | data-leak | 2014-04-01 | BlackPOS (Kaptoxa) RAM-scraper |  |
| [2014-04_staples-pos-malware.yaml](data-leak/2014-04_staples-pos-malware.yaml) | data-leak | 2014-04-01 | POS RAM-scraping malware |  |
| [2014-04_community-health-systems-apt.yaml](data-leak/2014-04_community-health-systems-apt.yaml) | data-leak | 2014-04-01 | Custom Mimikatz variant |  |
| [2014-05_ebay-employee-credentials-145m.yaml](data-leak/2014-05_ebay-employee-credentials-145m.yaml) | credential-theft | 2014-02-01 |  |  |
| [2014-01_morrisons-insider-100k-employees.yaml](data-leak/2014-01_morrisons-insider-100k-employees.yaml) | data-leak | 2014-01-01 |  |  |
| [2018-11_marriott-starwood.yaml](data-leak/2018-11_marriott-starwood.yaml) | data-leak | 2014-01-01 | Remote Access Trojan (name un… |  |
| [2013-12_excellus-bcbs-apt.yaml](data-leak/2013-12_excellus-bcbs-apt.yaml) | data-leak | 2013-12-23 |  |  |
| [2013-11_target-blackpos.yaml](other/2013-11_target-blackpos.yaml) | other | 2013-11-15 | BlackPOS / Kaptoxa |  |
| [2013-11_toyota-connected-gps-10year-exposure.yaml](data-leak/2013-11_toyota-connected-gps-10year-exposure.yaml) | data-leak | 2013-11-06 |  |  |
| [2013-11_cupid-media-42m-plaintext.yaml](data-leak/2013-11_cupid-media-42m-plaintext.yaml) | data-leak | 2013-11-01 |  |  |
| [2013-11_target-fazio-mechanical-service.yaml](supply-chain/2013-11_target-fazio-mechanical-service.yaml) | supply-chain | 2013-11-01 |  |  |
| [2013-10_adobe-source-code-153m.yaml](data-leak/2013-10_adobe-source-code-153m.yaml) | data-leak | 2013-08-01 |  |  |
| [2013-07_advocate-medical-4m-stolen-laptops.yaml](data-leak/2013-07_advocate-medical-4m-stolen-laptops.yaml) | data-leak | 2013-07-15 |  |  |
| [2016-09_yahoo-3-billion-accounts.yaml](data-leak/2016-09_yahoo-3-billion-accounts.yaml) | credential-theft | 2013-07-01 |  |  |
| [2013-07_rt-jones-capital-not-disclosed.yaml](supply-chain/2013-07_rt-jones-capital-not-disclosed.yaml) | supply-chain | 2013-07-01 |  |  |
| [2018-03_facebook-cambridge-analytica-87m.yaml](data-leak/2018-03_facebook-cambridge-analytica-87m.yaml) | data-leak | 2013-06-01 |  |  |
| [2013-05_michaels-stores-pos-malware.yaml](data-leak/2013-05_michaels-stores-pos-malware.yaml) | data-leak | 2013-05-08 | POS RAM-scraping malware |  |
| [2013-04_livingsocial-50m-accounts.yaml](data-leak/2013-04_livingsocial-50m-accounts.yaml) | data-leak | 2013-04-26 |  |  |
| [2013-02_evernote-50m-breach.yaml](data-leak/2013-02_evernote-50m-breach.yaml) | data-leak | 2013-02-28 |  |  |
| [2013-02_goodwill-ck-systems-pos.yaml](supply-chain/2013-02_goodwill-ck-systems-pos.yaml) | supply-chain | 2013-02-01 | POS RAM-scraping malware |  |
| [2012-08_blizzard-battle-net-14m.yaml](data-leak/2012-08_blizzard-battle-net-14m.yaml) | data-leak | 2012-08-04 |  |  |
| [2016-08_dropbox-credential-reuse-68m.yaml](credential-theft/2016-08_dropbox-credential-reuse-68m.yaml) | credential-theft | 2012-07-01 |  |  |
| [2012-07_disqus-17m-breach-disclosed-2017.yaml](data-leak/2012-07_disqus-17m-breach-disclosed-2017.yaml) | data-leak | 2012-07-01 |  |  |
| [2012-06_linkedin-unsalted-sha1-117m.yaml](data-leak/2012-06_linkedin-unsalted-sha1-117m.yaml) | credential-theft | 2012-05-01 |  |  |
| [2012-01_facebook-plaintext-passwords-600m.yaml](data-leak/2012-01_facebook-plaintext-passwords-600m.yaml) | data-leak | 2012-01-01 |  |  |
| [2012-03_global-payments-card-processor.yaml](data-leak/2012-03_global-payments-card-processor.yaml) | data-leak | 2012-01-01 |  |  |
| [2011-04_sony-psn-76m-offline.yaml](data-leak/2011-04_sony-psn-76m-offline.yaml) | data-leak | 2011-04-17 |  |  |
| [2011-03_rsa-securid-token-seed-theft.yaml](other/2011-03_rsa-securid-token-seed-theft.yaml) | other | 2011-03-01 |  | CVE-2011-0609 |
| [2009-12_rockyou-plaintext-passwords-32m.yaml](data-leak/2009-12_rockyou-plaintext-passwords-32m.yaml) | data-leak | 2009-11-01 |  |  |
| [2009-01_twitter-admin-panel-brute-force.yaml](credential-theft/2009-01_twitter-admin-panel-brute-force.yaml) | credential-theft | 2009-01-05 |  |  |
| [2016-05_myspace-360m-sha1-unsalted.yaml](data-leak/2016-05_myspace-360m-sha1-unsalted.yaml) | data-leak | 2008-01-01 |  |  |
| [2009-01_heartland-payment-systems-130m.yaml](data-leak/2009-01_heartland-payment-systems-130m.yaml) | data-leak | 2007-12-01 |  |  |
| [2008-03_hannaford-pos-malware-4m.yaml](data-leak/2008-03_hannaford-pos-malware-4m.yaml) | data-leak | 2007-12-01 |  |  |
| [2006-08_aol-search-data-leak-650k.yaml](data-leak/2006-08_aol-search-data-leak-650k.yaml) | data-leak | 2006-08-04 |  |  |
| [2006-05_veterans-affairs-laptop-26m.yaml](data-leak/2006-05_veterans-affairs-laptop-26m.yaml) | data-leak | 2006-05-03 |  |  |
| [2007-01_tjx-wardriving-wifi-94m.yaml](data-leak/2007-01_tjx-wardriving-wifi-94m.yaml) | data-leak | 2005-07-01 |  |  |
| [2004-01_mydoom-worm-fastest-email.yaml](other/2004-01_mydoom-worm-fastest-email.yaml) | other | 2004-01-26 | MyDoom (W32/Mydoom, Novarg, M… |  |
| [2005-02_choicepoint-fraud-163k.yaml](data-leak/2005-02_choicepoint-fraud-163k.yaml) | data-leak | 2004-01-01 |  |  |
| [2005-06_cardsystems-sql-injection-40m.yaml](data-leak/2005-06_cardsystems-sql-injection-40m.yaml) | data-leak | 2004-01-01 |  |  |
| [2003-01_sql-slammer-worm-75k-hosts.yaml](other/2003-01_sql-slammer-worm-75k-hosts.yaml) | other | 2003-01-25 | SQL Slammer (W32/SQLSlam, Sap… | CVE-2002-0649 |
| [2004-10_shadowcrew-operation-firewall.yaml](credential-theft/2004-10_shadowcrew-operation-firewall.yaml) | credential-theft | 2002-08-01 |  |  |
| [2001-09_nimda-multi-vector-worm.yaml](other/2001-09_nimda-multi-vector-worm.yaml) | other | 2001-09-18 | Nimda (W32/Nimda, 'admin' rev… | CVE-2001-0333, CVE-2001-0507 |
| [2001-07_code-red-iis-worm.yaml](other/2001-07_code-red-iis-worm.yaml) | other | 2001-07-13 | Code Red (W32/CodeRed) | CVE-2001-0500 |
| [2002-03_gary-mckinnon-military-breach.yaml](data-leak/2002-03_gary-mckinnon-military-breach.yaml) | data-leak | 2001-03-01 |  |  |
| [2000-05_iloveyou-vbs-worm-10b.yaml](other/2000-05_iloveyou-vbs-worm-10b.yaml) | other | 2000-05-04 | ILOVEYOU (VBS/LoveLetter) |  |
| [1999-12_cd-universe-maxus-extortion.yaml](credential-theft/1999-12_cd-universe-maxus-extortion.yaml) | credential-theft | 1999-12-01 |  |  |
| [1999-08_jonathan-james-nasa-dod-breach.yaml](data-leak/1999-08_jonathan-james-nasa-dod-breach.yaml) | data-leak | 1999-08-01 |  |  |
| [1999-03_melissa-virus-email-worm.yaml](other/1999-03_melissa-virus-email-worm.yaml) | other | 1999-03-26 | Melissa (W97M/Melissa) |  |
| [1998-02_solar-sunrise-dod-teen-hackers.yaml](data-leak/1998-02_solar-sunrise-dod-teen-hackers.yaml) | data-leak | 1998-02-01 |  |  |
| [1996-10_moonlight-maze-russian-espionage.yaml](data-leak/1996-10_moonlight-maze-russian-espionage.yaml) | data-leak | 1996-10-01 |  |  |

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
