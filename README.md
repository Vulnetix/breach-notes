# breach-notes

Structured YAML records of breach reports, advisories, and cyber incidents.

**Last updated:** 2026-04-10  **Total records:** 537

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total incidents | 537 |
| With CVE/GHSA references | 47 (9%) |
| Unique CVEs/GHSAs | 59 |
| With malware identified | 160 (30%) |
| Supply chain claimed | 91 (17%) |
| Unique vendor products | 308 |
| Median disclosure lag (days) | 40 |
| Max disclosure lag (days) | 3474 |

## Incidents by Category

| Category | Count | % |
|----------|-------|---|
| ransomware | 91 | 17% |
| data-leak | 237 | 44% |
| supply-chain | 46 | 9% |
| credential-theft | 90 | 17% |
| other | 73 | 14% |

## Incidents by Year

| Year | Count |
|------|-------|
| 2000 | 1 |
| 2001 | 3 |
| 2002 | 1 |
| 2003 | 3 |
| 2004 | 3 |
| 2005 | 8 |
| 2006 | 2 |
| 2007 | 2 |
| 2008 | 3 |
| 2009 | 5 |
| 2010 | 2 |
| 2011 | 10 |
| 2012 | 14 |
| 2013 | 17 |
| 2014 | 24 |
| 2015 | 10 |
| 2016 | 19 |
| 2017 | 17 |
| 2018 | 10 |
| 2019 | 14 |
| 2020 | 25 |
| 2021 | 32 |
| 2022 | 26 |
| 2023 | 47 |
| 2024 | 103 |
| 2025 | 97 |
| 2026 | 34 |

## Top Malware Families

| Malware | Incidents |
|---------|----------|
| ALPHV/BlackCat | 6 |
| POS RAM-scraping | 6 |
| Qilin | 5 |
| RansomHub | 5 |
| Black Basta | 4 |
| DragonForce | 4 |
| Hunters International | 4 |
| Interlock | 4 |
| LockBit | 4 |
| POS | 4 |
| TeamPCP Cloud Stealer | 4 |
| BlackSuit | 3 |
| INC Ransom | 3 |
| Medusa | 3 |
| POS malware (Track data scraper) | 3 |

## CVE / GHSA References

```
CVE-2001-0333
CVE-2001-0500
CVE-2001-0507
CVE-2002-0649
CVE-2005-1983
CVE-2010-0249
CVE-2010-2568
CVE-2010-2729
CVE-2010-2772
CVE-2011-0609
CVE-2014-0160
CVE-2017-0143
CVE-2017-0144
CVE-2017-0145
CVE-2017-5638
CVE-2019-11510
CVE-2020-10148
CVE-2020-5741
CVE-2020-8260
CVE-2021-22893
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
| CWE-284: Improper Access Control | 15 |
| CWE-307: Improper Restriction of Excessive Authentication Attempts (stolen credentials reused against Snowflake tenant with no MFA) | 5 |
| CWE-522: Insufficiently Protected Credentials (infostealer-harvested credentials, no MFA on Snowflake) | 2 |
| 0ktapus / Scattered Spider threat actors phished an employee of an unnamed third-party vendor with access to DoorDash systems via SMS phishing (smishing), then used the stolen credentials to access DoorDash's internal tools and customer data | 1 |
| A Columbia University physician decommissioned a personal server that was connected to the shared Columbia/NYP network without following proper procedures; the server lacked server-level firewall protections, resulting in approximately 6,800 patient records becoming accessible on the internet | 1 |
| A Dropbox employee reused their LinkedIn password for their Dropbox work account; when the 2012 LinkedIn breach exposed that password, attackers used it to log into the employee's Dropbox work account, which contained a document with hashed Dropbox user passwords | 1 |
| A First Republic Bank employee with legitimate AWS access used their credentials to exfiltrate customer data from AWS-hosted banking systems | 1 |
| A VA data analyst took home a VA-issued laptop and external hard drive containing 26.5 million veterans' PII without authorization; the equipment was stolen from his home in a burglary | 1 |
| A bug in the Redis client library (redis-py) used by OpenAI caused race conditions in connection pooling under high load, resulting in users being served cached data from other users' sessions — exposing conversation titles and personal payment information | 1 |
| A contract worker with knowledge of the credentials used Chegg's AWS root account credentials and shared access keys to access an S3 bucket containing user data, exfiltrating records for 40 million users | 1 |
| A former business partner of Ascension Health mistakenly included Ascension patient data in a data file sent to a software vendor for testing purposes; that vendor's systems were then compromised by an attacker who accessed the data | 1 |
| A fraudster posing as a legitimate client of Experian South Africa used social engineering to convince Experian to provide a dataset containing personal information; the attacker presented fraudulent credentials and business information to obtain the data transfer | 1 |
| A group calling themselves 'The Shadow Brokers' claimed to have stolen cyberweapons from the NSA's Tailored Access Operations (TAO) unit; released NSA exploit tools in staged leaks from August 2016 through April 2017; method of original exfiltration from NSA never officially confirmed | 1 |
| A malicious insider (a Desjardins employee) collected and exfiltrated personal data of members over a period of approximately 26 months, sharing the data with unauthorized third parties outside the organization | 1 |
| A publicly accessible Jenkins CI/CD server misconfiguration at CommuteAir exposed AWS credentials, which a security researcher used to access multiple S3 buckets — including one containing the TSA's No Fly List | 1 |

## Incident Index

| File | Category | Breach Date | Malware | CVEs |
|------|----------|-------------|---------|------|
| [2026-04_chipsoft-netherlands-hospitals.yaml](ransomware/2026-04_chipsoft-netherlands-hospitals.yaml) | ransomware | 2026-04-07 |  |  |
| [2026-04_cisco-trivy-teamPCP-source-code.yaml](supply-chain/2026-04_cisco-trivy-teamPCP-source-code.yaml) | supply-chain | 2026-04-03 | TeamPCP Cloud Stealer |  |
| [2026-04_drift-protocol-dprk-285m.yaml](other/2026-04_drift-protocol-dprk-285m.yaml) | other | 2026-04-01 |  |  |
| [2026-03_axios-npm-sapphire-sleet-dprk.yaml](supply-chain/2026-03_axios-npm-sapphire-sleet-dprk.yaml) | supply-chain | 2026-03-31 | Sapphire Sleet RAT |  |
| [2026-03_litellm-pypi-mercor-teamPCP.yaml](supply-chain/2026-03_litellm-pypi-mercor-teamPCP.yaml) | supply-chain | 2026-03-27 |  |  |
| [2026-03_teamPCP-telnyx-pypi.yaml](supply-chain/2026-03_teamPCP-telnyx-pypi.yaml) | supply-chain | 2026-03-27 | TeamPCP Cloud Stealer |  |
| [2026-03_die-linke-qilin-germany.yaml](ransomware/2026-03_die-linke-qilin-germany.yaml) | ransomware | 2026-03-26 | Qilin |  |
| [2026-03_teamPCP-checkmarx-kics.yaml](supply-chain/2026-03_teamPCP-checkmarx-kics.yaml) | supply-chain | 2026-03-21 | TeamPCP Cloud Stealer |  |
| [2026-03_lapd-city-attorney-worldleaks.yaml](data-leak/2026-03_lapd-city-attorney-worldleaks.yaml) | data-leak | 2026-03-20 |  |  |
| [2026-03_bitcoin-depot-crypto-theft.yaml](other/2026-03_bitcoin-depot-crypto-theft.yaml) | other | 2026-03-20 |  |  |
| [2026-03_teamPCP-trivy-github-actions.yaml](supply-chain/2026-03_teamPCP-trivy-github-actions.yaml) | supply-chain | 2026-03-19 | TeamPCP Cloud Stealer | CVE-2026-33634 |
| [2026-03_european-commission-shinyhunters-aws.yaml](data-leak/2026-03_european-commission-shinyhunters-aws.yaml) | data-leak | 2026-03-19 |  |  |
| [2026-03_aura-identity-shinyhunters-vishing.yaml](data-leak/2026-03_aura-identity-shinyhunters-vishing.yaml) | data-leak | 2026-03-17 |  |  |
| [2026-03_carecloud-ehr-breach.yaml](data-leak/2026-03_carecloud-ehr-breach.yaml) | data-leak | 2026-03-16 |  |  |
| [2026-03_crunchyroll-bpo-okta-breach.yaml](data-leak/2026-03_crunchyroll-bpo-okta-breach.yaml) | data-leak | 2026-03-12 | infostealer (unspecified) |  |
| [2026-03_stryker-handala-intune-wiper.yaml](other/2026-03_stryker-handala-intune-wiper.yaml) | other | 2026-03-11 |  |  |
| [2026-03_unc6426-nx-npm-aws-takeover.yaml](supply-chain/2026-03_unc6426-nx-npm-aws-takeover.yaml) | supply-chain | 2026-03-01 |  |  |
| [2026-04_anodot-shinyhunters-snowflake-tokens.yaml](credential-theft/2026-04_anodot-shinyhunters-snowflake-tokens.yaml) | credential-theft | 2026-03-01 |  |  |
| [2026-02_malaysia-airlines-qilin.yaml](ransomware/2026-02_malaysia-airlines-qilin.yaml) | ransomware | 2026-02-26 | Qilin |  |
| [2026-02_ummc-medusa-ransomware.yaml](ransomware/2026-02_ummc-medusa-ransomware.yaml) | ransomware | 2026-02-19 | Medusa |  |
| [2026-02_fbi-dcsnet-china-surveillance.yaml](other/2026-02_fbi-dcsnet-china-surveillance.yaml) | other | 2026-02-17 |  |  |
| [2026-02_odido-dutch-telecom-shinyhunters.yaml](data-leak/2026-02_odido-dutch-telecom-shinyhunters.yaml) | data-leak | 2026-02-07 |  |  |
| [2026-02_bridgepay-ransomware-outage.yaml](ransomware/2026-02_bridgepay-ransomware-outage.yaml) | ransomware | 2026-02-06 |  |  |
| [2026-02_hims-hers-zendesk-shinyhunters.yaml](data-leak/2026-02_hims-hers-zendesk-shinyhunters.yaml) | data-leak | 2026-02-04 |  |  |
| [2026-02_sears-home-services-chatbot-exposure.yaml](data-leak/2026-02_sears-home-services-chatbot-exposure.yaml) | data-leak | 2026-02-03 |  |  |
| [2026-03_lexisnexis-law-firm-breach.yaml](data-leak/2026-03_lexisnexis-law-firm-breach.yaml) | data-leak | 2026-02-01 |  |  |
| [2026-02_cargurus-shinyhunters-social-engineering.yaml](data-leak/2026-02_cargurus-shinyhunters-social-engineering.yaml) | data-leak | 2026-02-01 |  |  |
| [2026-01_glassworm-open-vsx-extensions.yaml](supply-chain/2026-01_glassworm-open-vsx-extensions.yaml) | supply-chain | 2026-01-30 | GlassWorm |  |
| [2026-01_starbucks-partner-central-phishing.yaml](credential-theft/2026-01_starbucks-partner-central-phishing.yaml) | credential-theft | 2026-01-19 |  |  |
| [2026-01_betterment-shinyhunters-vishing.yaml](data-leak/2026-01_betterment-shinyhunters-vishing.yaml) | data-leak | 2026-01-09 |  |  |
| [2026-01_crunchbase-shinyhunters-vishing.yaml](data-leak/2026-01_crunchbase-shinyhunters-vishing.yaml) | data-leak | 2026-01-09 |  |  |
| [2026-01_bumble-match-shinyhunters-vishing.yaml](data-leak/2026-01_bumble-match-shinyhunters-vishing.yaml) | data-leak | 2026-01-01 |  |  |
| [2026-01_figure-fintech-shinyhunters-vishing.yaml](data-leak/2026-01_figure-fintech-shinyhunters-vishing.yaml) | data-leak | 2026-01-01 |  |  |
| [2026-03_telus-digital-shinyhunters.yaml](data-leak/2026-03_telus-digital-shinyhunters.yaml) | data-leak | 2026-01-01 |  |  |
| [2025-12_sedgwick-government-tridentlocker.yaml](ransomware/2025-12_sedgwick-government-tridentlocker.yaml) | ransomware | 2025-12-31 | TridentLocker |  |
| [2025-12_eurail-aws-s3-passport-breach.yaml](data-leak/2025-12_eurail-aws-s3-passport-breach.yaml) | data-leak | 2025-12-26 |  |  |
| [2026-01_navia-benefit-solutions-bola.yaml](data-leak/2026-01_navia-benefit-solutions-bola.yaml) | data-leak | 2025-12-22 |  |  |
| [2025-12_conde-nast-wired-idor-breach.yaml](data-leak/2025-12_conde-nast-wired-idor-breach.yaml) | data-leak | 2025-12-20 |  |  |
| [2025-12_soundcloud-shinyhunters-vishing.yaml](data-leak/2025-12_soundcloud-shinyhunters-vishing.yaml) | data-leak | 2025-12-15 |  |  |
| [2026-01_ledger-global-e-third-party.yaml](data-leak/2026-01_ledger-global-e-third-party.yaml) | data-leak | 2025-12-01 |  |  |
| [2026-01_brightspeed-crimson-collective.yaml](data-leak/2026-01_brightspeed-crimson-collective.yaml) | data-leak | 2025-12-01 |  |  |
| [2026-02_cegedim-sante-monlogicielmedical.yaml](data-leak/2026-02_cegedim-sante-monlogicielmedical.yaml) | data-leak | 2025-12-01 |  |  |
| [2025-11_openai-mixpanel-vendor.yaml](other/2025-11_openai-mixpanel-vendor.yaml) | other | 2025-11-26 |  |  |
| [2025-11_situsamc-banks-breach.yaml](data-leak/2025-11_situsamc-banks-breach.yaml) | data-leak | 2025-11-12 |  |  |
| [2025-11_idmerit-mongodb-kyc-exposure.yaml](data-leak/2025-11_idmerit-mongodb-kyc-exposure.yaml) | data-leak | 2025-11-11 |  |  |
| [2025-11_coupang-insider-33m-korea.yaml](data-leak/2025-11_coupang-insider-33m-korea.yaml) | data-leak | 2025-11-08 |  |  |
| [2025-12_freedom-mobile-third-party.yaml](data-leak/2025-12_freedom-mobile-third-party.yaml) | data-leak | 2025-11-01 |  |  |
| [2025-12_marquis-software-74-banks.yaml](data-leak/2025-12_marquis-software-74-banks.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-11_cbo-china-hack.yaml](other/2025-11_cbo-china-hack.yaml) | other | 2025-11-01 |  |  |
| [2025-11_under-armour-everest-ransomware.yaml](ransomware/2025-11_under-armour-everest-ransomware.yaml) | ransomware | 2025-11-01 | Everest |  |
| [2025-10_doordash-social-engineering.yaml](data-leak/2025-10_doordash-social-engineering.yaml) | data-leak | 2025-10-25 |  |  |
| [2025-11_mixpanel-analytics-multi-company.yaml](supply-chain/2025-11_mixpanel-analytics-multi-company.yaml) | supply-chain | 2025-10-15 |  |  |
| [2025-11_iberia-iag-loyalty-breach.yaml](data-leak/2025-11_iberia-iag-loyalty-breach.yaml) | data-leak | 2025-10-15 |  |  |
| [2025-10_docketwise-credential-immigration.yaml](data-leak/2025-10_docketwise-credential-immigration.yaml) | data-leak | 2025-10-01 |  |  |
| [2025-11_openai-mixpanel-analytics-leak.yaml](data-leak/2025-11_openai-mixpanel-analytics-leak.yaml) | data-leak | 2025-10-01 |  |  |
| [2025-10_discord-third-party-customer-service-55m.yaml](data-leak/2025-10_discord-third-party-customer-service-55m.yaml) | data-leak | 2025-10-01 |  |  |
| [2025-11_washington-post-oracle-ebs-breach.yaml](data-leak/2025-11_washington-post-oracle-ebs-breach.yaml) | data-leak | 2025-10-01 |  | CVE-2025-61882 |
| [2025-10_redhat-gitlab-crimson-collective.yaml](supply-chain/2025-10_redhat-gitlab-crimson-collective.yaml) | supply-chain | 2025-10-01 |  |  |
| [2025-09_insightin-health-goanywhere-medusa.yaml](ransomware/2025-09_insightin-health-goanywhere-medusa.yaml) | ransomware | 2025-09-17 | Medusa |  |
| [2025-10_mango-marketing-provider-breach.yaml](data-leak/2025-10_mango-marketing-provider-breach.yaml) | data-leak | 2025-09-15 |  |  |
| [2025-09_shai-hulud-npm-worm.yaml](supply-chain/2025-09_shai-hulud-npm-worm.yaml) | supply-chain | 2025-09-14 | Shai-Hulud |  |
| [2025-09_npm-chalk-debug-phishing.yaml](supply-chain/2025-09_npm-chalk-debug-phishing.yaml) | supply-chain | 2025-09-08 | Browser crypto wallet stealer… |  |
| [2025-10_renault-dacia-uk-third-party.yaml](data-leak/2025-10_renault-dacia-uk-third-party.yaml) | data-leak | 2025-09-01 |  |  |
| [2025-09_wynn-resorts-oracle-shinyhunters.yaml](data-leak/2025-09_wynn-resorts-oracle-shinyhunters.yaml) | data-leak | 2025-09-01 |  |  |
| [2025-09_swissborg-kiln-staking-41m-sol.yaml](data-leak/2025-09_swissborg-kiln-staking-41m-sol.yaml) | other | 2025-09-01 |  |  |
| [2025-09_jaguar-land-rover-scattered-lapsus.yaml](ransomware/2025-09_jaguar-land-rover-scattered-lapsus.yaml) | ransomware | 2025-08-31 |  |  |
| [2025-08_university-hawaii-cancer-center.yaml](ransomware/2025-08_university-hawaii-cancer-center.yaml) | ransomware | 2025-08-31 |  |  |
| [2025-08_minnesota-dhs-fei-systems-insider.yaml](data-leak/2025-08_minnesota-dhs-fei-systems-insider.yaml) | data-leak | 2025-08-28 |  |  |
| [2025-08_insight-hospital-chicago-termite.yaml](ransomware/2025-08_insight-hospital-chicago-termite.yaml) | ransomware | 2025-08-22 | Termite |  |
| [2025-09_lner-third-party-vendor.yaml](data-leak/2025-09_lner-third-party-vendor.yaml) | data-leak | 2025-08-15 |  |  |
| [2025-09_wealthsimple-third-party-breach.yaml](data-leak/2025-09_wealthsimple-third-party-breach.yaml) | data-leak | 2025-08-15 |  |  |
| [2025-08_marquis-software-akira-banks.yaml](ransomware/2025-08_marquis-software-akira-banks.yaml) | ransomware | 2025-08-14 | Akira | CVE-2024-40766 |
| [2025-08_pennsylvania-ag-inc-ransom.yaml](ransomware/2025-08_pennsylvania-ag-inc-ransom.yaml) | ransomware | 2025-08-09 | INC Ransom | CVE-2025-5777 |
| [2025-08_clop-oracle-ebs-education.yaml](supply-chain/2025-08_clop-oracle-ebs-education.yaml) | supply-chain | 2025-08-09 |  | CVE-2025-61882, CVE-2025-61884 |
| [2025-08_salesloft-drift-oauth-salesforce.yaml](supply-chain/2025-08_salesloft-drift-oauth-salesforce.yaml) | supply-chain | 2025-08-08 |  |  |
| [2025-08_bouygues-telecom-france-6m.yaml](data-leak/2025-08_bouygues-telecom-france-6m.yaml) | data-leak | 2025-08-04 |  |  |
| [2025-09_chess-com-file-transfer-breach.yaml](data-leak/2025-09_chess-com-file-transfer-breach.yaml) | data-leak | 2025-08-01 |  |  |
| [2025-09_harrods-third-party-breach.yaml](data-leak/2025-09_harrods-third-party-breach.yaml) | data-leak | 2025-08-01 |  |  |
| [2025-09_canada-2keys-government-accounts.yaml](data-leak/2025-09_canada-2keys-government-accounts.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_university-phoenix-oracle-ebs-clop.yaml](data-leak/2025-08_university-phoenix-oracle-ebs-clop.yaml) | data-leak | 2025-08-01 |  | CVE-2025-61882 |
| [2025-07_transunion-salesforce-unc6395.yaml](data-leak/2025-07_transunion-salesforce-unc6395.yaml) | data-leak | 2025-07-28 |  |  |
| [2025-07_st-paul-minnesota-interlock.yaml](ransomware/2025-07_st-paul-minnesota-interlock.yaml) | ransomware | 2025-07-25 | Interlock ransomware |  |
| [2025-07_allianz-life-shiny-hunters.yaml](data-leak/2025-07_allianz-life-shiny-hunters.yaml) | data-leak | 2025-07-16 |  |  |
| [2025-07_ingram-micro-safepay.yaml](ransomware/2025-07_ingram-micro-safepay.yaml) | ransomware | 2025-07-02 | SafePay |  |
| [2025-08_pandora-chanel-salesforce-shinyhunters.yaml](data-leak/2025-08_pandora-chanel-salesforce-shinyhunters.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-08_transunion-salesforce-44m.yaml](data-leak/2025-08_transunion-salesforce-44m.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-08_cisco-salesforce-shinyhunters.yaml](data-leak/2025-08_cisco-salesforce-shinyhunters.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-08_air-france-klm-salesforce.yaml](data-leak/2025-08_air-france-klm-salesforce.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-09_stellantis-salesforce-shinyhunters.yaml](data-leak/2025-09_stellantis-salesforce-shinyhunters.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_qantas-salesforce-shinyhunters-vishing.yaml](data-leak/2025-07_qantas-salesforce-shinyhunters-vishing.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_paypal-working-capital-code-error.yaml](data-leak/2025-07_paypal-working-capital-code-error.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_mcdonalds-paradox-ai-chatbot-64m.yaml](data-leak/2025-07_mcdonalds-paradox-ai-chatbot-64m.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_700credit-api-automotive-dealers.yaml](data-leak/2025-07_700credit-api-automotive-dealers.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-06_aflac-scattered-spider.yaml](data-leak/2025-06_aflac-scattered-spider.yaml) | data-leak | 2025-06-12 |  |  |
| [2025-06_prosper-marketplace-credential-17m.yaml](data-leak/2025-06_prosper-marketplace-credential-17m.yaml) | data-leak | 2025-06-01 |  |  |
| [2025-10_vietnam-airlines-salesforce-scattered-lapsus.yaml](data-leak/2025-10_vietnam-airlines-salesforce-scattered-lapsus.yaml) | data-leak | 2025-06-01 |  |  |
| [2025-05_farmers-insurance-salesforce-shinyhunters.yaml](data-leak/2025-05_farmers-insurance-salesforce-shinyhunters.yaml) | data-leak | 2025-05-29 |  |  |
| [2025-05_kettering-health-interlock.yaml](ransomware/2025-05_kettering-health-interlock.yaml) | ransomware | 2025-05-20 | Interlock ransomware |  |
| [2025-05_covenant-health-qilin.yaml](ransomware/2025-05_covenant-health-qilin.yaml) | ransomware | 2025-05-18 | Qilin |  |
| [2025-05_dragonforce-simplehelp-msp.yaml](supply-chain/2025-05_dragonforce-simplehelp-msp.yaml) | supply-chain | 2025-05-01 | DragonForce ransomware | CVE-2024-57726, CVE-2024-57727, CVE-202… |
| [2025-06_sharp-healthcare-episource-breach.yaml](supply-chain/2025-06_sharp-healthcare-episource-breach.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_marks-spencer-tcs-breach.yaml](data-leak/2025-05_marks-spencer-tcs-breach.yaml) | data-leak | 2025-04-22 | DragonForce ransomware |  |
| [2025-04_sk-telecom-bpfdoor-sim-data.yaml](other/2025-04_sk-telecom-bpfdoor-sim-data.yaml) | other | 2025-04-18 | BPFDoor; Tiny Shell |  |
| [2025-04_ericsson-us-third-party-breach.yaml](data-leak/2025-04_ericsson-us-third-party-breach.yaml) | data-leak | 2025-04-17 |  |  |
| [2025-05_legal-aid-agency-uk-2000-providers.yaml](data-leak/2025-05_legal-aid-agency-uk-2000-providers.yaml) | data-leak | 2025-04-01 |  |  |
| [2025-04_coop-harrods-dragonforce.yaml](ransomware/2025-04_coop-harrods-dragonforce.yaml) | ransomware | 2025-04-01 | DragonForce ransomware |  |
| [2025-05_nationwide-recovery-services-healthcare-cluster.yaml](supply-chain/2025-05_nationwide-recovery-services-healthcare-cluster.yaml) | supply-chain | 2025-04-01 |  |  |
| [2025-05_adidas-customer-service-breach.yaml](data-leak/2025-05_adidas-customer-service-breach.yaml) | data-leak | 2025-04-01 |  |  |
| [2025-04_royal-mail-spectos-breach.yaml](data-leak/2025-04_royal-mail-spectos-breach.yaml) | data-leak | 2025-03-29 |  |  |
| [2025-04_davita-interlock.yaml](ransomware/2025-04_davita-interlock.yaml) | ransomware | 2025-03-24 | Interlock ransomware |  |
| [2025-04_ivanti-connect-secure-cve-2025-22457.yaml](other/2025-04_ivanti-connect-secure-cve-2025-22457.yaml) | other | 2025-03-15 | TRAILBLAZE (in-memory dropper… | CVE-2025-22457 |
| [2025-03_yale-new-haven-health.yaml](ransomware/2025-03_yale-new-haven-health.yaml) | ransomware | 2025-03-08 |  |  |
| [2025-03_berkeley-research-group-chaos.yaml](ransomware/2025-03_berkeley-research-group-chaos.yaml) | ransomware | 2025-02-28 | Chaos ransomware |  |
| [2025-02_bybit-safe-wallet-lazarus.yaml](supply-chain/2025-02_bybit-safe-wallet-lazarus.yaml) | supply-chain | 2025-02-21 |  |  |
| [2025-02_opexus-insider-federal.yaml](other/2025-02_opexus-insider-federal.yaml) | other | 2025-02-18 |  |  |
| [2025-03_streamelements-gooten-breach.yaml](supply-chain/2025-03_streamelements-gooten-breach.yaml) | supply-chain | 2025-02-15 |  |  |
| [2025-02_anne-arundel-dermatology-breach.yaml](data-leak/2025-02_anne-arundel-dermatology-breach.yaml) | data-leak | 2025-02-14 |  |  |
| [2025-04_marks-and-spencer.yaml](ransomware/2025-04_marks-and-spencer.yaml) | ransomware | 2025-02-01 | DragonForce ransomware |  |
| [2025-01_western-sydney-university.yaml](data-leak/2025-01_western-sydney-university.yaml) | data-leak | 2025-01-28 |  |  |
| [2025-02_episource-optum-unitedhealth.yaml](ransomware/2025-02_episource-optum-unitedhealth.yaml) | ransomware | 2025-01-27 |  |  |
| [2025-01_frederick-health-ransomware.yaml](ransomware/2025-01_frederick-health-ransomware.yaml) | ransomware | 2025-01-27 |  |  |
| [2025-01_oracle-health-cerner-hospitals.yaml](supply-chain/2025-01_oracle-health-cerner-hospitals.yaml) | supply-chain | 2025-01-22 |  | CVE-2025-30154 |
| [2025-01_simonmed-imaging-medusa.yaml](ransomware/2025-01_simonmed-imaging-medusa.yaml) | ransomware | 2025-01-21 | Medusa |  |
| [2025-06_heritage-foundation-doge.yaml](data-leak/2025-06_heritage-foundation-doge.yaml) | other | 2025-01-20 |  |  |
| [2025-05_magento-tigren-meetanshi-extensions.yaml](supply-chain/2025-05_magento-tigren-meetanshi-extensions.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-05_coinbase-insider-bribery.yaml](credential-theft/2025-05_coinbase-insider-bribery.yaml) | credential-theft | 2025-01-01 |  |  |
| [2025-01_tata-technologies-hunters-intl.yaml](ransomware/2025-01_tata-technologies-hunters-intl.yaml) | ransomware | 2025-01-01 | Hunters International ransomw… |  |
| [2025-05_trimble-cityworks-us-local-govts.yaml](supply-chain/2025-05_trimble-cityworks-us-local-govts.yaml) | supply-chain | 2025-01-01 |  | CVE-2025-0994 |
| [2025-06_coinbase-taskus-customer-support.yaml](data-leak/2025-06_coinbase-taskus-customer-support.yaml) | data-leak | 2025-01-01 |  |  |
| [2025-01_talktalk-csg-ascendon-subscriber.yaml](supply-chain/2025-01_talktalk-csg-ascendon-subscriber.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-02_grubhub-third-party-vendor.yaml](data-leak/2025-02_grubhub-third-party-vendor.yaml) | data-leak | 2025-01-01 |  |  |
| [2024-12_powerschool-extortion-followon.yaml](data-leak/2024-12_powerschool-extortion-followon.yaml) | data-leak | 2024-12-19 |  |  |
| [2024-12_powerschool-sis.yaml](supply-chain/2024-12_powerschool-sis.yaml) | supply-chain | 2024-12-19 |  |  |
| [2025-01_ivanti-connect-secure-cve-2025-0282.yaml](other/2025-01_ivanti-connect-secure-cve-2025-0282.yaml) | other | 2024-12-15 | SPAWN ecosystem (SPAWNANT ins… | CVE-2025-0282, CVE-2025-0283 |
| [2024-12_monroe-university.yaml](data-leak/2024-12_monroe-university.yaml) | data-leak | 2024-12-09 |  |  |
| [2024-12_ultralytics-pypi-github-actions-cryptominer.yaml](supply-chain/2024-12_ultralytics-pypi-github-actions-cryptominer.yaml) | supply-chain | 2024-12-04 | XMRig (Monero cryptominer) |  |
| [2025-04_ascension-former-partner-ehr.yaml](supply-chain/2025-04_ascension-former-partner-ehr.yaml) | supply-chain | 2024-12-01 |  |  |
| [2025-04_hertz-cleo-clop-breach.yaml](data-leak/2025-04_hertz-cleo-clop-breach.yaml) | data-leak | 2024-12-01 |  | CVE-2024-50623, CVE-2024-55956 |
| [2025-01_orange-romania-hellcat-jira.yaml](data-leak/2025-01_orange-romania-hellcat-jira.yaml) | data-leak | 2024-12-01 |  |  |
| [2024-11_krispy-kreme-play.yaml](ransomware/2024-11_krispy-kreme-play.yaml) | ransomware | 2024-11-29 | Play ransomware |  |
| [2024-11_lockton-companies-southeast-breach.yaml](data-leak/2024-11_lockton-companies-southeast-breach.yaml) | data-leak | 2024-11-20 |  |  |
| [2024-12_cleo-mft-clop.yaml](supply-chain/2024-12_cleo-mft-clop.yaml) | supply-chain | 2024-11-15 | Clop (Cl0p) ransomware | CVE-2024-50623, CVE-2024-55956 |
| [2024-11_legends-international.yaml](data-leak/2024-11_legends-international.yaml) | data-leak | 2024-11-09 |  |  |
| [2024-11_ahold-delhaize-inc-ransom.yaml](ransomware/2024-11_ahold-delhaize-inc-ransom.yaml) | ransomware | 2024-11-05 | INC Ransom |  |
| [2024-12_arc-community-services.yaml](ransomware/2024-12_arc-community-services.yaml) | ransomware | 2024-11-01 |  |  |
| [2024-11_bologna-fc-ransomhub.yaml](ransomware/2024-11_bologna-fc-ransomhub.yaml) | ransomware | 2024-11-01 | RansomHub ransomware |  |
| [2024-11_schneider-electric-hellcat.yaml](ransomware/2024-11_schneider-electric-hellcat.yaml) | ransomware | 2024-11-01 | Hellcat |  |
| [2024-11_finastra-sftp-banking-software.yaml](data-leak/2024-11_finastra-sftp-banking-software.yaml) | data-leak | 2024-10-31 |  |  |
| [2024-10_midnight-blizzard-rdp-spearphish.yaml](other/2024-10_midnight-blizzard-rdp-spearphish.yaml) | other | 2024-10-22 |  |  |
| [2024-10_conduent-safepay.yaml](ransomware/2024-10_conduent-safepay.yaml) | ransomware | 2024-10-21 | SafePay ransomware |  |
| [2025-01_conduent-safepay-state-benefits.yaml](ransomware/2025-01_conduent-safepay-state-benefits.yaml) | ransomware | 2024-10-21 | SafePay |  |
| [2024-10_radiant-capital-defi-lazarus.yaml](credential-theft/2024-10_radiant-capital-defi-lazarus.yaml) | credential-theft | 2024-10-16 | InletDrift |  |
| [2024-10_mut8694-npm-pypi-roblox.yaml](supply-chain/2024-10_mut8694-npm-pypi-roblox.yaml) | supply-chain | 2024-10-10 | Blank Grabber infostealer; Sk… |  |
| [2024-10_casio-underground.yaml](ransomware/2024-10_casio-underground.yaml) | ransomware | 2024-10-05 | Underground ransomware |  |
| [2024-10_american-water-works.yaml](other/2024-10_american-water-works.yaml) | other | 2024-10-03 |  |  |
| [2024-10_hot-topic.yaml](data-leak/2024-10_hot-topic.yaml) | data-leak | 2024-10-01 | Infostealer malware (targetin… |  |
| [2025-01_stiiizy-cannabis-pos-breach-380k.yaml](data-leak/2025-01_stiiizy-cannabis-pos-breach-380k.yaml) | data-leak | 2024-10-01 |  |  |
| [2024-11_byte-federal-bitcoin-atm-gitlab.yaml](data-leak/2024-11_byte-federal-bitcoin-atm-gitlab.yaml) | data-leak | 2024-09-30 |  |  |
| [2024-10_internet-archive.yaml](data-leak/2024-10_internet-archive.yaml) | data-leak | 2024-09-28 |  |  |
| [2024-10_free-mobile-france-vpn-24m.yaml](data-leak/2024-10_free-mobile-france-vpn-24m.yaml) | data-leak | 2024-09-28 |  |  |
| [2024-09_moneygram-social-engineering.yaml](data-leak/2024-09_moneygram-social-engineering.yaml) | data-leak | 2024-09-20 |  |  |
| [2024-09_serviceaide-catholic-health-elasticsearch.yaml](data-leak/2024-09_serviceaide-catholic-health-elasticsearch.yaml) | data-leak | 2024-09-19 |  |  |
| [2024-09_texas-tech-health-interlock.yaml](ransomware/2024-09_texas-tech-health-interlock.yaml) | ransomware | 2024-09-17 | Interlock ransomware |  |
| [2024-11_icbc-london-hunters-intl.yaml](other/2024-11_icbc-london-hunters-intl.yaml) | ransomware | 2024-09-01 | Hunters International ransomw… |  |
| [2024-09_transport-for-london-scattered-spider.yaml](other/2024-09_transport-for-london-scattered-spider.yaml) | credential-theft | 2024-08-31 |  |  |
| [2024-08_halliburton.yaml](ransomware/2024-08_halliburton.yaml) | ransomware | 2024-08-21 | RansomHub ransomware |  |
| [2024-08_fidelity-investments-account-abuse.yaml](data-leak/2024-08_fidelity-investments-account-abuse.yaml) | data-leak | 2024-08-17 |  |  |
| [2023-03_royal-mail-lockbit-v2.yaml](ransomware/2023-03_royal-mail-lockbit-v2.yaml) | ransomware | 2024-08-11 | Hunters International ransomw… |  |
| [2024-07_wazirx-lazarus-multisig.yaml](credential-theft/2024-07_wazirx-lazarus-multisig.yaml) | credential-theft | 2024-07-18 | Safe Wallet front-end manipul… |  |
| [2024-08_mclaren-health.yaml](ransomware/2024-08_mclaren-health.yaml) | ransomware | 2024-07-17 | INC Ransom ransomware |  |
| [2024-11_trizetto-cognizant-healthcare-3m.yaml](supply-chain/2024-11_trizetto-cognizant-healthcare-3m.yaml) | supply-chain | 2024-07-01 |  |  |
| [2025-01_otelier-hotel-reservation-platform.yaml](supply-chain/2025-01_otelier-hotel-reservation-platform.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-06_acadian-ambulance-daixin.yaml](ransomware/2024-06_acadian-ambulance-daixin.yaml) | ransomware | 2024-06-19 | Daixin Team ransomware |  |
| [2024-06_cdk-global.yaml](ransomware/2024-06_cdk-global.yaml) | ransomware | 2024-06-18 | BlackSuit |  |
| [2024-06_globe-life-insurance-extortion.yaml](data-leak/2024-06_globe-life-insurance-extortion.yaml) | data-leak | 2024-06-13 |  |  |
| [2024-06_kadokawa-niconico-blacksuit.yaml](ransomware/2024-06_kadokawa-niconico-blacksuit.yaml) | ransomware | 2024-06-08 | BlackSuit |  |
| [2024-06_rite-aid-ransomhub.yaml](ransomware/2024-06_rite-aid-ransomhub.yaml) | ransomware | 2024-06-06 | RansomHub |  |
| [2024-06_synnovis-nhs.yaml](ransomware/2024-06_synnovis-nhs.yaml) | ransomware | 2024-06-03 | Qilin ransomware |  |
| [2024-06_cbiz-benefits-insurance-breach.yaml](data-leak/2024-06_cbiz-benefits-insurance-breach.yaml) | data-leak | 2024-06-02 |  |  |
| [2024-06_tile-life360-extortion.yaml](data-leak/2024-06_tile-life360-extortion.yaml) | data-leak | 2024-06-01 |  |  |
| [2024-05_dmm-bitcoin-tradertraitor.yaml](credential-theft/2024-05_dmm-bitcoin-tradertraitor.yaml) | credential-theft | 2024-05-31 |  |  |
| [2024-05_evolve-bank-lockbit.yaml](ransomware/2024-05_evolve-bank-lockbit.yaml) | ransomware | 2024-05-29 | LockBit ransomware |  |
| [2024-06_patelco-credit-union.yaml](ransomware/2024-06_patelco-credit-union.yaml) | ransomware | 2024-05-23 | RansomHub ransomware |  |
| [2024-05_landmark-admin-insurance.yaml](ransomware/2024-05_landmark-admin-insurance.yaml) | ransomware | 2024-05-13 |  |  |
| [2024-05_landmark-admin-insurance-ransomware.yaml](ransomware/2024-05_landmark-admin-insurance-ransomware.yaml) | ransomware | 2024-05-13 |  |  |
| [2024-05_ascension-health.yaml](ransomware/2024-05_ascension-health.yaml) | ransomware | 2024-05-08 | Black Basta ransomware |  |
| [2024-05_keytronic-black-basta.yaml](ransomware/2024-05_keytronic-black-basta.yaml) | ransomware | 2024-05-06 | Black Basta ransomware |  |
| [2024-07_snowflake-bausch-health-pharma.yaml](credential-theft/2024-07_snowflake-bausch-health-pharma.yaml) | credential-theft | 2024-05-01 |  |  |
| [2024-06_pure-storage-snowflake.yaml](credential-theft/2024-06_pure-storage-snowflake.yaml) | credential-theft | 2024-05-01 |  |  |
| [2024-05_dell-api-scrape.yaml](data-leak/2024-05_dell-api-scrape.yaml) | data-leak | 2024-04-28 |  |  |
| [2024-04_london-drugs-lockbit.yaml](ransomware/2024-04_london-drugs-lockbit.yaml) | ransomware | 2024-04-28 | LockBit ransomware |  |
| [2024-04_santander-snowflake.yaml](credential-theft/2024-04_santander-snowflake.yaml) | credential-theft | 2024-04-17 |  |  |
| [2024-04_frontier-communications-ransomhub.yaml](ransomware/2024-04_frontier-communications-ransomhub.yaml) | ransomware | 2024-04-14 | RansomHub |  |
| [2024-07_att-snowflake-110million-metadata.yaml](data-leak/2024-07_att-snowflake-110million-metadata.yaml) | data-leak | 2024-04-14 | Lumma/Vidar/RedLine infosteal… |  |
| [2024-05_neiman-marcus-snowflake-31m-email.yaml](credential-theft/2024-05_neiman-marcus-snowflake-31m-email.yaml) | credential-theft | 2024-04-14 | VIDAR/RISEPRO/REDLINE infoste… |  |
| [2024-04_advance-auto-parts-snowflake.yaml](credential-theft/2024-04_advance-auto-parts-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-04_att-snowflake.yaml](credential-theft/2024-04_att-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-05_lendingtree-quotewizard-snowflake.yaml](credential-theft/2024-05_lendingtree-quotewizard-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-04_ticketmaster-snowflake.yaml](credential-theft/2024-04_ticketmaster-snowflake.yaml) | credential-theft | 2024-04-14 | VIDAR, RISEPRO, REDLINE, RACO… |  |
| [2024-04_young-consulting-blacksuit.yaml](ransomware/2024-04_young-consulting-blacksuit.yaml) | ransomware | 2024-04-10 | BlackSuit ransomware |  |
| [2024-05_neiman-marcus-snowflake.yaml](credential-theft/2024-05_neiman-marcus-snowflake.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-04_snowflake-unc5537-165-customers.yaml](supply-chain/2024-04_snowflake-unc5537-165-customers.yaml) | credential-theft | 2024-04-01 | Lumma; Vidar; RedLine; RisePr… |  |
| [2024-04_snowflake-customers.yaml](credential-theft/2024-04_snowflake-customers.yaml) | credential-theft | 2024-04-01 | Redline Stealer / Lumma Steal… |  |
| [2024-04_medisecure-australia.yaml](ransomware/2024-04_medisecure-australia.yaml) | ransomware | 2024-04-01 |  |  |
| [2024-04_national-public-data.yaml](data-leak/2024-04_national-public-data.yaml) | data-leak | 2024-04-01 |  |  |
| [2024-07_disney-slack-nullbulge.yaml](data-leak/2024-07_disney-slack-nullbulge.yaml) | data-leak | 2024-04-01 |  |  |
| [2024-04_snowflake-cylance-blackberry.yaml](credential-theft/2024-04_snowflake-cylance-blackberry.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-06_lausd-snowflake.yaml](credential-theft/2024-06_lausd-snowflake.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-05_ticketek-australia-teg-cloud.yaml](credential-theft/2024-05_ticketek-australia-teg-cloud.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-04_palo-alto-pan-os.yaml](other/2024-04_palo-alto-pan-os.yaml) | other | 2024-03-26 | UPSTYLE Python backdoor | CVE-2024-3400 |
| [2024-03_healthequity-vendor-breach.yaml](data-leak/2024-03_healthequity-vendor-breach.yaml) | data-leak | 2024-03-09 |  |  |
| [2024-03_wacks-law-group-qilin.yaml](ransomware/2024-03_wacks-law-group-qilin.yaml) | ransomware | 2024-03-09 | Qilin ransomware |  |
| [2024-03_acuity-federal-contractor-github.yaml](data-leak/2024-03_acuity-federal-contractor-github.yaml) | data-leak | 2024-03-07 |  |  |
| [2024-04_roku-credential-stuffing.yaml](credential-theft/2024-04_roku-credential-stuffing.yaml) | credential-theft | 2024-03-01 |  |  |
| [2024-03_mintlify-github-tokens.yaml](supply-chain/2024-03_mintlify-github-tokens.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-02_verisource-hr-benefits-breach.yaml](data-leak/2024-02_verisource-hr-benefits-breach.yaml) | data-leak | 2024-02-27 |  |  |
| [2024-03_xz-utils-backdoor.yaml](supply-chain/2024-03_xz-utils-backdoor.yaml) | supply-chain | 2024-02-24 |  | CVE-2024-3094 |
| [2024-02_cencora-pharma.yaml](data-leak/2024-02_cencora-pharma.yaml) | data-leak | 2024-02-21 |  |  |
| [2024-02_fbcs-comcast-truist.yaml](data-leak/2024-02_fbcs-comcast-truist.yaml) | data-leak | 2024-02-14 |  |  |
| [2024-09_comcast-xfinity-fcc-fine.yaml](data-leak/2024-09_comcast-xfinity-fcc-fine.yaml) | data-leak | 2024-02-14 |  |  |
| [2024-02_change-healthcare.yaml](ransomware/2024-02_change-healthcare.yaml) | ransomware | 2024-02-11 | ALPHV/BlackCat |  |
| [2024-02_disa-global-employment-screening.yaml](data-leak/2024-02_disa-global-employment-screening.yaml) | data-leak | 2024-02-09 |  |  |
| [2024-02_prudential-financial-alphv.yaml](ransomware/2024-02_prudential-financial-alphv.yaml) | ransomware | 2024-02-04 | ALPHV/BlackCat |  |
| [2024-02_prudential-financial.yaml](data-leak/2024-02_prudential-financial.yaml) | data-leak | 2024-02-04 | ALPHV/BlackCat ransomware |  |
| [2025-03_ntt-communications-corporate-customers.yaml](data-leak/2025-03_ntt-communications-corporate-customers.yaml) | data-leak | 2024-02-01 |  |  |
| [2024-01_lurie-childrens-hospital.yaml](ransomware/2024-01_lurie-childrens-hospital.yaml) | ransomware | 2024-01-26 | Rhysida |  |
| [2024-01_tietoevry-ransomware-swedish-orgs.yaml](supply-chain/2024-01_tietoevry-ransomware-swedish-orgs.yaml) | ransomware | 2024-01-19 | Akira ransomware |  |
| [2024-02_sandworm-texas-water-muleshoe.yaml](other/2024-02_sandworm-texas-water-muleshoe.yaml) | other | 2024-01-18 |  |  |
| [2024-01_trello-api-scrape.yaml](data-leak/2024-01_trello-api-scrape.yaml) | data-leak | 2024-01-16 |  |  |
| [2024-01_loandepot-alphv.yaml](ransomware/2024-01_loandepot-alphv.yaml) | ransomware | 2024-01-04 | ALPHV/BlackCat ransomware |  |
| [2024-12_volkswagen-cariad-aws-location.yaml](data-leak/2024-12_volkswagen-cariad-aws-location.yaml) | data-leak | 2024-01-01 |  |  |
| [2024-04_sisense-analytics-cisa-advisory.yaml](other/2024-04_sisense-analytics-cisa-advisory.yaml) | other | 2024-01-01 |  |  |
| [2024-04_kaiser-permanente-tracker.yaml](data-leak/2024-04_kaiser-permanente-tracker.yaml) | data-leak | 2024-01-01 |  |  |
| [2024-05_outabox-biometric-australia.yaml](data-leak/2024-05_outabox-biometric-australia.yaml) | data-leak | 2024-01-01 |  |  |
| [2023-12_anna-jaques-hospital-money-message.yaml](ransomware/2023-12_anna-jaques-hospital-money-message.yaml) | ransomware | 2023-12-25 | Money Message |  |
| [2023-12_first-american-financial-ransomware.yaml](ransomware/2023-12_first-american-financial-ransomware.yaml) | ransomware | 2023-12-20 |  |  |
| [2024-01_ivanti-connect-secure.yaml](other/2024-01_ivanti-connect-secure.yaml) | other | 2023-12-01 | ZIPLINE backdoor / LIGHTWIRE … | CVE-2023-46805, CVE-2024-21887, CVE-202… |
| [2023-11_integris-health.yaml](ransomware/2023-11_integris-health.yaml) | ransomware | 2023-11-28 |  |  |
| [2023-11_geisinger-nuance-insider-breach.yaml](data-leak/2023-11_geisinger-nuance-insider-breach.yaml) | data-leak | 2023-11-27 |  |  |
| [2024-01_cloudflare-midnight-blizzard.yaml](credential-theft/2024-01_cloudflare-midnight-blizzard.yaml) | credential-theft | 2023-11-14 |  |  |
| [2023-11_fred-hutch-hunters-intl.yaml](ransomware/2023-11_fred-hutch-hunters-intl.yaml) | ransomware | 2023-11-10 | Hunters International ransomw… |  |
| [2023-11_dp-world-australia.yaml](ransomware/2023-11_dp-world-australia.yaml) | ransomware | 2023-11-10 |  | CVE-2023-4966 |
| [2023-11_icbc-us-lockbit-treasury.yaml](other/2023-11_icbc-us-lockbit-treasury.yaml) | ransomware | 2023-11-08 | LockBit ransomware | CVE-2023-4966 |
| [2023-11_sumo-logic-aws-access-key.yaml](credential-theft/2023-11_sumo-logic-aws-access-key.yaml) | credential-theft | 2023-11-03 |  |  |
| [2024-01_microsoft-midnight-blizzard.yaml](credential-theft/2024-01_microsoft-midnight-blizzard.yaml) | credential-theft | 2023-11-01 |  |  |
| [2023-10_infosys-mccamish-lockbit.yaml](supply-chain/2023-10_infosys-mccamish-lockbit.yaml) | supply-chain | 2023-10-29 | LockBit ransomware |  |
| [2024-06_truist-bank-sp1d3r-dark-web.yaml](data-leak/2024-06_truist-bank-sp1d3r-dark-web.yaml) | data-leak | 2023-10-27 |  |  |
| [2023-10_marina-bay-sands-singapore-pdpc.yaml](data-leak/2023-10_marina-bay-sands-singapore-pdpc.yaml) | data-leak | 2023-10-19 |  |  |
| [2023-10_xfinity-comcast-citrixbleed-35m.yaml](data-leak/2023-10_xfinity-comcast-citrixbleed-35m.yaml) | data-leak | 2023-10-16 |  | CVE-2023-4966 |
| [2023-10_truist-bank-dark-web.yaml](data-leak/2023-10_truist-bank-dark-web.yaml) | data-leak | 2023-10-01 |  |  |
| [2023-10_boeing-citrixbleed.yaml](ransomware/2023-10_boeing-citrixbleed.yaml) | ransomware | 2023-10-01 | LockBit 3.0 | CVE-2023-4966 |
| [2023-10_okta-support-system.yaml](credential-theft/2023-10_okta-support-system.yaml) | credential-theft | 2023-09-28 |  |  |
| [2023-09_mgm-resorts.yaml](ransomware/2023-09_mgm-resorts.yaml) | ransomware | 2023-09-08 | ALPHV/BlackCat |  |
| [2023-08_retool-mfa-google-cloud-phishing.yaml](other/2023-08_retool-mfa-google-cloud-phishing.yaml) | other | 2023-08-27 |  |  |
| [2023-08_caesars-entertainment.yaml](ransomware/2023-08_caesars-entertainment.yaml) | ransomware | 2023-08-18 | Scattered Spider ransomware |  |
| [2024-09_slim-cd-payment-processor.yaml](data-leak/2024-09_slim-cd-payment-processor.yaml) | data-leak | 2023-08-17 |  |  |
| [2023-08_rapattoni-mls-ransomware.yaml](ransomware/2023-08_rapattoni-mls-ransomware.yaml) | ransomware | 2023-08-09 |  |  |
| [2023-11_dollar-tree-zeroed-in.yaml](supply-chain/2023-11_dollar-tree-zeroed-in.yaml) | supply-chain | 2023-08-07 |  |  |
| [2024-02_flax-typhoon-taiwan-botnet.yaml](other/2024-02_flax-typhoon-taiwan-botnet.yaml) | other | 2023-06-01 | Flax Typhoon botnet (Raptor T… |  |
| [2023-07_moveit-maximus.yaml](supply-chain/2023-07_moveit-maximus.yaml) | supply-chain | 2023-05-27 | LEMURLOOT web shell | CVE-2023-34362 |
| [2023-05_moveit-transfer-clop.yaml](supply-chain/2023-05_moveit-transfer-clop.yaml) | supply-chain | 2023-05-27 | LEMURLOOT web shell | CVE-2023-34362, CVE-2023-35708 |
| [2023-05_storm-0558-microsoft-exchange.yaml](other/2023-05_storm-0558-microsoft-exchange.yaml) | other | 2023-05-15 |  |  |
| [2023-10_23andme-credential-stuffing.yaml](data-leak/2023-10_23andme-credential-stuffing.yaml) | credential-theft | 2023-04-29 |  |  |
| [2024-04_webtpa-health-insurance.yaml](data-leak/2024-04_webtpa-health-insurance.yaml) | data-leak | 2023-04-18 |  |  |
| [2023-04_ncb-management-services.yaml](data-leak/2023-04_ncb-management-services.yaml) | data-leak | 2023-04-04 |  |  |
| [2023-06_hwl-ebsworth-alphv-australia.yaml](data-leak/2023-06_hwl-ebsworth-alphv-australia.yaml) | data-leak | 2023-04-01 | ALPHV/BlackCat ransomware |  |
| [2023-02_pja-concentra-healthcare.yaml](data-leak/2023-02_pja-concentra-healthcare.yaml) | data-leak | 2023-03-27 |  |  |
| [2023-03_capita-black-basta.yaml](ransomware/2023-03_capita-black-basta.yaml) | ransomware | 2023-03-22 | Black Basta ransomware |  |
| [2023-03_openai-chatgpt-redis-bug.yaml](data-leak/2023-03_openai-chatgpt-redis-bug.yaml) | data-leak | 2023-03-20 |  |  |
| [2023-03_3cx-desktop-app.yaml](supply-chain/2023-03_3cx-desktop-app.yaml) | supply-chain | 2023-03-16 | SUDDENICON downloader / ICONI… | CVE-2023-29059 |
| [2023-03_latitude-financial.yaml](data-leak/2023-03_latitude-financial.yaml) | data-leak | 2023-03-16 |  |  |
| [2023-03_orrick-herrington-law-firm.yaml](data-leak/2023-03_orrick-herrington-law-firm.yaml) | data-leak | 2023-02-28 | SilentRansom/Luna Moth |  |
| [2023-02_dish-network-blackbasta.yaml](ransomware/2023-02_dish-network-blackbasta.yaml) | ransomware | 2023-02-23 | Black Basta ransomware |  |
| [2023-03_cfpb-employee-data-emailed-personal-account.yaml](data-leak/2023-03_cfpb-employee-data-emailed-personal-account.yaml) | data-leak | 2023-02-14 |  |  |
| [2023-02_reddit-blackcat.yaml](data-leak/2023-02_reddit-blackcat.yaml) | data-leak | 2023-02-05 |  |  |
| [2023-02_volt-typhoon-lelwd-utility.yaml](other/2023-02_volt-typhoon-lelwd-utility.yaml) | other | 2023-02-01 |  |  |
| [2023-01_goanywhere-clop.yaml](supply-chain/2023-01_goanywhere-clop.yaml) | supply-chain | 2023-01-18 |  | CVE-2023-0669 |
| [2023-01_royal-mail-lockbit.yaml](ransomware/2023-01_royal-mail-lockbit.yaml) | ransomware | 2023-01-10 | LockBit 3.0 |  |
| [2023-03_forever21-employee-breach.yaml](data-leak/2023-03_forever21-employee-breach.yaml) | data-leak | 2023-01-05 |  |  |
| [2024-10_salt-typhoon-lumen-verizon-att-telecom.yaml](other/2024-10_salt-typhoon-lumen-verizon-att-telecom.yaml) | other | 2023-01-01 | Demodex (kernel-mode rootkit) |  |
| [2024-10_salt-typhoon-telecoms.yaml](other/2024-10_salt-typhoon-telecoms.yaml) | other | 2023-01-01 |  |  |
| [2024-08_toyota-240gb-dark-web.yaml](data-leak/2024-08_toyota-240gb-dark-web.yaml) | data-leak | 2022-12-25 |  |  |
| [2022-12_activision-smishing-employee-data.yaml](data-leak/2022-12_activision-smishing-employee-data.yaml) | data-leak | 2022-12-04 |  |  |
| [2023-01_commuteair-jenkins-aws-s3.yaml](credential-theft/2023-01_commuteair-jenkins-aws-s3.yaml) | credential-theft | 2022-12-01 |  |  |
| [2023-01_t-mobile-api.yaml](data-leak/2023-01_t-mobile-api.yaml) | data-leak | 2022-11-25 |  |  |
| [2022-11_ftx-aws-secrets-compromise.yaml](credential-theft/2022-11_ftx-aws-secrets-compromise.yaml) | credential-theft | 2022-11-11 |  |  |
| [2022-11_killnet-ddos-nato-european-parliament.yaml](other/2022-11_killnet-ddos-nato-european-parliament.yaml) | other | 2022-10-10 |  |  |
| [2022-09_optus.yaml](data-leak/2022-09_optus.yaml) | data-leak | 2022-09-19 |  |  |
| [2022-09_uber-mfa-fatigue.yaml](credential-theft/2022-09_uber-mfa-fatigue.yaml) | credential-theft | 2022-09-15 |  |  |
| [2022-09_revolut-social-engineering-50k.yaml](credential-theft/2022-09_revolut-social-engineering-50k.yaml) | credential-theft | 2022-09-11 |  |  |
| [2022-09_lausd-vice-society.yaml](ransomware/2022-09_lausd-vice-society.yaml) | ransomware | 2022-09-03 | Vice Society ransomware |  |
| [2022-10_medibank.yaml](ransomware/2022-10_medibank.yaml) | ransomware | 2022-08-25 | BlogXX / REvil variant |  |
| [2022-08_lastpass.yaml](data-leak/2022-08_lastpass.yaml) | data-leak | 2022-08-08 |  | CVE-2020-5741 |
| [2022-08_doordash-0ktapus-vendor.yaml](data-leak/2022-08_doordash-0ktapus-vendor.yaml) | data-leak | 2022-08-01 |  |  |
| [2022-08_nomad-bridge-exploit.yaml](other/2022-08_nomad-bridge-exploit.yaml) | other | 2022-08-01 |  |  |
| [2022-08_twilio-0ktapus.yaml](credential-theft/2022-08_twilio-0ktapus.yaml) | credential-theft | 2022-06-01 |  |  |
| [2022-04_industroyer2-ukraine-blocked.yaml](other/2022-04_industroyer2-ukraine-blocked.yaml) | other | 2022-04-08 | Industroyer2; CaddyWiper; ORC… |  |
| [2022-03_ronin-axie-infinity-lazarus-625m.yaml](credential-theft/2022-03_ronin-axie-infinity-lazarus-625m.yaml) | credential-theft | 2022-03-23 |  |  |
| [2022-03_microsoft-lapsus-bing-cortana-source.yaml](credential-theft/2022-03_microsoft-lapsus-bing-cortana-source.yaml) | credential-theft | 2022-03-20 |  |  |
| [2022-03_samsung-lapsus.yaml](data-leak/2022-03_samsung-lapsus.yaml) | data-leak | 2022-03-04 |  |  |
| [2022-02_nvidia-lapsus-gpu-source-code.yaml](credential-theft/2022-02_nvidia-lapsus-gpu-source-code.yaml) | credential-theft | 2022-02-23 |  |  |
| [2022-02_wormhole-bridge-exploit.yaml](other/2022-02_wormhole-bridge-exploit.yaml) | other | 2022-02-02 |  |  |
| [2022-02_australian-clinical-labs-medlab.yaml](data-leak/2022-02_australian-clinical-labs-medlab.yaml) | ransomware | 2022-02-01 |  |  |
| [2022-01_okta-lapsus.yaml](credential-theft/2022-01_okta-lapsus.yaml) | credential-theft | 2022-01-16 | Mimikatz |  |
| [2022-10_football-australia-aws-s3-keys.yaml](credential-theft/2022-10_football-australia-aws-s3-keys.yaml) | credential-theft | 2022-01-01 |  |  |
| [2022-08_twitter-api-54m-accounts.yaml](data-leak/2022-08_twitter-api-54m-accounts.yaml) | data-leak | 2022-01-01 |  |  |
| [2022-11_whatsapp-487m-phone-scrape.yaml](data-leak/2022-11_whatsapp-487m-phone-scrape.yaml) | data-leak | 2022-01-01 |  |  |
| [2021-12_bitmart-exchange-hack-196m.yaml](other/2021-12_bitmart-exchange-hack-196m.yaml) | other | 2021-12-04 |  |  |
| [2021-12_log4shell.yaml](other/2021-12_log4shell.yaml) | other | 2021-12-01 | Conti (ransomware), various c… | CVE-2021-44228, CVE-2021-45046, CVE-202… |
| [2022-04_lincoln-college-closure.yaml](ransomware/2022-04_lincoln-college-closure.yaml) | ransomware | 2021-12-01 |  |  |
| [2021-12_badgerdao-frontend-exploit.yaml](other/2021-12_badgerdao-frontend-exploit.yaml) | other | 2021-11-10 |  |  |
| [2021-11_robinhood-social-engineering-7m.yaml](credential-theft/2021-11_robinhood-social-engineering-7m.yaml) | credential-theft | 2021-11-03 |  |  |
| [2021-10_cream-finance-flash-loan-130m.yaml](other/2021-10_cream-finance-flash-loan-130m.yaml) | other | 2021-10-27 |  |  |
| [2021-10_cox-communications-social-engineering.yaml](data-leak/2021-10_cox-communications-social-engineering.yaml) | data-leak | 2021-10-11 |  |  |
| [2021-10_twitch-source-code-125gb-leak.yaml](data-leak/2021-10_twitch-source-code-125gb-leak.yaml) | data-leak | 2021-10-04 |  |  |
| [2021-11_godaddy-wordpress-hosting-1m.yaml](credential-theft/2021-11_godaddy-wordpress-hosting-1m.yaml) | credential-theft | 2021-09-06 |  |  |
| [2021-08_poly-network-defi-611m.yaml](other/2021-08_poly-network-defi-611m.yaml) | other | 2021-08-10 |  |  |
| [2021-08_tmobile-john-binns-54m.yaml](data-leak/2021-08_tmobile-john-binns-54m.yaml) | data-leak | 2021-08-01 |  |  |
| [2024-09_tmobile-fcc-settlement.yaml](data-leak/2024-09_tmobile-fcc-settlement.yaml) | data-leak | 2021-08-01 |  |  |
| [2021-07_kaseya-vsa-revil.yaml](supply-chain/2021-07_kaseya-vsa-revil.yaml) | supply-chain | 2021-07-02 | REvil / Sodinokibi | CVE-2021-30116 |
| [2022-06_unc2903-imdsv1-aws-metadata.yaml](credential-theft/2022-06_unc2903-imdsv1-aws-metadata.yaml) | credential-theft | 2021-06-21 |  |  |
| [2023-01_twitter-api-scrape.yaml](data-leak/2023-01_twitter-api-scrape.yaml) | data-leak | 2021-06-01 |  |  |
| [2024-02_volt-typhoon-critical-infrastructure.yaml](other/2024-02_volt-typhoon-critical-infrastructure.yaml) | other | 2021-06-01 |  | CVE-2021-40539, CVE-2021-27860 |
| [2021-05_jbs-foods.yaml](ransomware/2021-05_jbs-foods.yaml) | ransomware | 2021-05-30 | REvil / Sodinokibi |  |
| [2021-05_ireland-hse-conti-ransomware.yaml](ransomware/2021-05_ireland-hse-conti-ransomware.yaml) | ransomware | 2021-05-14 | Conti ransomware; Cobalt Stri… |  |
| [2021-05_colonial-pipeline.yaml](ransomware/2021-05_colonial-pipeline.yaml) | ransomware | 2021-05-07 | DarkSide |  |
| [2021-06_linkedin-700m-api-scrape.yaml](data-leak/2021-06_linkedin-700m-api-scrape.yaml) | data-leak | 2021-05-01 |  |  |
| [2021-05_scripps-health-conti.yaml](ransomware/2021-05_scripps-health-conti.yaml) | ransomware | 2021-04-26 | Conti ransomware |  |
| [2021-04_illinois-dhs-medicaid-misconfiguration.yaml](data-leak/2021-04_illinois-dhs-medicaid-misconfiguration.yaml) | data-leak | 2021-04-01 |  |  |
| [2025-04_blue-shield-california-google-analytics.yaml](data-leak/2025-04_blue-shield-california-google-analytics.yaml) | data-leak | 2021-04-01 |  |  |
| [2021-03_cna-financial.yaml](ransomware/2021-03_cna-financial.yaml) | ransomware | 2021-03-21 | Phoenix CryptoLocker (WastedL… |  |
| [2021-03_revil-acer-proxylogen-50m.yaml](ransomware/2021-03_revil-acer-proxylogen-50m.yaml) | ransomware | 2021-03-14 | REvil (Sodinokibi) ransomware | CVE-2021-26855 |
| [2021-03_verkada-cameras-jenkins-credentials.yaml](credential-theft/2021-03_verkada-cameras-jenkins-credentials.yaml) | credential-theft | 2021-03-08 |  |  |
| [2021-02_oldsmar-florida-water-treatment-hack.yaml](other/2021-02_oldsmar-florida-water-treatment-hack.yaml) | other | 2021-02-05 |  |  |
| [2021-01_westrock-ransomware-ot.yaml](ransomware/2021-01_westrock-ransomware-ot.yaml) | ransomware | 2021-01-23 |  |  |
| [2021-01_parler-70tb-data-scraped-before-takedown.yaml](data-leak/2021-01_parler-70tb-data-scraped-before-takedown.yaml) | data-leak | 2021-01-09 |  |  |
| [2021-03_microsoft-exchange-proxylogon.yaml](other/2021-03_microsoft-exchange-proxylogon.yaml) | other | 2021-01-03 | China Chopper webshell / HAFN… | CVE-2021-26855, CVE-2021-26857, CVE-202… |
| [2021-04_pulse-secure-apt5-defense-contractors.yaml](other/2021-04_pulse-secure-apt5-defense-contractors.yaml) | other | 2021-01-01 |  | CVE-2021-22893, CVE-2019-11510, CVE-202… |
| [2021-05_peloton-api-private-user-data-exposure.yaml](data-leak/2021-05_peloton-api-private-user-data-exposure.yaml) | data-leak | 2021-01-01 |  |  |
| [2021-01_accellion-fta-clop.yaml](supply-chain/2021-01_accellion-fta-clop.yaml) | supply-chain | 2020-12-25 | DEWMODE webshell / FINTEAM | CVE-2021-27101, CVE-2021-27102, CVE-202… |
| [2021-01_ubiquiti-insider-threat.yaml](data-leak/2021-01_ubiquiti-insider-threat.yaml) | data-leak | 2020-12-10 |  |  |
| [2020-10_harvest-finance-exploit.yaml](other/2020-10_harvest-finance-exploit.yaml) | other | 2020-10-26 |  |  |
| [2020-10_gravatar-profile-scraping-167m.yaml](data-leak/2020-10_gravatar-profile-scraping-167m.yaml) | data-leak | 2020-10-03 |  |  |
| [2020-12_fireeye-solarwinds-red-team-tools.yaml](supply-chain/2020-12_fireeye-solarwinds-red-team-tools.yaml) | supply-chain | 2020-10-01 | SUNBURST; TEARDROP |  |
| [2020-09_universal-health-services-ryuk.yaml](ransomware/2020-09_universal-health-services-ryuk.yaml) | ransomware | 2020-09-27 | Ryuk ransomware; TrickBot; Em… |  |
| [2020-09_kucoin-hack-281m-lazarus.yaml](other/2020-09_kucoin-hack-281m-lazarus.yaml) | other | 2020-09-25 |  |  |
| [2021-09_cisco-webex-iam-compromise.yaml](credential-theft/2021-09_cisco-webex-iam-compromise.yaml) | credential-theft | 2020-09-24 |  |  |
| [2020-11_spotify-credential-stuffing-350k.yaml](credential-theft/2020-11_spotify-credential-stuffing-350k.yaml) | credential-theft | 2020-09-01 |  |  |
| [2020-07_garmin-wastedlocker-evil-corp.yaml](ransomware/2020-07_garmin-wastedlocker-evil-corp.yaml) | ransomware | 2020-07-23 | WastedLocker ransomware; Fake… |  |
| [2023-09_microsoft-ai-sas-token-38tb.yaml](data-leak/2023-09_microsoft-ai-sas-token-38tb.yaml) | data-leak | 2020-07-20 |  |  |
| [2020-07_twitter-bitcoin-scam-vishing.yaml](credential-theft/2020-07_twitter-bitcoin-scam-vishing.yaml) | credential-theft | 2020-07-15 |  |  |
| [2020-06_drizly-github-rds-breach.yaml](credential-theft/2020-06_drizly-github-rds-breach.yaml) | credential-theft | 2020-06-12 |  |  |
| [2020-07_wattpad-shinyhunters-268m.yaml](credential-theft/2020-07_wattpad-shinyhunters-268m.yaml) | credential-theft | 2020-06-01 |  |  |
| [2020-05_experian-south-africa.yaml](data-leak/2020-05_experian-south-africa.yaml) | data-leak | 2020-05-01 |  |  |
| [2020-04_magellan-health.yaml](ransomware/2020-04_magellan-health.yaml) | ransomware | 2020-04-11 |  |  |
| [2020-12_solarwinds-sunburst.yaml](supply-chain/2020-12_solarwinds-sunburst.yaml) | supply-chain | 2020-03-26 | SUNBURST / TEARDROP / SUNSPOT | CVE-2020-10148 |
| [2020-03_cam4-elasticsearch-10bn-records.yaml](data-leak/2020-03_cam4-elasticsearch-10bn-records.yaml) | data-leak | 2020-03-16 |  |  |
| [2020-03_first-republic-bank-aws-insider.yaml](data-leak/2020-03_first-republic-bank-aws-insider.yaml) | data-leak | 2020-03-11 |  |  |
| [2020-04_nintendo-160k-account-takeover.yaml](credential-theft/2020-04_nintendo-160k-account-takeover.yaml) | credential-theft | 2020-03-01 |  |  |
| [2020-03_norwegian-cruise-line-phishing.yaml](data-leak/2020-03_norwegian-cruise-line-phishing.yaml) | data-leak | 2020-03-01 |  |  |
| [2020-04_zoom-credential-stuffing-530k-accounts.yaml](credential-theft/2020-04_zoom-credential-stuffing-530k-accounts.yaml) | credential-theft | 2020-03-01 |  |  |
| [2020-07_blackbaud-crm-ransomware.yaml](supply-chain/2020-07_blackbaud-crm-ransomware.yaml) | supply-chain | 2020-02-07 |  |  |
| [2020-05_easyjet-9m-customers.yaml](data-leak/2020-05_easyjet-9m-customers.yaml) | data-leak | 2020-01-01 |  |  |
| [2020-09_national-general-allstate-insurance.yaml](data-leak/2020-09_national-general-allstate-insurance.yaml) | data-leak | 2020-01-01 |  |  |
| [2020-01_travelex-revil-pulse-secure.yaml](ransomware/2020-01_travelex-revil-pulse-secure.yaml) | ransomware | 2019-12-31 | REvil (Sodinokibi) ransomware | CVE-2019-11510 |
| [2019-11_tmobile-prepaid-customers.yaml](credential-theft/2019-11_tmobile-prepaid-customers.yaml) | credential-theft | 2019-11-01 |  |  |
| [2023-03_cerebral-health-tracking-pixels-3m.yaml](data-leak/2023-03_cerebral-health-tracking-pixels-3m.yaml) | data-leak | 2019-10-12 |  |  |
| [2023-03_cerebral-31m-health-data-meta-google-sharing.yaml](data-leak/2023-03_cerebral-31m-health-data-meta-google-sharing.yaml) | data-leak | 2019-10-01 |  |  |
| [2019-08_wood-ranch-medical-closure-ransomware.yaml](ransomware/2019-08_wood-ranch-medical-closure-ransomware.yaml) | ransomware | 2019-08-10 |  |  |
| [2019-08_choice-hotels-mongodb-vendor.yaml](data-leak/2019-08_choice-hotels-mongodb-vendor.yaml) | data-leak | 2019-07-02 |  |  |
| [2019-07_seven-eleven-japan-app-500k-stolen.yaml](data-leak/2019-07_seven-eleven-japan-app-500k-stolen.yaml) | data-leak | 2019-07-01 |  |  |
| [2019-07_sprint-samsung-add-a-line.yaml](data-leak/2019-07_sprint-samsung-add-a-line.yaml) | data-leak | 2019-06-01 |  |  |
| [2019-05_canva-gnosticplayers-137m.yaml](credential-theft/2019-05_canva-gnosticplayers-137m.yaml) | credential-theft | 2019-05-24 |  |  |
| [2019-05_binance-hack-7000-btc.yaml](other/2019-05_binance-hack-7000-btc.yaml) | other | 2019-05-07 |  |  |
| [2019-07_capital-one-ssrf-imdsv1-106m.yaml](data-leak/2019-07_capital-one-ssrf-imdsv1-106m.yaml) | credential-theft | 2019-03-22 |  |  |
| [2019-05_boost-mobile-credential-stuffing.yaml](credential-theft/2019-05_boost-mobile-credential-stuffing.yaml) | credential-theft | 2019-03-14 |  |  |
| [2024-03_att-dark-web-73million.yaml](data-leak/2024-03_att-dark-web-73million.yaml) | data-leak | 2019-01-01 |  |  |
| [2021-04_facebook-533m-phone-scrape.yaml](data-leak/2021-04_facebook-533m-phone-scrape.yaml) | data-leak | 2019-01-01 |  |  |
| [2018-08_cosmos-bank-india-atm-cashout.yaml](other/2018-08_cosmos-bank-india-atm-cashout.yaml) | other | 2018-08-11 |  |  |
| [2019-03_amca-quest-labcorp-billing.yaml](data-leak/2019-03_amca-quest-labcorp-billing.yaml) | data-leak | 2018-08-01 |  |  |
| [2018-06_exactis-elasticsearch-340m.yaml](data-leak/2018-06_exactis-elasticsearch-340m.yaml) | data-leak | 2018-06-01 |  |  |
| [2018-05_banco-de-chile-swift-wiper.yaml](other/2018-05_banco-de-chile-swift-wiper.yaml) | other | 2018-05-24 | KillMBR wiper (custom variant… |  |
| [2018-05_pageup-hr-saas-australia.yaml](data-leak/2018-05_pageup-hr-saas-australia.yaml) | data-leak | 2018-05-23 |  |  |
| [2018-09_chegg-s3-root-credentials.yaml](data-leak/2018-09_chegg-s3-root-credentials.yaml) | credential-theft | 2018-04-01 |  |  |
| [2018-07_unitypoint-health-phishing-14m-patients.yaml](data-leak/2018-07_unitypoint-health-phishing-14m-patients.yaml) | data-leak | 2018-03-14 |  |  |
| [2018-02_la-times-s3-cryptomining.yaml](other/2018-02_la-times-s3-cryptomining.yaml) | other | 2018-02-09 |  |  |
| [2018-01_allscripts-ransomware-ehr-vendor.yaml](ransomware/2018-01_allscripts-ransomware-ehr-vendor.yaml) | ransomware | 2018-01-18 | SamSam ransomware |  |
| [2019-01_collection1-773m-credential-dump.yaml](credential-theft/2019-01_collection1-773m-credential-dump.yaml) | credential-theft | 2018-01-01 |  |  |
| [2017-12_nicehash-hack-4700-btc.yaml](other/2017-12_nicehash-hack-4700-btc.yaml) | other | 2017-12-06 |  |  |
| [2019-08_imperva-rds-snapshot-exposure.yaml](data-leak/2019-08_imperva-rds-snapshot-exposure.yaml) | credential-theft | 2017-10-01 |  |  |
| [2017-07_aetna-hiv-envelope-disclosure.yaml](data-leak/2017-07_aetna-hiv-envelope-disclosure.yaml) | data-leak | 2017-07-28 |  |  |
| [2017-06_notpetya-medoc-maersk-10b.yaml](supply-chain/2017-06_notpetya-medoc-maersk-10b.yaml) | supply-chain | 2017-06-27 | NotPetya (Petya variant / wip… | CVE-2017-0144 |
| [2017-06_uk-parliament-owa-brute-force.yaml](credential-theft/2017-06_uk-parliament-owa-brute-force.yaml) | credential-theft | 2017-06-23 |  |  |
| [2017-08_triton-trisis-ics-safety-systems.yaml](other/2017-08_triton-trisis-ics-safety-systems.yaml) | other | 2017-06-01 | TRITON (TRISIS, HatMan) |  |
| [2017-05_wannacry-eternalblue-global.yaml](ransomware/2017-05_wannacry-eternalblue-global.yaml) | ransomware | 2017-05-12 | WannaCry (WannaCrypt, WannaCr… | CVE-2017-0144, CVE-2017-0145, CVE-2017-… |
| [2018-04_saks-lord-taylor-fin7-5m-cards.yaml](credential-theft/2018-04_saks-lord-taylor-fin7-5m-cards.yaml) | credential-theft | 2017-05-01 | BOOSTWRITE / POS malware (FIN… |  |
| [2017-11_forever21-pos-malware.yaml](credential-theft/2017-11_forever21-pos-malware.yaml) | credential-theft | 2017-04-03 | POS malware |  |
| [2017-04_chipotle-pos-malware.yaml](credential-theft/2017-04_chipotle-pos-malware.yaml) | credential-theft | 2017-03-24 | POS malware (Track data scrap… |  |
| [2017-05_equifax.yaml](data-leak/2017-05_equifax.yaml) | data-leak | 2017-03-10 |  | CVE-2017-5638 |
| [2019-05_first-american-financial-idor-885m-docs.yaml](data-leak/2019-05_first-american-financial-idor-885m-docs.yaml) | data-leak | 2017-03-01 |  |  |
| [2023-02_goodrx-health-data-meta-google-advertising.yaml](data-leak/2023-02_goodrx-health-data-meta-google-advertising.yaml) | data-leak | 2017-01-01 |  |  |
| [2023-02_goodrx-ftc-health-data-advertising.yaml](data-leak/2023-02_goodrx-ftc-health-data-advertising.yaml) | data-leak | 2017-01-01 |  |  |
| [2017-05_macron-campaign-apt28-macronleaks.yaml](other/2017-05_macron-campaign-apt28-macronleaks.yaml) | other | 2017-01-01 |  |  |
| [2019-06_desjardins-insider.yaml](data-leak/2019-06_desjardins-insider.yaml) | data-leak | 2017-01-01 |  |  |
| [2017-09_sonic-drive-in-pos-5m-cards.yaml](credential-theft/2017-09_sonic-drive-in-pos-5m-cards.yaml) | credential-theft | 2017-01-01 | POS malware |  |
| [2016-12_industroyer-ukraine-power-grid.yaml](other/2016-12_industroyer-ukraine-power-grid.yaml) | other | 2016-12-17 | Industroyer (CrashOverride); … |  |
| [2016-10_australian-red-cross-blood-service.yaml](data-leak/2016-10_australian-red-cross-blood-service.yaml) | data-leak | 2016-10-26 |  |  |
| [2017-02_arbys-pos-malware-355k-cards.yaml](credential-theft/2017-02_arbys-pos-malware-355k-cards.yaml) | credential-theft | 2016-10-25 | POS malware (Track 1/Track 2 … |  |
| [2016-10_dailymotion-85m-accounts.yaml](data-leak/2016-10_dailymotion-85m-accounts.yaml) | data-leak | 2016-10-20 |  |  |
| [2016-10_adult-friendfinder-lfi-412m.yaml](data-leak/2016-10_adult-friendfinder-lfi-412m.yaml) | data-leak | 2016-10-01 |  |  |
| [2016-10_uber-cover-up.yaml](data-leak/2016-10_uber-cover-up.yaml) | data-leak | 2016-10-01 |  |  |
| [2018-05_lifebridge-health-breach-538k-patients.yaml](data-leak/2018-05_lifebridge-health-breach-538k-patients.yaml) | data-leak | 2016-09-27 |  |  |
| [2016-08_shadow-brokers-nsa-exploit-leak.yaml](other/2016-08_shadow-brokers-nsa-exploit-leak.yaml) | other | 2016-08-13 | EternalBlue; EternalRomance; … | CVE-2017-0144, CVE-2017-0145 |
| [2017-05_sabre-synxis-hospitality-1-3m-cards.yaml](credential-theft/2017-05_sabre-synxis-hospitality-1-3m-cards.yaml) | credential-theft | 2016-08-10 |  |  |
| [2016-08_bitfinex-hack-119756-btc.yaml](other/2016-08_bitfinex-hack-119756-btc.yaml) | other | 2016-08-02 |  |  |
| [2017-04_ihg-intercontinental-pos-1200-locations.yaml](credential-theft/2017-04_ihg-intercontinental-pos-1200-locations.yaml) | credential-theft | 2016-08-01 | POS malware (Track data scrap… |  |
| [2016-07_datadog-aws-access-keys.yaml](credential-theft/2016-07_datadog-aws-access-keys.yaml) | credential-theft | 2016-07-07 |  |  |
| [2016-06_banner-health-pos-pivot-3-7m.yaml](data-leak/2016-06_banner-health-pos-pivot-3-7m.yaml) | data-leak | 2016-06-17 | POS malware |  |
| [2016-05_newkirk-products-bcbs-health-id-cards.yaml](data-leak/2016-05_newkirk-products-bcbs-health-id-cards.yaml) | data-leak | 2016-05-21 |  |  |
| [2016-06_dnc-podesta-apt28-gru.yaml](other/2016-06_dnc-podesta-apt28-gru.yaml) | other | 2016-03-19 | X-Agent (Sofacy) keylogger/cr… |  |
| [2016-02_bangladesh-bank-swift-81m.yaml](other/2016-02_bangladesh-bank-swift-81m.yaml) | other | 2016-02-04 | EVTDIAG; MSOUTC; MSOUTC (SWIF… |  |
| [2016-01_centene-corporation-missing-hard-drives.yaml](data-leak/2016-01_centene-corporation-missing-hard-drives.yaml) | data-leak | 2016-01-07 |  |  |
| [2016-07_vitagene-s3-unprotected-buckets.yaml](credential-theft/2016-07_vitagene-s3-unprotected-buckets.yaml) | data-leak | 2016-01-01 |  |  |
| [2018-10_fastcash-dprk-atm-cashout.yaml](other/2018-10_fastcash-dprk-atm-cashout.yaml) | other | 2016-01-01 | FASTCash implant (AIX trojan) |  |
| [2015-12_blackenergy-ukraine-power-grid.yaml](other/2015-12_blackenergy-ukraine-power-grid.yaml) | other | 2015-12-23 | BlackEnergy3; KillDisk |  |
| [2015-10_21st-century-oncology-fbi-2-2m.yaml](data-leak/2015-10_21st-century-oncology-fbi-2-2m.yaml) | data-leak | 2015-10-03 |  |  |
| [2016-05_wendys-pos-malware-1025-locations.yaml](credential-theft/2016-05_wendys-pos-malware-1025-locations.yaml) | credential-theft | 2015-10-01 | POS malware (two distinct str… |  |
| [2015-12_hyatt-hotels-pos-malware-250-hotels.yaml](credential-theft/2015-12_hyatt-hotels-pos-malware-250-hotels.yaml) | credential-theft | 2015-08-13 | POS malware |  |
| [2015-07_ashley-madison-impact-team.yaml](data-leak/2015-07_ashley-madison-impact-team.yaml) | data-leak | 2015-07-12 |  |  |
| [2015-05_bundestag-apt28-16gb-exfil.yaml](other/2015-05_bundestag-apt28-16gb-exfil.yaml) | other | 2015-04-01 |  |  |
| [2015-02_sally-beauty-pos-25k-cards.yaml](data-leak/2015-02_sally-beauty-pos-25k-cards.yaml) | data-leak | 2015-03-01 | POS RAM-scraping malware |  |
| [2015-01_centcom-twitter-youtube-isis-hijack.yaml](other/2015-01_centcom-twitter-youtube-isis-hijack.yaml) | other | 2015-01-12 |  |  |
| [2015-04_tv5monde-apt28-broadcast-disruption.yaml](other/2015-04_tv5monde-apt28-broadcast-disruption.yaml) | other | 2015-01-01 |  |  |
| [2015-05_irs-get-transcript-100k-ssn.yaml](data-leak/2015-05_irs-get-transcript-100k-ssn.yaml) | credential-theft | 2015-01-01 |  |  |
| [2015-02_anthem-health-insurance-78m.yaml](data-leak/2015-02_anthem-health-insurance-78m.yaml) | data-leak | 2014-12-10 |  |  |
| [2015-01_morgan-stanley-insider-350k-clients.yaml](data-leak/2015-01_morgan-stanley-insider-350k-clients.yaml) | data-leak | 2014-12-01 |  |  |
| [2014-11_sony-pictures-wiper-lazarus.yaml](other/2014-11_sony-pictures-wiper-lazarus.yaml) | other | 2014-11-24 | Destover (wiper/backdoor) |  |
| [2014-11_browserstack-aws-access-key-forgotten.yaml](credential-theft/2014-11_browserstack-aws-access-key-forgotten.yaml) | credential-theft | 2014-11-09 |  |  |
| [2015-11_state-department-unclassified-email.yaml](data-leak/2015-11_state-department-unclassified-email.yaml) | data-leak | 2014-10-01 |  |  |
| [2015-07_ucla-health.yaml](data-leak/2015-07_ucla-health.yaml) | data-leak | 2014-09-01 |  |  |
| [2014-09_kmart-sears-holdings-pos-malware.yaml](credential-theft/2014-09_kmart-sears-holdings-pos-malware.yaml) | credential-theft | 2014-09-01 | POS RAM-scraping malware (spe… |  |
| [2015-06_opm-security-clearance-breach.yaml](data-leak/2015-06_opm-security-clearance-breach.yaml) | data-leak | 2014-07-01 |  |  |
| [2014-06_codespaces-aws-ransomware.yaml](other/2014-06_codespaces-aws-ransomware.yaml) | other | 2014-06-17 |  |  |
| [2014-06_dominos-pizza-europe-600k-customers.yaml](data-leak/2014-06_dominos-pizza-europe-600k-customers.yaml) | data-leak | 2014-06-13 |  |  |
| [2015-05_carefirst-bcbs-apt-1-1m.yaml](data-leak/2015-05_carefirst-bcbs-apt-1-1m.yaml) | data-leak | 2014-06-01 |  |  |
| [2014-08_jpmorgan-chase-83m-accounts.yaml](data-leak/2014-08_jpmorgan-chase-83m-accounts.yaml) | data-leak | 2014-06-01 |  |  |
| [2015-01_premera-blue-cross.yaml](data-leak/2015-01_premera-blue-cross.yaml) | data-leak | 2014-05-05 |  |  |
| [2014-08_community-health-systems-apt18-heartbleed.yaml](data-leak/2014-08_community-health-systems-apt18-heartbleed.yaml) | data-leak | 2014-04-01 |  | CVE-2014-0160 |
| [2014-09_home-depot-blackpos-56m.yaml](data-leak/2014-09_home-depot-blackpos-56m.yaml) | data-leak | 2014-04-01 | BlackPOS (Kaptoxa) RAM-scraper |  |
| [2014-09_staples-pos-1-16m-cards.yaml](data-leak/2014-09_staples-pos-1-16m-cards.yaml) | data-leak | 2014-04-01 | POS RAM-scraping malware |  |
| [2014-03_opm-personnel-files-4-2m-earlier-breach.yaml](data-leak/2014-03_opm-personnel-files-4-2m-earlier-breach.yaml) | data-leak | 2014-03-01 | PlugX RAT |  |
| [2014-02_university-of-maryland-310k.yaml](data-leak/2014-02_university-of-maryland-310k.yaml) | data-leak | 2014-02-18 |  |  |
| [2014-03_kickstarter-user-data-breach.yaml](data-leak/2014-03_kickstarter-user-data-breach.yaml) | data-leak | 2014-02-12 |  |  |
| [2014-02_faa-employee-data-45k.yaml](data-leak/2014-02_faa-employee-data-45k.yaml) | data-leak | 2014-02-01 |  |  |
| [2014-05_ebay-employee-credentials-145m.yaml](data-leak/2014-05_ebay-employee-credentials-145m.yaml) | credential-theft | 2014-02-01 |  |  |
| [2018-11_marriott-starwood.yaml](data-leak/2018-11_marriott-starwood.yaml) | data-leak | 2014-01-01 | Remote Access Trojan (name un… |  |
| [2014-11_usps-china-apt-800k-employees.yaml](data-leak/2014-11_usps-china-apt-800k-employees.yaml) | data-leak | 2014-01-01 |  |  |
| [2014-06_indiana-university-146k-ssn-exposure.yaml](data-leak/2014-06_indiana-university-146k-ssn-exposure.yaml) | data-leak | 2014-01-01 |  |  |
| [2015-09_excellus-bcbs-apt-10m.yaml](data-leak/2015-09_excellus-bcbs-apt-10m.yaml) | data-leak | 2013-12-01 |  |  |
| [2013-11_target-blackpos.yaml](other/2013-11_target-blackpos.yaml) | other | 2013-11-15 | BlackPOS / Kaptoxa |  |
| [2023-05_toyota-connected-cloud-misconfiguration-2m.yaml](data-leak/2023-05_toyota-connected-cloud-misconfiguration-2m.yaml) | data-leak | 2013-11-06 |  |  |
| [2015-04_att-insider-callcenter-fcc.yaml](data-leak/2015-04_att-insider-callcenter-fcc.yaml) | data-leak | 2013-11-01 |  |  |
| [2015-10_scottrade-4-6m-customers.yaml](data-leak/2015-10_scottrade-4-6m-customers.yaml) | data-leak | 2013-10-01 |  |  |
| [2013-09_pf-changs-pos-malware.yaml](credential-theft/2013-09_pf-changs-pos-malware.yaml) | credential-theft | 2013-09-01 | POS malware (FIN6) |  |
| [2013-09_pf-changs-pos-malware-2m-cards.yaml](credential-theft/2013-09_pf-changs-pos-malware-2m-cards.yaml) | credential-theft | 2013-09-01 | POS RAM-scraping malware |  |
| [2013-10_adobe-source-code-153m.yaml](data-leak/2013-10_adobe-source-code-153m.yaml) | data-leak | 2013-08-01 |  |  |
| [2013-12_neiman-marcus-pos-malware-350k-cards.yaml](data-leak/2013-12_neiman-marcus-pos-malware-350k-cards.yaml) | data-leak | 2013-07-16 | POS RAM-scraping malware |  |
| [2013-07_advocate-health-care-stolen-computers.yaml](data-leak/2013-07_advocate-health-care-stolen-computers.yaml) | data-leak | 2013-07-15 |  |  |
| [2016-09_yahoo-3-billion-accounts.yaml](data-leak/2016-09_yahoo-3-billion-accounts.yaml) | credential-theft | 2013-07-01 |  |  |
| [2018-03_facebook-cambridge-analytica-87m.yaml](data-leak/2018-03_facebook-cambridge-analytica-87m.yaml) | data-leak | 2013-06-01 |  |  |
| [2013-01_michaels-stores-pos-malware-26m-cards.yaml](credential-theft/2013-01_michaels-stores-pos-malware-26m-cards.yaml) | credential-theft | 2013-05-08 | POS RAM-scraping malware |  |
| [2013-01_michaels-stores-pos-malware.yaml](credential-theft/2013-01_michaels-stores-pos-malware.yaml) | credential-theft | 2013-05-08 | POS malware (Track data scrap… |  |
| [2013-05_tumblr-65m-accounts-discovered-2016.yaml](data-leak/2013-05_tumblr-65m-accounts-discovered-2016.yaml) | data-leak | 2013-05-01 |  |  |
| [2013-04_livingsocial-50m-customers.yaml](data-leak/2013-04_livingsocial-50m-customers.yaml) | data-leak | 2013-04-01 |  |  |
| [2013-10_imgur-breach-17m-accounts-discovered-2017.yaml](data-leak/2013-10_imgur-breach-17m-accounts-discovered-2017.yaml) | data-leak | 2013-01-01 |  |  |
| [2012-12_schnucks-markets-pos-malware-24m-cards.yaml](credential-theft/2012-12_schnucks-markets-pos-malware-24m-cards.yaml) | credential-theft | 2012-12-01 | POS RAM-scraping malware |  |
| [2013-01_howard-university-hospital-stolen-laptop-34k.yaml](data-leak/2013-01_howard-university-hospital-stolen-laptop-34k.yaml) | data-leak | 2012-11-01 |  |  |
| [2015-05_penn-state-cs-apt-18k.yaml](data-leak/2015-05_penn-state-cs-apt-18k.yaml) | data-leak | 2012-09-01 |  |  |
| [2012-09_barnes-noble-pos-skimmers.yaml](credential-theft/2012-09_barnes-noble-pos-skimmers.yaml) | credential-theft | 2012-08-01 |  |  |
| [2016-08_dropbox-credential-reuse-68m.yaml](credential-theft/2016-08_dropbox-credential-reuse-68m.yaml) | credential-theft | 2012-07-01 |  |  |
| [2012-07_disqus-breach-17m-accounts-discovered-2017.yaml](data-leak/2012-07_disqus-breach-17m-accounts-discovered-2017.yaml) | data-leak | 2012-07-01 |  |  |
| [2012-06_south-carolina-dhhs-medicaid-228k.yaml](data-leak/2012-06_south-carolina-dhhs-medicaid-228k.yaml) | data-leak | 2012-06-14 |  |  |
| [2012-09_barnes-noble-pos-skimmers-63-stores.yaml](credential-theft/2012-09_barnes-noble-pos-skimmers-63-stores.yaml) | credential-theft | 2012-06-01 |  |  |
| [2012-06_eharmony-passwords-unsalted.yaml](credential-theft/2012-06_eharmony-passwords-unsalted.yaml) | credential-theft | 2012-05-01 |  |  |
| [2012-06_linkedin-unsalted-sha1-117m.yaml](data-leak/2012-06_linkedin-unsalted-sha1-117m.yaml) | credential-theft | 2012-05-01 |  |  |
| [2012-06_eharmony-15m-passwords-leaked.yaml](credential-theft/2012-06_eharmony-15m-passwords-leaked.yaml) | credential-theft | 2012-05-01 |  |  |
| [2012-03_lastfm-43m-passwords-breach.yaml](credential-theft/2012-03_lastfm-43m-passwords-breach.yaml) | credential-theft | 2012-03-01 |  |  |
| [2012-01_zappos-24m-customers.yaml](data-leak/2012-01_zappos-24m-customers.yaml) | data-leak | 2012-01-15 |  |  |
| [2012-03_global-payments-card-processor.yaml](data-leak/2012-03_global-payments-card-processor.yaml) | data-leak | 2012-01-01 |  |  |
| [2011-10_sutter-health-stolen-laptop-4m.yaml](data-leak/2011-10_sutter-health-stolen-laptop-4m.yaml) | data-leak | 2011-10-15 |  |  |
| [2011-10_sutter-health-stolen-laptop-424m.yaml](data-leak/2011-10_sutter-health-stolen-laptop-424m.yaml) | data-leak | 2011-10-14 |  |  |
| [2011-09_tricare-saic-stolen-backup-tapes.yaml](data-leak/2011-09_tricare-saic-stolen-backup-tapes.yaml) | data-leak | 2011-09-14 |  |  |
| [2011-09_tricare-stolen-backup-tapes-49m.yaml](data-leak/2011-09_tricare-stolen-backup-tapes-49m.yaml) | data-leak | 2011-09-14 |  |  |
| [2014-02_mt-gox-bitcoin-exchange-850k-btc.yaml](other/2014-02_mt-gox-bitcoin-exchange-850k-btc.yaml) | other | 2011-09-01 |  |  |
| [2011-04_sony-psn-76m-offline.yaml](data-leak/2011-04_sony-psn-76m-offline.yaml) | data-leak | 2011-04-17 |  |  |
| [2011-06_citigroup-direct-webapp-360k.yaml](data-leak/2011-06_citigroup-direct-webapp-360k.yaml) | data-leak | 2011-04-01 |  |  |
| [2011-03_rsa-securid-token-seed-theft.yaml](other/2011-03_rsa-securid-token-seed-theft.yaml) | other | 2011-03-01 |  | CVE-2011-0609 |
| [2011-04_epsilon-email-marketing-60m-records.yaml](data-leak/2011-04_epsilon-email-marketing-60m-records.yaml) | data-leak | 2011-03-01 |  |  |
| [2011-12_subway-pos-malware-3m-cards.yaml](credential-theft/2011-12_subway-pos-malware-3m-cards.yaml) | credential-theft | 2011-01-01 | POS keylogger/scraping malware |  |
| [2010-05_nyp-columbia-univ-shared-network-6800.yaml](data-leak/2010-05_nyp-columbia-univ-shared-network-6800.yaml) | data-leak | 2010-09-01 |  |  |
| [2010-09_nyp-columbia-university-shared-network.yaml](data-leak/2010-09_nyp-columbia-university-shared-network.yaml) | data-leak | 2010-09-01 |  |  |
| [2009-12_rockyou-plaintext-passwords-32m.yaml](data-leak/2009-12_rockyou-plaintext-passwords-32m.yaml) | data-leak | 2009-11-01 |  |  |
| [2010-12_fis-worldpay-prepaid-card-13m.yaml](data-leak/2010-12_fis-worldpay-prepaid-card-13m.yaml) | data-leak | 2009-10-01 |  |  |
| [2010-01_operation-aurora-apt17-google-adobe.yaml](other/2010-01_operation-aurora-apt17-google-adobe.yaml) | other | 2009-06-01 | Hydraq (Aurora backdoor) | CVE-2010-0249 |
| [2010-06_stuxnet-olympic-games-natanz-iran.yaml](other/2010-06_stuxnet-olympic-games-natanz-iran.yaml) | other | 2009-06-01 | Stuxnet | CVE-2010-2568, CVE-2010-2772, CVE-2010-… |
| [2009-01_twitter-admin-panel-brute-force.yaml](credential-theft/2009-01_twitter-admin-panel-brute-force.yaml) | credential-theft | 2009-01-05 |  |  |
| [2008-11_rbs-worldpay-atm-cashout-9m.yaml](credential-theft/2008-11_rbs-worldpay-atm-cashout-9m.yaml) | credential-theft | 2008-11-04 |  |  |
| [2012-06_wyndham-hotels-ftc-three-breaches.yaml](data-leak/2012-06_wyndham-hotels-ftc-three-breaches.yaml) | data-leak | 2008-04-01 |  |  |
| [2016-05_myspace-360m-sha1-unsalted.yaml](data-leak/2016-05_myspace-360m-sha1-unsalted.yaml) | data-leak | 2008-01-01 |  |  |
| [2009-01_heartland-payment-systems-130m.yaml](data-leak/2009-01_heartland-payment-systems-130m.yaml) | data-leak | 2007-12-01 |  |  |
| [2008-03_hannaford-pos-malware-4m.yaml](data-leak/2008-03_hannaford-pos-malware-4m.yaml) | data-leak | 2007-12-01 |  |  |
| [2006-08_aol-search-data-leak-650k.yaml](data-leak/2006-08_aol-search-data-leak-650k.yaml) | data-leak | 2006-08-04 |  |  |
| [2006-05_veterans-affairs-laptop-26m.yaml](data-leak/2006-05_veterans-affairs-laptop-26m.yaml) | data-leak | 2006-05-03 |  |  |
| [2005-10_samy-worm-myspace-xss-1m-friends.yaml](other/2005-10_samy-worm-myspace-xss-1m-friends.yaml) | other | 2005-10-04 | Samy worm (JS/Samy) |  |
| [2005-10_samy-worm-myspace-xss.yaml](other/2005-10_samy-worm-myspace-xss.yaml) | other | 2005-10-04 | Samy worm (JavaScript XSS wor… |  |
| [2005-08_zotob-worm-ms05-039.yaml](other/2005-08_zotob-worm-ms05-039.yaml) | other | 2005-08-13 | Zotob (IRCBot variant) | CVE-2005-1983 |
| [2005-08_zotob-worm-windows2000-cnn-nyt-dhs.yaml](other/2005-08_zotob-worm-windows2000-cnn-nyt-dhs.yaml) | other | 2005-08-13 | Zotob (W32/Zotob, also Tpbot,… | CVE-2005-1983 |
| [2007-01_tjx-wardriving-wifi-94m.yaml](data-leak/2007-01_tjx-wardriving-wifi-94m.yaml) | data-leak | 2005-07-01 |  |  |
| [2005-02_paris-hilton-tmobile-sidekick-hack.yaml](data-leak/2005-02_paris-hilton-tmobile-sidekick-hack.yaml) | data-leak | 2005-02-19 |  |  |
| [2005-03_dsw-designer-shoe-warehouse-14m-cards.yaml](data-leak/2005-03_dsw-designer-shoe-warehouse-14m-cards.yaml) | data-leak | 2005-01-01 |  |  |
| [2005-03_dsw-designer-shoe-warehouse.yaml](data-leak/2005-03_dsw-designer-shoe-warehouse.yaml) | credential-theft | 2005-01-01 |  |  |
| [2004-01_mydoom-worm-fastest-email.yaml](other/2004-01_mydoom-worm-fastest-email.yaml) | other | 2004-01-26 | MyDoom (W32/Mydoom, Novarg, M… |  |
| [2005-02_choicepoint-fraud-163k.yaml](data-leak/2005-02_choicepoint-fraud-163k.yaml) | data-leak | 2004-01-01 |  |  |
| [2005-06_cardsystems-sql-injection-40m.yaml](data-leak/2005-06_cardsystems-sql-injection-40m.yaml) | data-leak | 2004-01-01 |  |  |
| [2003-01_sql-slammer-worm-75k-hosts.yaml](other/2003-01_sql-slammer-worm-75k-hosts.yaml) | other | 2003-01-25 | SQL Slammer (W32/SQLSlam, Sap… | CVE-2002-0649 |
| [2004-06_bjs-wholesale-club-ftc.yaml](data-leak/2004-06_bjs-wholesale-club-ftc.yaml) | credential-theft | 2003-01-01 |  |  |
| [2004-06_bjs-wholesale-club-card-breach-ftc.yaml](data-leak/2004-06_bjs-wholesale-club-card-breach-ftc.yaml) | data-leak | 2003-01-01 |  |  |
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
