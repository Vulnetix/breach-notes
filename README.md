# breach-notes

Structured YAML records of breach reports, advisories, and cyber incidents.

**Last updated:** 2026-04-10  **Total records:** 3425

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total incidents | 3425 |
| With CVE/GHSA references | 70 (2%) |
| Unique CVEs/GHSAs | 78 |
| With malware identified | 272 (8%) |
| Supply chain claimed | 821 (24%) |
| Unique vendor products | 2793 |
| Median disclosure lag (days) | 0 |
| Max disclosure lag (days) | 3474 |

## Incidents by Category

| Category | Count | % |
|----------|-------|---|
| ransomware | 129 | 4% |
| data-leak | 1078 | 31% |
| supply-chain | 769 | 22% |
| credential-theft | 116 | 3% |
| other | 1333 | 39% |

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
| 2012 | 18 |
| 2013 | 29 |
| 2014 | 42 |
| 2015 | 21 |
| 2016 | 41 |
| 2017 | 48 |
| 2018 | 85 |
| 2019 | 85 |
| 2020 | 117 |
| 2021 | 326 |
| 2022 | 985 |
| 2023 | 665 |
| 2024 | 477 |
| 2025 | 341 |
| 2026 | 97 |

## Top Malware Families

| Malware | Incidents |
|---------|----------|
| POS RAM-scraping | 12 |
| DEWMODE web shell | 11 |
| ALPHV/BlackCat | 8 |
| Black Basta | 5 |
| Cl0p; Truebot web shell | 5 |
| Qilin | 5 |
| RansomHub | 5 |
| DoppelPaymer | 4 |
| DragonForce | 4 |
| Hunters International | 4 |
| Interlock | 4 |
| LockBit | 4 |
| POS | 4 |
| REvil (Sodinokibi) | 4 |
| TeamPCP Cloud Stealer | 4 |

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
CVE-2017-10271
CVE-2017-3248
CVE-2017-3506
CVE-2017-5638
CVE-2019-11510
CVE-2019-18187
CVE-2019-19781
CVE-2020-10148
CVE-2020-5741
CVE-2020-8260
CVE-2021-20016
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
CVE-2024-1708
CVE-2024-1709
CVE-2024-21887
CVE-2024-21893
CVE-2024-27198
CVE-2024-27199
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
| Compromise of third-party service provider / vendor relationship | 556 |
| Smart contract exploit / hack | 361 |
| Regulatory / legal action | 279 |
| Protocol collapse / insolvency | 111 |
| Exit scam / rug pull | 101 |
| On-chain theft (attributed by zachxbt) | 66 |
| Flash loan attack on smart contract | 60 |
| Software bug / unintentional loss | 58 |
| Phishing attack | 53 |
| Ponzi / pyramid scheme | 42 |
| Withdrawal halt / insolvency | 39 |
| Nation-state attack (Lazarus/DPRK) — private key or social engineering compromise | 22 |
| AI-assisted attack or AI-generated exploit | 19 |
| Oracle price manipulation | 18 |
| CWE-284: Improper Access Control | 15 |

## Incident Index

| File | Category | Breach Date | Malware | CVEs |
|------|----------|-------------|---------|------|
| [2026-04_massachusetts-hospital-ambulance-diversion.yaml](ransomware/2026-04_massachusetts-hospital-ambulance-diversion.yaml) | ransomware | 2026-04-07 |  |  |
| [2026-04_chipsoft-netherlands-hospitals.yaml](ransomware/2026-04_chipsoft-netherlands-hospitals.yaml) | ransomware | 2026-04-07 |  |  |
| [2026-04_bitcoin-depot-hack.yaml](data-leak/2026-04_bitcoin-depot-hack.yaml) | data-leak | 2026-04-06 |  |  |
| [2026-04_cisco-trivy-teamPCP-source-code.yaml](supply-chain/2026-04_cisco-trivy-teamPCP-source-code.yaml) | supply-chain | 2026-04-03 | TeamPCP Cloud Stealer |  |
| [2026-04_drift-protocol-dprk-285m.yaml](other/2026-04_drift-protocol-dprk-285m.yaml) | other | 2026-04-01 |  |  |
| [2026-04_drift-exploit.yaml](data-leak/2026-04_drift-exploit.yaml) | data-leak | 2026-04-01 |  |  |
| [2026-03_axios-npm-sapphire-sleet-dprk.yaml](supply-chain/2026-03_axios-npm-sapphire-sleet-dprk.yaml) | supply-chain | 2026-03-31 | Sapphire Sleet RAT |  |
| [2026-03_litellm-pypi-mercor-teamPCP.yaml](supply-chain/2026-03_litellm-pypi-mercor-teamPCP.yaml) | supply-chain | 2026-03-27 |  |  |
| [2026-03_teamPCP-telnyx-pypi.yaml](supply-chain/2026-03_teamPCP-telnyx-pypi.yaml) | supply-chain | 2026-03-27 | TeamPCP Cloud Stealer |  |
| [2026-03_litellm-hit-in-cascading-supply-chain-attack.yaml](credential-theft/2026-03_litellm-hit-in-cascading-supply-chain-attack.yaml) | supply-chain | 2026-03-26 |  |  |
| [2026-03_nyc-health-notifying-patients-of-2-third-party-hacks.yaml](supply-chain/2026-03_nyc-health-notifying-patients-of-2-third-party-hacks.yaml) | supply-chain | 2026-03-26 |  |  |
| [2026-03_die-linke-qilin-germany.yaml](ransomware/2026-03_die-linke-qilin-germany.yaml) | ransomware | 2026-03-26 | Qilin |  |
| [2026-03_handala-iran-fbi-director-kash-patel-email.yaml](credential-theft/2026-03_handala-iran-fbi-director-kash-patel-email.yaml) | credential-theft | 2026-03-25 |  |  |
| [2026-04_hasbro-it-systems-breach.yaml](data-leak/2026-04_hasbro-it-systems-breach.yaml) | data-leak | 2026-03-25 |  |  |
| [2026-03_balancer-labs-shuts-down.yaml](other/2026-03_balancer-labs-shuts-down.yaml) | other | 2026-03-24 |  |  |
| [2026-03_moonwell-governance-attack.yaml](other/2026-03_moonwell-governance-attack.yaml) | other | 2026-03-24 |  |  |
| [2026-03_resolv-protocol-24m-defi-exploit.yaml](other/2026-03_resolv-protocol-24m-defi-exploit.yaml) | other | 2026-03-22 |  |  |
| [2026-03_usr-stablecoin-depeg.yaml](data-leak/2026-03_usr-stablecoin-depeg.yaml) | data-leak | 2026-03-22 |  |  |
| [2026-03_teamPCP-checkmarx-kics.yaml](supply-chain/2026-03_teamPCP-checkmarx-kics.yaml) | supply-chain | 2026-03-21 | TeamPCP Cloud Stealer |  |
| [2026-03_lapd-city-attorney-worldleaks.yaml](data-leak/2026-03_lapd-city-attorney-worldleaks.yaml) | data-leak | 2026-03-20 |  |  |
| [2026-03_multi-month-cyberespionage-campaign-hits-libyan-oil-refinery.yaml](credential-theft/2026-03_multi-month-cyberespionage-campaign-hits-libyan-oil-refinery.yaml) | other | 2026-03-20 |  |  |
| [2026-03_bitcoin-depot-crypto-theft.yaml](other/2026-03_bitcoin-depot-crypto-theft.yaml) | other | 2026-03-20 |  |  |
| [2026-03_european-commission-shinyhunters-aws.yaml](data-leak/2026-03_european-commission-shinyhunters-aws.yaml) | data-leak | 2026-03-19 |  |  |
| [2026-03_cryptohack-roundup-appsflyer-sdk-breach-enabled-theft.yaml](data-leak/2026-03_cryptohack-roundup-appsflyer-sdk-breach-enabled-theft.yaml) | supply-chain | 2026-03-19 |  |  |
| [2026-03_teamPCP-trivy-github-actions.yaml](supply-chain/2026-03_teamPCP-trivy-github-actions.yaml) | supply-chain | 2026-03-19 | TeamPCP Cloud Stealer | CVE-2026-33634 |
| [2026-03_worker-benefits-administrator-notifying-2-7m-of-hack.yaml](data-leak/2026-03_worker-benefits-administrator-notifying-2-7m-of-hack.yaml) | data-leak | 2026-03-19 |  |  |
| [2026-03_interlock-ransomware-exploited-cisco-firewall-flaw-for-weeks.yaml](ransomware/2026-03_interlock-ransomware-exploited-cisco-firewall-flaw-for-weeks.yaml) | ransomware | 2026-03-18 |  |  |
| [2026-03_stryker-wiper-attack-hackers-boast-as-lawsuits-pile-up.yaml](ransomware/2026-03_stryker-wiper-attack-hackers-boast-as-lawsuits-pile-up.yaml) | other | 2026-03-18 |  |  |
| [2026-03_aura-identity-shinyhunters-vishing.yaml](data-leak/2026-03_aura-identity-shinyhunters-vishing.yaml) | data-leak | 2026-03-17 |  |  |
| [2026-03_venus-protocol-bad-debt.yaml](data-leak/2026-03_venus-protocol-bad-debt.yaml) | data-leak | 2026-03-17 |  |  |
| [2026-03_carecloud-ehr-breach.yaml](data-leak/2026-03_carecloud-ehr-breach.yaml) | data-leak | 2026-03-16 |  |  |
| [2026-03_blockfills-goes-bankrupt.yaml](other/2026-03_blockfills-goes-bankrupt.yaml) | other | 2026-03-15 |  |  |
| [2026-03_crunchyroll-bpo-okta-breach.yaml](data-leak/2026-03_crunchyroll-bpo-okta-breach.yaml) | data-leak | 2026-03-12 | infostealer (unspecified) |  |
| [2026-03_aave-swap-loss.yaml](other/2026-03_aave-swap-loss.yaml) | other | 2026-03-12 |  |  |
| [2026-03_stryker-handala-intune-wiper.yaml](other/2026-03_stryker-handala-intune-wiper.yaml) | other | 2026-03-11 |  |  |
| [2026-03_chaos-labs-aave-liquidations.yaml](other/2026-03_chaos-labs-aave-liquidations.yaml) | other | 2026-03-10 |  |  |
| [2026-03_gondi-theft.yaml](data-leak/2026-03_gondi-theft.yaml) | data-leak | 2026-03-09 |  |  |
| [2026-03_hhs-ocr-fines-firm-10k-in-breach-affecting-15m.yaml](supply-chain/2026-03_hhs-ocr-fines-firm-10k-in-breach-affecting-15m.yaml) | supply-chain | 2026-03-06 |  |  |
| [2026-03_trizetto-notifying-3-4m-of-2024-hack-detected-in-2025.yaml](supply-chain/2026-03_trizetto-notifying-3-4m-of-2024-hack-detected-in-2025.yaml) | supply-chain | 2026-03-05 |  |  |
| [2026-03_solv-protocol-exploit.yaml](data-leak/2026-03_solv-protocol-exploit.yaml) | data-leak | 2026-03-05 |  |  |
| [2026-03_cancer-center-research-study-hack-affects-1-2m.yaml](ransomware/2026-03_cancer-center-research-study-hack-affects-1-2m.yaml) | ransomware | 2026-03-04 |  |  |
| [2026-03_returned-crypto-stolen-again-from-korean-authorities.yaml](data-leak/2026-03_returned-crypto-stolen-again-from-korean-authorities.yaml) | data-leak | 2026-03-03 |  |  |
| [2026-03_unc6426-nx-npm-aws-takeover.yaml](supply-chain/2026-03_unc6426-nx-npm-aws-takeover.yaml) | supply-chain | 2026-03-01 |  |  |
| [2026-04_anodot-shinyhunters-snowflake-tokens.yaml](credential-theft/2026-04_anodot-shinyhunters-snowflake-tokens.yaml) | credential-theft | 2026-03-01 |  |  |
| [2026-03_california-orthopedic-device-maker-hack.yaml](data-leak/2026-03_california-orthopedic-device-maker-hack.yaml) | data-leak | 2026-03-01 |  |  |
| [2026-03_dutch-ministry-finance-breach.yaml](data-leak/2026-03_dutch-ministry-finance-breach.yaml) | data-leak | 2026-03-01 |  |  |
| [2026-03_lloyds-banking-group-450k-leak.yaml](data-leak/2026-03_lloyds-banking-group-450k-leak.yaml) | data-leak | 2026-03-01 |  |  |
| [2026-03_bithumb-exchange-hack-recovery.yaml](other/2026-03_bithumb-exchange-hack-recovery.yaml) | other | 2026-03-01 |  |  |
| [2026-03_fbi-seizes-handala-iranian-leak-domains.yaml](other/2026-03_fbi-seizes-handala-iranian-leak-domains.yaml) | other | 2026-03-01 |  |  |
| [2026-02_malaysia-airlines-qilin.yaml](ransomware/2026-02_malaysia-airlines-qilin.yaml) | ransomware | 2026-02-26 | Qilin |  |
| [2026-02_crypto-stolen-from-korean-authorities-after-they-post-wallet-seed-phrase.yaml](data-leak/2026-02_crypto-stolen-from-korean-authorities-after-they-post-wallet-seed-phrase.yaml) | data-leak | 2026-02-26 |  |  |
| [2026-02_medical-device-maker-reports-data-theft-hack-to-sec.yaml](data-leak/2026-02_medical-device-maker-reports-data-theft-hack-to-sec.yaml) | data-leak | 2026-02-25 |  |  |
| [2026-02_paypal-ties-small-data-breach-and-fraud-to-app-coding-error.yaml](data-leak/2026-02_paypal-ties-small-data-breach-and-fraud-to-app-coding-error.yaml) | data-leak | 2026-02-23 |  |  |
| [2026-02_step-finance-shuts-down.yaml](other/2026-02_step-finance-shuts-down.yaml) | other | 2026-02-23 |  |  |
| [2026-02_iotex-bridge-exploit.yaml](data-leak/2026-02_iotex-bridge-exploit.yaml) | data-leak | 2026-02-21 |  |  |
| [2026-02_yieldblox-theft.yaml](data-leak/2026-02_yieldblox-theft.yaml) | data-leak | 2026-02-21 |  |  |
| [2026-02_goliath-ventures-ceo-charged.yaml](data-leak/2026-02_goliath-ventures-ceo-charged.yaml) | data-leak | 2026-02-20 |  |  |
| [2026-02_phishing-attack-on-south-korean-prosecutors.yaml](data-leak/2026-02_phishing-attack-on-south-korean-prosecutors.yaml) | data-leak | 2026-02-19 |  |  |
| [2026-02_ummc-medusa-ransomware.yaml](ransomware/2026-02_ummc-medusa-ransomware.yaml) | ransomware | 2026-02-19 | Medusa |  |
| [2026-02_fbi-dcsnet-china-surveillance.yaml](other/2026-02_fbi-dcsnet-china-surveillance.yaml) | other | 2026-02-17 |  |  |
| [2026-02_kettering-health-notifying-patients-of-interlock-breach.yaml](data-leak/2026-02_kettering-health-notifying-patients-of-interlock-breach.yaml) | ransomware | 2026-02-17 |  |  |
| [2026-02_moonwell-exploit.yaml](other/2026-02_moonwell-exploit.yaml) | other | 2026-02-15 |  |  |
| [2026-02_blockfills-crypto-lender-halts-withdrawals.yaml](other/2026-02_blockfills-crypto-lender-halts-withdrawals.yaml) | other | 2026-02-11 |  |  |
| [2026-02_bithumb-giveaway-error.yaml](other/2026-02_bithumb-giveaway-error.yaml) | other | 2026-02-07 |  |  |
| [2026-02_odido-dutch-telecom-shinyhunters.yaml](data-leak/2026-02_odido-dutch-telecom-shinyhunters.yaml) | data-leak | 2026-02-07 |  |  |
| [2026-02_bridgepay-ransomware-outage.yaml](ransomware/2026-02_bridgepay-ransomware-outage.yaml) | ransomware | 2026-02-06 |  |  |
| [2026-02_gemini-layoffs.yaml](other/2026-02_gemini-layoffs.yaml) | other | 2026-02-05 |  |  |
| [2026-02_ex-nuance-it-worker-faces-more-charges-in-geisinger-breach.yaml](data-leak/2026-02_ex-nuance-it-worker-faces-more-charges-in-geisinger-breach.yaml) | data-leak | 2026-02-05 |  |  |
| [2026-02_harvard-upenn-data-leaked-in-shinyhunters-shakedown.yaml](data-leak/2026-02_harvard-upenn-data-leaked-in-shinyhunters-shakedown.yaml) | data-leak | 2026-02-04 |  |  |
| [2026-02_hims-hers-zendesk-shinyhunters.yaml](data-leak/2026-02_hims-hers-zendesk-shinyhunters.yaml) | data-leak | 2026-02-04 |  |  |
| [2026-02_sears-home-services-chatbot-exposure.yaml](data-leak/2026-02_sears-home-services-chatbot-exposure.yaml) | data-leak | 2026-02-03 |  |  |
| [2026-02_capital-health-to-pay-4-5m-in-lockbit-breach-settlement.yaml](ransomware/2026-02_capital-health-to-pay-4-5m-in-lockbit-breach-settlement.yaml) | ransomware | 2026-02-02 |  |  |
| [2026-02_crosscurve-users-exploited-for-around-3-million.yaml](data-leak/2026-02_crosscurve-users-exploited-for-around-3-million.yaml) | data-leak | 2026-02-01 |  |  |
| [2026-02_cargurus-shinyhunters-social-engineering.yaml](data-leak/2026-02_cargurus-shinyhunters-social-engineering.yaml) | data-leak | 2026-02-01 |  |  |
| [2026-03_lexisnexis-law-firm-breach.yaml](data-leak/2026-03_lexisnexis-law-firm-breach.yaml) | data-leak | 2026-02-01 |  |  |
| [2026-01_step-finance-theft.yaml](data-leak/2026-01_step-finance-theft.yaml) | data-leak | 2026-01-31 |  |  |
| [2026-01_glassworm-open-vsx-extensions.yaml](supply-chain/2026-01_glassworm-open-vsx-extensions.yaml) | supply-chain | 2026-01-30 | GlassWorm |  |
| [2026-01_ambulance-billing-firm-pays-515k-fine-to-2-states-in-hack.yaml](data-leak/2026-01_ambulance-billing-firm-pays-515k-fine-to-2-states-in-hack.yaml) | data-leak | 2026-01-29 |  |  |
| [2026-01_ai-powered-services-firm-says-hack-affects-3-1m.yaml](data-leak/2026-01_ai-powered-services-firm-says-hack-affects-3-1m.yaml) | data-leak | 2026-01-28 |  |  |
| [2026-01_aperture-finance-exploit.yaml](data-leak/2026-01_aperture-finance-exploit.yaml) | data-leak | 2026-01-25 |  |  |
| [2026-01_matcha-meta-exploit.yaml](data-leak/2026-01_matcha-meta-exploit.yaml) | data-leak | 2026-01-25 |  |  |
| [2026-01_lick-theft.yaml](other/2026-01_lick-theft.yaml) | other | 2026-01-23 |  |  |
| [2026-01_breach-roundup-doge-uploaded-social-security-data-to-cloud.yaml](credential-theft/2026-01_breach-roundup-doge-uploaded-social-security-data-to-cloud.yaml) | data-leak | 2026-01-22 |  |  |
| [2026-01_saga-exploit.yaml](data-leak/2026-01_saga-exploit.yaml) | data-leak | 2026-01-21 |  |  |
| [2026-01_ehr-vendor-veradigm-to-pay-10-5m-to-settle-hack-lawsuit.yaml](supply-chain/2026-01_ehr-vendor-veradigm-to-pay-10-5m-to-settle-hack-lawsuit.yaml) | supply-chain | 2026-01-21 |  |  |
| [2026-01_minnesota-agency-notifies-304-000-of-vendor-breach.yaml](supply-chain/2026-01_minnesota-agency-notifies-304-000-of-vendor-breach.yaml) | supply-chain | 2026-01-20 |  |  |
| [2026-01_ransomware-most-wanted-cops-seek-head-of-black-basta.yaml](ransomware/2026-01_ransomware-most-wanted-cops-seek-head-of-black-basta.yaml) | other | 2026-01-19 |  |  |
| [2026-01_starbucks-partner-central-phishing.yaml](credential-theft/2026-01_starbucks-partner-central-phishing.yaml) | credential-theft | 2026-01-19 |  |  |
| [2026-01_nyc-token-crash.yaml](other/2026-01_nyc-token-crash.yaml) | other | 2026-01-12 |  |  |
| [2026-01_trezor-support-scam.yaml](data-leak/2026-01_trezor-support-scam.yaml) | data-leak | 2026-01-10 |  |  |
| [2026-01_crunchbase-shinyhunters-vishing.yaml](data-leak/2026-01_crunchbase-shinyhunters-vishing.yaml) | data-leak | 2026-01-09 |  |  |
| [2026-01_betterment-shinyhunters-vishing.yaml](data-leak/2026-01_betterment-shinyhunters-vishing.yaml) | data-leak | 2026-01-09 |  |  |
| [2026-01_truebit-exploit.yaml](data-leak/2026-01_truebit-exploit.yaml) | data-leak | 2026-01-08 |  |  |
| [2026-01_bumble-match-shinyhunters-vishing.yaml](data-leak/2026-01_bumble-match-shinyhunters-vishing.yaml) | data-leak | 2026-01-01 |  |  |
| [2026-04_gru-apt28-soho-router-dns-hijacking.yaml](other/2026-04_gru-apt28-soho-router-dns-hijacking.yaml) | other | 2026-01-01 | MooBot (Mirai variant), custo… |  |
| [2026-01_figure-fintech-shinyhunters-vishing.yaml](data-leak/2026-01_figure-fintech-shinyhunters-vishing.yaml) | data-leak | 2026-01-01 |  |  |
| [2026-03_telus-digital-shinyhunters.yaml](data-leak/2026-03_telus-digital-shinyhunters.yaml) | data-leak | 2026-01-01 |  |  |
| [2025-12_sedgwick-government-tridentlocker.yaml](ransomware/2025-12_sedgwick-government-tridentlocker.yaml) | ransomware | 2025-12-31 | TridentLocker |  |
| [2025-12_unleash-protocol-exploit.yaml](data-leak/2025-12_unleash-protocol-exploit.yaml) | data-leak | 2025-12-30 |  |  |
| [2025-12_flow-infinite-mint-exploit.yaml](data-leak/2025-12_flow-infinite-mint-exploit.yaml) | data-leak | 2025-12-27 |  |  |
| [2025-12_eurail-aws-s3-passport-breach.yaml](data-leak/2025-12_eurail-aws-s3-passport-breach.yaml) | data-leak | 2025-12-26 |  |  |
| [2025-12_trust-wallet-hack.yaml](supply-chain/2025-12_trust-wallet-hack.yaml) | supply-chain | 2025-12-25 |  |  |
| [2026-01_navia-benefit-solutions-bola.yaml](data-leak/2026-01_navia-benefit-solutions-bola.yaml) | data-leak | 2025-12-22 |  |  |
| [2025-12_conde-nast-wired-idor-breach.yaml](data-leak/2025-12_conde-nast-wired-idor-breach.yaml) | data-leak | 2025-12-20 |  |  |
| [2025-12_0xcb8078-address-poisoning.yaml](data-leak/2025-12_0xcb8078-address-poisoning.yaml) | data-leak | 2025-12-19 |  |  |
| [2025-12_yearn-finance-exploit-4.yaml](data-leak/2025-12_yearn-finance-exploit-4.yaml) | data-leak | 2025-12-16 |  |  |
| [2025-12_soundcloud-shinyhunters-vishing.yaml](data-leak/2025-12_soundcloud-shinyhunters-vishing.yaml) | data-leak | 2025-12-15 |  |  |
| [2025-12_ribbon-finance-exploit.yaml](data-leak/2025-12_ribbon-finance-exploit.yaml) | data-leak | 2025-12-12 |  |  |
| [2025-12_binance-employee-suspended.yaml](other/2025-12_binance-employee-suspended.yaml) | other | 2025-12-08 |  |  |
| [2025-12_prysm-consensus-client-bug.yaml](other/2025-12_prysm-consensus-client-bug.yaml) | other | 2025-12-04 |  |  |
| [2025-12_shuffles-pinterest-app-mixpanel.yaml](supply-chain/2025-12_shuffles-pinterest-app-mixpanel.yaml) | supply-chain | 2025-12-01 |  |  |
| [2026-01_brightspeed-crimson-collective.yaml](data-leak/2026-01_brightspeed-crimson-collective.yaml) | data-leak | 2025-12-01 |  |  |
| [2025-12_pornhub-mixpanel.yaml](supply-chain/2025-12_pornhub-mixpanel.yaml) | supply-chain | 2025-12-01 |  |  |
| [2026-01_ledger-global-e-third-party.yaml](data-leak/2026-01_ledger-global-e-third-party.yaml) | data-leak | 2025-12-01 |  |  |
| [2025-12_freedom-mobile-third-party-vendor.yaml](supply-chain/2025-12_freedom-mobile-third-party-vendor.yaml) | supply-chain | 2025-12-01 |  |  |
| [2025-12_customers-of-74-banks-and-credit-unions-served-by-marquis-software-solutions-marquis-software-solutions.yaml](supply-chain/2025-12_customers-of-74-banks-and-credit-unions-served-by-marquis-software-solutions-marquis-software-solutions.yaml) | supply-chain | 2025-12-01 |  |  |
| [2026-02_cegedim-sante-monlogicielmedical.yaml](data-leak/2026-02_cegedim-sante-monlogicielmedical.yaml) | data-leak | 2025-12-01 |  |  |
| [2025-11_yearn-finance-hack-3.yaml](data-leak/2025-11_yearn-finance-hack-3.yaml) | data-leak | 2025-11-30 |  |  |
| [2025-11_upbit-hack.yaml](data-leak/2025-11_upbit-hack.yaml) | data-leak | 2025-11-27 |  |  |
| [2025-11_openai-mixpanel-vendor.yaml](other/2025-11_openai-mixpanel-vendor.yaml) | other | 2025-11-26 |  |  |
| [2025-11_aerodrome-and-velodrome-suffer-website-takeovers.yaml](data-leak/2025-11_aerodrome-and-velodrome-suffer-website-takeovers.yaml) | data-leak | 2025-11-22 |  |  |
| [2025-11_cardano-founder-calls-the-fbi-after-chainsplit.yaml](other/2025-11_cardano-founder-calls-the-fbi-after-chainsplit.yaml) | other | 2025-11-21 |  |  |
| [2025-11_gana-payment-hacked-for-3-1-million.yaml](data-leak/2025-11_gana-payment-hacked-for-3-1-million.yaml) | data-leak | 2025-11-20 |  |  |
| [2025-11_dappradar-shuts-down.yaml](other/2025-11_dappradar-shuts-down.yaml) | other | 2025-11-17 |  |  |
| [2025-11_cardano-holder-loses-6-million-to-slippage.yaml](other/2025-11_cardano-holder-loses-6-million-to-slippage.yaml) | other | 2025-11-16 |  |  |
| [2025-11_situsamc-banks-breach.yaml](data-leak/2025-11_situsamc-banks-breach.yaml) | data-leak | 2025-11-12 |  |  |
| [2025-11_idmerit-mongodb-kyc-exposure.yaml](data-leak/2025-11_idmerit-mongodb-kyc-exposure.yaml) | data-leak | 2025-11-11 |  |  |
| [2025-11_coupang-insider-33m-korea.yaml](data-leak/2025-11_coupang-insider-33m-korea.yaml) | data-leak | 2025-11-08 |  |  |
| [2025-11_elixir-shuts-down-deusd.yaml](other/2025-11_elixir-shuts-down-deusd.yaml) | other | 2025-11-06 |  |  |
| [2025-11_stream-finance-loss.yaml](data-leak/2025-11_stream-finance-loss.yaml) | data-leak | 2025-11-04 |  |  |
| [2025-11_moonwell-oracle-malfunction.yaml](data-leak/2025-11_moonwell-oracle-malfunction.yaml) | data-leak | 2025-11-04 |  |  |
| [2025-11_balancer-exploit-2.yaml](data-leak/2025-11_balancer-exploit-2.yaml) | data-leak | 2025-11-03 |  |  |
| [2025-11_iberia-international-airlines-group-third-party-vendor.yaml](supply-chain/2025-11_iberia-international-airlines-group-third-party-vendor.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-11_logitech-third-party-vendor.yaml](supply-chain/2025-11_logitech-third-party-vendor.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-11_openai-mixpanel.yaml](supply-chain/2025-11_openai-mixpanel.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-11_terminalen-a-s-docubizz.yaml](supply-chain/2025-11_terminalen-a-s-docubizz.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-11_under-armour-everest-ransomware.yaml](ransomware/2025-11_under-armour-everest-ransomware.yaml) | ransomware | 2025-11-01 | Everest |  |
| [2025-11_cbo-china-hack.yaml](other/2025-11_cbo-china-hack.yaml) | other | 2025-11-01 |  |  |
| [2025-11_checkout-com-third-party-vendor.yaml](supply-chain/2025-11_checkout-com-third-party-vendor.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-12_freedom-mobile-third-party.yaml](data-leak/2025-12_freedom-mobile-third-party.yaml) | data-leak | 2025-11-01 |  |  |
| [2025-11_the-washington-post-oracle-e-business-suite.yaml](supply-chain/2025-11_the-washington-post-oracle-e-business-suite.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-12_marquis-software-74-banks.yaml](data-leak/2025-12_marquis-software-74-banks.yaml) | supply-chain | 2025-11-01 |  |  |
| [2025-10_garden-hacked-for-11-million.yaml](data-leak/2025-10_garden-hacked-for-11-million.yaml) | data-leak | 2025-10-30 |  |  |
| [2025-10_doordash-social-engineering.yaml](data-leak/2025-10_doordash-social-engineering.yaml) | data-leak | 2025-10-25 |  |  |
| [2025-10_fortress-trust-insolvency.yaml](other/2025-10_fortress-trust-insolvency.yaml) | other | 2025-10-22 |  |  |
| [2025-10_cryptomus-fine.yaml](other/2025-10_cryptomus-fine.yaml) | other | 2025-10-22 |  |  |
| [2025-11_mixpanel-analytics-multi-company.yaml](supply-chain/2025-11_mixpanel-analytics-multi-company.yaml) | supply-chain | 2025-10-15 |  |  |
| [2025-10_paxos-accidental-mint.yaml](other/2025-10_paxos-accidental-mint.yaml) | other | 2025-10-15 |  |  |
| [2025-11_iberia-iag-loyalty-breach.yaml](data-leak/2025-11_iberia-iag-loyalty-breach.yaml) | data-leak | 2025-10-15 |  |  |
| [2025-10_0x0cdc-theft.yaml](data-leak/2025-10_0x0cdc-theft.yaml) | data-leak | 2025-10-10 |  |  |
| [2025-10_abracadabra-exploit-3.yaml](data-leak/2025-10_abracadabra-exploit-3.yaml) | data-leak | 2025-10-04 |  |  |
| [2025-11_openai-mixpanel-analytics-leak.yaml](data-leak/2025-11_openai-mixpanel-analytics-leak.yaml) | data-leak | 2025-10-01 |  |  |
| [2025-11_washington-post-oracle-ebs-breach.yaml](data-leak/2025-11_washington-post-oracle-ebs-breach.yaml) | data-leak | 2025-10-01 |  | CVE-2025-61882 |
| [2025-10_redhat-gitlab-crimson-collective.yaml](supply-chain/2025-10_redhat-gitlab-crimson-collective.yaml) | supply-chain | 2025-10-01 |  |  |
| [2025-10_renault-and-dacia-uk-third-party-vendor.yaml](supply-chain/2025-10_renault-and-dacia-uk-third-party-vendor.yaml) | supply-chain | 2025-10-01 |  |  |
| [2025-10_discord-third-party-vendor.yaml](supply-chain/2025-10_discord-third-party-vendor.yaml) | supply-chain | 2025-10-01 |  |  |
| [2025-10_docketwise-credential-immigration.yaml](data-leak/2025-10_docketwise-credential-immigration.yaml) | data-leak | 2025-10-01 |  |  |
| [2025-10_discord-third-party-customer-service-55m.yaml](data-leak/2025-10_discord-third-party-customer-service-55m.yaml) | data-leak | 2025-10-01 |  |  |
| [2025-10_mango-third-party-vendor.yaml](supply-chain/2025-10_mango-third-party-vendor.yaml) | supply-chain | 2025-10-01 |  |  |
| [2025-09_futureverse-announces-restructuring.yaml](other/2025-09_futureverse-announces-restructuring.yaml) | other | 2025-09-29 |  |  |
| [2025-09_hyperdrive-exploit.yaml](data-leak/2025-09_hyperdrive-exploit.yaml) | data-leak | 2025-09-27 |  |  |
| [2025-09_hypervault-rug-pull.yaml](other/2025-09_hypervault-rug-pull.yaml) | other | 2025-09-26 |  |  |
| [2025-09_griffin-ai-exploit.yaml](data-leak/2025-09_griffin-ai-exploit.yaml) | data-leak | 2025-09-24 |  |  |
| [2025-09_sbi-crypto-theft.yaml](data-leak/2025-09_sbi-crypto-theft.yaml) | data-leak | 2025-09-24 |  |  |
| [2025-09_seedify-bridge-exploit.yaml](data-leak/2025-09_seedify-bridge-exploit.yaml) | data-leak | 2025-09-23 |  |  |
| [2025-09_uxlink-exploit.yaml](data-leak/2025-09_uxlink-exploit.yaml) | data-leak | 2025-09-22 |  |  |
| [2025-09_insightin-health-goanywhere-medusa.yaml](ransomware/2025-09_insightin-health-goanywhere-medusa.yaml) | ransomware | 2025-09-17 | Medusa |  |
| [2025-10_mango-marketing-provider-breach.yaml](data-leak/2025-10_mango-marketing-provider-breach.yaml) | data-leak | 2025-09-15 |  |  |
| [2025-09_yala-stablecoin-depegs.yaml](other/2025-09_yala-stablecoin-depegs.yaml) | other | 2025-09-14 |  |  |
| [2025-09_shai-hulud-npm-worm.yaml](supply-chain/2025-09_shai-hulud-npm-worm.yaml) | supply-chain | 2025-09-14 | Shai-Hulud |  |
| [2025-09_shibarium-bridge-hit-with-2-4-million-flash-loan-attack.yaml](data-leak/2025-09_shibarium-bridge-hit-with-2-4-million-flash-loan-attack.yaml) | data-leak | 2025-09-12 |  |  |
| [2025-09_swissborg-exploit.yaml](data-leak/2025-09_swissborg-exploit.yaml) | data-leak | 2025-09-09 |  |  |
| [2025-09_thorchain-founder-exploited.yaml](data-leak/2025-09_thorchain-founder-exploited.yaml) | data-leak | 2025-09-09 |  |  |
| [2025-09_massive-npm-supply-chain-attack-puts-crypto-transactions-at-risk.yaml](supply-chain/2025-09_massive-npm-supply-chain-attack-puts-crypto-transactions-at-risk.yaml) | supply-chain | 2025-09-08 |  |  |
| [2025-09_npm-chalk-debug-phishing.yaml](supply-chain/2025-09_npm-chalk-debug-phishing.yaml) | supply-chain | 2025-09-08 | Browser crypto wallet stealer… |  |
| [2025-09_nemo-protocol-exploit.yaml](data-leak/2025-09_nemo-protocol-exploit.yaml) | data-leak | 2025-09-07 |  |  |
| [2025-09_bunni-exploit.yaml](data-leak/2025-09_bunni-exploit.yaml) | data-leak | 2025-09-02 |  |  |
| [2025-09_venus-protocol-user-exploited.yaml](data-leak/2025-09_venus-protocol-user-exploited.yaml) | data-leak | 2025-09-02 |  |  |
| [2025-09_wynn-resorts-oracle-shinyhunters.yaml](data-leak/2025-09_wynn-resorts-oracle-shinyhunters.yaml) | data-leak | 2025-09-01 |  |  |
| [2025-09_cloudflare-drift-salesloft.yaml](supply-chain/2025-09_cloudflare-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_hackerone-drift-salesloft.yaml](supply-chain/2025-09_hackerone-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_harrods-third-party-vendor.yaml](supply-chain/2025-09_harrods-third-party-vendor.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_liveramp-drift-salesloft.yaml](supply-chain/2025-09_liveramp-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_london-north-eastern-railway-lner-third-party-vendor.yaml](supply-chain/2025-09_london-north-eastern-railway-lner-third-party-vendor.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_esker-drift-salesloft.yaml](supply-chain/2025-09_esker-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_ericom-software-drift-salesloft.yaml](supply-chain/2025-09_ericom-software-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_omada-drift-salesloft.yaml](supply-chain/2025-09_omada-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_onespan-drift-salesloft.yaml](supply-chain/2025-09_onespan-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_palo-alto-networks-drift-salesloft.yaml](supply-chain/2025-09_palo-alto-networks-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_pantheon-drift-salesloft.yaml](supply-chain/2025-09_pantheon-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_proofpoint-drift-salesloft.yaml](supply-chain/2025-09_proofpoint-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_qualys-inc-drift-salesloft.yaml](supply-chain/2025-09_qualys-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_employment-and-social-development-canada-esdc-2keys-corporation.yaml](supply-chain/2025-09_employment-and-social-development-canada-esdc-2keys-corporation.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_sigma-computing-drift-salesloft.yaml](supply-chain/2025-09_sigma-computing-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_sophos-ltd-drift-salesloft.yaml](supply-chain/2025-09_sophos-ltd-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_sprout-social-inc-drift-salesloft.yaml](supply-chain/2025-09_sprout-social-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_spycloud-inc-drift-salesloft.yaml](supply-chain/2025-09_spycloud-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_stellantis-salesforce.yaml](supply-chain/2025-09_stellantis-salesforce.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_swissborg-kiln.yaml](supply-chain/2025-09_swissborg-kiln.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_tenable-inc-drift-salesloft.yaml](supply-chain/2025-09_tenable-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_wealthsimple-third-party-vendor.yaml](supply-chain/2025-09_wealthsimple-third-party-vendor.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_workday-drift-salesloft.yaml](supply-chain/2025-09_workday-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_workiva-drift-salesloft.yaml](supply-chain/2025-09_workiva-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_elasticsearch-b-v-drift-salesloft.yaml](supply-chain/2025-09_elasticsearch-b-v-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_dynatrace-llc-drift-salesloft.yaml](supply-chain/2025-09_dynatrace-llc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_cyberark-software-ltd-drift-salesloft.yaml](supply-chain/2025-09_cyberark-software-ltd-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_contentsquare-drift-salesloft.yaml](supply-chain/2025-09_contentsquare-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_fastly-drift-salesloft.yaml](supply-chain/2025-09_fastly-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_chess-com-third-party-vendor.yaml](supply-chain/2025-09_chess-com-third-party-vendor.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_cato-networks-drift-salesloft.yaml](supply-chain/2025-09_cato-networks-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_bugcrowd-drift-salesloft.yaml](supply-chain/2025-09_bugcrowd-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_black-duck-software-inc-drift-salesloft.yaml](supply-chain/2025-09_black-duck-software-inc-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_beyondtrust-drift-salesloft.yaml](supply-chain/2025-09_beyondtrust-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_agility-pr-solutions-drift-salesloft.yaml](supply-chain/2025-09_agility-pr-solutions-drift-salesloft.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_327-unknown-users-github-workflows.yaml](supply-chain/2025-09_327-unknown-users-github-workflows.yaml) | supply-chain | 2025-09-01 |  |  |
| [2025-09_swissborg-kiln-staking-41m-sol.yaml](data-leak/2025-09_swissborg-kiln-staking-41m-sol.yaml) | other | 2025-09-01 |  |  |
| [2025-10_renault-dacia-uk-third-party.yaml](data-leak/2025-10_renault-dacia-uk-third-party.yaml) | data-leak | 2025-09-01 |  |  |
| [2025-08_university-hawaii-cancer-center.yaml](ransomware/2025-08_university-hawaii-cancer-center.yaml) | ransomware | 2025-08-31 |  |  |
| [2025-09_jaguar-land-rover-scattered-lapsus.yaml](ransomware/2025-09_jaguar-land-rover-scattered-lapsus.yaml) | ransomware | 2025-08-31 |  |  |
| [2025-08_minnesota-dhs-fei-systems-insider.yaml](data-leak/2025-08_minnesota-dhs-fei-systems-insider.yaml) | data-leak | 2025-08-28 |  |  |
| [2025-08_reddit-shuts-down-nft-avatars.yaml](other/2025-08_reddit-shuts-down-nft-avatars.yaml) | other | 2025-08-28 |  |  |
| [2025-08_betterbank-exploit.yaml](other/2025-08_betterbank-exploit.yaml) | other | 2025-08-27 |  |  |
| [2025-08_insight-hospital-chicago-termite.yaml](ransomware/2025-08_insight-hospital-chicago-termite.yaml) | ransomware | 2025-08-22 | Termite |  |
| [2025-08_bitcoiner-socially-engineered-out-of-91-million.yaml](data-leak/2025-08_bitcoiner-socially-engineered-out-of-91-million.yaml) | data-leak | 2025-08-19 |  |  |
| [2025-09_wealthsimple-third-party-breach.yaml](data-leak/2025-09_wealthsimple-third-party-breach.yaml) | data-leak | 2025-08-15 |  |  |
| [2025-09_lner-third-party-vendor.yaml](data-leak/2025-09_lner-third-party-vendor.yaml) | data-leak | 2025-08-15 |  |  |
| [2025-08_btcturk-exploit-2.yaml](data-leak/2025-08_btcturk-exploit-2.yaml) | data-leak | 2025-08-14 |  |  |
| [2025-08_marquis-software-akira-banks.yaml](ransomware/2025-08_marquis-software-akira-banks.yaml) | ransomware | 2025-08-14 | Akira | CVE-2024-40766 |
| [2025-08_odin-fun-exploit.yaml](data-leak/2025-08_odin-fun-exploit.yaml) | data-leak | 2025-08-12 |  |  |
| [2025-08_monero-51-attack.yaml](other/2025-08_monero-51-attack.yaml) | other | 2025-08-12 |  |  |
| [2025-08_clop-oracle-ebs-education.yaml](supply-chain/2025-08_clop-oracle-ebs-education.yaml) | supply-chain | 2025-08-09 |  | CVE-2025-61882, CVE-2025-61884 |
| [2025-08_pennsylvania-ag-inc-ransom.yaml](ransomware/2025-08_pennsylvania-ag-inc-ransom.yaml) | ransomware | 2025-08-09 | INC Ransom | CVE-2025-5777 |
| [2025-08_salesloft-drift-oauth-salesforce.yaml](supply-chain/2025-08_salesloft-drift-oauth-salesforce.yaml) | supply-chain | 2025-08-08 |  |  |
| [2025-08_mev-bot-scam.yaml](data-leak/2025-08_mev-bot-scam.yaml) | data-leak | 2025-08-07 |  |  |
| [2025-08_wnba-sex-toy-incidents.yaml](other/2025-08_wnba-sex-toy-incidents.yaml) | other | 2025-08-07 |  |  |
| [2025-08_credix-exploit.yaml](data-leak/2025-08_credix-exploit.yaml) | data-leak | 2025-08-04 |  |  |
| [2025-08_bouygues-telecom-france-6m.yaml](data-leak/2025-08_bouygues-telecom-france-6m.yaml) | data-leak | 2025-08-04 |  |  |
| [2025-08_pagerduty-drift-salesloft.yaml](supply-chain/2025-08_pagerduty-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_pandora-salesforce.yaml](supply-chain/2025-08_pandora-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-09_harrods-third-party-breach.yaml](data-leak/2025-09_harrods-third-party-breach.yaml) | data-leak | 2025-08-01 |  |  |
| [2025-08_access-personal-checking-services-apcs-intradev.yaml](supply-chain/2025-08_access-personal-checking-services-apcs-intradev.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-09_chess-com-file-transfer-breach.yaml](data-leak/2025-09_chess-com-file-transfer-breach.yaml) | data-leak | 2025-08-01 |  |  |
| [2025-09_canada-2keys-government-accounts.yaml](data-leak/2025-09_canada-2keys-government-accounts.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_university-phoenix-oracle-ebs-clop.yaml](data-leak/2025-08_university-phoenix-oracle-ebs-clop.yaml) | data-leak | 2025-08-01 |  | CVE-2025-61882 |
| [2025-08_air-france-klm-group-salesforce.yaml](supply-chain/2025-08_air-france-klm-group-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_chanel-salesforce.yaml](supply-chain/2025-08_chanel-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_cisco-salesforce.yaml](supply-chain/2025-08_cisco-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_farmers-insurance-salesforce.yaml](supply-chain/2025-08_farmers-insurance-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_jfrog-drift-salesloft.yaml](supply-chain/2025-08_jfrog-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_lucid-software-inc-drift-salesloft.yaml](supply-chain/2025-08_lucid-software-inc-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_megaport-drift-salesloft.yaml](supply-chain/2025-08_megaport-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_miami-plastic-surgery-keys-dermatology-and-more-dermcare-management.yaml](supply-chain/2025-08_miami-plastic-surgery-keys-dermatology-and-more-dermcare-management.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_pi-hole-givewp-wordpress.yaml](supply-chain/2025-08_pi-hole-givewp-wordpress.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_rubrik-drift-salesloft.yaml](supply-chain/2025-08_rubrik-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_swedish-municipalities-milj-data.yaml](supply-chain/2025-08_swedish-municipalities-milj-data.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_tanium-drift-salesloft.yaml](supply-chain/2025-08_tanium-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_transunion-salesforce.yaml](supply-chain/2025-08_transunion-salesforce.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_uk-s-defence-ministry-and-the-cabinet-office-inflite-the-jet-centre-ltd.yaml](supply-chain/2025-08_uk-s-defence-ministry-and-the-cabinet-office-inflite-the-jet-centre-ltd.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-08_zscaler-drift-salesloft.yaml](supply-chain/2025-08_zscaler-drift-salesloft.yaml) | supply-chain | 2025-08-01 |  |  |
| [2025-07_abra-pauses-withdrawals-for-international-customers.yaml](other/2025-07_abra-pauses-withdrawals-for-international-customers.yaml) | other | 2025-07-29 |  |  |
| [2025-07_transunion-salesforce-unc6395.yaml](data-leak/2025-07_transunion-salesforce-unc6395.yaml) | data-leak | 2025-07-28 |  |  |
| [2025-07_superrare-hack.yaml](data-leak/2025-07_superrare-hack.yaml) | data-leak | 2025-07-28 |  |  |
| [2025-07_st-paul-minnesota-interlock.yaml](ransomware/2025-07_st-paul-minnesota-interlock.yaml) | ransomware | 2025-07-25 | Interlock ransomware |  |
| [2025-07_woo-x-hack.yaml](data-leak/2025-07_woo-x-hack.yaml) | data-leak | 2025-07-24 |  |  |
| [2025-07_coindcx-hack.yaml](data-leak/2025-07_coindcx-hack.yaml) | data-leak | 2025-07-18 |  |  |
| [2025-07_allianz-life-shiny-hunters.yaml](data-leak/2025-07_allianz-life-shiny-hunters.yaml) | data-leak | 2025-07-16 |  |  |
| [2025-07_bigone-hack.yaml](data-leak/2025-07_bigone-hack.yaml) | data-leak | 2025-07-16 |  |  |
| [2025-07_arcadia-finance-exploit.yaml](data-leak/2025-07_arcadia-finance-exploit.yaml) | data-leak | 2025-07-15 |  |  |
| [2025-07_moonpay-donation-scam.yaml](data-leak/2025-07_moonpay-donation-scam.yaml) | data-leak | 2025-07-11 |  |  |
| [2025-07_kinto-token-crashes.yaml](data-leak/2025-07_kinto-token-crashes.yaml) | data-leak | 2025-07-10 |  |  |
| [2025-07_vennbuild-discloses-bug.yaml](other/2025-07_vennbuild-discloses-bug.yaml) | other | 2025-07-09 |  |  |
| [2025-07_texture-hack.yaml](data-leak/2025-07_texture-hack.yaml) | data-leak | 2025-07-09 |  |  |
| [2025-07_gmx-hack.yaml](data-leak/2025-07_gmx-hack.yaml) | data-leak | 2025-07-09 |  |  |
| [2025-07_ingram-micro-safepay.yaml](ransomware/2025-07_ingram-micro-safepay.yaml) | ransomware | 2025-07-02 | SafePay |  |
| [2025-08_air-france-klm-salesforce.yaml](data-leak/2025-08_air-france-klm-salesforce.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-08_pandora-chanel-salesforce-shinyhunters.yaml](data-leak/2025-08_pandora-chanel-salesforce-shinyhunters.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_louis-vuitton-third-party-vendor.yaml](supply-chain/2025-07_louis-vuitton-third-party-vendor.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_mcdonald-s-paradox-inc.yaml](supply-chain/2025-07_mcdonald-s-paradox-inc.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_qantas-airways-limited-third-party-vendor.yaml](supply-chain/2025-07_qantas-airways-limited-third-party-vendor.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_texas-centers-for-infectious-disease-associates-third-party-vendor.yaml](supply-chain/2025-07_texas-centers-for-infectious-disease-associates-third-party-vendor.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_qantas-salesforce-shinyhunters-vishing.yaml](data-leak/2025-07_qantas-salesforce-shinyhunters-vishing.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_united-healthcare-aetna-life-insurance-company-cvs-health-and-46-more-kelly-associates-insurance-g.yaml](supply-chain/2025-07_united-healthcare-aetna-life-insurance-company-cvs-health-and-46-more-kelly-associates-insurance-g.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_paypal-working-capital-code-error.yaml](data-leak/2025-07_paypal-working-capital-code-error.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_allianz-life-third-party-vendor.yaml](supply-chain/2025-07_allianz-life-third-party-vendor.yaml) | supply-chain | 2025-07-01 |  |  |
| [2025-07_mcdonalds-paradox-ai-chatbot-64m.yaml](data-leak/2025-07_mcdonalds-paradox-ai-chatbot-64m.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-09_stellantis-salesforce-shinyhunters.yaml](data-leak/2025-09_stellantis-salesforce-shinyhunters.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-08_transunion-salesforce-44m.yaml](data-leak/2025-08_transunion-salesforce-44m.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-07_700credit-api-automotive-dealers.yaml](data-leak/2025-07_700credit-api-automotive-dealers.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-08_cisco-salesforce-shinyhunters.yaml](data-leak/2025-08_cisco-salesforce-shinyhunters.yaml) | data-leak | 2025-07-01 |  |  |
| [2025-06_resupply-exploit.yaml](data-leak/2025-06_resupply-exploit.yaml) | data-leak | 2025-06-26 |  |  |
| [2025-06_daytwo-thefts.yaml](data-leak/2025-06_daytwo-thefts.yaml) | data-leak | 2025-06-23 |  |  |
| [2025-06_self-chain-fires-founder.yaml](data-leak/2025-06_self-chain-fires-founder.yaml) | data-leak | 2025-06-23 |  |  |
| [2025-06_hacken-token-crash.yaml](data-leak/2025-06_hacken-token-crash.yaml) | data-leak | 2025-06-21 |  |  |
| [2025-06_nobitex-hack.yaml](data-leak/2025-06_nobitex-hack.yaml) | data-leak | 2025-06-18 |  |  |
| [2025-06_meta-pool-exploit.yaml](data-leak/2025-06_meta-pool-exploit.yaml) | data-leak | 2025-06-17 |  |  |
| [2025-06_aflac-scattered-spider.yaml](data-leak/2025-06_aflac-scattered-spider.yaml) | data-leak | 2025-06-12 |  |  |
| [2025-06_alex-lab-exploit-2.yaml](data-leak/2025-06_alex-lab-exploit-2.yaml) | data-leak | 2025-06-06 |  |  |
| [2025-06_bitopro-hack.yaml](data-leak/2025-06_bitopro-hack.yaml) | data-leak | 2025-06-02 |  |  |
| [2025-10_vietnam-airlines-salesforce-scattered-lapsus.yaml](data-leak/2025-10_vietnam-airlines-salesforce-scattered-lapsus.yaml) | data-leak | 2025-06-01 |  |  |
| [2025-06_sharp-healthcare-episource.yaml](supply-chain/2025-06_sharp-healthcare-episource.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-06_switzerland-government-radix-zurich-based-and-non-p.yaml](supply-chain/2025-06_switzerland-government-radix-zurich-based-and-non-p.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-06_mainstreet-bank-third-party-vendor.yaml](supply-chain/2025-06_mainstreet-bank-third-party-vendor.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-06_glasgow-city-council-third-party-vendor.yaml](supply-chain/2025-06_glasgow-city-council-third-party-vendor.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-06_coinbase-taskus.yaml](supply-chain/2025-06_coinbase-taskus.yaml) | supply-chain | 2025-06-01 |  |  |
| [2025-06_prosper-marketplace-credential-17m.yaml](data-leak/2025-06_prosper-marketplace-credential-17m.yaml) | data-leak | 2025-06-01 |  |  |
| [2025-05_farmers-insurance-salesforce-shinyhunters.yaml](data-leak/2025-05_farmers-insurance-salesforce-shinyhunters.yaml) | data-leak | 2025-05-29 |  |  |
| [2025-05_cork-protocol-hack.yaml](data-leak/2025-05_cork-protocol-hack.yaml) | data-leak | 2025-05-28 |  |  |
| [2025-05_cetus-exploit.yaml](data-leak/2025-05_cetus-exploit.yaml) | data-leak | 2025-05-22 |  |  |
| [2025-05_kettering-health-interlock.yaml](ransomware/2025-05_kettering-health-interlock.yaml) | ransomware | 2025-05-20 | Interlock ransomware |  |
| [2025-05_covenant-health-qilin.yaml](ransomware/2025-05_covenant-health-qilin.yaml) | ransomware | 2025-05-18 | Qilin |  |
| [2025-05_curve-finance-website-and-twitter-account-hacked.yaml](data-leak/2025-05_curve-finance-website-and-twitter-account-hacked.yaml) | data-leak | 2025-05-12 |  |  |
| [2025-05_founder-of-zerebro-token-fakes-his-death-promotes-new-legacy-coin.yaml](other/2025-05_founder-of-zerebro-token-fakes-his-death-promotes-new-legacy-coin.yaml) | other | 2025-05-08 |  |  |
| [2025-05_dragonforce-simplehelp-msp.yaml](supply-chain/2025-05_dragonforce-simplehelp-msp.yaml) | supply-chain | 2025-05-01 | DragonForce ransomware | CVE-2024-57726, CVE-2024-57727, CVE-202… |
| [2025-05_marks-spencer-tata-consultancy-services-tc.yaml](supply-chain/2025-05_marks-spencer-tata-consultancy-services-tc.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_trg-medical-imaging-nationwide-recovery-services.yaml](supply-chain/2025-05_trg-medical-imaging-nationwide-recovery-services.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_adidas-third-party-vendor.yaml](supply-chain/2025-05_adidas-third-party-vendor.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_catholic-health-serviceaide.yaml](supply-chain/2025-05_catholic-health-serviceaide.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-06_sharp-healthcare-episource-breach.yaml](supply-chain/2025-06_sharp-healthcare-episource-breach.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_multiple-local-governing-bodies-across-the-united-states-trimble-cityworks.yaml](supply-chain/2025-05_multiple-local-governing-bodies-across-the-united-states-trimble-cityworks.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_500-1-000-e-commerce-stores-tigren-meetanshi-and-mgs.yaml](supply-chain/2025-05_500-1-000-e-commerce-stores-tigren-meetanshi-and-mgs.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-05_2-000-providers-including-barristers-solicitor-firms-and-non-profit-organizations-legal-aid-agency-laa.yaml](supply-chain/2025-05_2-000-providers-including-barristers-solicitor-firms-and-non-profit-organizations-legal-aid-agency-laa.yaml) | supply-chain | 2025-05-01 |  |  |
| [2025-04_330-million-in-bitcoin-apparently-stolen-laundering-spikes-monero-price-by-over-40.yaml](data-leak/2025-04_330-million-in-bitcoin-apparently-stolen-laundering-spikes-monero-price-by-over-40.yaml) | data-leak | 2025-04-27 |  |  |
| [2025-04_voxel-manipulation.yaml](other/2025-04_voxel-manipulation.yaml) | other | 2025-04-27 |  |  |
| [2025-04_loopscale-exploit.yaml](data-leak/2025-04_loopscale-exploit.yaml) | data-leak | 2025-04-26 |  |  |
| [2025-04_term-finance-misconfiguration.yaml](other/2025-04_term-finance-misconfiguration.yaml) | other | 2025-04-26 |  |  |
| [2025-05_marks-spencer-tcs-breach.yaml](data-leak/2025-05_marks-spencer-tcs-breach.yaml) | data-leak | 2025-04-22 | DragonForce ransomware |  |
| [2025-04_sk-telecom-bpfdoor-sim-data.yaml](other/2025-04_sk-telecom-bpfdoor-sim-data.yaml) | other | 2025-04-18 | BPFDoor; Tiny Shell |  |
| [2025-04_ericsson-us-third-party-breach.yaml](data-leak/2025-04_ericsson-us-third-party-breach.yaml) | data-leak | 2025-04-17 |  |  |
| [2025-04_cbex-scam.yaml](data-leak/2025-04_cbex-scam.yaml) | data-leak | 2025-04-15 |  |  |
| [2025-04_zksync-theft.yaml](data-leak/2025-04_zksync-theft.yaml) | data-leak | 2025-04-15 |  |  |
| [2025-04_kiloex-exploit.yaml](data-leak/2025-04_kiloex-exploit.yaml) | data-leak | 2025-04-14 |  |  |
| [2025-04_mantra-token-price-suddenly-collapses-by-90.yaml](other/2025-04_mantra-token-price-suddenly-collapses-by-90.yaml) | other | 2025-04-14 |  |  |
| [2025-04_fdusd-depegs.yaml](other/2025-04_fdusd-depegs.yaml) | other | 2025-04-02 |  |  |
| [2025-05_legal-aid-agency-uk-2000-providers.yaml](data-leak/2025-05_legal-aid-agency-uk-2000-providers.yaml) | data-leak | 2025-04-01 |  |  |
| [2025-05_nationwide-recovery-services-healthcare-cluster.yaml](supply-chain/2025-05_nationwide-recovery-services-healthcare-cluster.yaml) | supply-chain | 2025-04-01 |  |  |
| [2025-04_royal-mail-spectos-gmbh.yaml](supply-chain/2025-04_royal-mail-spectos-gmbh.yaml) | supply-chain | 2025-04-01 |  |  |
| [2025-05_adidas-customer-service-breach.yaml](data-leak/2025-05_adidas-customer-service-breach.yaml) | data-leak | 2025-04-01 |  |  |
| [2025-04_ascension-former-business-partner.yaml](supply-chain/2025-04_ascension-former-business-partner.yaml) | supply-chain | 2025-04-01 |  |  |
| [2025-04_12-insurance-company-landmark-admin.yaml](supply-chain/2025-04_12-insurance-company-landmark-admin.yaml) | supply-chain | 2025-04-01 |  |  |
| [2025-04_coop-harrods-dragonforce.yaml](ransomware/2025-04_coop-harrods-dragonforce.yaml) | ransomware | 2025-04-01 | DragonForce ransomware |  |
| [2025-03_zklend-thief-gets-robbed.yaml](data-leak/2025-03_zklend-thief-gets-robbed.yaml) | data-leak | 2025-03-31 |  |  |
| [2025-03_iceraid.yaml](other/2025-03_iceraid.yaml) | other | 2025-03-30 |  |  |
| [2025-04_royal-mail-spectos-breach.yaml](data-leak/2025-04_royal-mail-spectos-breach.yaml) | data-leak | 2025-03-29 |  |  |
| [2025-03_galaxy-digital-agrees-to-200-million-settlement-over-alleged-luna-manipulation.yaml](other/2025-03_galaxy-digital-agrees-to-200-million-settlement-over-alleged-luna-manipulation.yaml) | other | 2025-03-28 |  |  |
| [2025-03_bc1qvl-theft.yaml](data-leak/2025-03_bc1qvl-theft.yaml) | data-leak | 2025-03-28 |  |  |
| [2025-03_polymarket-governance-attack.yaml](other/2025-03_polymarket-governance-attack.yaml) | other | 2025-03-27 |  |  |
| [2025-03_hyperliquid-manipulation.yaml](other/2025-03_hyperliquid-manipulation.yaml) | other | 2025-03-27 |  |  |
| [2025-03_abracadabra-exploit-2.yaml](data-leak/2025-03_abracadabra-exploit-2.yaml) | data-leak | 2025-03-25 |  |  |
| [2025-03_binance-insider-trading.yaml](other/2025-03_binance-insider-trading.yaml) | other | 2025-03-24 |  |  |
| [2025-04_davita-interlock.yaml](ransomware/2025-04_davita-interlock.yaml) | ransomware | 2025-03-24 | Interlock ransomware |  |
| [2025-03_zoth-hack-2.yaml](data-leak/2025-03_zoth-hack-2.yaml) | data-leak | 2025-03-21 |  |  |
| [2025-03_four-meme-hack-2.yaml](data-leak/2025-03_four-meme-hack-2.yaml) | data-leak | 2025-03-18 |  |  |
| [2025-04_ivanti-connect-secure-cve-2025-22457.yaml](other/2025-04_ivanti-connect-secure-cve-2025-22457.yaml) | other | 2025-03-15 | TRAILBLAZE (in-memory dropper… | CVE-2025-22457 |
| [2025-03_yale-new-haven-health.yaml](ransomware/2025-03_yale-new-haven-health.yaml) | ransomware | 2025-03-08 |  |  |
| [2025-03_zoth-hack-1.yaml](data-leak/2025-03_zoth-hack-1.yaml) | data-leak | 2025-03-06 |  |  |
| [2025-03_1inch-loses-5-million-to-smart-contract-bug.yaml](data-leak/2025-03_1inch-loses-5-million-to-smart-contract-bug.yaml) | data-leak | 2025-03-05 |  |  |
| [2025-03_17-891-corporate-customers-companies-ntt-communications-corporati.yaml](supply-chain/2025-03_17-891-corporate-customers-companies-ntt-communications-corporati.yaml) | supply-chain | 2025-03-01 |  |  |
| [2025-03_streamelements-gooten.yaml](supply-chain/2025-03_streamelements-gooten.yaml) | supply-chain | 2025-03-01 |  |  |
| [2025-03_multiple-us-healthcare-organizations-and-hospitals-oracle-health-formerly-cerne.yaml](supply-chain/2025-03_multiple-us-healthcare-organizations-and-hospitals-oracle-health-formerly-cerne.yaml) | supply-chain | 2025-03-01 |  |  |
| [2025-03_dozens-of-public-schools-across-the-usa-carruth-compliance-consultin.yaml](supply-chain/2025-03_dozens-of-public-schools-across-the-usa-carruth-compliance-consultin.yaml) | supply-chain | 2025-03-01 |  |  |
| [2025-02_wemix-foundation-hack.yaml](data-leak/2025-02_wemix-foundation-hack.yaml) | data-leak | 2025-02-28 |  |  |
| [2025-03_berkeley-research-group-chaos.yaml](ransomware/2025-03_berkeley-research-group-chaos.yaml) | ransomware | 2025-02-28 | Chaos ransomware |  |
| [2025-02_mirashi-hack.yaml](data-leak/2025-02_mirashi-hack.yaml) | data-leak | 2025-02-27 |  |  |
| [2025-02_suji-yan-wallet-hack.yaml](data-leak/2025-02_suji-yan-wallet-hack.yaml) | data-leak | 2025-02-27 |  |  |
| [2025-02_almost-50-million-stolen-from-infini-stablecoin-neobank.yaml](data-leak/2025-02_almost-50-million-stolen-from-infini-stablecoin-neobank.yaml) | data-leak | 2025-02-24 |  |  |
| [2025-02_bybit-hack.yaml](data-leak/2025-02_bybit-hack.yaml) | data-leak | 2025-02-21 |  |  |
| [2025-02_bybit-safe-wallet-lazarus.yaml](supply-chain/2025-02_bybit-safe-wallet-lazarus.yaml) | supply-chain | 2025-02-21 |  |  |
| [2025-02_opexus-insider-federal.yaml](other/2025-02_opexus-insider-federal.yaml) | other | 2025-02-18 |  |  |
| [2025-02_abstract-cardex-hack.yaml](data-leak/2025-02_abstract-cardex-hack.yaml) | data-leak | 2025-02-18 |  |  |
| [2025-03_streamelements-gooten-breach.yaml](supply-chain/2025-03_streamelements-gooten-breach.yaml) | supply-chain | 2025-02-15 |  |  |
| [2025-02_milei-memecoin-promotion.yaml](other/2025-02_milei-memecoin-promotion.yaml) | other | 2025-02-14 |  |  |
| [2025-02_anne-arundel-dermatology-breach.yaml](data-leak/2025-02_anne-arundel-dermatology-breach.yaml) | data-leak | 2025-02-14 |  |  |
| [2025-02_zklend-hack.yaml](data-leak/2025-02_zklend-hack.yaml) | data-leak | 2025-02-12 |  |  |
| [2025-02_trader-accidentally-sends-2-000-sol-to-bankrupt-ftx.yaml](other/2025-02_trader-accidentally-sends-2-000-sol-to-bankrupt-ftx.yaml) | other | 2025-02-11 |  |  |
| [2025-02_four-meme-hack.yaml](data-leak/2025-02_four-meme-hack.yaml) | data-leak | 2025-02-11 |  |  |
| [2025-02_coinbase-accused-of-failing-to-prevent-phishing.yaml](data-leak/2025-02_coinbase-accused-of-failing-to-prevent-phishing.yaml) | data-leak | 2025-02-03 |  |  |
| [2025-02_alleycat-project-developer-takes-presale-money-to-fund-gambling-habit.yaml](other/2025-02_alleycat-project-developer-takes-presale-money-to-fund-gambling-habit.yaml) | other | 2025-02-01 |  |  |
| [2025-02_17-banks-and-5-other-organizations-bankers-cooperative-group.yaml](supply-chain/2025-02_17-banks-and-5-other-organizations-bankers-cooperative-group.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-04_marks-and-spencer.yaml](ransomware/2025-04_marks-and-spencer.yaml) | ransomware | 2025-02-01 | DragonForce ransomware |  |
| [2025-02_current-former-and-prospective-employees-of-its-customers-disa-global-solutions.yaml](supply-chain/2025-02_current-former-and-prospective-employees-of-its-customers-disa-global-solutions.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-02_grubhub-third-party-vendor.yaml](supply-chain/2025-02_grubhub-third-party-vendor.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-02_local-credit-and-financial-businesses-lanit-group.yaml](supply-chain/2025-02_local-credit-and-financial-businesses-lanit-group.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-02_moses-weitzman-health-system-community-health-center.yaml](supply-chain/2025-02_moses-weitzman-health-system-community-health-center.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-02_river-region-cardiology-third-party-vendor.yaml](supply-chain/2025-02_river-region-cardiology-third-party-vendor.yaml) | supply-chain | 2025-02-01 |  |  |
| [2025-01_rugpuller-tool-rug-pulls-rugpullers.yaml](other/2025-01_rugpuller-tool-rug-pulls-rugpullers.yaml) | other | 2025-01-31 |  |  |
| [2025-01_dogwifhat-memecoin-lies-about-deal-to-put-the-meme-on-the-las-vegas-sphere-after-raising-700-000-to-pay-for-it.yaml](other/2025-01_dogwifhat-memecoin-lies-about-deal-to-put-the-meme-on-the-las-vegas-sphere-after-raising-700-000-to-pay-for-it.yaml) | other | 2025-01-31 |  |  |
| [2025-01_ether-strategy-destroys-over-500-000-of-eth.yaml](other/2025-01_ether-strategy-destroys-over-500-000-of-eth.yaml) | other | 2025-01-30 |  |  |
| [2025-01_ross-ulbricht-memecoin-mistake.yaml](other/2025-01_ross-ulbricht-memecoin-mistake.yaml) | other | 2025-01-30 |  |  |
| [2025-01_tsotchke-quantum-enhanced-ai-crypto-project-appears-to-be-based-on-lies.yaml](other/2025-01_tsotchke-quantum-enhanced-ai-crypto-project-appears-to-be-based-on-lies.yaml) | other | 2025-01-30 |  |  |
| [2025-01_western-sydney-university.yaml](data-leak/2025-01_western-sydney-university.yaml) | data-leak | 2025-01-28 |  |  |
| [2025-01_frederick-health-ransomware.yaml](ransomware/2025-01_frederick-health-ransomware.yaml) | ransomware | 2025-01-27 |  |  |
| [2025-01_kucoin-pleads-guilty.yaml](other/2025-01_kucoin-pleads-guilty.yaml) | other | 2025-01-27 |  |  |
| [2025-02_episource-optum-unitedhealth.yaml](ransomware/2025-02_episource-optum-unitedhealth.yaml) | ransomware | 2025-01-27 |  |  |
| [2025-01_thorchain-is-insolvent.yaml](other/2025-01_thorchain-is-insolvent.yaml) | other | 2025-01-23 |  |  |
| [2025-01_zero-edge-crypto-casino-liquidation.yaml](other/2025-01_zero-edge-crypto-casino-liquidation.yaml) | other | 2025-01-23 |  |  |
| [2025-01_phemex-hack.yaml](data-leak/2025-01_phemex-hack.yaml) | data-leak | 2025-01-23 |  |  |
| [2025-01_oracle-health-cerner-hospitals.yaml](supply-chain/2025-01_oracle-health-cerner-hospitals.yaml) | supply-chain | 2025-01-22 |  | CVE-2025-30154 |
| [2025-01_simonmed-imaging-medusa.yaml](ransomware/2025-01_simonmed-imaging-medusa.yaml) | ransomware | 2025-01-21 | Medusa |  |
| [2025-01_fake-trump-twitter-account-memecoins.yaml](data-leak/2025-01_fake-trump-twitter-account-memecoins.yaml) | data-leak | 2025-01-21 |  |  |
| [2025-01_trump-inauguration-pastor-launches-memecoin.yaml](other/2025-01_trump-inauguration-pastor-launches-memecoin.yaml) | other | 2025-01-20 |  |  |
| [2025-06_heritage-foundation-doge.yaml](data-leak/2025-06_heritage-foundation-doge.yaml) | other | 2025-01-20 |  |  |
| [2025-01_melania-trump-launches-a-memecoin.yaml](other/2025-01_melania-trump-launches-a-memecoin.yaml) | other | 2025-01-19 |  |  |
| [2025-01_students-for-trump-co-founder-admits-to-rugpulling-memecoin.yaml](other/2025-01_students-for-trump-co-founder-admits-to-rugpulling-memecoin.yaml) | other | 2025-01-19 |  |  |
| [2025-01_genesis-settles-with-the-sec.yaml](other/2025-01_genesis-settles-with-the-sec.yaml) | other | 2025-01-17 |  |  |
| [2025-01_trump-launches-a-shitcoin.yaml](other/2025-01_trump-launches-a-shitcoin.yaml) | other | 2025-01-17 |  |  |
| [2025-01_makersplace-nft-marketplace-shuts-down.yaml](other/2025-01_makersplace-nft-marketplace-shuts-down.yaml) | other | 2025-01-16 |  |  |
| [2025-01_bitmex-fined-additional-100-million.yaml](other/2025-01_bitmex-fined-additional-100-million.yaml) | other | 2025-01-15 |  |  |
| [2025-01_sony-accused-of-rugging.yaml](other/2025-01_sony-accused-of-rugging.yaml) | other | 2025-01-14 |  |  |
| [2025-01_the-idols-nft-exploit.yaml](data-leak/2025-01_the-idols-nft-exploit.yaml) | data-leak | 2025-01-14 |  |  |
| [2025-01_australian-open-apparently-scraps-its-nft-project.yaml](other/2025-01_australian-open-apparently-scraps-its-nft-project.yaml) | other | 2025-01-13 |  |  |
| [2025-01_unilend-exploit.yaml](data-leak/2025-01_unilend-exploit.yaml) | data-leak | 2025-01-12 |  |  |
| [2025-01_bankless-hosts-slammed-for-dumping-tokens.yaml](other/2025-01_bankless-hosts-slammed-for-dumping-tokens.yaml) | other | 2025-01-11 |  |  |
| [2025-01_2-2-million-stolen-by-fake-job-scammers.yaml](data-leak/2025-01_2-2-million-stolen-by-fake-job-scammers.yaml) | data-leak | 2025-01-09 |  |  |
| [2025-01_orange-finance-hack.yaml](data-leak/2025-01_orange-finance-hack.yaml) | data-leak | 2025-01-08 |  |  |
| [2025-01_moby-trade-theft.yaml](data-leak/2025-01_moby-trade-theft.yaml) | data-leak | 2025-01-08 |  |  |
| [2025-01_hengelo-man-arrested-in-alleged-crypto-pyramid-scheme.yaml](data-leak/2025-01_hengelo-man-arrested-in-alleged-crypto-pyramid-scheme.yaml) | data-leak | 2025-01-08 |  |  |
| [2025-01_kraken-spoofing-website-scam.yaml](data-leak/2025-01_kraken-spoofing-website-scam.yaml) | data-leak | 2025-01-07 |  |  |
| [2025-01_wyndham-otelier.yaml](supply-chain/2025-01_wyndham-otelier.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-02_grubhub-third-party-vendor.yaml](data-leak/2025-02_grubhub-third-party-vendor.yaml) | data-leak | 2025-01-01 |  |  |
| [2025-01_rostelecom-third-party-vendor.yaml](supply-chain/2025-01_rostelecom-third-party-vendor.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_square-medical-group-third-party-vendor.yaml](supply-chain/2025-01_square-medical-group-third-party-vendor.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_stiiizy-third-party-vendor.yaml](supply-chain/2025-01_stiiizy-third-party-vendor.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_talktalk-csg-ascendon-subscriber.yaml](supply-chain/2025-01_talktalk-csg-ascendon-subscriber.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_talktalk-csg-ascendon.yaml](supply-chain/2025-01_talktalk-csg-ascendon.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-06_coinbase-taskus-customer-support.yaml](data-leak/2025-06_coinbase-taskus-customer-support.yaml) | data-leak | 2025-01-01 |  |  |
| [2025-05_magento-tigren-meetanshi-extensions.yaml](supply-chain/2025-05_magento-tigren-meetanshi-extensions.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-05_trimble-cityworks-us-local-govts.yaml](supply-chain/2025-05_trimble-cityworks-us-local-govts.yaml) | supply-chain | 2025-01-01 |  | CVE-2025-0994 |
| [2025-01_khalil-foundation-transform-studios.yaml](supply-chain/2025-01_khalil-foundation-transform-studios.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_tata-technologies-hunters-intl.yaml](ransomware/2025-01_tata-technologies-hunters-intl.yaml) | ransomware | 2025-01-01 | Hunters International ransomw… |  |
| [2025-05_coinbase-insider-bribery.yaml](credential-theft/2025-05_coinbase-insider-bribery.yaml) | credential-theft | 2025-01-01 |  |  |
| [2025-01_centerpoint-energy-third-party-vendor.yaml](supply-chain/2025-01_centerpoint-energy-third-party-vendor.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_allegheny-health-network-intrasystems-llc.yaml](supply-chain/2025-01_allegheny-health-network-intrasystems-llc.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_ai-powered-identity-theft-wave.yaml](other/2025-01_ai-powered-identity-theft-wave.yaml) | other | 2025-01-01 |  |  |
| [2025-01_ai-accelerating-cyberattack-timelines.yaml](other/2025-01_ai-accelerating-cyberattack-timelines.yaml) | other | 2025-01-01 |  |  |
| [2025-01_oracle-cloud-sso-breach.yaml](data-leak/2025-01_oracle-cloud-sso-breach.yaml) | data-leak | 2025-01-01 |  | CVE-2021-35587 |
| [2025-01_noones-hacked-for-almost-8-million.yaml](data-leak/2025-01_noones-hacked-for-almost-8-million.yaml) | data-leak | 2025-01-01 |  |  |
| [2025-01_94-k-12-schools-powerschool.yaml](supply-chain/2025-01_94-k-12-schools-powerschool.yaml) | supply-chain | 2025-01-01 |  |  |
| [2025-01_machine-speed-attacks-ai-automation.yaml](other/2025-01_machine-speed-attacks-ai-automation.yaml) | other | 2025-01-01 |  |  |
| [2024-12_feed-every-gorilla-hack-2.yaml](data-leak/2024-12_feed-every-gorilla-hack-2.yaml) | data-leak | 2024-12-29 |  |  |
| [2024-12_sec-fines-jump-crypto-subsidiary.yaml](other/2024-12_sec-fines-jump-crypto-subsidiary.yaml) | other | 2024-12-20 |  |  |
| [2024-12_powerschool-sis.yaml](supply-chain/2024-12_powerschool-sis.yaml) | supply-chain | 2024-12-19 |  |  |
| [2024-12_powerschool-extortion-followon.yaml](data-leak/2024-12_powerschool-extortion-followon.yaml) | data-leak | 2024-12-19 |  |  |
| [2024-12_hay-and-mayo-rug-pull-indictment.yaml](other/2024-12_hay-and-mayo-rug-pull-indictment.yaml) | other | 2024-12-18 |  |  |
| [2025-01_ivanti-connect-secure-cve-2025-0282.yaml](other/2025-01_ivanti-connect-secure-cve-2025-0282.yaml) | other | 2024-12-15 | SPAWN ecosystem (SPAWNANT ins… | CVE-2025-0282, CVE-2025-0283 |
| [2024-12_kraken-fined-5-1-million-by-asic.yaml](other/2024-12_kraken-fined-5-1-million-by-asic.yaml) | other | 2024-12-12 |  |  |
| [2024-12_crypto-holder-loses-assets-priced-at-2-5-million.yaml](data-leak/2024-12_crypto-holder-loses-assets-priced-at-2-5-million.yaml) | data-leak | 2024-12-12 |  |  |
| [2024-12_clober-dex-hack.yaml](data-leak/2024-12_clober-dex-hack.yaml) | data-leak | 2024-12-11 |  |  |
| [2024-12_cftc-lawsuit-against-francier-obando-pinillo.yaml](data-leak/2024-12_cftc-lawsuit-against-francier-obando-pinillo.yaml) | data-leak | 2024-12-11 |  |  |
| [2024-12_alpaca-finance-oracle-issue.yaml](other/2024-12_alpaca-finance-oracle-issue.yaml) | other | 2024-12-10 |  |  |
| [2024-12_monroe-university.yaml](data-leak/2024-12_monroe-university.yaml) | data-leak | 2024-12-09 |  |  |
| [2024-12_85-year-old-painter-loses-life-savings-to-nft-art-dealer-scam.yaml](data-leak/2024-12_85-year-old-painter-loses-life-savings-to-nft-art-dealer-scam.yaml) | data-leak | 2024-12-06 |  |  |
| [2024-12_hawk-tuah-memecoin-immediately-crashes.yaml](other/2024-12_hawk-tuah-memecoin-immediately-crashes.yaml) | other | 2024-12-05 |  |  |
| [2024-12_ultralytics-pypi-github-actions-cryptominer.yaml](supply-chain/2024-12_ultralytics-pypi-github-actions-cryptominer.yaml) | supply-chain | 2024-12-04 | XMRig (Monero cryptominer) |  |
| [2024-12_nike-to-shut-down-rtfkt.yaml](other/2024-12_nike-to-shut-down-rtfkt.yaml) | other | 2024-12-02 |  |  |
| [2024-12_solana-javascript-library-compromised.yaml](supply-chain/2024-12_solana-javascript-library-compromised.yaml) | supply-chain | 2024-12-02 |  |  |
| [2024-12_clipper-dex-hack.yaml](data-leak/2024-12_clipper-dex-hack.yaml) | data-leak | 2024-12-01 |  |  |
| [2024-12_whittier-hospital-pih-health.yaml](supply-chain/2024-12_whittier-hospital-pih-health.yaml) | supply-chain | 2024-12-01 |  |  |
| [2024-12_veterans-health-administration-dbp-inc.yaml](supply-chain/2024-12_veterans-health-administration-dbp-inc.yaml) | supply-chain | 2024-12-01 |  |  |
| [2025-01_orange-romania-hellcat-jira.yaml](data-leak/2025-01_orange-romania-hellcat-jira.yaml) | data-leak | 2024-12-01 |  |  |
| [2025-04_ascension-former-partner-ehr.yaml](supply-chain/2025-04_ascension-former-partner-ehr.yaml) | supply-chain | 2024-12-01 |  |  |
| [2024-12_monument-health-change-healthcare.yaml](supply-chain/2024-12_monument-health-change-healthcare.yaml) | supply-chain | 2024-12-01 |  |  |
| [2024-12_ribridges-system-deloitte.yaml](supply-chain/2024-12_ribridges-system-deloitte.yaml) | supply-chain | 2024-12-01 |  |  |
| [2024-12_pavilion-of-bridgeview-pointclickcare.yaml](supply-chain/2024-12_pavilion-of-bridgeview-pointclickcare.yaml) | supply-chain | 2024-12-01 |  |  |
| [2025-04_hertz-cleo-clop-breach.yaml](data-leak/2025-04_hertz-cleo-clop-breach.yaml) | data-leak | 2024-12-01 |  | CVE-2024-50623, CVE-2024-55956 |
| [2024-11_krispy-kreme-play.yaml](ransomware/2024-11_krispy-kreme-play.yaml) | ransomware | 2024-11-29 | Play ransomware |  |
| [2024-11_xt-com-hack.yaml](data-leak/2024-11_xt-com-hack.yaml) | data-leak | 2024-11-28 |  |  |
| [2024-11_lockton-companies-southeast-breach.yaml](data-leak/2024-11_lockton-companies-southeast-breach.yaml) | data-leak | 2024-11-20 |  |  |
| [2024-11_quant-rug-pull.yaml](other/2024-11_quant-rug-pull.yaml) | other | 2024-11-20 |  |  |
| [2024-11_polter-finance-hack.yaml](data-leak/2024-11_polter-finance-hack.yaml) | data-leak | 2024-11-16 |  |  |
| [2024-11_dexx-losses.yaml](data-leak/2024-11_dexx-losses.yaml) | data-leak | 2024-11-16 |  |  |
| [2024-11_thala-hack.yaml](data-leak/2024-11_thala-hack.yaml) | data-leak | 2024-11-15 |  |  |
| [2024-12_cleo-mft-clop.yaml](supply-chain/2024-12_cleo-mft-clop.yaml) | supply-chain | 2024-11-15 | Clop (Cl0p) ransomware | CVE-2024-50623, CVE-2024-55956 |
| [2024-11_deltaprime-hack-2.yaml](data-leak/2024-11_deltaprime-hack-2.yaml) | data-leak | 2024-11-11 |  |  |
| [2024-11_qklpjeth-copypaste.yaml](other/2024-11_qklpjeth-copypaste.yaml) | other | 2024-11-10 |  |  |
| [2024-11_legends-international.yaml](data-leak/2024-11_legends-international.yaml) | data-leak | 2024-11-09 |  |  |
| [2024-11_coinpoker-hack.yaml](data-leak/2024-11_coinpoker-hack.yaml) | data-leak | 2024-11-08 |  |  |
| [2024-11_ahold-delhaize-inc-ransom.yaml](ransomware/2024-11_ahold-delhaize-inc-ransom.yaml) | ransomware | 2024-11-05 | INC Ransom |  |
| [2024-11_metawin-casino-hack.yaml](data-leak/2024-11_metawin-casino-hack.yaml) | data-leak | 2024-11-03 |  |  |
| [2024-11_schneider-electric-atlassian-s-jira-server.yaml](supply-chain/2024-11_schneider-electric-atlassian-s-jira-server.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_schneider-electric-hellcat.yaml](ransomware/2024-11_schneider-electric-hellcat.yaml) | ransomware | 2024-11-01 | Hellcat |  |
| [2024-11_presbyterian-healthcare-services-thompson-coburn.yaml](supply-chain/2024-11_presbyterian-healthcare-services-thompson-coburn.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_trihealth-physician-partners-trihealth-third-party-vendor.yaml](supply-chain/2024-11_trihealth-physician-partners-trihealth-third-party-vendor.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_bologna-fc-ransomhub.yaml](ransomware/2024-11_bologna-fc-ransomhub.yaml) | ransomware | 2024-11-01 | RansomHub ransomware |  |
| [2024-12_arc-community-services.yaml](ransomware/2024-12_arc-community-services.yaml) | ransomware | 2024-11-01 |  |  |
| [2024-11_mid-minnesota-management-services-central-resources-third-party-vendor.yaml](supply-chain/2024-11_mid-minnesota-management-services-central-resources-third-party-vendor.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_nokia-third-party-vendor.yaml](supply-chain/2024-11_nokia-third-party-vendor.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_sainsbury-s-blue-yonder.yaml](supply-chain/2024-11_sainsbury-s-blue-yonder.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-11_minist-re-du-travail-et-de-l-emploi-third-party-vendor.yaml](supply-chain/2024-11_minist-re-du-travail-et-de-l-emploi-third-party-vendor.yaml) | supply-chain | 2024-11-01 |  |  |
| [2024-10_lottiefiles-exploit.yaml](supply-chain/2024-10_lottiefiles-exploit.yaml) | supply-chain | 2024-10-31 |  |  |
| [2024-10_m2-hack.yaml](data-leak/2024-10_m2-hack.yaml) | data-leak | 2024-10-31 |  |  |
| [2024-11_finastra-sftp-banking-software.yaml](data-leak/2024-11_finastra-sftp-banking-software.yaml) | data-leak | 2024-10-31 |  |  |
| [2024-10_sunray-finance-hack.yaml](data-leak/2024-10_sunray-finance-hack.yaml) | data-leak | 2024-10-30 |  |  |
| [2024-10_possible-us-government-theft.yaml](data-leak/2024-10_possible-us-government-theft.yaml) | data-leak | 2024-10-24 |  |  |
| [2024-10_sharpei-memecoin-rug-pull.yaml](other/2024-10_sharpei-memecoin-rug-pull.yaml) | other | 2024-10-23 |  |  |
| [2024-10_forte-labs-game-studio-acquisitions.yaml](other/2024-10_forte-labs-game-studio-acquisitions.yaml) | other | 2024-10-22 |  |  |
| [2024-10_midnight-blizzard-rdp-spearphish.yaml](other/2024-10_midnight-blizzard-rdp-spearphish.yaml) | other | 2024-10-22 |  |  |
| [2024-10_conduent-safepay.yaml](ransomware/2024-10_conduent-safepay.yaml) | ransomware | 2024-10-21 | SafePay ransomware |  |
| [2025-01_conduent-safepay-state-benefits.yaml](ransomware/2025-01_conduent-safepay-state-benefits.yaml) | ransomware | 2024-10-21 | SafePay |  |
| [2024-10_tapioca-dao-exploit.yaml](data-leak/2024-10_tapioca-dao-exploit.yaml) | data-leak | 2024-10-18 |  |  |
| [2024-10_radiant-capital-defi-lazarus.yaml](credential-theft/2024-10_radiant-capital-defi-lazarus.yaml) | credential-theft | 2024-10-16 | InletDrift |  |
| [2024-10_radiant-capital-hack-2.yaml](data-leak/2024-10_radiant-capital-hack-2.yaml) | data-leak | 2024-10-16 |  |  |
| [2024-10_cosmos-lsm.yaml](other/2024-10_cosmos-lsm.yaml) | other | 2024-10-15 |  |  |
| [2024-10_pepe-token-permit-phishing.yaml](data-leak/2024-10_pepe-token-permit-phishing.yaml) | data-leak | 2024-10-13 |  |  |
| [2024-10_mut8694-npm-pypi-roblox.yaml](supply-chain/2024-10_mut8694-npm-pypi-roblox.yaml) | supply-chain | 2024-10-10 | Blank Grabber infostealer; Sk… |  |
| [2024-10_casio-underground.yaml](ransomware/2024-10_casio-underground.yaml) | ransomware | 2024-10-05 | Underground ransomware |  |
| [2024-10_eigen-token-theft.yaml](data-leak/2024-10_eigen-token-theft.yaml) | data-leak | 2024-10-04 |  |  |
| [2024-10_american-water-works.yaml](other/2024-10_american-water-works.yaml) | other | 2024-10-03 |  |  |
| [2024-10_rackspace-sciencelogic.yaml](supply-chain/2024-10_rackspace-sciencelogic.yaml) | supply-chain | 2024-10-01 |  |  |
| [2024-10_smile-design-management-third-party-vendor.yaml](supply-chain/2024-10_smile-design-management-third-party-vendor.yaml) | supply-chain | 2024-10-01 |  |  |
| [2025-01_stiiizy-cannabis-pos-breach-380k.yaml](data-leak/2025-01_stiiizy-cannabis-pos-breach-380k.yaml) | data-leak | 2024-10-01 |  |  |
| [2024-10_boston-children-s-health-physicians-axispoint-technology-solutio.yaml](supply-chain/2024-10_boston-children-s-health-physicians-axispoint-technology-solutio.yaml) | supply-chain | 2024-10-01 |  |  |
| [2024-10_hot-topic.yaml](data-leak/2024-10_hot-topic.yaml) | data-leak | 2024-10-01 | Infostealer malware (targetin… |  |
| [2024-10_adt-third-party-business-partner.yaml](supply-chain/2024-10_adt-third-party-business-partner.yaml) | supply-chain | 2024-10-01 |  |  |
| [2024-10_cf-medical-financial-business-and-consu.yaml](supply-chain/2024-10_cf-medical-financial-business-and-consu.yaml) | supply-chain | 2024-10-01 |  |  |
| [2024-11_byte-federal-bitcoin-atm-gitlab.yaml](data-leak/2024-11_byte-federal-bitcoin-atm-gitlab.yaml) | data-leak | 2024-09-30 |  |  |
| [2024-10_internet-archive.yaml](data-leak/2024-10_internet-archive.yaml) | data-leak | 2024-09-28 |  |  |
| [2024-10_free-mobile-france-vpn-24m.yaml](data-leak/2024-10_free-mobile-france-vpn-24m.yaml) | data-leak | 2024-09-28 |  |  |
| [2024-09_victim-loses-over-32-million-to-wallet-drainer.yaml](data-leak/2024-09_victim-loses-over-32-million-to-wallet-drainer.yaml) | data-leak | 2024-09-28 |  |  |
| [2024-09_bedrock-bug.yaml](data-leak/2024-09_bedrock-bug.yaml) | data-leak | 2024-09-27 |  |  |
| [2024-09_truflation-hack.yaml](data-leak/2024-09_truflation-hack.yaml) | data-leak | 2024-09-26 |  |  |
| [2024-09_onyx-hack-2.yaml](data-leak/2024-09_onyx-hack-2.yaml) | data-leak | 2024-09-26 |  |  |
| [2024-09_openai-twitter-account-hack.yaml](data-leak/2024-09_openai-twitter-account-hack.yaml) | data-leak | 2024-09-23 |  |  |
| [2024-09_shezmu-hack.yaml](data-leak/2024-09_shezmu-hack.yaml) | data-leak | 2024-09-20 |  |  |
| [2024-09_bingx-hack.yaml](data-leak/2024-09_bingx-hack.yaml) | data-leak | 2024-09-20 |  |  |
| [2024-09_moneygram-social-engineering.yaml](data-leak/2024-09_moneygram-social-engineering.yaml) | data-leak | 2024-09-20 |  |  |
| [2024-09_banana-gun-exploit.yaml](data-leak/2024-09_banana-gun-exploit.yaml) | data-leak | 2024-09-19 |  |  |
| [2024-09_serviceaide-catholic-health-elasticsearch.yaml](data-leak/2024-09_serviceaide-catholic-health-elasticsearch.yaml) | data-leak | 2024-09-19 |  |  |
| [2024-09_germany-seizes-47-cryptocurrency-exchanges.yaml](other/2024-09_germany-seizes-47-cryptocurrency-exchanges.yaml) | other | 2024-09-19 |  |  |
| [2024-09_gemini-phishing-attack.yaml](data-leak/2024-09_gemini-phishing-attack.yaml) | data-leak | 2024-09-19 |  |  |
| [2024-09_rari-capital-settles-with-the-sec.yaml](other/2024-09_rari-capital-settles-with-the-sec.yaml) | other | 2024-09-18 |  |  |
| [2024-09_ethena-website-compromised.yaml](data-leak/2024-09_ethena-website-compromised.yaml) | data-leak | 2024-09-18 |  |  |
| [2024-09_texas-tech-health-interlock.yaml](ransomware/2024-09_texas-tech-health-interlock.yaml) | ransomware | 2024-09-17 | Interlock ransomware |  |
| [2024-09_delta-prime-hack-1.yaml](data-leak/2024-09_delta-prime-hack-1.yaml) | data-leak | 2024-09-16 |  |  |
| [2024-09_flappy-bird-creator-disavows-crypto-spin-off.yaml](other/2024-09_flappy-bird-creator-disavows-crypto-spin-off.yaml) | other | 2024-09-15 |  |  |
| [2024-09_i-flappy-bird-i-creator-disavows-crypto-spin-off.yaml](other/2024-09_i-flappy-bird-i-creator-disavows-crypto-spin-off.yaml) | other | 2024-09-15 |  |  |
| [2024-09_eve-online-announcement.yaml](other/2024-09_eve-online-announcement.yaml) | other | 2024-09-13 |  |  |
| [2024-09_etoro-settlement.yaml](other/2024-09_etoro-settlement.yaml) | other | 2024-09-12 |  |  |
| [2024-09_cryptopunk-niftex-sale.yaml](other/2024-09_cryptopunk-niftex-sale.yaml) | other | 2024-09-11 |  |  |
| [2024-09_adam-neumann-s-flowcarbon-refunds-customers.yaml](other/2024-09_adam-neumann-s-flowcarbon-refunds-customers.yaml) | other | 2024-09-11 |  |  |
| [2024-09_indodax-hack.yaml](data-leak/2024-09_indodax-hack.yaml) | data-leak | 2024-09-10 |  |  |
| [2024-09_cut-token-exploit.yaml](data-leak/2024-09_cut-token-exploit.yaml) | data-leak | 2024-09-10 |  |  |
| [2024-09_gs-partners-settlements.yaml](data-leak/2024-09_gs-partners-settlements.yaml) | data-leak | 2024-09-09 |  |  |
| [2024-09_assangedao-accused-of-rug-pull.yaml](other/2024-09_assangedao-accused-of-rug-pull.yaml) | other | 2024-09-09 |  |  |
| [2024-09_friend-tech-team-abandons-project.yaml](other/2024-09_friend-tech-team-abandons-project.yaml) | other | 2024-09-07 |  |  |
| [2024-09_revelo-ventures-ceo-resigns-after-robbery.yaml](data-leak/2024-09_revelo-ventures-ceo-resigns-after-robbery.yaml) | data-leak | 2024-09-05 |  |  |
| [2024-09_robinhood-pays-settlement-to-california.yaml](other/2024-09_robinhood-pays-settlement-to-california.yaml) | other | 2024-09-04 |  |  |
| [2024-09_sec-charges-galois-capital-galois-settles.yaml](other/2024-09_sec-charges-galois-capital-galois-settles.yaml) | other | 2024-09-03 |  |  |
| [2024-09_penpie-hacked-for-27-3-million.yaml](data-leak/2024-09_penpie-hacked-for-27-3-million.yaml) | data-leak | 2024-09-03 |  |  |
| [2024-09_lacoste-quietly-ditches-its-undw3-project.yaml](other/2024-09_lacoste-quietly-ditches-its-undw3-project.yaml) | other | 2024-09-03 |  |  |
| [2024-09_trump-family-twitter-accounts-compromised.yaml](data-leak/2024-09_trump-family-twitter-accounts-compromised.yaml) | data-leak | 2024-09-03 |  |  |
| [2024-09_centers-for-medicare-medicaid-services-cms-wisconsin-physicians-service.yaml](supply-chain/2024-09_centers-for-medicare-medicaid-services-cms-wisconsin-physicians-service.yaml) | supply-chain | 2024-09-01 |  |  |
| [2024-09_t-mobile-capgemini.yaml](supply-chain/2024-09_t-mobile-capgemini.yaml) | supply-chain | 2024-09-01 |  |  |
| [2024-11_icbc-london-hunters-intl.yaml](other/2024-11_icbc-london-hunters-intl.yaml) | ransomware | 2024-09-01 | Hunters International ransomw… |  |
| [2024-09_nhs-england-synnovis.yaml](supply-chain/2024-09_nhs-england-synnovis.yaml) | supply-chain | 2024-09-01 |  |  |
| [2024-09_cultura-third-party-vendor.yaml](supply-chain/2024-09_cultura-third-party-vendor.yaml) | supply-chain | 2024-09-01 |  |  |
| [2024-09_transport-for-london-scattered-spider.yaml](other/2024-09_transport-for-london-scattered-spider.yaml) | credential-theft | 2024-08-31 |  |  |
| [2024-08_peripheral-aave-smart-contract-hack.yaml](data-leak/2024-08_peripheral-aave-smart-contract-hack.yaml) | data-leak | 2024-08-28 |  |  |
| [2024-08_opensea-wells-notice.yaml](other/2024-08_opensea-wells-notice.yaml) | other | 2024-08-28 |  |  |
| [2024-08_adam-brothers-charged-by-sec.yaml](data-leak/2024-08_adam-brothers-charged-by-sec.yaml) | data-leak | 2024-08-26 |  |  |
| [2024-08_rhodium-enterprises-bankruptcy.yaml](other/2024-08_rhodium-enterprises-bankruptcy.yaml) | other | 2024-08-26 |  |  |
| [2024-08_abra-charged-by-sec.yaml](other/2024-08_abra-charged-by-sec.yaml) | other | 2024-08-26 |  |  |
| [2024-08_users-suffer-losses-after-polygon-discord-hack.yaml](data-leak/2024-08_users-suffer-losses-after-polygon-discord-hack.yaml) | data-leak | 2024-08-24 |  |  |
| [2024-08_mcdonalds-instagram-hack.yaml](data-leak/2024-08_mcdonalds-instagram-hack.yaml) | data-leak | 2024-08-21 |  |  |
| [2024-08_halliburton.yaml](ransomware/2024-08_halliburton.yaml) | ransomware | 2024-08-21 | RansomHub ransomware |  |
| [2024-08_crypto-holder-loses-over-55-million-to-apparent-phishing-attack.yaml](data-leak/2024-08_crypto-holder-loses-over-55-million-to-apparent-phishing-attack.yaml) | data-leak | 2024-08-20 |  |  |
| [2024-08_former-ceo-of-heartland-tri-state-bank-sentenced-to-more-than-24-years-in-prison-after-putting-bank-funds-into-crypto-scheme.yaml](data-leak/2024-08_former-ceo-of-heartland-tri-state-bank-sentenced-to-more-than-24-years-in-prison-after-putting-bank-funds-into-crypto-scheme.yaml) | data-leak | 2024-08-19 |  |  |
| [2024-08_futurenet-founder-arrested.yaml](other/2024-08_futurenet-founder-arrested.yaml) | other | 2024-08-19 |  |  |
| [2024-08_fidelity-investments-account-abuse.yaml](data-leak/2024-08_fidelity-investments-account-abuse.yaml) | data-leak | 2024-08-17 |  |  |
| [2024-08_coinbase-support-scammer.yaml](data-leak/2024-08_coinbase-support-scammer.yaml) | data-leak | 2024-08-15 |  |  |
| [2024-08_dnp3-pleads-guilty-to-wire-fraud-after-gambling-away-investor-funds.yaml](data-leak/2024-08_dnp3-pleads-guilty-to-wire-fraud-after-gambling-away-investor-funds.yaml) | data-leak | 2024-08-15 |  |  |
| [2024-08_novatech-lawsuit.yaml](other/2024-08_novatech-lawsuit.yaml) | other | 2024-08-12 |  |  |
| [2023-03_royal-mail-lockbit-v2.yaml](ransomware/2023-03_royal-mail-lockbit-v2.yaml) | ransomware | 2024-08-11 | Hunters International ransomw… |  |
| [2024-08_ftx-cftc-settlement.yaml](other/2024-08_ftx-cftc-settlement.yaml) | other | 2024-08-08 |  |  |
| [2024-08_ripple-fined-125-million-by-the-sec.yaml](other/2024-08_ripple-fined-125-million-by-the-sec.yaml) | other | 2024-08-07 |  |  |
| [2024-08_7anpw-theft.yaml](data-leak/2024-08_7anpw-theft.yaml) | data-leak | 2024-08-07 |  |  |
| [2024-08_trump-themed-djt-token-rug-pulls-people-blame-martin-shkreli-or-barron-trump.yaml](other/2024-08_trump-themed-djt-token-rug-pulls-people-blame-martin-shkreli-or-barron-trump.yaml) | other | 2024-08-06 |  |  |
| [2024-08_12-million-taken-by-whitehats-from-ronin-bridge.yaml](data-leak/2024-08_12-million-taken-by-whitehats-from-ronin-bridge.yaml) | data-leak | 2024-08-06 |  |  |
| [2024-08_cftc-subpoenas-bitboy-s-former-company.yaml](other/2024-08_cftc-subpoenas-bitboy-s-former-company.yaml) | other | 2024-08-02 |  |  |
| [2024-08_13-000-students-in-singapore-mobile-guardian.yaml](supply-chain/2024-08_13-000-students-in-singapore-mobile-guardian.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_kujira-token-tanks-as-team-s-leveraged-bets-melt-down.yaml](other/2024-08_kujira-token-tanks-as-team-s-leveraged-bets-melt-down.yaml) | other | 2024-08-01 |  |  |
| [2024-08_blue-shield-of-california-young-consulting.yaml](supply-chain/2024-08_blue-shield-of-california-young-consulting.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_hah-group-holding-company-third-party-vendor.yaml](supply-chain/2024-08_hah-group-holding-company-third-party-vendor.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_national-payments-corporation-of-india-npci-c-edge-technologies-ltd.yaml](supply-chain/2024-08_national-payments-corporation-of-india-npci-c-edge-technologies-ltd.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_convergencefi-hack.yaml](data-leak/2024-08_convergencefi-hack.yaml) | data-leak | 2024-08-01 |  |  |
| [2024-08_surgery-center-of-mid-florida-third-party-vendor.yaml](supply-chain/2024-08_surgery-center-of-mid-florida-third-party-vendor.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-08_toyota-third-party-vendor.yaml](supply-chain/2024-08_toyota-third-party-vendor.yaml) | supply-chain | 2024-08-01 |  |  |
| [2024-07_zkx-shutdown.yaml](other/2024-07_zkx-shutdown.yaml) | other | 2024-07-30 |  |  |
| [2024-07_bitclout-founder-arrested.yaml](other/2024-07_bitclout-founder-arrested.yaml) | other | 2024-07-30 |  |  |
| [2024-07_draftkings-reignmakers-shutdown.yaml](other/2024-07_draftkings-reignmakers-shutdown.yaml) | other | 2024-07-30 |  |  |
| [2024-07_compound-dao-governance-attack.yaml](other/2024-07_compound-dao-governance-attack.yaml) | other | 2024-07-28 |  |  |
| [2024-07_monoswap-hack.yaml](data-leak/2024-07_monoswap-hack.yaml) | data-leak | 2024-07-24 |  |  |
| [2024-07_dydx-v3-exchange-website-compromised.yaml](data-leak/2024-07_dydx-v3-exchange-website-compromised.yaml) | data-leak | 2024-07-23 |  |  |
| [2024-07_ethtrustfund-rug-pull.yaml](other/2024-07_ethtrustfund-rug-pull.yaml) | other | 2024-07-20 |  |  |
| [2024-07_rho-loss.yaml](other/2024-07_rho-loss.yaml) | other | 2024-07-19 |  |  |
| [2024-07_crowdstrike-falcon-global-bsod.yaml](other/2024-07_crowdstrike-falcon-global-bsod.yaml) | other | 2024-07-19 |  |  |
| [2024-07_wazirx-hack.yaml](data-leak/2024-07_wazirx-hack.yaml) | data-leak | 2024-07-18 |  |  |
| [2024-07_wazirx-lazarus-multisig.yaml](credential-theft/2024-07_wazirx-lazarus-multisig.yaml) | credential-theft | 2024-07-18 | Safe Wallet front-end manipul… |  |
| [2024-07_trekki-nft-shutdown.yaml](other/2024-07_trekki-nft-shutdown.yaml) | other | 2024-07-17 |  |  |
| [2024-08_mclaren-health.yaml](ransomware/2024-08_mclaren-health.yaml) | ransomware | 2024-07-17 | INC Ransom ransomware |  |
| [2024-07_li-fi-exploit.yaml](data-leak/2024-07_li-fi-exploit.yaml) | data-leak | 2024-07-16 |  |  |
| [2024-07_metamax-pyramid-scheme.yaml](other/2024-07_metamax-pyramid-scheme.yaml) | other | 2024-07-15 |  |  |
| [2024-07_minterest-hack.yaml](data-leak/2024-07_minterest-hack.yaml) | data-leak | 2024-07-14 |  |  |
| [2024-07_dough-finance-hack.yaml](data-leak/2024-07_dough-finance-hack.yaml) | data-leak | 2024-07-12 |  |  |
| [2024-07_squarespace-domain-hijacking.yaml](data-leak/2024-07_squarespace-domain-hijacking.yaml) | data-leak | 2024-07-11 |  |  |
| [2024-07_bitmex-pays-110-million-fine.yaml](other/2024-07_bitmex-pays-110-million-fine.yaml) | other | 2024-07-10 |  |  |
| [2024-07_omegapro-founder-arrested.yaml](data-leak/2024-07_omegapro-founder-arrested.yaml) | data-leak | 2024-07-09 |  |  |
| [2024-07_doja-cat-twitter-hack.yaml](data-leak/2024-07_doja-cat-twitter-hack.yaml) | data-leak | 2024-07-08 |  |  |
| [2024-07_bittensor-wallet-drain.yaml](data-leak/2024-07_bittensor-wallet-drain.yaml) | data-leak | 2024-07-02 |  |  |
| [2024-07_bilt-evolve-bank-trust.yaml](supply-chain/2024-07_bilt-evolve-bank-trust.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_gemini-not-disclosed-automated-clea.yaml](supply-chain/2024-07_gemini-not-disclosed-automated-clea.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_silvergate-bank-settlement.yaml](other/2024-07_silvergate-bank-settlement.yaml) | other | 2024-07-01 |  |  |
| [2025-01_otelier-hotel-reservation-platform.yaml](supply-chain/2025-01_otelier-hotel-reservation-platform.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-11_trizetto-cognizant-healthcare-3m.yaml](supply-chain/2024-11_trizetto-cognizant-healthcare-3m.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_wisconsin-department-of-health-services-disability-rights-wisconsin.yaml](supply-chain/2024-07_wisconsin-department-of-health-services-disability-rights-wisconsin.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_roblox-fntech.yaml](supply-chain/2024-07_roblox-fntech.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_mobile-medical-response-cbm-services.yaml](supply-chain/2024-07_mobile-medical-response-cbm-services.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_300-small-indian-banks-c-edge-technologies-ltd.yaml](supply-chain/2024-07_300-small-indian-banks-c-edge-technologies-ltd.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_at-t-snowflake.yaml](supply-chain/2024-07_at-t-snowflake.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_kairos-health-arizona-a-third-party-vendor.yaml](supply-chain/2024-07_kairos-health-arizona-a-third-party-vendor.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_autonation-cdk-global.yaml](supply-chain/2024-07_autonation-cdk-global.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-07_clear-spring-health-change-healthcare.yaml](supply-chain/2024-07_clear-spring-health-change-healthcare.yaml) | supply-chain | 2024-07-01 |  |  |
| [2024-06_sec-sues-consensys.yaml](other/2024-06_sec-sues-consensys.yaml) | other | 2024-06-28 |  |  |
| [2024-06_yield-app-shuts-down.yaml](other/2024-06_yield-app-shuts-down.yaml) | other | 2024-06-28 |  |  |
| [2024-06_logan-paul-lawsuit-against-coffeezilla.yaml](other/2024-06_logan-paul-lawsuit-against-coffeezilla.yaml) | other | 2024-06-27 |  |  |
| [2024-06_remy-st-felix-conviction.yaml](other/2024-06_remy-st-felix-conviction.yaml) | other | 2024-06-25 |  |  |
| [2024-06_polyfill-io-cdn-attack.yaml](supply-chain/2024-06_polyfill-io-cdn-attack.yaml) | supply-chain | 2024-06-25 |  |  |
| [2024-06_farcana-token-plunge.yaml](data-leak/2024-06_farcana-token-plunge.yaml) | data-leak | 2024-06-23 |  |  |
| [2024-06_0xfb94d-theft.yaml](data-leak/2024-06_0xfb94d-theft.yaml) | data-leak | 2024-06-23 |  |  |
| [2024-06_btcturk-exploit.yaml](data-leak/2024-06_btcturk-exploit.yaml) | data-leak | 2024-06-22 |  |  |
| [2024-06_sportsbet-io-hack.yaml](data-leak/2024-06_sportsbet-io-hack.yaml) | data-leak | 2024-06-22 |  |  |
| [2024-06_coinstats-wallet-compromises.yaml](data-leak/2024-06_coinstats-wallet-compromises.yaml) | data-leak | 2024-06-22 |  |  |
| [2024-06_50-cent-account-compromise.yaml](data-leak/2024-06_50-cent-account-compromise.yaml) | data-leak | 2024-06-22 |  |  |
| [2024-06_certik-and-kraken-bug-dispute.yaml](data-leak/2024-06_certik-and-kraken-bug-dispute.yaml) | data-leak | 2024-06-19 |  |  |
| [2024-06_acadian-ambulance-daixin.yaml](ransomware/2024-06_acadian-ambulance-daixin.yaml) | ransomware | 2024-06-19 | Daixin Team ransomware |  |
| [2024-06_martin-shkreli-claims-to-have-been-behind-a-donald-trump-memecoin.yaml](other/2024-06_martin-shkreli-claims-to-have-been-behind-a-donald-trump-memecoin.yaml) | other | 2024-06-18 |  |  |
| [2024-06_cdk-global.yaml](ransomware/2024-06_cdk-global.yaml) | ransomware | 2024-06-18 | BlackSuit |  |
| [2024-06_holograph-hack.yaml](data-leak/2024-06_holograph-hack.yaml) | data-leak | 2024-06-13 |  |  |
| [2024-06_uwu-lend-hack-2.yaml](data-leak/2024-06_uwu-lend-hack-2.yaml) | data-leak | 2024-06-13 |  |  |
| [2024-06_globe-life-insurance-extortion.yaml](data-leak/2024-06_globe-life-insurance-extortion.yaml) | data-leak | 2024-06-13 |  |  |
| [2024-06_terraform-labs-settlement.yaml](other/2024-06_terraform-labs-settlement.yaml) | other | 2024-06-12 |  |  |
| [2024-06_andreessen-horowitz-phishing.yaml](data-leak/2024-06_andreessen-horowitz-phishing.yaml) | data-leak | 2024-06-12 |  |  |
| [2024-06_uwu-lend-hack-1.yaml](data-leak/2024-06_uwu-lend-hack-1.yaml) | data-leak | 2024-06-10 |  |  |
| [2024-06_loopring-wallet-hack.yaml](data-leak/2024-06_loopring-wallet-hack.yaml) | data-leak | 2024-06-09 |  |  |
| [2024-06_kadokawa-niconico-blacksuit.yaml](ransomware/2024-06_kadokawa-niconico-blacksuit.yaml) | ransomware | 2024-06-08 | BlackSuit |  |
| [2024-06_novatech-and-aws-mining-crypto-pyramid-schemes.yaml](data-leak/2024-06_novatech-and-aws-mining-crypto-pyramid-schemes.yaml) | data-leak | 2024-06-06 |  |  |
| [2024-06_rite-aid-ransomhub.yaml](ransomware/2024-06_rite-aid-ransomhub.yaml) | ransomware | 2024-06-06 | RansomHub |  |
| [2024-06_br1an-eth-private-key-compromise.yaml](data-leak/2024-06_br1an-eth-private-key-compromise.yaml) | data-leak | 2024-06-05 |  |  |
| [2024-06_lykke-hack.yaml](data-leak/2024-06_lykke-hack.yaml) | data-leak | 2024-06-04 |  |  |
| [2024-06_bill-guan-indictment.yaml](data-leak/2024-06_bill-guan-indictment.yaml) | data-leak | 2024-06-03 |  |  |
| [2024-06_synnovis-nhs.yaml](ransomware/2024-06_synnovis-nhs.yaml) | ransomware | 2024-06-03 | Qilin ransomware |  |
| [2024-06_cbiz-benefits-insurance-breach.yaml](data-leak/2024-06_cbiz-benefits-insurance-breach.yaml) | data-leak | 2024-06-02 |  |  |
| [2024-06_velocore-hack.yaml](data-leak/2024-06_velocore-hack.yaml) | data-leak | 2024-06-02 |  |  |
| [2024-06_lithia-motors-sonic-automotive-penske-automotive-group-inc-and-more-cdk-global.yaml](supply-chain/2024-06_lithia-motors-sonic-automotive-penske-automotive-group-inc-and-more-cdk-global.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_aptihealth-sisense.yaml](supply-chain/2024-06_aptihealth-sisense.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_geisinger-nuance-communications.yaml](supply-chain/2024-06_geisinger-nuance-communications.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_iact-health-advarra.yaml](supply-chain/2024-06_iact-health-advarra.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_king-s-college-hospital-guy-s-hospital-st-thomas-hospital-and-more-synnovis.yaml](supply-chain/2024-06_king-s-college-hospital-guy-s-hospital-st-thomas-hospital-and-more-synnovis.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_adventist-health-tulare-signature-performance.yaml](supply-chain/2024-06_adventist-health-tulare-signature-performance.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_newton-centre-dental-affinity-dental-management.yaml](supply-chain/2024-06_newton-centre-dental-affinity-dental-management.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-06_tile-life360-extortion.yaml](data-leak/2024-06_tile-life360-extortion.yaml) | data-leak | 2024-06-01 |  |  |
| [2024-06_t-mobile-third-party-vendor.yaml](supply-chain/2024-06_t-mobile-third-party-vendor.yaml) | supply-chain | 2024-06-01 |  |  |
| [2024-05_dmm-bitcoin-tradertraitor.yaml](credential-theft/2024-05_dmm-bitcoin-tradertraitor.yaml) | credential-theft | 2024-05-31 |  |  |
| [2024-05_dmm-bitcoin-loss.yaml](data-leak/2024-05_dmm-bitcoin-loss.yaml) | data-leak | 2024-05-31 |  |  |
| [2024-05_evolve-bank-lockbit.yaml](ransomware/2024-05_evolve-bank-lockbit.yaml) | ransomware | 2024-05-29 | LockBit ransomware |  |
| [2024-05_ryan-salame-sentenced.yaml](other/2024-05_ryan-salame-sentenced.yaml) | other | 2024-05-28 |  |  |
| [2024-05_cat-memecoin-team-hacks-gcr.yaml](data-leak/2024-05_cat-memecoin-team-hacks-gcr.yaml) | data-leak | 2024-05-27 |  |  |
| [2024-05_caitlyn-jenner-memecoin.yaml](other/2024-05_caitlyn-jenner-memecoin.yaml) | other | 2024-05-26 |  |  |
| [2024-05_normie-exploit.yaml](data-leak/2024-05_normie-exploit.yaml) | data-leak | 2024-05-26 |  |  |
| [2024-06_patelco-credit-union.yaml](ransomware/2024-06_patelco-credit-union.yaml) | ransomware | 2024-05-23 | RansomHub ransomware |  |
| [2024-05_gala-games-hack.yaml](data-leak/2024-05_gala-games-hack.yaml) | data-leak | 2024-05-20 |  |  |
| [2024-05_crypto-scam-money-launderers-charged-for-laundering-more-than-73-million-through-deltec.yaml](other/2024-05_crypto-scam-money-launderers-charged-for-laundering-more-than-73-million-through-deltec.yaml) | other | 2024-05-17 |  |  |
| [2024-05_aiden-pleterski-arrested.yaml](other/2024-05_aiden-pleterski-arrested.yaml) | other | 2024-05-16 |  |  |
| [2024-05_pump-fun-exploit.yaml](data-leak/2024-05_pump-fun-exploit.yaml) | data-leak | 2024-05-16 |  |  |
| [2024-05_peraire-bueno-mev-indictment.yaml](data-leak/2024-05_peraire-bueno-mev-indictment.yaml) | data-leak | 2024-05-15 |  |  |
| [2024-05_sonne-finance-hack.yaml](data-leak/2024-05_sonne-finance-hack.yaml) | data-leak | 2024-05-14 |  |  |
| [2024-05_alexey-pertsev-sentencing.yaml](other/2024-05_alexey-pertsev-sentencing.yaml) | other | 2024-05-14 |  |  |
| [2024-05_alex-xlink-bridge-theft.yaml](data-leak/2024-05_alex-xlink-bridge-theft.yaml) | data-leak | 2024-05-14 |  |  |
| [2024-05_landmark-admin-insurance-ransomware.yaml](ransomware/2024-05_landmark-admin-insurance-ransomware.yaml) | ransomware | 2024-05-13 |  |  |
| [2024-05_landmark-admin-insurance.yaml](ransomware/2024-05_landmark-admin-insurance.yaml) | ransomware | 2024-05-13 |  |  |
| [2024-05_cypher-contributor-theft.yaml](data-leak/2024-05_cypher-contributor-theft.yaml) | data-leak | 2024-05-13 |  |  |
| [2024-05_ascension-health.yaml](ransomware/2024-05_ascension-health.yaml) | ransomware | 2024-05-08 | Black Basta ransomware |  |
| [2024-05_keytronic-black-basta.yaml](ransomware/2024-05_keytronic-black-basta.yaml) | ransomware | 2024-05-06 | Black Basta ransomware |  |
| [2024-05_sec-sends-wells-notice-to-robinhood-crypto.yaml](other/2024-05_sec-sends-wells-notice-to-robinhood-crypto.yaml) | other | 2024-05-06 |  |  |
| [2024-05_gnus-ai-exploi.yaml](data-leak/2024-05_gnus-ai-exploi.yaml) | data-leak | 2024-05-05 |  |  |
| [2024-05_0x1e227-address-poisoning.yaml](data-leak/2024-05_0x1e227-address-poisoning.yaml) | data-leak | 2024-05-03 |  |  |
| [2024-05_cred-executives-indicted.yaml](other/2024-05_cred-executives-indicted.yaml) | other | 2024-05-03 |  |  |
| [2024-05_advance-auto-parts-snowflake.yaml](supply-chain/2024-05_advance-auto-parts-snowflake.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-06_pure-storage-snowflake.yaml](credential-theft/2024-06_pure-storage-snowflake.yaml) | credential-theft | 2024-05-01 |  |  |
| [2024-07_snowflake-bausch-health-pharma.yaml](credential-theft/2024-07_snowflake-bausch-health-pharma.yaml) | credential-theft | 2024-05-01 |  |  |
| [2024-05_ticketmaster-snowflake.yaml](supply-chain/2024-05_ticketmaster-snowflake.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_acrotech-biopharma-inc-cencora-inc.yaml](supply-chain/2024-05_acrotech-biopharma-inc-cencora-inc.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_medisecure-third-party-vendor.yaml](supply-chain/2024-05_medisecure-third-party-vendor.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_hsbc-baton-systems.yaml](supply-chain/2024-05_hsbc-baton-systems.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_gerber-life-insurance-webtpa.yaml](supply-chain/2024-05_gerber-life-insurance-webtpa.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_continuum-health-alliance-consensus-medical-group.yaml](supply-chain/2024-05_continuum-health-alliance-consensus-medical-group.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_bym-fashion-lizay-kuyumculuk-aker-magazac-l-k-and-more-tekrom-technology-a-s-t-soft.yaml](supply-chain/2024-05_bym-fashion-lizay-kuyumculuk-aker-magazac-l-k-and-more-tekrom-technology-a-s-t-soft.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-05_alexion-pharmaceuticals-trade-limited-eclinical-solutions-llc.yaml](supply-chain/2024-05_alexion-pharmaceuticals-trade-limited-eclinical-solutions-llc.yaml) | supply-chain | 2024-05-01 |  |  |
| [2024-04_pike-finance-hacks.yaml](data-leak/2024-04_pike-finance-hacks.yaml) | data-leak | 2024-04-30 |  |  |
| [2024-04_changpeng-zhao-sentenced.yaml](other/2024-04_changpeng-zhao-sentenced.yaml) | other | 2024-04-30 |  |  |
| [2024-04_roger-ver-arrested-for-50-million-tax-fraud.yaml](other/2024-04_roger-ver-arrested-for-50-million-tax-fraud.yaml) | other | 2024-04-30 |  |  |
| [2024-04_zkasino-scam-suspect-arrested-by-dutch-police.yaml](other/2024-04_zkasino-scam-suspect-arrested-by-dutch-police.yaml) | other | 2024-04-29 |  |  |
| [2024-04_rain-hack.yaml](data-leak/2024-04_rain-hack.yaml) | data-leak | 2024-04-29 |  |  |
| [2024-05_dell-api-scrape.yaml](data-leak/2024-05_dell-api-scrape.yaml) | data-leak | 2024-04-28 |  |  |
| [2024-04_london-drugs-lockbit.yaml](ransomware/2024-04_london-drugs-lockbit.yaml) | ransomware | 2024-04-28 | LockBit ransomware |  |
| [2024-04_jay-mazini-sentenced.yaml](data-leak/2024-04_jay-mazini-sentenced.yaml) | data-leak | 2024-04-24 |  |  |
| [2024-04_samourai-wallet-operators-charged.yaml](other/2024-04_samourai-wallet-operators-charged.yaml) | other | 2024-04-24 |  |  |
| [2024-04_dropbox-sign-mfa-seeds.yaml](credential-theft/2024-04_dropbox-sign-mfa-seeds.yaml) | credential-theft | 2024-04-24 |  |  |
| [2024-04_zkasino-rug-pull.yaml](other/2024-04_zkasino-rug-pull.yaml) | other | 2024-04-20 |  |  |
| [2024-04_hedgey-finance-hack.yaml](data-leak/2024-04_hedgey-finance-hack.yaml) | data-leak | 2024-04-19 |  |  |
| [2024-04_jpex-police-action.yaml](other/2024-04_jpex-police-action.yaml) | other | 2024-04-18 |  |  |
| [2024-04_avi-eisenberg-convicted.yaml](other/2024-04_avi-eisenberg-convicted.yaml) | other | 2024-04-18 |  |  |
| [2024-04_santander-snowflake.yaml](credential-theft/2024-04_santander-snowflake.yaml) | credential-theft | 2024-04-17 |  |  |
| [2024-04_roger-stone-endorses-trump-memecoin.yaml](other/2024-04_roger-stone-endorses-trump-memecoin.yaml) | other | 2024-04-17 |  |  |
| [2024-04_grand-base-theft.yaml](data-leak/2024-04_grand-base-theft.yaml) | data-leak | 2024-04-15 |  |  |
| [2024-04_frontier-communications-ransomhub.yaml](ransomware/2024-04_frontier-communications-ransomhub.yaml) | ransomware | 2024-04-14 | RansomHub |  |
| [2024-04_ticketmaster-snowflake.yaml](credential-theft/2024-04_ticketmaster-snowflake.yaml) | credential-theft | 2024-04-14 | VIDAR, RISEPRO, REDLINE, RACO… |  |
| [2024-04_att-snowflake.yaml](credential-theft/2024-04_att-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-05_lendingtree-quotewizard-snowflake.yaml](credential-theft/2024-05_lendingtree-quotewizard-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-07_att-snowflake-110million-metadata.yaml](data-leak/2024-07_att-snowflake-110million-metadata.yaml) | data-leak | 2024-04-14 | Lumma/Vidar/RedLine infosteal… |  |
| [2024-04_tea-xyz-causes-open-source-software-spam-problems-again.yaml](other/2024-04_tea-xyz-causes-open-source-software-spam-problems-again.yaml) | other | 2024-04-14 |  |  |
| [2024-04_advance-auto-parts-snowflake.yaml](credential-theft/2024-04_advance-auto-parts-snowflake.yaml) | credential-theft | 2024-04-14 |  |  |
| [2024-05_neiman-marcus-snowflake-31m-email.yaml](credential-theft/2024-05_neiman-marcus-snowflake-31m-email.yaml) | credential-theft | 2024-04-14 | VIDAR/RISEPRO/REDLINE infoste… |  |
| [2024-04_australian-ngs-crypto-mining-fund-collapses.yaml](other/2024-04_australian-ngs-crypto-mining-fund-collapses.yaml) | other | 2024-04-12 |  |  |
| [2024-04_dca-fund-collapse.yaml](other/2024-04_dca-fund-collapse.yaml) | other | 2024-04-12 |  |  |
| [2024-04_nirvana-finance-hacker-sentenced.yaml](other/2024-04_nirvana-finance-hacker-sentenced.yaml) | other | 2024-04-12 |  |  |
| [2024-04_pac-finance-liquidations.yaml](other/2024-04_pac-finance-liquidations.yaml) | other | 2024-04-12 |  |  |
| [2024-04_marginfi-ceo-resignation.yaml](other/2024-04_marginfi-ceo-resignation.yaml) | other | 2024-04-10 |  |  |
| [2024-04_uniswap-wells-notice.yaml](other/2024-04_uniswap-wells-notice.yaml) | other | 2024-04-10 |  |  |
| [2024-04_young-consulting-blacksuit.yaml](ransomware/2024-04_young-consulting-blacksuit.yaml) | ransomware | 2024-04-10 | BlackSuit ransomware |  |
| [2024-04_stfil-investigation.yaml](other/2024-04_stfil-investigation.yaml) | other | 2024-04-09 |  |  |
| [2024-04_muskswap-exit-scam.yaml](other/2024-04_muskswap-exit-scam.yaml) | other | 2024-04-08 |  |  |
| [2024-04_bored-hungry-shuts-down.yaml](other/2024-04_bored-hungry-shuts-down.yaml) | other | 2024-04-07 |  |  |
| [2024-04_do-kwon-and-terraform-labs-found-liable-for-40-billion-fraud.yaml](other/2024-04_do-kwon-and-terraform-labs-found-liable-for-40-billion-fraud.yaml) | other | 2024-04-05 |  |  |
| [2024-04_sushiswap-treasury-vote.yaml](other/2024-04_sushiswap-treasury-vote.yaml) | other | 2024-04-04 |  |  |
| [2024-04_rug-pull-token.yaml](other/2024-04_rug-pull-token.yaml) | other | 2024-04-03 |  |  |
| [2024-04_d-c-department-of-insurance-securities-and-banking-disb-tyler-technologies.yaml](supply-chain/2024-04_d-c-department-of-insurance-securities-and-banking-disb-tyler-technologies.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_snowflake-unc5537-165-customers.yaml](supply-chain/2024-04_snowflake-unc5537-165-customers.yaml) | credential-theft | 2024-04-01 | Lumma; Vidar; RedLine; RisePr… |  |
| [2024-04_snowflake-cylance-blackberry.yaml](credential-theft/2024-04_snowflake-cylance-blackberry.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-04_snowflake-customers.yaml](credential-theft/2024-04_snowflake-customers.yaml) | credential-theft | 2024-04-01 | Redline Stealer / Lumma Steal… |  |
| [2024-05_neiman-marcus-snowflake.yaml](credential-theft/2024-05_neiman-marcus-snowflake.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-05_ticketek-australia-teg-cloud.yaml](credential-theft/2024-05_ticketek-australia-teg-cloud.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-06_lausd-snowflake.yaml](credential-theft/2024-06_lausd-snowflake.yaml) | credential-theft | 2024-04-01 |  |  |
| [2024-04_multiple-u-s-agencies-acuity-consulting.yaml](supply-chain/2024-04_multiple-u-s-agencies-acuity-consulting.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_cisco-duo-unknown-telephony-provider.yaml](supply-chain/2024-04_cisco-duo-unknown-telephony-provider.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_catholic-medical-center-cmc-lamont-hanley-associates.yaml](supply-chain/2024-04_catholic-medical-center-cmc-lamont-hanley-associates.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_moffitt-cancer-center-gunster-yoakley-and-stewart.yaml](supply-chain/2024-04_moffitt-cancer-center-gunster-yoakley-and-stewart.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_heilbronn-city-library-genios.yaml](supply-chain/2024-04_heilbronn-city-library-genios.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_national-public-data.yaml](data-leak/2024-04_national-public-data.yaml) | data-leak | 2024-04-01 |  |  |
| [2024-04_department-of-justice-greylock-mckinnon-associates.yaml](supply-chain/2024-04_department-of-justice-greylock-mckinnon-associates.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-04_amg-healthcare-management-services-marshall-medical-center-south-coast-er-medical-group-and-more-designed-receivable-solution.yaml](supply-chain/2024-04_amg-healthcare-management-services-marshall-medical-center-south-coast-er-medical-group-and-more-designed-receivable-solution.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-07_disney-slack-nullbulge.yaml](data-leak/2024-07_disney-slack-nullbulge.yaml) | data-leak | 2024-04-01 |  |  |
| [2024-04_fixedfloat-hack-2.yaml](data-leak/2024-04_fixedfloat-hack-2.yaml) | data-leak | 2024-04-01 |  |  |
| [2024-04_medisecure-australia.yaml](ransomware/2024-04_medisecure-australia.yaml) | ransomware | 2024-04-01 |  |  |
| [2024-04_moffitt-cancer-center-advarra.yaml](supply-chain/2024-04_moffitt-cancer-center-advarra.yaml) | supply-chain | 2024-04-01 |  |  |
| [2024-03_solana-drain-attacks.yaml](data-leak/2024-03_solana-drain-attacks.yaml) | data-leak | 2024-03-30 |  |  |
| [2024-03_sam-bankman-fried-sentenced.yaml](other/2024-03_sam-bankman-fried-sentenced.yaml) | other | 2024-03-28 |  |  |
| [2024-03_prisma-finance-hack.yaml](data-leak/2024-03_prisma-finance-hack.yaml) | data-leak | 2024-03-28 |  |  |
| [2024-03_kucoin-and-founders-indicted.yaml](other/2024-03_kucoin-and-founders-indicted.yaml) | other | 2024-03-26 |  |  |
| [2024-03_lenx-rug-pull.yaml](data-leak/2024-03_lenx-rug-pull.yaml) | data-leak | 2024-03-26 |  |  |
| [2024-03_munchables-hack.yaml](data-leak/2024-03_munchables-hack.yaml) | data-leak | 2024-03-26 |  |  |
| [2024-04_palo-alto-pan-os.yaml](other/2024-04_palo-alto-pan-os.yaml) | other | 2024-03-26 | UPSTYLE Python backdoor | CVE-2024-3400 |
| [2024-03_curio-hack.yaml](data-leak/2024-03_curio-hack.yaml) | data-leak | 2024-03-25 |  |  |
| [2024-03_lucky-star-currency-rug-pull-2.yaml](data-leak/2024-03_lucky-star-currency-rug-pull-2.yaml) | data-leak | 2024-03-22 |  |  |
| [2024-03_solana-racist-memecoins.yaml](other/2024-03_solana-racist-memecoins.yaml) | other | 2024-03-22 |  |  |
| [2024-03_super-sushi-samurai-exploit.yaml](data-leak/2024-03_super-sushi-samurai-exploit.yaml) | data-leak | 2024-03-21 |  |  |
| [2024-03_ticker-rug-pull.yaml](other/2024-03_ticker-rug-pull.yaml) | other | 2024-03-21 |  |  |
| [2024-03_airdao-exploit.yaml](data-leak/2024-03_airdao-exploit.yaml) | data-leak | 2024-03-20 |  |  |
| [2024-03_sec-ethereum-foundation-investigation.yaml](other/2024-03_sec-ethereum-foundation-investigation.yaml) | other | 2024-03-20 |  |  |
| [2024-03_dolomite-exchange-hack.yaml](data-leak/2024-03_dolomite-exchange-hack.yaml) | data-leak | 2024-03-20 |  |  |
| [2024-03_bitcoin-flash-crashes-on-bitmex.yaml](other/2024-03_bitcoin-flash-crashes-on-bitmex.yaml) | other | 2024-03-19 |  |  |
| [2024-03_slerf-memecoin-meltdown-only-adds-to-mania.yaml](other/2024-03_slerf-memecoin-meltdown-only-adds-to-mania.yaml) | other | 2024-03-18 |  |  |
| [2024-03_remilia-collective-reports-multi-million-dollar-hack.yaml](data-leak/2024-03_remilia-collective-reports-multi-million-dollar-hack.yaml) | data-leak | 2024-03-16 |  |  |
| [2024-03_ansem-twitter-impersonator.yaml](data-leak/2024-03_ansem-twitter-impersonator.yaml) | data-leak | 2024-03-16 |  |  |
| [2024-03_wilder-world-theft.yaml](data-leak/2024-03_wilder-world-theft.yaml) | data-leak | 2024-03-16 |  |  |
| [2024-03_tether-user-s-accidental-burn.yaml](other/2024-03_tether-user-s-accidental-burn.yaml) | other | 2024-03-15 |  |  |
| [2024-03_nfprompt-discloses-hack.yaml](data-leak/2024-03_nfprompt-discloses-hack.yaml) | data-leak | 2024-03-15 |  |  |
| [2024-03_mozaic-exploit.yaml](data-leak/2024-03_mozaic-exploit.yaml) | data-leak | 2024-03-15 |  |  |
| [2024-03_mobox-exploit.yaml](data-leak/2024-03_mobox-exploit.yaml) | data-leak | 2024-03-14 |  |  |
| [2024-03_massachusetts-crypto-romance-scam.yaml](data-leak/2024-03_massachusetts-crypto-romance-scam.yaml) | data-leak | 2024-03-13 |  |  |
| [2024-03_ether-fi-phishing.yaml](data-leak/2024-03_ether-fi-phishing.yaml) | data-leak | 2024-03-13 |  |  |
| [2024-03_kickstarter-s-a16z-induced-pivot-to-blockchain.yaml](other/2024-03_kickstarter-s-a16z-induced-pivot-to-blockchain.yaml) | other | 2024-03-11 |  |  |
| [2024-03_incognito-market-exit-scam.yaml](data-leak/2024-03_incognito-market-exit-scam.yaml) | data-leak | 2024-03-11 |  |  |
| [2024-03_february-2024-twitter-phishing.yaml](data-leak/2024-03_february-2024-twitter-phishing.yaml) | data-leak | 2024-03-10 |  |  |
| [2024-03_wacks-law-group-qilin.yaml](ransomware/2024-03_wacks-law-group-qilin.yaml) | ransomware | 2024-03-09 | Qilin ransomware |  |
| [2024-03_crypto4winners-theft.yaml](data-leak/2024-03_crypto4winners-theft.yaml) | data-leak | 2024-03-09 |  |  |
| [2024-03_healthequity-vendor-breach.yaml](data-leak/2024-03_healthequity-vendor-breach.yaml) | data-leak | 2024-03-09 |  |  |
| [2024-03_unizen-hack.yaml](data-leak/2024-03_unizen-hack.yaml) | data-leak | 2024-03-08 |  |  |
| [2024-03_acuity-federal-contractor-github.yaml](data-leak/2024-03_acuity-federal-contractor-github.yaml) | data-leak | 2024-03-07 |  |  |
| [2024-03_woofi-hack.yaml](data-leak/2024-03_woofi-hack.yaml) | data-leak | 2024-03-05 |  |  |
| [2024-03_jetbrains-teamcity-cve-2024-27198.yaml](supply-chain/2024-03_jetbrains-teamcity-cve-2024-27198.yaml) | supply-chain | 2024-03-04 | Various backdoors and remote … | CVE-2024-27198, CVE-2024-27199 |
| [2024-03_swiss-goverment-xplain.yaml](supply-chain/2024-03_swiss-goverment-xplain.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_santa-clarita-community-college-keenan-associates.yaml](supply-chain/2024-03_santa-clarita-community-college-keenan-associates.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_virginia-farm-bureau-service-corporation-employee-benefits-corporatio.yaml](supply-chain/2024-03_virginia-farm-bureau-service-corporation-employee-benefits-corporatio.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_university-of-tennessee-health-science-center-kmj-health-solutions.yaml](supply-chain/2024-03_university-of-tennessee-health-science-center-kmj-health-solutions.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_the-hanoi-stock-exchange-hnx-vndirect.yaml](supply-chain/2024-03_the-hanoi-stock-exchange-hnx-vndirect.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-04_roku-credential-stuffing.yaml](credential-theft/2024-04_roku-credential-stuffing.yaml) | credential-theft | 2024-03-01 |  |  |
| [2024-03_ai-protocol-theft-and-burn.yaml](data-leak/2024-03_ai-protocol-theft-and-burn.yaml) | data-leak | 2024-03-01 |  |  |
| [2024-03_american-express-a-merchant-processor.yaml](supply-chain/2024-03_american-express-a-merchant-processor.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_mintlify-github-tokens.yaml](supply-chain/2024-03_mintlify-github-tokens.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_bay-area-anesthesia-bowden-barlow-law-p-a.yaml](supply-chain/2024-03_bay-area-anesthesia-bowden-barlow-law-p-a.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_health-plan-intermediaries-holdings-benefytt-multiplan-inc.yaml](supply-chain/2024-03_health-plan-intermediaries-holdings-benefytt-multiplan-inc.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_fidelity-infosys-mccamish-systems-ims.yaml](supply-chain/2024-03_fidelity-infosys-mccamish-systems-ims.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-03_baylor-college-of-medicine-advarra.yaml](supply-chain/2024-03_baylor-college-of-medicine-advarra.yaml) | supply-chain | 2024-03-01 |  |  |
| [2024-02_shido-contract-exploit.yaml](data-leak/2024-02_shido-contract-exploit.yaml) | data-leak | 2024-02-28 |  |  |
| [2024-02_seneca-protocol-bug.yaml](data-leak/2024-02_seneca-protocol-bug.yaml) | data-leak | 2024-02-28 |  |  |
| [2024-02_serenity-shield-hack.yaml](data-leak/2024-02_serenity-shield-hack.yaml) | data-leak | 2024-02-27 |  |  |
| [2024-02_matthew-perry-twitter-hack.yaml](data-leak/2024-02_matthew-perry-twitter-hack.yaml) | data-leak | 2024-02-27 |  |  |
| [2024-02_verisource-hr-benefits-breach.yaml](data-leak/2024-02_verisource-hr-benefits-breach.yaml) | data-leak | 2024-02-27 |  |  |
| [2024-02_tea-xyz-spam.yaml](other/2024-02_tea-xyz-spam.yaml) | other | 2024-02-26 |  |  |
| [2024-02_bitforex-withdrawals.yaml](other/2024-02_bitforex-withdrawals.yaml) | other | 2024-02-26 |  |  |
| [2024-02_microstrategy-twitter-hack.yaml](data-leak/2024-02_microstrategy-twitter-hack.yaml) | data-leak | 2024-02-26 |  |  |
| [2024-02_dechat-token-launch-error.yaml](data-leak/2024-02_dechat-token-launch-error.yaml) | data-leak | 2024-02-26 |  |  |
| [2024-02_riskonblast-gambling-platform-rug-pulls-for-1-3-million.yaml](other/2024-02_riskonblast-gambling-platform-rug-pulls-for-1-3-million.yaml) | other | 2024-02-25 |  |  |
| [2024-02_aleo-privacy-error.yaml](other/2024-02_aleo-privacy-error.yaml) | other | 2024-02-25 |  |  |
| [2024-02_tornado-cash-exploit.yaml](data-leak/2024-02_tornado-cash-exploit.yaml) | data-leak | 2024-02-25 |  |  |
| [2024-02_myanmar-based-pig-butchering-scam.yaml](data-leak/2024-02_myanmar-based-pig-butchering-scam.yaml) | data-leak | 2024-02-25 |  |  |
| [2024-03_xz-utils-backdoor.yaml](supply-chain/2024-03_xz-utils-backdoor.yaml) | supply-chain | 2024-02-24 |  | CVE-2024-3094 |
| [2024-02_kow-seng-chai-disappearance.yaml](other/2024-02_kow-seng-chai-disappearance.yaml) | other | 2024-02-24 |  |  |
| [2024-02_jihoz-zirlin-wallet-hack.yaml](data-leak/2024-02_jihoz-zirlin-wallet-hack.yaml) | data-leak | 2024-02-22 |  |  |
| [2024-02_blueberry-protocol-narrowly-avoids-1-3-million-hack.yaml](data-leak/2024-02_blueberry-protocol-narrowly-avoids-1-3-million-hack.yaml) | data-leak | 2024-02-22 |  |  |
| [2024-02_deeznutz-404-hack.yaml](data-leak/2024-02_deeznutz-404-hack.yaml) | data-leak | 2024-02-22 |  |  |
| [2024-02_cencora-pharma.yaml](data-leak/2024-02_cencora-pharma.yaml) | data-leak | 2024-02-21 |  |  |
| [2024-02_aax-money-movement.yaml](other/2024-02_aax-money-movement.yaml) | other | 2024-02-20 |  |  |
| [2024-02_influencer-crypto-rover-accused-of-pump-and-dump-and-other-shady-behavior.yaml](other/2024-02_influencer-crypto-rover-accused-of-pump-and-dump-and-other-shady-behavior.yaml) | other | 2024-02-20 |  |  |
| [2024-02_airdrop-hunters-spam-github-projects.yaml](other/2024-02_airdrop-hunters-spam-github-projects.yaml) | other | 2024-02-19 |  |  |
| [2024-02_connectwise-screenconnect-auth-bypass.yaml](supply-chain/2024-02_connectwise-screenconnect-auth-bypass.yaml) | supply-chain | 2024-02-19 | LockBit ransomware, Bl00dy ra… | CVE-2024-1709, CVE-2024-1708 |
| [2024-02_fixedfloat-hack-1.yaml](data-leak/2024-02_fixedfloat-hack-1.yaml) | data-leak | 2024-02-18 |  |  |
| [2024-02_kirilm-eth-phishing.yaml](data-leak/2024-02_kirilm-eth-phishing.yaml) | data-leak | 2024-02-16 |  |  |
| [2024-02_yuga-labs-moonbirds-insider-trading.yaml](other/2024-02_yuga-labs-moonbirds-insider-trading.yaml) | other | 2024-02-16 |  |  |
| [2024-02_youtuber-ksi-accused-of-pump-and-dump.yaml](other/2024-02_youtuber-ksi-accused-of-pump-and-dump.yaml) | other | 2024-02-15 |  |  |
| [2024-02_farcaster-name-controversy.yaml](other/2024-02_farcaster-name-controversy.yaml) | other | 2024-02-15 |  |  |
| [2024-02_creator-of-robotos-nft-project-once-collaborating-on-a-tv-series-with-i-time-i-studios-accused-of-rug-pull.yaml](other/2024-02_creator-of-robotos-nft-project-once-collaborating-on-a-tv-series-with-i-time-i-studios-accused-of-rug-pull.yaml) | other | 2024-02-14 |  |  |
| [2024-02_creator-of-robotos-nft-project-once-collaborating-on-a-tv-series-with-time-studios-accused-of-rug-pull.yaml](other/2024-02_creator-of-robotos-nft-project-once-collaborating-on-a-tv-series-with-time-studios-accused-of-rug-pull.yaml) | other | 2024-02-14 |  |  |
| [2024-02_fbcs-comcast-truist.yaml](data-leak/2024-02_fbcs-comcast-truist.yaml) | data-leak | 2024-02-14 |  |  |
| [2024-09_comcast-xfinity-fcc-fine.yaml](data-leak/2024-09_comcast-xfinity-fcc-fine.yaml) | data-leak | 2024-02-14 |  |  |
| [2024-02_duelbits-hack.yaml](data-leak/2024-02_duelbits-hack.yaml) | data-leak | 2024-02-13 |  |  |
| [2026-04_iowa-ag-sues-unitedhealth-change-healthcare.yaml](ransomware/2026-04_iowa-ag-sues-unitedhealth-change-healthcare.yaml) | ransomware | 2024-02-12 | ALPHV/BlackCat ransomware (or… |  |
| [2024-02_change-healthcare.yaml](ransomware/2024-02_change-healthcare.yaml) | ransomware | 2024-02-11 | ALPHV/BlackCat |  |
| [2024-02_disa-global-employment-screening.yaml](data-leak/2024-02_disa-global-employment-screening.yaml) | data-leak | 2024-02-09 |  |  |
| [2024-02_yuga-labs-bungles-free-otherside-nft-drop.yaml](other/2024-02_yuga-labs-bungles-free-otherside-nft-drop.yaml) | other | 2024-02-09 |  |  |
| [2024-02_playdapp-crypto-gaming-platform-exploited-spurring-misleading-headlines.yaml](data-leak/2024-02_playdapp-crypto-gaming-platform-exploited-spurring-misleading-headlines.yaml) | data-leak | 2024-02-09 |  |  |
| [2024-02_february-2024-solana-outage.yaml](other/2024-02_february-2024-solana-outage.yaml) | other | 2024-02-06 |  |  |
| [2024-02_prudential-financial.yaml](data-leak/2024-02_prudential-financial.yaml) | data-leak | 2024-02-04 | ALPHV/BlackCat ransomware |  |
| [2024-02_prudential-financial-alphv.yaml](ransomware/2024-02_prudential-financial-alphv.yaml) | ransomware | 2024-02-04 | ALPHV/BlackCat |  |
| [2024-02_forward-healthcare-philips-respironics.yaml](supply-chain/2024-02_forward-healthcare-philips-respironics.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_qualcomm-incorporated-unknown-third-party-vendor.yaml](supply-chain/2024-02_qualcomm-incorporated-unknown-third-party-vendor.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_opnx-shutdown.yaml](other/2024-02_opnx-shutdown.yaml) | other | 2024-02-01 |  |  |
| [2024-02_the-u-s-government-accountability-office-cgi-federal.yaml](supply-chain/2024-02_the-u-s-government-accountability-office-cgi-federal.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_audiens-viamedis.yaml](supply-chain/2024-02_audiens-viamedis.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_rotech-healthcare-philips-respironics.yaml](supply-chain/2024-02_rotech-healthcare-philips-respironics.yaml) | supply-chain | 2024-02-01 |  |  |
| [2025-03_ntt-communications-corporate-customers.yaml](data-leak/2025-03_ntt-communications-corporate-customers.yaml) | data-leak | 2024-02-01 |  |  |
| [2024-02_sim-swapping-ring-charged.yaml](other/2024-02_sim-swapping-ring-charged.yaml) | other | 2024-02-01 |  |  |
| [2024-02_bay-area-heart-center-bowden-barlow-law-p-a.yaml](supply-chain/2024-02_bay-area-heart-center-bowden-barlow-law-p-a.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_100-romanian-hospitals-hipocrate-information-system.yaml](supply-chain/2024-02_100-romanian-hospitals-hipocrate-information-system.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_prime-healthcare-keenan-associates.yaml](supply-chain/2024-02_prime-healthcare-keenan-associates.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_hawaii-medical-service-association-hmsa-navvis-company.yaml](supply-chain/2024-02_hawaii-medical-service-association-hmsa-navvis-company.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-02_nabholz-construction-cadence-bank.yaml](supply-chain/2024-02_nabholz-construction-cadence-bank.yaml) | supply-chain | 2024-02-01 |  |  |
| [2024-01_chris-larsen-xrp-theft.yaml](data-leak/2024-01_chris-larsen-xrp-theft.yaml) | data-leak | 2024-01-31 |  |  |
| [2024-01_january-2024-twitter-phishing.yaml](data-leak/2024-01_january-2024-twitter-phishing.yaml) | data-leak | 2024-01-31 |  |  |
| [2024-01_abracadabra-exploit.yaml](data-leak/2024-01_abracadabra-exploit.yaml) | data-leak | 2024-01-30 |  |  |
| [2024-01_hyperverse-founder-sam-lee-charged.yaml](data-leak/2024-01_hyperverse-founder-sam-lee-charged.yaml) | data-leak | 2024-01-29 |  |  |
| [2024-01_goledo-finance-hack.yaml](data-leak/2024-01_goledo-finance-hack.yaml) | data-leak | 2024-01-28 |  |  |
| [2024-01_somesing-hack.yaml](data-leak/2024-01_somesing-hack.yaml) | data-leak | 2024-01-27 |  |  |
| [2024-01_8-100-bitcoin-forfeited-by-silk-road-drugs-distributor-in-guilty-plea.yaml](other/2024-01_8-100-bitcoin-forfeited-by-silk-road-drugs-distributor-in-guilty-plea.yaml) | other | 2024-01-26 |  |  |
| [2024-01_lurie-childrens-hospital.yaml](ransomware/2024-01_lurie-childrens-hospital.yaml) | ransomware | 2024-01-26 | Rhysida |  |
| [2024-01_wallstreetmemes-exploit.yaml](data-leak/2024-01_wallstreetmemes-exploit.yaml) | data-leak | 2024-01-25 |  |  |
| [2024-01_mailerlite-hack.yaml](data-leak/2024-01_mailerlite-hack.yaml) | data-leak | 2024-01-23 |  |  |
| [2024-01_animoca-brands-owned-gamee-tokens-stolen.yaml](data-leak/2024-01_animoca-brands-owned-gamee-tokens-stolen.yaml) | data-leak | 2024-01-22 |  |  |
| [2024-01_concentric-finance-exploit.yaml](data-leak/2024-01_concentric-finance-exploit.yaml) | data-leak | 2024-01-22 |  |  |
| [2024-01_terraform-labs-files-for-bankruptcy.yaml](other/2024-01_terraform-labs-files-for-bankruptcy.yaml) | other | 2024-01-21 |  |  |
| [2024-01_anydesk-source-code-breach.yaml](data-leak/2024-01_anydesk-source-code-breach.yaml) | data-leak | 2024-01-20 |  |  |
| [2024-01_dwight-howard-s-nft-project-flops.yaml](other/2024-01_dwight-howard-s-nft-project-flops.yaml) | other | 2024-01-20 |  |  |
| [2024-01_debiex-cftc-complaint.yaml](data-leak/2024-01_debiex-cftc-complaint.yaml) | data-leak | 2024-01-19 |  |  |
| [2024-01_tietoevry-ransomware-swedish-orgs.yaml](supply-chain/2024-01_tietoevry-ransomware-swedish-orgs.yaml) | ransomware | 2024-01-19 | Akira ransomware |  |
| [2024-02_sandworm-texas-water-muleshoe.yaml](other/2024-02_sandworm-texas-water-muleshoe.yaml) | other | 2024-01-18 |  |  |
| [2024-01_indxcoin.yaml](data-leak/2024-01_indxcoin.yaml) | data-leak | 2024-01-18 |  |  |
| [2024-01_luis-rubiales-nft.yaml](other/2024-01_luis-rubiales-nft.yaml) | other | 2024-01-17 |  |  |
| [2024-01_hector-network-compensation-fund-theft.yaml](data-leak/2024-01_hector-network-compensation-fund-theft.yaml) | data-leak | 2024-01-16 |  |  |
| [2024-01_trueusd-loses-peg.yaml](other/2024-01_trueusd-loses-peg.yaml) | other | 2024-01-16 |  |  |
| [2024-01_socket-hack.yaml](data-leak/2024-01_socket-hack.yaml) | data-leak | 2024-01-16 |  |  |
| [2024-01_trello-api-scrape.yaml](data-leak/2024-01_trello-api-scrape.yaml) | data-leak | 2024-01-16 |  |  |
| [2024-01_gamestop-shuts-down-nft-marketplace.yaml](other/2024-01_gamestop-shuts-down-nft-marketplace.yaml) | other | 2024-01-15 |  |  |
| [2024-01_harmony-infinite-mint-bug.yaml](other/2024-01_harmony-infinite-mint-bug.yaml) | other | 2024-01-15 |  |  |
| [2024-01_genesis-nydfs-settlement.yaml](other/2024-01_genesis-nydfs-settlement.yaml) | other | 2024-01-12 |  |  |
| [2024-01_euler-finance-private-key-loss.yaml](other/2024-01_euler-finance-private-key-loss.yaml) | other | 2024-01-10 |  |  |
| [2024-01_dogwifhat-slippage.yaml](other/2024-01_dogwifhat-slippage.yaml) | other | 2024-01-10 |  |  |
| [2024-01_twitter-removes-nft-profile-picture-support.yaml](other/2024-01_twitter-removes-nft-profile-picture-support.yaml) | other | 2024-01-10 |  |  |
| [2024-01_bitcoin-rodney-arrest.yaml](other/2024-01_bitcoin-rodney-arrest.yaml) | other | 2024-01-09 |  |  |
| [2024-01_sec-twitter-account-compromised.yaml](data-leak/2024-01_sec-twitter-account-compromised.yaml) | data-leak | 2024-01-09 |  |  |
| [2024-01_undead-apes-rug-pull.yaml](other/2024-01_undead-apes-rug-pull.yaml) | other | 2024-01-08 |  |  |
| [2024-01_narwhal-exit-scam.yaml](data-leak/2024-01_narwhal-exit-scam.yaml) | data-leak | 2024-01-07 |  |  |
| [2024-01_mangofarmsol-rug-pull.yaml](other/2024-01_mangofarmsol-rug-pull.yaml) | other | 2024-01-07 |  |  |
| [2024-01_coinspaid-hack-2.yaml](data-leak/2024-01_coinspaid-hack-2.yaml) | data-leak | 2024-01-06 |  |  |
| [2024-01_xkingdom-rug-pull.yaml](other/2024-01_xkingdom-rug-pull.yaml) | other | 2024-01-06 |  |  |
| [2024-01_certik-twitter-hack.yaml](data-leak/2024-01_certik-twitter-hack.yaml) | data-leak | 2024-01-05 |  |  |
| [2024-01_gamma-strategies-exploit.yaml](data-leak/2024-01_gamma-strategies-exploit.yaml) | data-leak | 2024-01-04 |  |  |
| [2024-01_loandepot-alphv.yaml](ransomware/2024-01_loandepot-alphv.yaml) | ransomware | 2024-01-04 | ALPHV/BlackCat ransomware |  |
| [2024-01_radiant-capital-hack.yaml](data-leak/2024-01_radiant-capital-hack.yaml) | data-leak | 2024-01-02 |  |  |
| [2024-01_bill-lou-scammed.yaml](data-leak/2024-01_bill-lou-scammed.yaml) | data-leak | 2024-01-02 |  |  |
| [2024-01_upstate-family-health-center-inc-healthec-llc.yaml](supply-chain/2024-01_upstate-family-health-center-inc-healthec-llc.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_tycoon2fa-phishing-as-a-service-aitm.yaml](credential-theft/2024-01_tycoon2fa-phishing-as-a-service-aitm.yaml) | credential-theft | 2024-01-01 | Tycoon2FA phishing kit |  |
| [2024-01_primula-tietoevry.yaml](supply-chain/2024-01_primula-tietoevry.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-04_sisense-analytics-cisa-advisory.yaml](other/2024-04_sisense-analytics-cisa-advisory.yaml) | other | 2024-01-01 |  |  |
| [2024-01_uppsala-county-tietoevry.yaml](supply-chain/2024-01_uppsala-county-tietoevry.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_ransomware-law-enforcement-disruption-wave.yaml](other/2024-01_ransomware-law-enforcement-disruption-wave.yaml) | other | 2024-01-01 | LockBit, ALPHV/BlackCat, Hive… |  |
| [2024-04_kaiser-permanente-tracker.yaml](data-leak/2024-04_kaiser-permanente-tracker.yaml) | data-leak | 2024-01-01 |  |  |
| [2024-01_us-small-business-administration-orrick-herrington-sutcliffe.yaml](supply-chain/2024-01_us-small-business-administration-orrick-herrington-sutcliffe.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_woundcare-innovations-of-golf-land-consensiohealth.yaml](supply-chain/2024-01_woundcare-innovations-of-golf-land-consensiohealth.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_meritas-health-corporation-perry-johnson-associates-inc.yaml](supply-chain/2024-01_meritas-health-corporation-perry-johnson-associates-inc.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_framework-computer-keating-consulting-group.yaml](supply-chain/2024-01_framework-computer-keating-consulting-group.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-12_volkswagen-cariad-aws-location.yaml](data-leak/2024-12_volkswagen-cariad-aws-location.yaml) | data-leak | 2024-01-01 |  |  |
| [2024-01_40-affiliated-nursing-facilities-in-texas-and-kansas-hmg-healthcare.yaml](supply-chain/2024-01_40-affiliated-nursing-facilities-in-texas-and-kansas-hmg-healthcare.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-01_healthcare-vendor-supply-chain-systemic-risk.yaml](other/2024-01_healthcare-vendor-supply-chain-systemic-risk.yaml) | other | 2024-01-01 |  |  |
| [2024-01_family-healthcare-brady-martz-associates.yaml](supply-chain/2024-01_family-healthcare-brady-martz-associates.yaml) | supply-chain | 2024-01-01 |  |  |
| [2024-05_outabox-biometric-australia.yaml](data-leak/2024-05_outabox-biometric-australia.yaml) | data-leak | 2024-01-01 |  |  |
| [2023-12_orbit-bridge-hack.yaml](data-leak/2023-12_orbit-bridge-hack.yaml) | data-leak | 2023-12-31 |  |  |
| [2023-12_ust-and-luna-deemed-securities.yaml](other/2023-12_ust-and-luna-deemed-securities.yaml) | other | 2023-12-28 |  |  |
| [2023-12_wallet-gets-phished-for-4-4-million.yaml](data-leak/2023-12_wallet-gets-phished-for-4-4-million.yaml) | data-leak | 2023-12-28 |  |  |
| [2023-12_barry-silbert-grayscale-board-resignation.yaml](other/2023-12_barry-silbert-grayscale-board-resignation.yaml) | other | 2023-12-26 |  |  |
| [2023-12_levana-protocol-exploit.yaml](data-leak/2023-12_levana-protocol-exploit.yaml) | data-leak | 2023-12-26 |  |  |
| [2023-12_telcoin-exploit.yaml](data-leak/2023-12_telcoin-exploit.yaml) | data-leak | 2023-12-26 |  |  |
| [2023-12_anna-jaques-hospital-money-message.yaml](ransomware/2023-12_anna-jaques-hospital-money-message.yaml) | ransomware | 2023-12-25 | Money Message |  |
| [2023-12_megabot-exit-scam.yaml](other/2023-12_megabot-exit-scam.yaml) | other | 2023-12-25 |  |  |
| [2023-12_tether-christmas-2023-mint.yaml](other/2023-12_tether-christmas-2023-mint.yaml) | other | 2023-12-25 |  |  |
| [2023-12_barnbridge-settlement.yaml](other/2023-12_barnbridge-settlement.yaml) | other | 2023-12-22 |  |  |
| [2023-12_qredo-overhaul.yaml](other/2023-12_qredo-overhaul.yaml) | other | 2023-12-21 |  |  |
| [2023-12_catalyx-trading-freeze.yaml](data-leak/2023-12_catalyx-trading-freeze.yaml) | data-leak | 2023-12-21 |  |  |
| [2023-12_ms-drainer.yaml](data-leak/2023-12_ms-drainer.yaml) | data-leak | 2023-12-21 |  |  |
| [2023-12_first-american-financial-ransomware.yaml](ransomware/2023-12_first-american-financial-ransomware.yaml) | ransomware | 2023-12-20 |  |  |
| [2023-12_st-vincents-health-australia.yaml](data-leak/2023-12_st-vincents-health-australia.yaml) | data-leak | 2023-12-19 |  |  |
| [2023-12_aurory-bridge-hack.yaml](data-leak/2023-12_aurory-bridge-hack.yaml) | data-leak | 2023-12-17 |  |  |
| [2023-12_nft-trader-hack.yaml](data-leak/2023-12_nft-trader-hack.yaml) | data-leak | 2023-12-16 |  |  |
| [2023-12_safemoon-files-for-bankruptcy.yaml](other/2023-12_safemoon-files-for-bankruptcy.yaml) | other | 2023-12-14 |  |  |
| [2023-12_ledger-supply-chain-attack.yaml](supply-chain/2023-12_ledger-supply-chain-attack.yaml) | supply-chain | 2023-12-14 |  |  |
| [2023-12_ledger-connect-kit-supply-chain.yaml](supply-chain/2023-12_ledger-connect-kit-supply-chain.yaml) | supply-chain | 2023-12-14 | Angel Drainer (cryptocurrency… |  |
| [2023-12_80-million-romance-scam.yaml](data-leak/2023-12_80-million-romance-scam.yaml) | data-leak | 2023-12-13 |  |  |
| [2023-12_exw-fraud.yaml](other/2023-12_exw-fraud.yaml) | other | 2023-12-13 |  |  |
| [2023-12_hyperverse-scam.yaml](data-leak/2023-12_hyperverse-scam.yaml) | data-leak | 2023-12-13 |  |  |
| [2023-12_coinlist-sanctions-settlement.yaml](other/2023-12_coinlist-sanctions-settlement.yaml) | other | 2023-12-13 |  |  |
| [2023-12_okx-dex-hack.yaml](data-leak/2023-12_okx-dex-hack.yaml) | data-leak | 2023-12-12 |  |  |
| [2023-12_grifter-in-chief-donald-trump-hawks-mugshot-nfts.yaml](other/2023-12_grifter-in-chief-donald-trump-hawks-mugshot-nfts.yaml) | other | 2023-12-12 |  |  |
| [2023-12_immortal-game-shuts-down-token.yaml](other/2023-12_immortal-game-shuts-down-token.yaml) | other | 2023-12-12 |  |  |
| [2023-12_kucoin-fine.yaml](other/2023-12_kucoin-fine.yaml) | other | 2023-12-12 |  |  |
| [2023-12_ai-powered-crypto-ponzi.yaml](data-leak/2023-12_ai-powered-crypto-ponzi.yaml) | data-leak | 2023-12-12 |  |  |
| [2023-12_yearn-treasury-swap.yaml](other/2023-12_yearn-treasury-swap.yaml) | other | 2023-12-11 |  |  |
| [2023-12_uranium-finance-hacker-cash-out.yaml](data-leak/2023-12_uranium-finance-hacker-cash-out.yaml) | data-leak | 2023-12-07 |  |  |
| [2023-12_do-kwon-extradition.yaml](other/2023-12_do-kwon-extradition.yaml) | other | 2023-12-07 |  |  |
| [2023-12_nostr-assets-gets-clogged-up.yaml](other/2023-12_nostr-assets-gets-clogged-up.yaml) | other | 2023-12-05 |  |  |
| [2023-12_aeur-depeg.yaml](other/2023-12_aeur-depeg.yaml) | other | 2023-12-05 |  |  |
| [2023-12_rob-robb-scam.yaml](data-leak/2023-12_rob-robb-scam.yaml) | data-leak | 2023-12-04 |  |  |
| [2023-12_thirdweb-vulnerability.yaml](other/2023-12_thirdweb-vulnerability.yaml) | other | 2023-12-04 |  |  |
| [2023-12_safe-wallet-thefts.yaml](data-leak/2023-12_safe-wallet-thefts.yaml) | data-leak | 2023-12-03 |  |  |
| [2023-12_valley-health-system-eso-solutions-inc.yaml](supply-chain/2023-12_valley-health-system-eso-solutions-inc.yaml) | supply-chain | 2023-12-01 |  |  |
| [2023-12_40-healthcare-companies-asper-biogene.yaml](supply-chain/2023-12_40-healthcare-companies-asper-biogene.yaml) | supply-chain | 2023-12-01 |  |  |
| [2024-01_ivanti-connect-secure.yaml](other/2024-01_ivanti-connect-secure.yaml) | other | 2023-12-01 | ZIPLINE backdoor / LIGHTWIRE … | CVE-2023-46805, CVE-2024-21887, CVE-202… |
| [2023-12_60-credit-unions-trellance.yaml](supply-chain/2023-12_60-credit-unions-trellance.yaml) | supply-chain | 2023-12-01 |  |  |
| [2023-11_i-forkast-i-shutdown.yaml](other/2023-11_i-forkast-i-shutdown.yaml) | other | 2023-11-30 |  |  |
| [2023-11_draftkings-polygon-partnership.yaml](other/2023-11_draftkings-polygon-partnership.yaml) | other | 2023-11-30 |  |  |
| [2023-11_florence-finance-theft.yaml](data-leak/2023-11_florence-finance-theft.yaml) | data-leak | 2023-11-30 |  |  |
| [2023-11_forkast-shutdown.yaml](other/2023-11_forkast-shutdown.yaml) | other | 2023-11-30 |  |  |
| [2023-11_sofi-exits-crypto.yaml](other/2023-11_sofi-exits-crypto.yaml) | other | 2023-11-29 |  |  |
| [2023-11_bitstable-sale-failure.yaml](other/2023-11_bitstable-sale-failure.yaml) | other | 2023-11-29 |  |  |
| [2023-11_integris-health.yaml](ransomware/2023-11_integris-health.yaml) | ransomware | 2023-11-28 |  |  |
| [2023-11_hounax-scam.yaml](data-leak/2023-11_hounax-scam.yaml) | data-leak | 2023-11-27 |  |  |
| [2023-11_geisinger-nuance-insider-breach.yaml](data-leak/2023-11_geisinger-nuance-insider-breach.yaml) | data-leak | 2023-11-27 |  |  |
| [2023-11_bitcoiner-spends-3-million-on-transaction-fee.yaml](other/2023-11_bitcoiner-spends-3-million-on-transaction-fee.yaml) | other | 2023-11-23 |  |  |
| [2023-11_htx-and-heco-chain-hack.yaml](data-leak/2023-11_htx-and-heco-chain-hack.yaml) | data-leak | 2023-11-22 |  |  |
| [2023-11_kyberswap-hack-2.yaml](data-leak/2023-11_kyberswap-hack-2.yaml) | data-leak | 2023-11-22 |  |  |
| [2023-11_iran-irgc-cyberav3ngers-water-utilities.yaml](other/2023-11_iran-irgc-cyberav3ngers-water-utilities.yaml) | other | 2023-11-22 |  | CVE-2023-6448 |
| [2023-11_binance-legal-action.yaml](other/2023-11_binance-legal-action.yaml) | other | 2023-11-21 |  |  |
| [2023-11_aragon-dao-to-sue-founders.yaml](other/2023-11_aragon-dao-to-sue-founders.yaml) | other | 2023-11-21 |  |  |
| [2023-11_doj-binance-resolution-rumors.yaml](other/2023-11_doj-binance-resolution-rumors.yaml) | other | 2023-11-20 |  |  |
| [2023-11_kraken-sued-by-u-s-sec.yaml](other/2023-11_kraken-sued-by-u-s-sec.yaml) | other | 2023-11-20 |  |  |
| [2023-11_bittrex-winds-down.yaml](other/2023-11_bittrex-winds-down.yaml) | other | 2023-11-20 |  |  |
| [2023-11_crypto-romance-scam-in-southeast-asia.yaml](other/2023-11_crypto-romance-scam-in-southeast-asia.yaml) | other | 2023-11-20 |  |  |
| [2023-11_kronos-breach.yaml](data-leak/2023-11_kronos-breach.yaml) | data-leak | 2023-11-18 |  |  |
| [2023-11_dydx-insurance-fund-attack.yaml](data-leak/2023-11_dydx-insurance-fund-attack.yaml) | data-leak | 2023-11-18 |  |  |
| [2023-11_the-blockchain-group-financial-crisis.yaml](other/2023-11_the-blockchain-group-financial-crisis.yaml) | other | 2023-11-17 |  |  |
| [2023-11_aqua-shutdown.yaml](other/2023-11_aqua-shutdown.yaml) | other | 2023-11-17 |  |  |
| [2024-01_cloudflare-midnight-blizzard.yaml](credential-theft/2024-01_cloudflare-midnight-blizzard.yaml) | credential-theft | 2023-11-14 |  |  |
| [2023-11_twitter-security-account-impersonator-scam.yaml](data-leak/2023-11_twitter-security-account-impersonator-scam.yaml) | data-leak | 2023-11-14 |  |  |
| [2023-11_randstorm.yaml](other/2023-11_randstorm.yaml) | other | 2023-11-14 |  |  |
| [2023-11_create2-wallet-drainer.yaml](data-leak/2023-11_create2-wallet-drainer.yaml) | data-leak | 2023-11-12 |  |  |
| [2023-11_binance-linked-wallet-hacked.yaml](data-leak/2023-11_binance-linked-wallet-hacked.yaml) | data-leak | 2023-11-12 |  |  |
| [2023-11_raft-hack.yaml](data-leak/2023-11_raft-hack.yaml) | data-leak | 2023-11-11 |  |  |
| [2023-11_samudai-treasury-drained.yaml](data-leak/2023-11_samudai-treasury-drained.yaml) | data-leak | 2023-11-10 |  |  |
| [2023-11_poloniex-hack.yaml](data-leak/2023-11_poloniex-hack.yaml) | data-leak | 2023-11-10 |  |  |
| [2023-11_fred-hutch-hunters-intl.yaml](ransomware/2023-11_fred-hutch-hunters-intl.yaml) | ransomware | 2023-11-10 | Hunters International ransomw… |  |
| [2023-11_dp-world-australia.yaml](ransomware/2023-11_dp-world-australia.yaml) | ransomware | 2023-11-10 |  | CVE-2023-4966 |
| [2023-11_dp-world-australia-port-attack.yaml](ransomware/2023-11_dp-world-australia-port-attack.yaml) | ransomware | 2023-11-10 |  |  |
| [2023-11_coinspot-hack.yaml](data-leak/2023-11_coinspot-hack.yaml) | data-leak | 2023-11-08 |  |  |
| [2023-11_icbc-us-lockbit-treasury.yaml](other/2023-11_icbc-us-lockbit-treasury.yaml) | ransomware | 2023-11-08 | LockBit ransomware | CVE-2023-4966 |
| [2023-11_mev-bot-0x05f01-exploit.yaml](data-leak/2023-11_mev-bot-0x05f01-exploit.yaml) | data-leak | 2023-11-07 |  |  |
| [2023-11_wintermute-near-aurora-breakup.yaml](other/2023-11_wintermute-near-aurora-breakup.yaml) | other | 2023-11-07 |  |  |
| [2023-11_himachal-pradesh-scam.yaml](data-leak/2023-11_himachal-pradesh-scam.yaml) | data-leak | 2023-11-06 |  |  |
| [2023-11_yuga-labs-social-media-lead-resigns.yaml](other/2023-11_yuga-labs-social-media-lead-resigns.yaml) | other | 2023-11-05 |  |  |
| [2023-11_apefest-photokeratitis.yaml](other/2023-11_apefest-photokeratitis.yaml) | other | 2023-11-04 |  |  |
| [2023-11_sumo-logic-aws-access-key.yaml](credential-theft/2023-11_sumo-logic-aws-access-key.yaml) | credential-theft | 2023-11-03 |  |  |
| [2023-11_sam-bankman-fried-convicted.yaml](other/2023-11_sam-bankman-fried-convicted.yaml) | other | 2023-11-02 |  |  |
| [2023-11_northwell-health-perry-johnson-associates-inc.yaml](supply-chain/2023-11_northwell-health-perry-johnson-associates-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_samsung-electronics-unknown.yaml](supply-chain/2023-11_samsung-electronics-unknown.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_westat-inc-nuance-communications-inc.yaml](supply-chain/2023-11_westat-inc-nuance-communications-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_monero-community-wallet-hack.yaml](data-leak/2023-11_monero-community-wallet-hack.yaml) | data-leak | 2023-11-01 |  |  |
| [2023-11_onyx-hack-1.yaml](data-leak/2023-11_onyx-hack-1.yaml) | data-leak | 2023-11-01 |  |  |
| [2023-11_taylor-rose-cts.yaml](supply-chain/2023-11_taylor-rose-cts.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_safemoon-executives-charged-and-arrested.yaml](other/2023-11_safemoon-executives-charged-and-arrested.yaml) | other | 2023-11-01 |  |  |
| [2023-11_california-physicians-service-d-b-a-blue-shield-of-california-medical-eye-services-inc.yaml](supply-chain/2023-11_california-physicians-service-d-b-a-blue-shield-of-california-medical-eye-services-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2024-01_microsoft-midnight-blizzard.yaml](credential-theft/2024-01_microsoft-midnight-blizzard.yaml) | credential-theft | 2023-11-01 |  |  |
| [2023-11_the-canadian-government-sirva-worldwide-inc.yaml](supply-chain/2023-11_the-canadian-government-sirva-worldwide-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_1password-okta.yaml](supply-chain/2023-11_1password-okta.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_dollar-tree-zeroed-in-technologies.yaml](supply-chain/2023-11_dollar-tree-zeroed-in-technologies.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_crouse-health-in-syracuse-perry-johnson-associates-inc.yaml](supply-chain/2023-11_crouse-health-in-syracuse-perry-johnson-associates-inc.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_sutter-health-virgin-pulse.yaml](supply-chain/2023-11_sutter-health-virgin-pulse.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-11_blue-cross-and-blue-shield-of-minnesota-and-blue-plus-welltok.yaml](supply-chain/2023-11_blue-cross-and-blue-shield-of-minnesota-and-blue-plus-welltok.yaml) | supply-chain | 2023-11-01 |  |  |
| [2023-10_infosys-mccamish-lockbit.yaml](supply-chain/2023-10_infosys-mccamish-lockbit.yaml) | supply-chain | 2023-10-29 | LockBit ransomware |  |
| [2024-06_truist-bank-sp1d3r-dark-web.yaml](data-leak/2024-06_truist-bank-sp1d3r-dark-web.yaml) | data-leak | 2023-10-27 |  |  |
| [2023-10_ryder-ripps-loses-lawsuit.yaml](other/2023-10_ryder-ripps-loses-lawsuit.yaml) | other | 2023-10-25 |  |  |
| [2023-10_aubit-liquidation.yaml](other/2023-10_aubit-liquidation.yaml) | other | 2023-10-20 |  |  |
| [2023-10_superdao-to-shut-down.yaml](other/2023-10_superdao-to-shut-down.yaml) | other | 2023-10-19 |  |  |
| [2023-10_treasury-department-introduces-proposal-targeting-crypto-mixers.yaml](other/2023-10_treasury-department-introduces-proposal-targeting-crypto-mixers.yaml) | other | 2023-10-19 |  |  |
| [2023-10_marina-bay-sands-singapore-pdpc.yaml](data-leak/2023-10_marina-bay-sands-singapore-pdpc.yaml) | data-leak | 2023-10-19 |  |  |
| [2023-10_gemini-genesis-and-dcg-lawsuit.yaml](other/2023-10_gemini-genesis-and-dcg-lawsuit.yaml) | other | 2023-10-19 |  |  |
| [2023-10_hope-lend-hack.yaml](data-leak/2023-10_hope-lend-hack.yaml) | data-leak | 2023-10-18 |  |  |
| [2023-10_everscale-hack.yaml](data-leak/2023-10_everscale-hack.yaml) | data-leak | 2023-10-17 |  |  |
| [2023-10_fantom-wallet-hacks.yaml](data-leak/2023-10_fantom-wallet-hacks.yaml) | data-leak | 2023-10-17 |  |  |
| [2023-10_reddit-abandons-blockchain-based-community-points.yaml](other/2023-10_reddit-abandons-blockchain-based-community-points.yaml) | other | 2023-10-17 |  |  |
| [2023-10_xfinity-comcast-citrixbleed-35m.yaml](data-leak/2023-10_xfinity-comcast-citrixbleed-35m.yaml) | data-leak | 2023-10-16 |  | CVE-2023-4966 |
| [2023-10_fake-etf-approval-news.yaml](other/2023-10_fake-etf-approval-news.yaml) | other | 2023-10-16 |  |  |
| [2023-10_south-korean-regulators-allege-sui-foundation-manipulated-markets.yaml](other/2023-10_south-korean-regulators-allege-sui-foundation-manipulated-markets.yaml) | other | 2023-10-16 |  |  |
| [2023-10_trueusd-teuro-announcement.yaml](other/2023-10_trueusd-teuro-announcement.yaml) | other | 2023-10-16 |  |  |
| [2023-10_hackers-host-malicious-code-on-binance-chain-to-circumvent-takedowns.yaml](data-leak/2023-10_hackers-host-malicious-code-on-binance-chain-to-circumvent-takedowns.yaml) | data-leak | 2023-10-13 |  |  |
| [2023-10_stephen-ehrlich-lawsuits.yaml](other/2023-10_stephen-ehrlich-lawsuits.yaml) | other | 2023-10-12 |  |  |
| [2023-10_usdr-stablecoin-de-pegs.yaml](other/2023-10_usdr-stablecoin-de-pegs.yaml) | other | 2023-10-12 |  |  |
| [2023-10_platypus-finance-hack-3.yaml](data-leak/2023-10_platypus-finance-hack-3.yaml) | data-leak | 2023-10-12 |  |  |
| [2023-10_black-hole-token-hack.yaml](data-leak/2023-10_black-hole-token-hack.yaml) | data-leak | 2023-10-11 |  |  |
| [2023-10_trader-joe-s-sues-trader-joe.yaml](other/2023-10_trader-joe-s-sues-trader-joe.yaml) | other | 2023-10-10 |  |  |
| [2023-10_3commas-breach.yaml](data-leak/2023-10_3commas-breach.yaml) | data-leak | 2023-10-10 |  |  |
| [2023-10_goldfinch-lending-platform-facing-7-million-loss.yaml](other/2023-10_goldfinch-lending-platform-facing-7-million-loss.yaml) | other | 2023-10-10 |  |  |
| [2023-10_finsoul-exit-scam.yaml](data-leak/2023-10_finsoul-exit-scam.yaml) | data-leak | 2023-10-10 |  |  |
| [2023-10_fsl-rug-pull.yaml](other/2023-10_fsl-rug-pull.yaml) | other | 2023-10-10 |  |  |
| [2023-10_bitmain-stops-paying-employees.yaml](other/2023-10_bitmain-stops-paying-employees.yaml) | other | 2023-10-09 |  |  |
| [2023-10_uk-fca-adds-more-unauthorized-firms-to-list.yaml](other/2023-10_uk-fca-adds-more-unauthorized-firms-to-list.yaml) | other | 2023-10-09 |  |  |
| [2023-10_lucky-star-currency-rug-pull.yaml](data-leak/2023-10_lucky-star-currency-rug-pull.yaml) | data-leak | 2023-10-09 |  |  |
| [2023-10_stars-arena-exploit.yaml](data-leak/2023-10_stars-arena-exploit.yaml) | data-leak | 2023-10-07 |  |  |
| [2023-10_gitcoin-transfer-mistake.yaml](other/2023-10_gitcoin-transfer-mistake.yaml) | other | 2023-10-06 |  |  |
| [2023-10_bored-apes-yuga-labs-lays-off-employees.yaml](other/2023-10_bored-apes-yuga-labs-lays-off-employees.yaml) | other | 2023-10-06 |  |  |
| [2023-10_thorswap-temporarily-shuts-down-web-interface-as-ftx-hacker-tries-to-launder-131-million.yaml](data-leak/2023-10_thorswap-temporarily-shuts-down-web-interface-as-ftx-hacker-tries-to-launder-131-million.yaml) | data-leak | 2023-10-06 |  |  |
| [2023-10_bigwhale-hack.yaml](data-leak/2023-10_bigwhale-hack.yaml) | data-leak | 2023-10-03 |  |  |
| [2023-10_crypto-com-fine.yaml](other/2023-10_crypto-com-fine.yaml) | other | 2023-10-02 |  |  |
| [2023-10_chatham-kent-health-alliance-transform.yaml](supply-chain/2023-10_chatham-kent-health-alliance-transform.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_super-sa-former-external-service-prov.yaml](supply-chain/2023-10_super-sa-former-external-service-prov.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_boeing-citrixbleed.yaml](ransomware/2023-10_boeing-citrixbleed.yaml) | ransomware | 2023-10-01 | LockBit 3.0 | CVE-2023-4966 |
| [2023-10_united-states-department-of-justice-ipswitch-inc.yaml](supply-chain/2023-10_united-states-department-of-justice-ipswitch-inc.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_arietis-health-ipswitch-inc.yaml](supply-chain/2023-10_arietis-health-ipswitch-inc.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_cook-county-health-perry-johnson-associates-inc.yaml](supply-chain/2023-10_cook-county-health-perry-johnson-associates-inc.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_flagstar-bank-fiserv.yaml](supply-chain/2023-10_flagstar-bank-fiserv.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_truist-bank-dark-web.yaml](data-leak/2023-10_truist-bank-dark-web.yaml) | data-leak | 2023-10-01 |  |  |
| [2023-10_humana-inc-pnc-bank.yaml](supply-chain/2023-10_humana-inc-pnc-bank.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_northstar-anesthesia-arietis-health.yaml](supply-chain/2023-10_northstar-anesthesia-arietis-health.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_sa-health-personify-care.yaml](supply-chain/2023-10_sa-health-personify-care.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_virginia-dept-of-medical-assistance-services-maximus.yaml](supply-chain/2023-10_virginia-dept-of-medical-assistance-services-maximus.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-10_sony-ipswitch-inc.yaml](supply-chain/2023-10_sony-ipswitch-inc.yaml) | supply-chain | 2023-10-01 |  |  |
| [2023-09_auditor-prager-metis-sued-by-sec.yaml](other/2023-09_auditor-prager-metis-sued-by-sec.yaml) | other | 2023-09-29 |  |  |
| [2023-09_three-arrows-capital-co-founder-su-zhu-jailed-for-four-months.yaml](other/2023-09_three-arrows-capital-co-founder-su-zhu-jailed-for-four-months.yaml) | other | 2023-09-29 |  |  |
| [2023-09_mercedes-benz-github-token.yaml](credential-theft/2023-09_mercedes-benz-github-token.yaml) | credential-theft | 2023-09-29 |  |  |
| [2023-10_okta-support-system.yaml](credential-theft/2023-10_okta-support-system.yaml) | credential-theft | 2023-09-28 |  |  |
| [2023-09_okta-support-system-breach.yaml](credential-theft/2023-09_okta-support-system-breach.yaml) | credential-theft | 2023-09-28 |  |  |
| [2023-09_chase-uk-to-block-payments-for-crypto.yaml](other/2023-09_chase-uk-to-block-payments-for-crypto.yaml) | other | 2023-09-26 |  |  |
| [2023-09_jpex-collapse.yaml](data-leak/2023-09_jpex-collapse.yaml) | data-leak | 2023-09-25 |  |  |
| [2023-09_johnson-controls-dark-angels.yaml](ransomware/2023-09_johnson-controls-dark-angels.yaml) | ransomware | 2023-09-25 | Dark Angels ransomware |  |
| [2023-09_huobi-exchange-hacked.yaml](data-leak/2023-09_huobi-exchange-hacked.yaml) | data-leak | 2023-09-24 |  |  |
| [2023-09_upbit-aptos-transaction-spoofing.yaml](data-leak/2023-09_upbit-aptos-transaction-spoofing.yaml) | data-leak | 2023-09-24 |  |  |
| [2023-09_mixin-network-hack.yaml](data-leak/2023-09_mixin-network-hack.yaml) | data-leak | 2023-09-23 |  |  |
| [2023-09_0x5e422-phishing-attack.yaml](data-leak/2023-09_0x5e422-phishing-attack.yaml) | data-leak | 2023-09-20 |  |  |
| [2023-09_balancer-frontend-compromise.yaml](data-leak/2023-09_balancer-frontend-compromise.yaml) | data-leak | 2023-09-19 |  |  |
| [2023-09_jpex-issues.yaml](other/2023-09_jpex-issues.yaml) | other | 2023-09-17 |  |  |
| [2023-09_killer-whales-crypto-reality-show.yaml](other/2023-09_killer-whales-crypto-reality-show.yaml) | other | 2023-09-15 |  |  |
| [2023-09_i-killer-whales-i-crypto-reality-show.yaml](other/2023-09_i-killer-whales-i-crypto-reality-show.yaml) | other | 2023-09-15 |  |  |
| [2023-09_mark-cuban-hack.yaml](data-leak/2023-09_mark-cuban-hack.yaml) | data-leak | 2023-09-15 |  |  |
| [2023-09_polkaworld-pause.yaml](other/2023-09_polkaworld-pause.yaml) | other | 2023-09-15 |  |  |
| [2023-09_nouns-dao-fractures-in-27-million-split.yaml](other/2023-09_nouns-dao-fractures-in-27-million-split.yaml) | other | 2023-09-15 |  |  |
| [2023-09_remitano-hack.yaml](data-leak/2023-09_remitano-hack.yaml) | data-leak | 2023-09-15 |  |  |
| [2023-09_ethereum-bungles-holesky-testnet-launch.yaml](other/2023-09_ethereum-bungles-holesky-testnet-launch.yaml) | other | 2023-09-15 |  |  |
| [2023-09_ftx-class-action-settlements.yaml](other/2023-09_ftx-class-action-settlements.yaml) | other | 2023-09-15 |  |  |
| [2023-09_genesis-closes-trading-entirely.yaml](other/2023-09_genesis-closes-trading-entirely.yaml) | other | 2023-09-14 |  |  |
| [2023-09_sec-charges-stoner-cats-nft-project.yaml](other/2023-09_sec-charges-stoner-cats-nft-project.yaml) | other | 2023-09-13 |  |  |
| [2023-09_onecoin-cofounder-sentenced-to-prison.yaml](other/2023-09_onecoin-cofounder-sentenced-to-prison.yaml) | other | 2023-09-12 |  |  |
| [2023-09_binance-us-ceo-leaves.yaml](other/2023-09_binance-us-ceo-leaves.yaml) | other | 2023-09-12 |  |  |
| [2023-09_coinex-hack.yaml](data-leak/2023-09_coinex-hack.yaml) | data-leak | 2023-09-12 |  |  |
| [2023-09_remilia-theft.yaml](data-leak/2023-09_remilia-theft.yaml) | data-leak | 2023-09-11 |  |  |
| [2023-09_banana-gun-bot-flubbed-token-launch.yaml](other/2023-09_banana-gun-bot-flubbed-token-launch.yaml) | other | 2023-09-11 |  |  |
| [2023-09_fortress-trust-breach.yaml](data-leak/2023-09_fortress-trust-breach.yaml) | data-leak | 2023-09-11 |  |  |
| [2023-09_paxos-fee-overpayment.yaml](other/2023-09_paxos-fee-overpayment.yaml) | other | 2023-09-10 |  |  |
| [2023-09_vitalik-buterin-s-twitter-account-hacked.yaml](data-leak/2023-09_vitalik-buterin-s-twitter-account-hacked.yaml) | data-leak | 2023-09-09 |  |  |
| [2023-09_thodex-ceo-sentenced.yaml](other/2023-09_thodex-ceo-sentenced.yaml) | other | 2023-09-08 |  |  |
| [2023-09_nft-startup-glass-shuts-down.yaml](other/2023-09_nft-startup-glass-shuts-down.yaml) | other | 2023-09-08 |  |  |
| [2023-09_mgm-resorts.yaml](ransomware/2023-09_mgm-resorts.yaml) | ransomware | 2023-09-08 | ALPHV/BlackCat |  |
| [2023-09_cftc-goes-after-three-defi-projects.yaml](other/2023-09_cftc-goes-after-three-defi-projects.yaml) | other | 2023-09-07 |  |  |
| [2023-09_ryan-salame-plea.yaml](other/2023-09_ryan-salame-plea.yaml) | other | 2023-09-07 |  |  |
| [2023-09_0x13e38-phished.yaml](data-leak/2023-09_0x13e38-phished.yaml) | data-leak | 2023-09-06 |  |  |
| [2023-09_high-profile-streamers-bail-on-mrbeast-promoted-creator-league-after-learning-there-are-blockchains-involved.yaml](other/2023-09_high-profile-streamers-bail-on-mrbeast-promoted-creator-league-after-learning-there-are-blockchains-involved.yaml) | other | 2023-09-06 |  |  |
| [2023-09_gmbl-computer-exploit.yaml](data-leak/2023-09_gmbl-computer-exploit.yaml) | data-leak | 2023-09-05 |  |  |
| [2023-09_stolen-lastpass-vaults-possibly-cracked.yaml](data-leak/2023-09_stolen-lastpass-vaults-possibly-cracked.yaml) | data-leak | 2023-09-05 |  |  |
| [2023-09_genesis-to-close-u-s-spot-trading-business.yaml](other/2023-09_genesis-to-close-u-s-spot-trading-business.yaml) | other | 2023-09-05 |  |  |
| [2023-09_metamask-phishing-scammers-hijack-government-websites.yaml](data-leak/2023-09_metamask-phishing-scammers-hijack-government-websites.yaml) | data-leak | 2023-09-05 |  |  |
| [2023-09_nima-capital-rug-pull.yaml](other/2023-09_nima-capital-rug-pull.yaml) | other | 2023-09-04 |  |  |
| [2023-09_stake-hack.yaml](data-leak/2023-09_stake-hack.yaml) | data-leak | 2023-09-04 |  |  |
| [2023-09_airbus-turkish-airlines.yaml](supply-chain/2023-09_airbus-turkish-airlines.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_sutter-north-surgery-center-patients-sightpath-medical.yaml](supply-chain/2023-09_sutter-north-surgery-center-patients-sightpath-medical.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_judiciary-branch-ifx-networks-colombia.yaml](supply-chain/2023-09_judiciary-branch-ifx-networks-colombia.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_university-of-sydney-unknown.yaml](supply-chain/2023-09_university-of-sydney-unknown.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_890-schools-national-student-clearinghou.yaml](supply-chain/2023-09_890-schools-national-student-clearinghou.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_ftx-kroll-inc.yaml](supply-chain/2023-09_ftx-kroll-inc.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_born-ontario-ipswitch-inc.yaml](supply-chain/2023-09_born-ontario-ipswitch-inc.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-09_amerita-pharmerica.yaml](supply-chain/2023-09_amerita-pharmerica.yaml) | supply-chain | 2023-09-01 |  |  |
| [2023-08_gala-games-lawsuits.yaml](other/2023-08_gala-games-lawsuits.yaml) | other | 2023-08-31 |  |  |
| [2023-08_starknet-upgrade-leaves-550-000-inaccessible.yaml](other/2023-08_starknet-upgrade-leaves-550-000-inaccessible.yaml) | other | 2023-08-30 |  |  |
| [2023-08_fraternidade-crypto-theft.yaml](data-leak/2023-08_fraternidade-crypto-theft.yaml) | data-leak | 2023-08-29 |  |  |
| [2023-08_impact-theory-fined-by-sec.yaml](other/2023-08_impact-theory-fined-by-sec.yaml) | other | 2023-08-28 |  |  |
| [2023-08_balancer-exploit.yaml](data-leak/2023-08_balancer-exploit.yaml) | data-leak | 2023-08-27 |  |  |
| [2023-08_retool-mfa-google-cloud-phishing.yaml](other/2023-08_retool-mfa-google-cloud-phishing.yaml) | other | 2023-08-27 |  |  |
| [2023-08_clockwork-project-to-shut-down.yaml](other/2023-08_clockwork-project-to-shut-down.yaml) | other | 2023-08-27 |  |  |
| [2023-08_sol-big-brain-phishing-attack.yaml](data-leak/2023-08_sol-big-brain-phishing-attack.yaml) | data-leak | 2023-08-25 |  |  |
| [2023-08_magnate-finance-rug-pull.yaml](other/2023-08_magnate-finance-rug-pull.yaml) | other | 2023-08-25 |  |  |
| [2023-08_suspicious-pepe-transfers.yaml](data-leak/2023-08_suspicious-pepe-transfers.yaml) | data-leak | 2023-08-24 |  |  |
| [2023-08_u-s-drug-enforcement-administration-scammed.yaml](data-leak/2023-08_u-s-drug-enforcement-administration-scammed.yaml) | data-leak | 2023-08-24 |  |  |
| [2023-08_blazar-token-sec-lawsuit.yaml](data-leak/2023-08_blazar-token-sec-lawsuit.yaml) | data-leak | 2023-08-23 |  |  |
| [2023-08_doj-charges-two-founders-of-tornado-cash.yaml](other/2023-08_doj-charges-two-founders-of-tornado-cash.yaml) | other | 2023-08-23 |  |  |
| [2023-08_balancer-vulnerability.yaml](other/2023-08_balancer-vulnerability.yaml) | other | 2023-08-22 |  |  |
| [2023-08_celer-bridge-google-ad-phishing.yaml](data-leak/2023-08_celer-bridge-google-ad-phishing.yaml) | data-leak | 2023-08-21 |  |  |
| [2023-08_sec-cracks-down-on-titan-crypto-investment-manager-for-advertising-2-700-returns.yaml](other/2023-08_sec-cracks-down-on-titan-crypto-investment-manager-for-advertising-2-700-returns.yaml) | other | 2023-08-21 |  |  |
| [2023-08_harbor-protocol-exploit.yaml](data-leak/2023-08_harbor-protocol-exploit.yaml) | data-leak | 2023-08-19 |  |  |
| [2023-08_crypto-founder-loses-over-250-000-to-crypto-scam.yaml](other/2023-08_crypto-founder-loses-over-250-000-to-crypto-scam.yaml) | other | 2023-08-18 |  |  |
| [2023-08_recur-nft-platform-shuts-down-after-50-million-series-a.yaml](other/2023-08_recur-nft-platform-shuts-down-after-50-million-series-a.yaml) | other | 2023-08-18 |  |  |
| [2023-08_fed-issues-cease-and-desist-to-ftx-connected-farmington-state-bank.yaml](other/2023-08_fed-issues-cease-and-desist-to-ftx-connected-farmington-state-bank.yaml) | other | 2023-08-18 |  |  |
| [2023-08_exactly-protocol-hack.yaml](data-leak/2023-08_exactly-protocol-hack.yaml) | data-leak | 2023-08-18 |  |  |
| [2023-08_terra-website-hijacked-by-phisher.yaml](data-leak/2023-08_terra-website-hijacked-by-phisher.yaml) | data-leak | 2023-08-18 |  |  |
| [2023-08_caesars-entertainment.yaml](ransomware/2023-08_caesars-entertainment.yaml) | ransomware | 2023-08-18 | Scattered Spider ransomware |  |
| [2024-09_slim-cd-payment-processor.yaml](data-leak/2024-09_slim-cd-payment-processor.yaml) | data-leak | 2023-08-17 |  |  |
| [2023-08_bart-stephens-sim-swap-hack.yaml](data-leak/2023-08_bart-stephens-sim-swap-hack.yaml) | data-leak | 2023-08-16 |  |  |
| [2023-08_shibarium-bridge-failure.yaml](other/2023-08_shibarium-bridge-failure.yaml) | other | 2023-08-16 |  |  |
| [2023-08_swirllend-rug-pull.yaml](other/2023-08_swirllend-rug-pull.yaml) | other | 2023-08-16 |  |  |
| [2023-08_prime-trust-files-for-bankruptcy.yaml](other/2023-08_prime-trust-files-for-bankruptcy.yaml) | other | 2023-08-15 |  |  |
| [2023-08_shenzhen-shikongyun-technology-scheme.yaml](other/2023-08_shenzhen-shikongyun-technology-scheme.yaml) | other | 2023-08-15 |  |  |
| [2023-08_rocketswap-exploited-after-key-compromise.yaml](data-leak/2023-08_rocketswap-exploited-after-key-compromise.yaml) | data-leak | 2023-08-14 |  |  |
| [2023-08_zunami-protocol-exploit-2-1-million.yaml](data-leak/2023-08_zunami-protocol-exploit-2-1-million.yaml) | data-leak | 2023-08-13 |  |  |
| [2023-08_frenstech-rug-pull.yaml](other/2023-08_frenstech-rug-pull.yaml) | other | 2023-08-12 |  |  |
| [2023-08_clorox-scattered-spider.yaml](ransomware/2023-08_clorox-scattered-spider.yaml) | ransomware | 2023-08-11 | ALPHV/BlackCat ransomware |  |
| [2023-08_bittrex-settles-with-sec-for-24-million.yaml](other/2023-08_bittrex-settles-with-sec-for-24-million.yaml) | other | 2023-08-10 |  |  |
| [2023-08_libbitcoin-vulnerability.yaml](data-leak/2023-08_libbitcoin-vulnerability.yaml) | data-leak | 2023-08-09 |  |  |
| [2023-08_spiritswap-to-shut-down.yaml](other/2023-08_spiritswap-to-shut-down.yaml) | other | 2023-08-09 |  |  |
| [2023-08_rapattoni-mls-ransomware.yaml](ransomware/2023-08_rapattoni-mls-ransomware.yaml) | ransomware | 2023-08-09 |  |  |
| [2023-08_hundred-finance-shuts-down.yaml](other/2023-08_hundred-finance-shuts-down.yaml) | other | 2023-08-09 |  |  |
| [2023-08_scammers-target-victims-via-web3-job-search-boards.yaml](data-leak/2023-08_scammers-target-victims-via-web3-job-search-boards.yaml) | data-leak | 2023-08-08 |  |  |
| [2023-08_disney-exits-the-metaverse.yaml](other/2023-08_disney-exits-the-metaverse.yaml) | other | 2023-08-08 |  |  |
| [2023-08_rumors-swirl-that-huobi-executives-have-been-arrested-exchange-is-insolvent.yaml](other/2023-08_rumors-swirl-that-huobi-executives-have-been-arrested-exchange-is-insolvent.yaml) | other | 2023-08-07 |  |  |
| [2023-11_dollar-tree-zeroed-in.yaml](supply-chain/2023-11_dollar-tree-zeroed-in.yaml) | supply-chain | 2023-08-07 |  |  |
| [2023-08_worldcoin-warehouse-in-nairobi-raided-by-authorities.yaml](other/2023-08_worldcoin-warehouse-in-nairobi-raided-by-authorities.yaml) | other | 2023-08-07 |  |  |
| [2023-08_cypher-protocol-exploit.yaml](data-leak/2023-08_cypher-protocol-exploit.yaml) | data-leak | 2023-08-07 |  |  |
| [2023-08_bitsonic-ceo-arrested-for-allegedly-stealing-7-5-million.yaml](other/2023-08_bitsonic-ceo-arrested-for-allegedly-stealing-7-5-million.yaml) | other | 2023-08-07 |  |  |
| [2023-08_steadefi-exploit.yaml](data-leak/2023-08_steadefi-exploit.yaml) | data-leak | 2023-08-07 |  |  |
| [2023-08_nft-copytrader-tricked.yaml](other/2023-08_nft-copytrader-tricked.yaml) | other | 2023-08-05 |  |  |
| [2023-08_revolut-shuts-down-crypto-business-in-the-us.yaml](other/2023-08_revolut-shuts-down-crypto-business-in-the-us.yaml) | other | 2023-08-04 |  |  |
| [2023-08_web3-platform-nifty-s-shuts-down.yaml](other/2023-08_web3-platform-nifty-s-shuts-down.yaml) | other | 2023-08-02 |  |  |
| [2023-08_uwerx-exploit.yaml](data-leak/2023-08_uwerx-exploit.yaml) | data-leak | 2023-08-02 |  |  |
| [2023-08_eversource-energy-clearesult.yaml](supply-chain/2023-08_eversource-energy-clearesult.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_nuance-communications-ipswitch-inc.yaml](supply-chain/2023-08_nuance-communications-ipswitch-inc.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_automobile-plan-operational-vehicle-rental-trade-vodatech-it.yaml](supply-chain/2023-08_automobile-plan-operational-vehicle-rental-trade-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_agesalife-and-retirement-as-vodatech-it.yaml](supply-chain/2023-08_agesalife-and-retirement-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_leetswap-exploit.yaml](data-leak/2023-08_leetswap-exploit.yaml) | data-leak | 2023-08-01 |  |  |
| [2023-08_serco-inc-group-health-plan-ipswitch-inc.yaml](supply-chain/2023-08_serco-inc-group-health-plan-ipswitch-inc.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_janssen-healthcare-platform-ibm.yaml](supply-chain/2023-08_janssen-healthcare-platform-ibm.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_ups-cargo-vodatech-it.yaml](supply-chain/2023-08_ups-cargo-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_be-ikta-sportive-products-industry-and-trade-as-vodatech-it.yaml](supply-chain/2023-08_be-ikta-sportive-products-industry-and-trade-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_20-million-zero-transfer-attack.yaml](data-leak/2023-08_20-million-zero-transfer-attack.yaml) | data-leak | 2023-08-01 |  |  |
| [2023-08_child-health-plan-plus-chp-ibm.yaml](supply-chain/2023-08_child-health-plan-plus-chp-ibm.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_puma-sportswear-industry-and-trade-vodatech-it.yaml](supply-chain/2023-08_puma-sportswear-industry-and-trade-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_do-an-trend-automotive-trade-service-and-technology-joint-stock-company-vodatech-it.yaml](supply-chain/2023-08_do-an-trend-automotive-trade-service-and-technology-joint-stock-company-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_dagi-clothing-industry-and-trade-as-vodatech-it.yaml](supply-chain/2023-08_dagi-clothing-industry-and-trade-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_gulf-insurance-as-vodatech-it.yaml](supply-chain/2023-08_gulf-insurance-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_derimod-leather-garment-marketing-industry-and-trade-as-vodatech-it.yaml](supply-chain/2023-08_derimod-leather-garment-marketing-industry-and-trade-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_yoyo-information-technologies-and-tourism-trade-as-vodatech-it.yaml](supply-chain/2023-08_yoyo-information-technologies-and-tourism-trade-as-vodatech-it.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-08_zillow-rapattoni-corporation.yaml](supply-chain/2023-08_zillow-rapattoni-corporation.yaml) | supply-chain | 2023-08-01 |  |  |
| [2023-07_sec-goes-after-richard-heart-and-his-projects-hex-pulsechain-and-pulsex.yaml](other/2023-07_sec-goes-after-richard-heart-and-his-projects-hex-pulsechain-and-pulsex.yaml) | other | 2023-07-31 |  |  |
| [2023-07_bald-rug-pull.yaml](other/2023-07_bald-rug-pull.yaml) | other | 2023-07-31 |  |  |
| [2023-07_vyper-vulnerability-affecting-curve.yaml](data-leak/2023-07_vyper-vulnerability-affecting-curve.yaml) | data-leak | 2023-07-30 |  |  |
| [2023-07_kannagi-finance-rug-pull.yaml](other/2023-07_kannagi-finance-rug-pull.yaml) | other | 2023-07-29 |  |  |
| [2023-07_pond0x-bug.yaml](data-leak/2023-07_pond0x-bug.yaml) | data-leak | 2023-07-28 |  |  |
| [2023-07_defilabs-rug-pull.yaml](other/2023-07_defilabs-rug-pull.yaml) | other | 2023-07-27 |  |  |
| [2023-07_eralend-exploit.yaml](data-leak/2023-07_eralend-exploit.yaml) | data-leak | 2023-07-25 |  |  |
| [2023-07_coinspaid-hack-1.yaml](data-leak/2023-07_coinspaid-hack-1.yaml) | data-leak | 2023-07-25 |  |  |
| [2023-07_iegt-token-rug-pull.yaml](other/2023-07_iegt-token-rug-pull.yaml) | other | 2023-07-22 |  |  |
| [2023-07_alphapo-hack.yaml](data-leak/2023-07_alphapo-hack.yaml) | data-leak | 2023-07-22 |  |  |
| [2023-07_party-parrot-treasury-distribution.yaml](other/2023-07_party-parrot-treasury-distribution.yaml) | other | 2023-07-21 |  |  |
| [2023-07_conic-finance-exploit-2.yaml](data-leak/2023-07_conic-finance-exploit-2.yaml) | data-leak | 2023-07-21 |  |  |
| [2023-07_conic-finance-exploit-1.yaml](data-leak/2023-07_conic-finance-exploit-1.yaml) | data-leak | 2023-07-21 |  |  |
| [2023-07_melania-trump-apollo-nfts.yaml](other/2023-07_melania-trump-apollo-nfts.yaml) | other | 2023-07-20 |  |  |
| [2023-07_gmeta-rug-pull.yaml](other/2023-07_gmeta-rug-pull.yaml) | other | 2023-07-18 |  |  |
| [2023-07_feds-seize-tens-of-millions-from-deltec-bank-in-connection-to-fake-crypto-investment-schemes.yaml](data-leak/2023-07_feds-seize-tens-of-millions-from-deltec-bank-in-connection-to-fake-crypto-investment-schemes.yaml) | data-leak | 2023-07-17 |  |  |
| [2023-07_scammer-soup-makes-more-than-1-million-through-discord-hacks.yaml](data-leak/2023-07_scammer-soup-makes-more-than-1-million-through-discord-hacks.yaml) | data-leak | 2023-07-17 |  |  |
| [2023-07_hector-dao-shuts-down.yaml](other/2023-07_hector-dao-shuts-down.yaml) | other | 2023-07-17 |  |  |
| [2023-07_five-men-including-inspector-in-bankruptcy-proceeding-charged-with-kidnapping-crypto-king-alleged-scammer.yaml](other/2023-07_five-men-including-inspector-in-bankruptcy-proceeding-charged-with-kidnapping-crypto-king-alleged-scammer.yaml) | other | 2023-07-17 |  |  |
| [2023-07_neopets-shuts-down-its-neopets-metaverse-project.yaml](other/2023-07_neopets-shuts-down-its-neopets-metaverse-project.yaml) | other | 2023-07-17 |  |  |
| [2023-07_geist-finance-shuts-down.yaml](other/2023-07_geist-finance-shuts-down.yaml) | other | 2023-07-14 |  |  |
| [2023-07_multichain-finally-confirms-their-ceo-was-arrested-in-china.yaml](other/2023-07_multichain-finally-confirms-their-ceo-was-arrested-in-china.yaml) | other | 2023-07-14 |  |  |
| [2023-07_celsius-lawsuits-ceo-arrest.yaml](other/2023-07_celsius-lawsuits-ceo-arrest.yaml) | other | 2023-07-13 |  |  |
| [2023-07_digitex-futures-ceo-to-pay-15-million-over-commodities-violations.yaml](other/2023-07_digitex-futures-ceo-to-pay-15-million-over-commodities-violations.yaml) | other | 2023-07-12 |  |  |
| [2023-07_rodeo-finance-hack.yaml](data-leak/2023-07_rodeo-finance-hack.yaml) | data-leak | 2023-07-11 |  |  |
| [2023-07_platypus-finance-hack-2.yaml](data-leak/2023-07_platypus-finance-hack-2.yaml) | data-leak | 2023-07-11 |  |  |
| [2023-07_optyfi-shuts-down.yaml](other/2023-07_optyfi-shuts-down.yaml) | other | 2023-07-11 |  |  |
| [2023-07_nft-phisher-charged-over-opensea-lookalike-scam.yaml](data-leak/2023-07_nft-phisher-charged-over-opensea-lookalike-scam.yaml) | data-leak | 2023-07-10 |  |  |
| [2023-07_algofi-announces-shutdown.yaml](other/2023-07_algofi-announces-shutdown.yaml) | other | 2023-07-10 |  |  |
| [2023-07_arkham-intelligence-intelligence-exchange.yaml](data-leak/2023-07_arkham-intelligence-intelligence-exchange.yaml) | data-leak | 2023-07-10 |  |  |
| [2023-07_arkham-intelligence-referral-program-exposes-user-emails.yaml](other/2023-07_arkham-intelligence-referral-program-exposes-user-emails.yaml) | other | 2023-07-10 |  |  |
| [2023-07_multichain-theft-3.yaml](data-leak/2023-07_multichain-theft-3.yaml) | data-leak | 2023-07-10 |  |  |
| [2023-07_arcadia-finance-exploit.yaml](data-leak/2023-07_arcadia-finance-exploit.yaml) | data-leak | 2023-07-09 |  |  |
| [2023-07_dubai-regulator-cracks-down-on-bitoasis.yaml](other/2023-07_dubai-regulator-cracks-down-on-bitoasis.yaml) | other | 2023-07-09 |  |  |
| [2023-07_gutter-cat-gang-twitter-compromise.yaml](data-leak/2023-07_gutter-cat-gang-twitter-compromise.yaml) | data-leak | 2023-07-07 |  |  |
| [2023-07_nftperp-blows-up.yaml](other/2023-07_nftperp-blows-up.yaml) | other | 2023-07-06 |  |  |
| [2023-07_decentralized-barnbridge-closes-up-shop-after-claiming-they-are-under-sec-investigation.yaml](other/2023-07_decentralized-barnbridge-closes-up-shop-after-claiming-they-are-under-sec-investigation.yaml) | other | 2023-07-06 |  |  |
| [2023-07_multichain-suspected-hack-2.yaml](data-leak/2023-07_multichain-suspected-hack-2.yaml) | data-leak | 2023-07-06 |  |  |
| [2023-07_hca-healthcare-11m-patients.yaml](data-leak/2023-07_hca-healthcare-11m-patients.yaml) | data-leak | 2023-07-05 |  |  |
| [2023-07_azukidao-exploit.yaml](data-leak/2023-07_azukidao-exploit.yaml) | data-leak | 2023-07-03 |  |  |
| [2023-07_lovemake-eth-wallet-drain.yaml](data-leak/2023-07_lovemake-eth-wallet-drain.yaml) | data-leak | 2023-07-03 |  |  |
| [2023-07_poly-network-hack-2.yaml](data-leak/2023-07_poly-network-hack-2.yaml) | data-leak | 2023-07-02 |  |  |
| [2023-07_encryption-ai-rug-pull.yaml](other/2023-07_encryption-ai-rug-pull.yaml) | other | 2023-07-02 |  |  |
| [2023-07_celik-motor-trade-joint-stock-company-mivento-it-services.yaml](supply-chain/2023-07_celik-motor-trade-joint-stock-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_vestel-mivento-it-services.yaml](supply-chain/2023-07_vestel-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_blue-cross-blue-shield-of-arizona-az-blue-cognizant-technology-solutio.yaml](supply-chain/2023-07_blue-cross-blue-shield-of-arizona-az-blue-cognizant-technology-solutio.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_toyota-turkey-marketing-and-sales-joint-stock-company-mivento-it-services.yaml](supply-chain/2023-07_toyota-turkey-marketing-and-sales-joint-stock-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_henrietta-johnson-medical-center-delaware-health-network.yaml](supply-chain/2023-07_henrietta-johnson-medical-center-delaware-health-network.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_lenders-choice-escrow-cashcall-inc.yaml](supply-chain/2023-07_lenders-choice-escrow-cashcall-inc.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_geberit-installation-systems-trade-limited-company-mivento-it-services.yaml](supply-chain/2023-07_geberit-installation-systems-trade-limited-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_vodafone-turkey-mivento-it-services.yaml](supply-chain/2023-07_vodafone-turkey-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_mais-motor-vehicles-manufacturing-and-sales-joint-stock-company-mivento-it-services.yaml](supply-chain/2023-07_mais-motor-vehicles-manufacturing-and-sales-joint-stock-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_postbank-majorel.yaml](supply-chain/2023-07_postbank-majorel.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_anadolu-isuzu-automotive-industry-and-trade-inc-mivento-it-services.yaml](supply-chain/2023-07_anadolu-isuzu-automotive-industry-and-trade-inc-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-07_dymocks-australia-836k.yaml](data-leak/2023-07_dymocks-australia-836k.yaml) | data-leak | 2023-07-01 |  |  |
| [2023-07_schneider-electric-industry-and-trade-joint-stock-company-mivento-it-services.yaml](supply-chain/2023-07_schneider-electric-industry-and-trade-joint-stock-company-mivento-it-services.yaml) | supply-chain | 2023-07-01 |  |  |
| [2023-06_kraken-ordered-to-turn-over-user-information-to-u-s-tax-investigators.yaml](other/2023-06_kraken-ordered-to-turn-over-user-information-to-u-s-tax-investigators.yaml) | other | 2023-06-30 |  |  |
| [2023-06_huobi-vulnerability.yaml](other/2023-06_huobi-vulnerability.yaml) | other | 2023-06-28 |  |  |
| [2023-06_cardinal-labs-shuts-down.yaml](other/2023-06_cardinal-labs-shuts-down.yaml) | other | 2023-06-28 |  |  |
| [2023-06_chibi-finance-rug-pull.yaml](other/2023-06_chibi-finance-rug-pull.yaml) | other | 2023-06-27 |  |  |
| [2023-06_themis-protocol-hack.yaml](data-leak/2023-06_themis-protocol-hack.yaml) | data-leak | 2023-06-27 |  |  |
| [2023-06_azuki-elementals-mint.yaml](other/2023-06_azuki-elementals-mint.yaml) | other | 2023-06-27 |  |  |
| [2023-06_ishan-seenar-sappideen-s-bitcoin-scam.yaml](data-leak/2023-06_ishan-seenar-sappideen-s-bitcoin-scam.yaml) | data-leak | 2023-06-26 |  |  |
| [2023-06_we-are-bamboo-alleged-embezzlement.yaml](other/2023-06_we-are-bamboo-alleged-embezzlement.yaml) | other | 2023-06-26 |  |  |
| [2023-06_prime-trust-insolvency.yaml](other/2023-06_prime-trust-insolvency.yaml) | other | 2023-06-26 |  |  |
| [2023-06_spirebit-crypto-scam.yaml](data-leak/2023-06_spirebit-crypto-scam.yaml) | data-leak | 2023-06-25 |  |  |
| [2023-06_inferno-drainer-thefts-on-polygon.yaml](data-leak/2023-06_inferno-drainer-thefts-on-polygon.yaml) | data-leak | 2023-06-23 |  |  |
| [2023-06_binance-ordered-to-halt-operations-in-belgium.yaml](other/2023-06_binance-ordered-to-halt-operations-in-belgium.yaml) | other | 2023-06-23 |  |  |
| [2023-06_prime-trust-is-insolvent.yaml](other/2023-06_prime-trust-is-insolvent.yaml) | other | 2023-06-22 |  |  |
| [2023-06_dog-noseprint-ponzi-scheme.yaml](data-leak/2023-06_dog-noseprint-ponzi-scheme.yaml) | data-leak | 2023-06-22 |  |  |
| [2023-06_alleged-scam-by-zachery-ty-bryan.yaml](other/2023-06_alleged-scam-by-zachery-ty-bryan.yaml) | other | 2023-06-22 |  |  |
| [2023-06_prime-trust-halts-withdrawals.yaml](other/2023-06_prime-trust-halts-withdrawals.yaml) | other | 2023-06-22 |  |  |
| [2023-06_elena-stolen-art.yaml](other/2023-06_elena-stolen-art.yaml) | other | 2023-06-21 |  |  |
| [2023-06_i-financial-times-i-alleges-crypto-zerowidthspace-com-is-trading-against-its-own-customers.yaml](other/2023-06_i-financial-times-i-alleges-crypto-zerowidthspace-com-is-trading-against-its-own-customers.yaml) | other | 2023-06-19 |  |  |
| [2023-06_financial-times-alleges-crypto-com-is-trading-against-its-own-customers.yaml](other/2023-06_financial-times-alleges-crypto-com-is-trading-against-its-own-customers.yaml) | other | 2023-06-19 |  |  |
| [2023-06_binance-cancels-registration-in-the-united-kingdom.yaml](other/2023-06_binance-cancels-registration-in-the-united-kingdom.yaml) | other | 2023-06-19 |  |  |
| [2023-06_wyre-finally-shuts-down.yaml](other/2023-06_wyre-finally-shuts-down.yaml) | other | 2023-06-16 |  |  |
| [2023-06_binance-exits-the-netherlands.yaml](other/2023-06_binance-exits-the-netherlands.yaml) | other | 2023-06-16 |  |  |
| [2023-06_machi-big-brother-sues-zachxbt.yaml](other/2023-06_machi-big-brother-sues-zachxbt.yaml) | other | 2023-06-16 |  |  |
| [2023-06_coinex-settlement.yaml](other/2023-06_coinex-settlement.yaml) | other | 2023-06-15 |  |  |
| [2023-06_binance-looks-to-exit-cyprus.yaml](other/2023-06_binance-looks-to-exit-cyprus.yaml) | other | 2023-06-15 |  |  |
| [2023-06_fpg-hack.yaml](data-leak/2023-06_fpg-hack.yaml) | data-leak | 2023-06-15 |  |  |
| [2023-06_abra-insolvency.yaml](other/2023-06_abra-insolvency.yaml) | other | 2023-06-15 |  |  |
| [2023-06_binance-us-cuts-staff-following-sec-lawsuit.yaml](other/2023-06_binance-us-cuts-staff-following-sec-lawsuit.yaml) | other | 2023-06-15 |  |  |
| [2023-06_delio-suspends-withdrawals.yaml](other/2023-06_delio-suspends-withdrawals.yaml) | other | 2023-06-14 |  |  |
| [2023-06_banq-bankruptcy.yaml](other/2023-06_banq-bankruptcy.yaml) | other | 2023-06-13 |  |  |
| [2023-06_haru-invest-suspends-withdrawals.yaml](other/2023-06_haru-invest-suspends-withdrawals.yaml) | other | 2023-06-13 |  |  |
| [2023-06_bnb-chain-team-prepares-to-step-in-to-prevent-venus-protocol-liquidation.yaml](data-leak/2023-06_bnb-chain-team-prepares-to-step-in-to-prevent-venus-protocol-liquidation.yaml) | data-leak | 2023-06-12 |  |  |
| [2023-06_atlantis-loans-exploit.yaml](data-leak/2023-06_atlantis-loans-exploit.yaml) | data-leak | 2023-06-12 |  |  |
| [2023-06_sturdy-finance-exploit.yaml](data-leak/2023-06_sturdy-finance-exploit.yaml) | data-leak | 2023-06-11 |  |  |
| [2023-06_tusd-depeg.yaml](other/2023-06_tusd-depeg.yaml) | other | 2023-06-10 |  |  |
| [2023-06_crypto-com-to-shut-down-institutional-trading-in-the-us.yaml](other/2023-06_crypto-com-to-shut-down-institutional-trading-in-the-us.yaml) | other | 2023-06-09 |  |  |
| [2023-06_cftc-awarded-summary-judgment-in-case-against-ooki-dao.yaml](other/2023-06_cftc-awarded-summary-judgment-in-case-against-ooki-dao.yaml) | other | 2023-06-09 |  |  |
| [2023-06_robinhood-to-delist-solana-cardano-polygon-tokens.yaml](other/2023-06_robinhood-to-delist-solana-cardano-polygon-tokens.yaml) | other | 2023-06-09 |  |  |
| [2023-06_sec-files-complaint-against-coinbase.yaml](other/2023-06_sec-files-complaint-against-coinbase.yaml) | other | 2023-06-06 |  |  |
| [2023-06_binance-discord-compromise.yaml](data-leak/2023-06_binance-discord-compromise.yaml) | data-leak | 2023-06-06 |  |  |
| [2023-06_sec-files-complaint-against-binance.yaml](other/2023-06_sec-files-complaint-against-binance.yaml) | other | 2023-06-05 |  |  |
| [2023-06_atomic-wallet-hacks.yaml](data-leak/2023-06_atomic-wallet-hacks.yaml) | data-leak | 2023-06-03 |  |  |
| [2023-06_tj-maxx-ipswitch-inc.yaml](supply-chain/2023-06_tj-maxx-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_majorel-ipswitch-inc.yaml](supply-chain/2023-06_majorel-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_vecino-health-centers-tx-ipswitch-inc.yaml](supply-chain/2023-06_vecino-health-centers-tx-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_pbi-research-services-pbi-ipswitch-inc.yaml](supply-chain/2023-06_pbi-research-services-pbi-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_australian-information-commissioner-oaic-hwl-ebsworth-lawyers.yaml](supply-chain/2023-06_australian-information-commissioner-oaic-hwl-ebsworth-lawyers.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_unsheth-exploit.yaml](data-leak/2023-06_unsheth-exploit.yaml) | data-leak | 2023-06-01 |  |  |
| [2023-06_oregon-driver-motor-vehicle-services-ipswitch-inc.yaml](supply-chain/2023-06_oregon-driver-motor-vehicle-services-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_southwest-airlines-pilot-credentials.yaml](supply-chain/2023-06_southwest-airlines-pilot-credentials.yaml) | supply-chain | 2023-06-01 |  |  |
| [2024-02_flax-typhoon-taiwan-botnet.yaml](other/2024-02_flax-typhoon-taiwan-botnet.yaml) | other | 2023-06-01 | Flax Typhoon botnet (Raptor T… |  |
| [2023-06_calpers-california-public-employees-retirement-system-pbi-research-services-pbi.yaml](supply-chain/2023-06_calpers-california-public-employees-retirement-system-pbi-research-services-pbi.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_coxhealth-intellihartx-llc.yaml](supply-chain/2023-06_coxhealth-intellihartx-llc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_the-new-york-city-department-of-education-nyc-doe-ipswitch-inc.yaml](supply-chain/2023-06_the-new-york-city-department-of-education-nyc-doe-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_exeter-finance-ncb-management-services-inc.yaml](supply-chain/2023-06_exeter-finance-ncb-management-services-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_dublin-airport-aon.yaml](supply-chain/2023-06_dublin-airport-aon.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-06_dhl-ipswitch-inc.yaml](supply-chain/2023-06_dhl-ipswitch-inc.yaml) | supply-chain | 2023-06-01 |  |  |
| [2023-05_binance-delists-privacycoins.yaml](other/2023-05_binance-delists-privacycoins.yaml) | other | 2023-05-31 |  |  |
| [2023-05_trust-reserve-formerly-cnhc-employees-arrested.yaml](other/2023-05_trust-reserve-formerly-cnhc-employees-arrested.yaml) | other | 2023-05-31 |  |  |
| [2023-05_binance-reportedly-begins-layoffs.yaml](other/2023-05_binance-reportedly-begins-layoffs.yaml) | other | 2023-05-31 |  |  |
| [2023-05_hopeexist1-nft-scam.yaml](data-leak/2023-05_hopeexist1-nft-scam.yaml) | data-leak | 2023-05-30 |  |  |
| [2023-05_bybit-exits-canada.yaml](other/2023-05_bybit-exits-canada.yaml) | other | 2023-05-30 |  |  |
| [2023-05_nfl-labor-union-is-out-almost-42-million-thanks-to-crypto-collapse.yaml](other/2023-05_nfl-labor-union-is-out-almost-42-million-thanks-to-crypto-collapse.yaml) | other | 2023-05-30 |  |  |
| [2023-05_moonpay-executives-pocketed-series-a-funding.yaml](other/2023-05_moonpay-executives-pocketed-series-a-funding.yaml) | other | 2023-05-30 |  |  |
| [2023-05_el-dorado-exchange-hack.yaml](data-leak/2023-05_el-dorado-exchange-hack.yaml) | data-leak | 2023-05-29 |  |  |
| [2023-05_bkex-halts-withdrawals.yaml](other/2023-05_bkex-halts-withdrawals.yaml) | other | 2023-05-29 |  |  |
| [2023-05_jimbos-protocol-exploit.yaml](data-leak/2023-05_jimbos-protocol-exploit.yaml) | data-leak | 2023-05-28 |  |  |
| [2023-05_welltok-moveit-8-5m-patients.yaml](supply-chain/2023-05_welltok-moveit-8-5m-patients.yaml) | supply-chain | 2023-05-27 | Cl0p ransomware | CVE-2023-34362 |
| [2023-05_malfunctioning-mev-bot.yaml](other/2023-05_malfunctioning-mev-bot.yaml) | other | 2023-05-27 |  |  |
| [2023-07_moveit-maximus.yaml](supply-chain/2023-07_moveit-maximus.yaml) | supply-chain | 2023-05-27 | LEMURLOOT web shell | CVE-2023-34362 |
| [2023-05_patricia-technologies-theft.yaml](data-leak/2023-05_patricia-technologies-theft.yaml) | data-leak | 2023-05-27 |  |  |
| [2023-05_moveit-transfer-clop.yaml](supply-chain/2023-05_moveit-transfer-clop.yaml) | supply-chain | 2023-05-27 | LEMURLOOT web shell | CVE-2023-34362, CVE-2023-35708 |
| [2023-05_unbanked-to-shut-down.yaml](other/2023-05_unbanked-to-shut-down.yaml) | other | 2023-05-26 |  |  |
| [2023-05_coinone-employees-admit-to-facts-in-bribery-case.yaml](other/2023-05_coinone-employees-admit-to-facts-in-bribery-case.yaml) | other | 2023-05-26 |  |  |
| [2023-05_dcg-shutters-tradeblock-subsidiary.yaml](other/2023-05_dcg-shutters-tradeblock-subsidiary.yaml) | other | 2023-05-26 |  |  |
| [2023-05_steve-aoki-twitter-compromise.yaml](data-leak/2023-05_steve-aoki-twitter-compromise.yaml) | data-leak | 2023-05-25 |  |  |
| [2023-05_multichain-malfunction.yaml](other/2023-05_multichain-malfunction.yaml) | other | 2023-05-24 |  |  |
| [2023-05_morgan-df-fintoch-exit-scam.yaml](data-leak/2023-05_morgan-df-fintoch-exit-scam.yaml) | data-leak | 2023-05-23 |  |  |
| [2023-05_cs-token-exploit.yaml](data-leak/2023-05_cs-token-exploit.yaml) | data-leak | 2023-05-23 |  |  |
| [2023-05_tornado-cash-dao-governance-attack.yaml](data-leak/2023-05_tornado-cash-dao-governance-attack.yaml) | data-leak | 2023-05-20 |  |  |
| [2023-05_bitlucky-collapse.yaml](other/2023-05_bitlucky-collapse.yaml) | other | 2023-05-20 |  |  |
| [2023-05_polygon-aave-bug.yaml](other/2023-05_polygon-aave-bug.yaml) | other | 2023-05-19 |  |  |
| [2023-05_inferno-drainer-phishing-service.yaml](data-leak/2023-05_inferno-drainer-phishing-service.yaml) | data-leak | 2023-05-19 |  |  |
| [2023-05_wdzd-swap-hack.yaml](data-leak/2023-05_wdzd-swap-hack.yaml) | data-leak | 2023-05-19 |  |  |
| [2023-05_coin-cafe-to-pay-restitution.yaml](other/2023-05_coin-cafe-to-pay-restitution.yaml) | other | 2023-05-18 |  |  |
| [2023-05_worldcoin-eyeball-theft.yaml](other/2023-05_worldcoin-eyeball-theft.yaml) | other | 2023-05-18 |  |  |
| [2023-05_grumpy-cat-cease-and-desist.yaml](other/2023-05_grumpy-cat-cease-and-desist.yaml) | other | 2023-05-18 |  |  |
| [2023-05_swaprum-rug-pull.yaml](other/2023-05_swaprum-rug-pull.yaml) | other | 2023-05-18 |  |  |
| [2023-05_fabric-cfo-funds-misappropriation.yaml](other/2023-05_fabric-cfo-funds-misappropriation.yaml) | other | 2023-05-17 |  |  |
| [2023-05_hitbtc-phishing-website.yaml](data-leak/2023-05_hitbtc-phishing-website.yaml) | data-leak | 2023-05-15 |  |  |
| [2023-05_storm-0558-microsoft-exchange.yaml](other/2023-05_storm-0558-microsoft-exchange.yaml) | other | 2023-05-15 |  |  |
| [2023-05_south-korean-legislator-kim-nam-kuk.yaml](other/2023-05_south-korean-legislator-kim-nam-kuk.yaml) | other | 2023-05-14 |  |  |
| [2023-05_mecha-fight-club-paused.yaml](other/2023-05_mecha-fight-club-paused.yaml) | other | 2023-05-13 |  |  |
| [2023-05_i-mecha-fight-club-i-paused.yaml](other/2023-05_i-mecha-fight-club-i-paused.yaml) | other | 2023-05-13 |  |  |
| [2023-05_fractional-nft-ownership-platform-tessera-shuts-down.yaml](other/2023-05_fractional-nft-ownership-platform-tessera-shuts-down.yaml) | other | 2023-05-12 |  |  |
| [2023-05_bakkt-delists-25-of-36-crypto-tokens-on-newly-acquired-apex-crypto.yaml](other/2023-05_bakkt-delists-25-of-36-crypto-tokens-on-newly-acquired-apex-crypto.yaml) | other | 2023-05-12 |  |  |
| [2023-05_stanford-university-ransomware-27k.yaml](data-leak/2023-05_stanford-university-ransomware-27k.yaml) | data-leak | 2023-05-12 | Akira |  |
| [2023-05_binance-exits-canada.yaml](other/2023-05_binance-exits-canada.yaml) | other | 2023-05-12 |  |  |
| [2023-05_aragon-dao-faces-governance-crisis.yaml](other/2023-05_aragon-dao-faces-governance-crisis.yaml) | other | 2023-05-11 |  |  |
| [2023-05_bittrex-files-for-bankruptcy.yaml](other/2023-05_bittrex-files-for-bankruptcy.yaml) | other | 2023-05-08 |  |  |
| [2023-05_everledger-collapses.yaml](other/2023-05_everledger-collapses.yaml) | other | 2023-05-08 |  |  |
| [2023-05_ethereum-user-pays-more-than-100-000-in-fees.yaml](other/2023-05_ethereum-user-pays-more-than-100-000-in-fees.yaml) | other | 2023-05-07 |  |  |
| [2023-05_deus-finance-hack-35-3.yaml](data-leak/2023-05_deus-finance-hack-35-3.yaml) | data-leak | 2023-05-06 |  |  |
| [2023-05_deus-finance-hack-3.yaml](data-leak/2023-05_deus-finance-hack-3.yaml) | data-leak | 2023-05-06 |  |  |
| [2023-05_xirtam-rug-pull.yaml](other/2023-05_xirtam-rug-pull.yaml) | other | 2023-05-04 |  |  |
| [2023-05_nate-chastain-conviction.yaml](other/2023-05_nate-chastain-conviction.yaml) | other | 2023-05-03 |  |  |
| [2023-05_wallstreetbets-coin-rugpull.yaml](other/2023-05_wallstreetbets-coin-rugpull.yaml) | other | 2023-05-03 |  |  |
| [2023-05_okx-withdrawal-limit-change.yaml](other/2023-05_okx-withdrawal-limit-change.yaml) | other | 2023-05-02 |  |  |
| [2023-05_paramount-health-care-nationsbenefits-holding-llc.yaml](supply-chain/2023-05_paramount-health-care-nationsbenefits-holding-llc.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_cornerstone-home-lending-unknown.yaml](supply-chain/2023-05_cornerstone-home-lending-unknown.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_poloniex-ofac-settlement.yaml](other/2023-05_poloniex-ofac-settlement.yaml) | other | 2023-05-01 |  |  |
| [2023-05_storybook-brawl-shuts-down.yaml](other/2023-05_storybook-brawl-shuts-down.yaml) | other | 2023-05-01 |  |  |
| [2023-05_kibble-equipment-razor-consulting-solutions.yaml](supply-chain/2023-05_kibble-equipment-razor-consulting-solutions.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_intel-micro-star-international-msi.yaml](supply-chain/2023-05_intel-micro-star-international-msi.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_coles-latitude-financial-services.yaml](supply-chain/2023-05_coles-latitude-financial-services.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_whitman-college-brightline-health.yaml](supply-chain/2023-05_whitman-college-brightline-health.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_webster-bank-guardian-analytics-inc.yaml](supply-chain/2023-05_webster-bank-guardian-analytics-inc.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_vcu-health-system-credit-control-corporation.yaml](supply-chain/2023-05_vcu-health-system-credit-control-corporation.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_cz-smacks-down-justin-sun-for-trying-to-game-sui-airdrop.yaml](other/2023-05_cz-smacks-down-justin-sun-for-trying-to-game-sui-airdrop.yaml) | other | 2023-05-01 |  |  |
| [2023-05_iowa-medicaid-telligen-inc.yaml](supply-chain/2023-05_iowa-medicaid-telligen-inc.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_discord-zendesk.yaml](supply-chain/2023-05_discord-zendesk.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_stanford-university-brightline-health.yaml](supply-chain/2023-05_stanford-university-brightline-health.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_fermanagh-and-omagh-district-council-evide-impact-limited.yaml](supply-chain/2023-05_fermanagh-and-omagh-district-council-evide-impact-limited.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_south-baldwin-regional-medical-center-community-health-systems.yaml](supply-chain/2023-05_south-baldwin-regional-medical-center-community-health-systems.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_medicare-medicaid-services-cms-palmetto-gba.yaml](supply-chain/2023-05_medicare-medicaid-services-cms-palmetto-gba.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_queensway-carleton-hospital-aetonix-systems-inc.yaml](supply-chain/2023-05_queensway-carleton-hospital-aetonix-systems-inc.yaml) | supply-chain | 2023-05-01 |  |  |
| [2023-05_i-storybook-brawl-i-shuts-down.yaml](other/2023-05_i-storybook-brawl-i-shuts-down.yaml) | other | 2023-05-01 |  |  |
| [2023-05_level-finance-exploited.yaml](data-leak/2023-05_level-finance-exploited.yaml) | data-leak | 2023-05-01 |  |  |
| [2023-04_permit-phishing-scams.yaml](data-leak/2023-04_permit-phishing-scams.yaml) | data-leak | 2023-04-30 |  |  |
| [2023-04_0vix-exploit.yaml](data-leak/2023-04_0vix-exploit.yaml) | data-leak | 2023-04-29 |  |  |
| [2023-10_23andme-credential-stuffing.yaml](data-leak/2023-10_23andme-credential-stuffing.yaml) | credential-theft | 2023-04-29 |  |  |
| [2023-04_hwl-ebsworth-alphv-blackcat.yaml](ransomware/2023-04_hwl-ebsworth-alphv-blackcat.yaml) | ransomware | 2023-04-28 | ALPHV/BlackCat ransomware |  |
| [2023-04_bitcoin-theft-against-russia.yaml](data-leak/2023-04_bitcoin-theft-against-russia.yaml) | data-leak | 2023-04-27 |  |  |
| [2023-04_steynberg-cftc-fine.yaml](other/2023-04_steynberg-cftc-fine.yaml) | other | 2023-04-27 |  |  |
| [2023-04_fbi-raids-home-of-ftx-exec-ryan-salame.yaml](other/2023-04_fbi-raids-home-of-ftx-exec-ryan-salame.yaml) | other | 2023-04-27 |  |  |
| [2023-04_bit4you-suspends-activities.yaml](other/2023-04_bit4you-suspends-activities.yaml) | other | 2023-04-27 |  |  |
| [2023-04_at-amp-t-customer-wallet-compromises.yaml](data-leak/2023-04_at-amp-t-customer-wallet-compromises.yaml) | data-leak | 2023-04-26 |  |  |
| [2023-04_at-t-customer-wallet-compromises.yaml](data-leak/2023-04_at-t-customer-wallet-compromises.yaml) | data-leak | 2023-04-26 |  |  |
| [2023-04_merlin-theft.yaml](data-leak/2023-04_merlin-theft.yaml) | data-leak | 2023-04-26 |  |  |
| [2023-04_coinloan-suspends-withdrawals.yaml](other/2023-04_coinloan-suspends-withdrawals.yaml) | other | 2023-04-25 |  |  |
| [2023-04_binance-cancels-voyager-acquisition.yaml](other/2023-04_binance-cancels-voyager-acquisition.yaml) | other | 2023-04-25 |  |  |
| [2023-04_ordinals-finance-rug-pull.yaml](other/2023-04_ordinals-finance-rug-pull.yaml) | other | 2023-04-24 |  |  |
| [2023-04_i-plush-i-nft-scam.yaml](other/2023-04_i-plush-i-nft-scam.yaml) | other | 2023-04-23 |  |  |
| [2023-04_plush-nft-scam.yaml](other/2023-04_plush-nft-scam.yaml) | other | 2023-04-23 |  |  |
| [2023-04_unisat-is-immediately-exploited.yaml](data-leak/2023-04_unisat-is-immediately-exploited.yaml) | data-leak | 2023-04-23 |  |  |
| [2023-04_ukrainedao-allegedly-misappropriates-funds.yaml](other/2023-04_ukrainedao-allegedly-misappropriates-funds.yaml) | other | 2023-04-21 |  |  |
| [2023-04_blur-bid-acceptance-bug.yaml](other/2023-04_blur-bid-acceptance-bug.yaml) | other | 2023-04-21 |  |  |
| [2024-04_webtpa-health-insurance.yaml](data-leak/2024-04_webtpa-health-insurance.yaml) | data-leak | 2023-04-18 |  |  |
| [2023-04_wallet-draining-operation.yaml](data-leak/2023-04_wallet-draining-operation.yaml) | data-leak | 2023-04-18 |  |  |
| [2023-04_rebase-co-founders-lawsuit.yaml](other/2023-04_rebase-co-founders-lawsuit.yaml) | other | 2023-04-17 |  |  |
| [2023-04_sec-charges-bittrex.yaml](other/2023-04_sec-charges-bittrex.yaml) | other | 2023-04-17 |  |  |
| [2023-04_hundred-finance-exploit.yaml](data-leak/2023-04_hundred-finance-exploit.yaml) | data-leak | 2023-04-15 |  |  |
| [2023-04_bitrue-hack.yaml](data-leak/2023-04_bitrue-hack.yaml) | data-leak | 2023-04-14 |  |  |
| [2023-04_franklin-claims-to-have-been-scammed.yaml](data-leak/2023-04_franklin-claims-to-have-been-scammed.yaml) | data-leak | 2023-04-13 |  |  |
| [2023-04_yearn-finance-hack-2.yaml](data-leak/2023-04_yearn-finance-hack-2.yaml) | data-leak | 2023-04-13 |  |  |
| [2023-04_ren-protocol-transfers-all-assets-to-ftx-bankruptcy-team.yaml](other/2023-04_ren-protocol-transfers-all-assets-to-ftx-bankruptcy-team.yaml) | other | 2023-04-12 |  |  |
| [2023-04_nicole-behnam-pumps-and-dumps.yaml](other/2023-04_nicole-behnam-pumps-and-dumps.yaml) | other | 2023-04-12 |  |  |
| [2023-04_goblintown-changes-nfts-to-middle-finger.yaml](other/2023-04_goblintown-changes-nfts-to-middle-finger.yaml) | other | 2023-04-11 |  |  |
| [2023-04_gdac-hack.yaml](data-leak/2023-04_gdac-hack.yaml) | data-leak | 2023-04-10 |  |  |
| [2023-04_terraport-finance-hack.yaml](data-leak/2023-04_terraport-finance-hack.yaml) | data-leak | 2023-04-10 |  |  |
| [2023-04_niantic-shutters-its-web3-project.yaml](other/2023-04_niantic-shutters-its-web3-project.yaml) | other | 2023-04-10 |  |  |
| [2023-04_trader-loses-14-377-ape-61-000-when-they-sell-their-bored-ape.yaml](other/2023-04_trader-loses-14-377-ape-61-000-when-they-sell-their-bored-ape.yaml) | other | 2023-04-09 |  |  |
| [2023-04_0xsifu-loses-3-3-million-to-sushiswap-hack.yaml](data-leak/2023-04_0xsifu-loses-3-3-million-to-sushiswap-hack.yaml) | data-leak | 2023-04-08 |  |  |
| [2023-04_dydx-exchange-announces-it-will-shut-down-canadian-operations.yaml](other/2023-04_dydx-exchange-announces-it-will-shut-down-canadian-operations.yaml) | other | 2023-04-07 |  |  |
| [2023-04_dez-bryant-s-bored-ape-stolen.yaml](data-leak/2023-04_dez-bryant-s-bored-ape-stolen.yaml) | data-leak | 2023-04-07 |  |  |
| [2023-04_sphere-3d-and-gryphon-digital-mining-dispute.yaml](data-leak/2023-04_sphere-3d-and-gryphon-digital-mining-dispute.yaml) | data-leak | 2023-04-07 |  |  |
| [2023-04_gemholic-gets-funds-stuck.yaml](other/2023-04_gemholic-gets-funds-stuck.yaml) | other | 2023-04-06 |  |  |
| [2023-04_someone-accidentally-spends-100-eth-185-000-on-a-free-nft.yaml](other/2023-04_someone-accidentally-spends-100-eth-185-000-on-a-free-nft.yaml) | other | 2023-04-05 |  |  |
| [2023-04_binance-closes-its-derivatives-arm-in-australia.yaml](other/2023-04_binance-closes-its-derivatives-arm-in-australia.yaml) | other | 2023-04-05 |  |  |
| [2023-04_ncb-management-services.yaml](data-leak/2023-04_ncb-management-services.yaml) | data-leak | 2023-04-04 |  |  |
| [2023-04_paxful-abruptly-shuts-down.yaml](other/2023-04_paxful-abruptly-shuts-down.yaml) | other | 2023-04-04 |  |  |
| [2023-04_sentiment-hack.yaml](data-leak/2023-04_sentiment-hack.yaml) | data-leak | 2023-04-04 |  |  |
| [2023-04_theft-from-mev-bot.yaml](data-leak/2023-04_theft-from-mev-bot.yaml) | data-leak | 2023-04-03 |  |  |
| [2023-04_rumor-tweet-by-crypto-influencer-causes-bnb-and-bitcoin-sell-off.yaml](other/2023-04_rumor-tweet-by-crypto-influencer-causes-bnb-and-bitcoin-sell-off.yaml) | other | 2023-04-03 |  |  |
| [2023-04_arbitrum-dao-vote-fiasco.yaml](other/2023-04_arbitrum-dao-vote-fiasco.yaml) | other | 2023-04-02 |  |  |
| [2023-04_allbridge-hack.yaml](data-leak/2023-04_allbridge-hack.yaml) | data-leak | 2023-04-01 |  |  |
| [2023-04_dynasty-loop-nft-games-studio-owes-millions.yaml](other/2023-04_dynasty-loop-nft-games-studio-owes-millions.yaml) | other | 2023-04-01 |  |  |
| [2023-04_iowa-department-of-health-and-human-services-iowa-medicaid-enterprise-iowa-hhs-ime-independent-living-systems.yaml](supply-chain/2023-04_iowa-department-of-health-and-human-services-iowa-medicaid-enterprise-iowa-hhs-ime-independent-living-systems.yaml) | supply-chain | 2023-04-01 |  |  |
| [2023-06_hwl-ebsworth-alphv-australia.yaml](data-leak/2023-06_hwl-ebsworth-alphv-australia.yaml) | data-leak | 2023-04-01 | ALPHV/BlackCat ransomware |  |
| [2023-03_arbitrum-airdrop-scams.yaml](data-leak/2023-03_arbitrum-airdrop-scams.yaml) | data-leak | 2023-03-31 |  |  |
| [2023-03_bittrex-crypto-exchange-to-close-us-operations.yaml](other/2023-03_bittrex-crypto-exchange-to-close-us-operations.yaml) | other | 2023-03-31 |  |  |
| [2023-03_sec-shuts-down-beaxy-crypto-exchange.yaml](other/2023-03_sec-shuts-down-beaxy-crypto-exchange.yaml) | other | 2023-03-29 |  |  |
| [2023-03_safemoon-exploit.yaml](data-leak/2023-03_safemoon-exploit.yaml) | data-leak | 2023-03-28 |  |  |
| [2023-03_cftc-sues-binance-and-ceo-changpeng-zhao.yaml](other/2023-03_cftc-sues-binance-and-ceo-changpeng-zhao.yaml) | other | 2023-03-27 |  |  |
| [2023-02_pja-concentra-healthcare.yaml](data-leak/2023-02_pja-concentra-healthcare.yaml) | data-leak | 2023-03-27 |  |  |
| [2023-03_kokomo-finance-rug-pull.yaml](data-leak/2023-03_kokomo-finance-rug-pull.yaml) | data-leak | 2023-03-26 |  |  |
| [2023-03_latest-sotheby-s-nft-sale-is-decidedly-tepid.yaml](other/2023-03_latest-sotheby-s-nft-sale-is-decidedly-tepid.yaml) | other | 2023-03-24 |  |  |
| [2023-03_collector-accidentally-burns-their-123-000-nft.yaml](other/2023-03_collector-accidentally-burns-their-123-000-nft.yaml) | other | 2023-03-24 |  |  |
| [2023-03_us-prosecutors-file-criminal-charges-against-do-kwon.yaml](other/2023-03_us-prosecutors-file-criminal-charges-against-do-kwon.yaml) | other | 2023-03-23 |  |  |
| [2023-03_terra-luna-founder-do-kwon-arrested.yaml](other/2023-03_terra-luna-founder-do-kwon-arrested.yaml) | other | 2023-03-23 |  |  |
| [2023-03_justin-sun-charged-with-offering-unregistered-securities.yaml](other/2023-03_justin-sun-charged-with-offering-unregistered-securities.yaml) | other | 2023-03-22 |  |  |
| [2023-03_sec-sends-a-wells-notice-to-coinbase.yaml](other/2023-03_sec-sends-a-wells-notice-to-coinbase.yaml) | other | 2023-03-22 |  |  |
| [2023-03_lindsay-lohan-jake-paul-and-other-celebrities-charged-for-illegally-touting-justin-sun-s-tokens.yaml](other/2023-03_lindsay-lohan-jake-paul-and-other-celebrities-charged-for-illegally-touting-justin-sun-s-tokens.yaml) | other | 2023-03-22 |  |  |
| [2023-03_capita-black-basta.yaml](ransomware/2023-03_capita-black-basta.yaml) | ransomware | 2023-03-22 | Black Basta ransomware |  |
| [2023-03_kraken-to-suspend-ach-transfers-after-silvergate-collapse.yaml](other/2023-03_kraken-to-suspend-ach-transfers-after-silvergate-collapse.yaml) | other | 2023-03-22 |  |  |
| [2023-03_spankpay-crypto-porn-payment-service-shuts-down.yaml](other/2023-03_spankpay-crypto-porn-payment-service-shuts-down.yaml) | other | 2023-03-20 |  |  |
| [2023-03_openai-chatgpt-redis-bug.yaml](data-leak/2023-03_openai-chatgpt-redis-bug.yaml) | data-leak | 2023-03-20 |  |  |
| [2023-03_general-bytes-bitcoin-atm-hack.yaml](data-leak/2023-03_general-bytes-bitcoin-atm-hack.yaml) | data-leak | 2023-03-18 |  |  |
| [2023-03_thwarted-hacker-asks-crypto-security-firm-to-reimburse-their-gas-fees.yaml](data-leak/2023-03_thwarted-hacker-asks-crypto-security-firm-to-reimburse-their-gas-fees.yaml) | data-leak | 2023-03-17 |  |  |
| [2023-03_iearn-bot-scam.yaml](data-leak/2023-03_iearn-bot-scam.yaml) | data-leak | 2023-03-17 |  |  |
| [2023-03_3cx-desktop-app.yaml](supply-chain/2023-03_3cx-desktop-app.yaml) | supply-chain | 2023-03-16 | SUDDENICON downloader / ICONI… | CVE-2023-29059 |
| [2023-03_latitude-financial.yaml](data-leak/2023-03_latitude-financial.yaml) | data-leak | 2023-03-16 |  |  |
| [2023-03_international-law-enforcement-agencies-shut-down-chipmixer.yaml](other/2023-03_international-law-enforcement-agencies-shut-down-chipmixer.yaml) | other | 2023-03-15 |  |  |
| [2023-03_phishers-take-advantage-of-fears-surrounding-the-usdc-de-peg.yaml](data-leak/2023-03_phishers-take-advantage-of-fears-surrounding-the-usdc-de-peg.yaml) | data-leak | 2023-03-14 |  |  |
| [2023-03_euler-finance-hack.yaml](data-leak/2023-03_euler-finance-hack.yaml) | data-leak | 2023-03-13 |  |  |
| [2023-03_meta-ends-support-for-nfts.yaml](other/2023-03_meta-ends-support-for-nfts.yaml) | other | 2023-03-13 |  |  |
| [2023-03_euler-finance-contagion.yaml](data-leak/2023-03_euler-finance-contagion.yaml) | data-leak | 2023-03-13 |  |  |
| [2023-03_pharmerica-money-message.yaml](ransomware/2023-03_pharmerica-money-message.yaml) | ransomware | 2023-03-12 | Money Message ransomware |  |
| [2023-03_regulators-shut-down-crypto-friendly-signature-bank.yaml](other/2023-03_regulators-shut-down-crypto-friendly-signature-bank.yaml) | other | 2023-03-12 |  |  |
| [2023-03_peopledao-theft.yaml](data-leak/2023-03_peopledao-theft.yaml) | data-leak | 2023-03-11 |  |  |
| [2023-03_usdc-loses-peg-to-the-dollar.yaml](other/2023-03_usdc-loses-peg-to-the-dollar.yaml) | other | 2023-03-10 |  |  |
| [2023-03_bankrupt-blockfi-has-227-million-at-collapsed-silicon-valley-bank.yaml](other/2023-03_bankrupt-blockfi-has-227-million-at-collapsed-silicon-valley-bank.yaml) | other | 2023-03-10 |  |  |
| [2023-03_coinbase-pauses-redemptions-of-usdc-for-dollars.yaml](other/2023-03_coinbase-pauses-redemptions-of-usdc-for-dollars.yaml) | other | 2023-03-10 |  |  |
| [2023-03_silicon-valley-bank-collapse-causes-crypto-contagion-concerns.yaml](other/2023-03_silicon-valley-bank-collapse-causes-crypto-contagion-concerns.yaml) | other | 2023-03-10 |  |  |
| [2023-03_huobi-token-flash-crashes.yaml](other/2023-03_huobi-token-flash-crashes.yaml) | other | 2023-03-10 |  |  |
| [2023-03_kyber-bug.yaml](other/2023-03_kyber-bug.yaml) | other | 2023-03-10 |  |  |
| [2023-03_blockchain-com-shutters-asset-management-arm.yaml](other/2023-03_blockchain-com-shutters-asset-management-arm.yaml) | other | 2023-03-09 |  |  |
| [2023-03_hedera-network-halts-after-exploit.yaml](data-leak/2023-03_hedera-network-halts-after-exploit.yaml) | data-leak | 2023-03-09 |  |  |
| [2023-03_new-york-attorney-general-sues-kucoin.yaml](other/2023-03_new-york-attorney-general-sues-kucoin.yaml) | other | 2023-03-09 |  |  |
| [2023-03_dc-health-link-congress-breach.yaml](data-leak/2023-03_dc-health-link-congress-breach.yaml) | data-leak | 2023-03-08 |  |  |
| [2023-03_gemini-reportedly-loses-banking-with-jp-morgan.yaml](other/2023-03_gemini-reportedly-loses-banking-with-jp-morgan.yaml) | other | 2023-03-08 |  |  |
| [2023-03_silvergate-bank-collapses.yaml](other/2023-03_silvergate-bank-collapses.yaml) | other | 2023-03-08 |  |  |
| [2023-03_togg-announces-and-then-cancels-nft-presale.yaml](other/2023-03_togg-announces-and-then-cancels-nft-presale.yaml) | other | 2023-03-08 |  |  |
| [2023-03_lido-token-price-tanks-after-podcaster-spreads-inaccurate-rumor-of-wells-notice.yaml](other/2023-03_lido-token-price-tanks-after-podcaster-spreads-inaccurate-rumor-of-wells-notice.yaml) | other | 2023-03-03 |  |  |
| [2023-03_wsj-alleges-tether-and-related-companies-used-falsified-documents-to-obtain-banking.yaml](other/2023-03_wsj-alleges-tether-and-related-companies-used-falsified-documents-to-obtain-banking.yaml) | other | 2023-03-03 |  |  |
| [2023-03_silvergate-crypto-focused-bank-faces-crisis.yaml](other/2023-03_silvergate-crypto-focused-bank-faces-crisis.yaml) | other | 2023-03-02 |  |  |
| [2023-03_ferrari-customer-data-breach.yaml](data-leak/2023-03_ferrari-customer-data-breach.yaml) | data-leak | 2023-03-01 |  |  |
| [2023-03_national-basketball-association-unknown.yaml](supply-chain/2023-03_national-basketball-association-unknown.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_netherlands-enterprise-agency-rvo-nebu-bv.yaml](supply-chain/2023-03_netherlands-enterprise-agency-rvo-nebu-bv.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_bitbns-hack-disclosure.yaml](data-leak/2023-03_bitbns-hack-disclosure.yaml) | data-leak | 2023-03-01 |  |  |
| [2023-03_developers-accuse-binance-of-stealing-their-hackathon-idea-after-binance-launches-similar-product.yaml](other/2023-03_developers-accuse-binance-of-stealing-their-hackathon-idea-after-binance-launches-similar-product.yaml) | other | 2023-03-01 |  |  |
| [2023-03_spacex-maximum-industries.yaml](supply-chain/2023-03_spacex-maximum-industries.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_uber-genova-burns.yaml](supply-chain/2023-03_uber-genova-burns.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_cornell-university-ithaca-college-virginia-tech-university-suny-oswego-colorado-state-university-loyola-university-chicago-and-mcmaster-university-audienceview.yaml](supply-chain/2023-03_cornell-university-ithaca-college-virginia-tech-university-suny-oswego-colorado-state-university-loyola-university-chicago-and-mcmaster-university-audienceview.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-03_at-t-unknown.yaml](supply-chain/2023-03_at-t-unknown.yaml) | supply-chain | 2023-03-01 |  |  |
| [2023-02_nishad-singh-agrees-to-cooperate-against-sbf.yaml](other/2023-02_nishad-singh-agrees-to-cooperate-against-sbf.yaml) | other | 2023-02-28 |  |  |
| [2023-03_orrick-herrington-law-firm.yaml](data-leak/2023-03_orrick-herrington-law-firm.yaml) | data-leak | 2023-02-28 | SilentRansom/Luna Moth |  |
| [2023-02_algorand-wallet-drains.yaml](data-leak/2023-02_algorand-wallet-drains.yaml) | data-leak | 2023-02-27 |  |  |
| [2023-02_launchzone-and-dungeonswap-hacked.yaml](data-leak/2023-02_launchzone-and-dungeonswap-hacked.yaml) | data-leak | 2023-02-27 |  |  |
| [2023-02_hideyoapes-wallet-drain.yaml](data-leak/2023-02_hideyoapes-wallet-drain.yaml) | data-leak | 2023-02-26 |  |  |
| [2023-02_solana-requires-a-restart.yaml](other/2023-02_solana-requires-a-restart.yaml) | other | 2023-02-25 |  |  |
| [2023-02_jump-crypto-recovers-wormhole-funds.yaml](other/2023-02_jump-crypto-recovers-wormhole-funds.yaml) | other | 2023-02-24 |  |  |
| [2023-02_sam-bankman-fried-indicted-on-four-new-charges-in-criminal-case.yaml](other/2023-02_sam-bankman-fried-indicted-on-four-new-charges-in-criminal-case.yaml) | other | 2023-02-23 |  |  |
| [2023-02_dish-network-black-basta.yaml](ransomware/2023-02_dish-network-black-basta.yaml) | ransomware | 2023-02-23 | Black Basta ransomware |  |
| [2023-02_dish-network-blackbasta.yaml](ransomware/2023-02_dish-network-blackbasta.yaml) | ransomware | 2023-02-23 | Black Basta ransomware |  |
| [2023-02_phoenix-community-capital-vanishes.yaml](other/2023-02_phoenix-community-capital-vanishes.yaml) | other | 2023-02-23 |  |  |
| [2023-02_metroverse-blockchain-game-implodes.yaml](other/2023-02_metroverse-blockchain-game-implodes.yaml) | other | 2023-02-23 |  |  |
| [2023-02_wazirx-closes-nft-marketplace.yaml](other/2023-02_wazirx-closes-nft-marketplace.yaml) | other | 2023-02-22 |  |  |
| [2023-02_canadian-regulators-tighten-rules-for-crypto-exchanges.yaml](other/2023-02_canadian-regulators-tighten-rules-for-crypto-exchanges.yaml) | other | 2023-02-22 |  |  |
| [2023-02_friendsies-rug-pull.yaml](other/2023-02_friendsies-rug-pull.yaml) | other | 2023-02-21 |  |  |
| [2023-02_galois-capital-shuts-down.yaml](other/2023-02_galois-capital-shuts-down.yaml) | other | 2023-02-20 |  |  |
| [2023-02_paul-pierce-to-pay-1-4-million-fine-over-undisclosed-touting.yaml](other/2023-02_paul-pierce-to-pay-1-4-million-fine-over-undisclosed-touting.yaml) | other | 2023-02-17 |  |  |
| [2023-02_dexible-hack.yaml](data-leak/2023-02_dexible-hack.yaml) | data-leak | 2023-02-17 |  |  |
| [2023-02_platypus-usd-exploit.yaml](data-leak/2023-02_platypus-usd-exploit.yaml) | data-leak | 2023-02-16 |  |  |
| [2023-02_loyalist-phishing-scammer.yaml](data-leak/2023-02_loyalist-phishing-scammer.yaml) | data-leak | 2023-02-16 |  |  |
| [2023-02_sec-files-fraud-charges-against-do-kwon.yaml](other/2023-02_sec-files-fraud-charges-against-do-kwon.yaml) | other | 2023-02-16 |  |  |
| [2023-02_fdic-demands-cex-io-stop-claiming-it-s-fdic-insured.yaml](other/2023-02_fdic-demands-cex-io-stop-claiming-it-s-fdic-insured.yaml) | other | 2023-02-15 |  |  |
| [2023-02_fart-noise-reportedly-sells-for-280-000.yaml](other/2023-02_fart-noise-reportedly-sells-for-280-000.yaml) | other | 2023-02-15 |  |  |
| [2023-02_south-korean-authorities-issue-arrest-warrant-to-ceo-of-tmon.yaml](other/2023-02_south-korean-authorities-issue-arrest-warrant-to-ceo-of-tmon.yaml) | other | 2023-02-15 |  |  |
| [2023-03_cfpb-employee-data-emailed-personal-account.yaml](data-leak/2023-03_cfpb-employee-data-emailed-personal-account.yaml) | data-leak | 2023-02-14 |  |  |
| [2023-02_paxos-ordered-to-stop-minting-binance-usd-stablecoin.yaml](other/2023-02_paxos-ordered-to-stop-minting-binance-usd-stablecoin.yaml) | other | 2023-02-13 |  |  |
| [2023-02_dforce-network-hack.yaml](data-leak/2023-02_dforce-network-hack.yaml) | data-leak | 2023-02-13 |  |  |
| [2023-02_kraken-ends-staking-pays-30-million-in-settlement-with-u-s-sec.yaml](other/2023-02_kraken-ends-staking-pays-30-million-in-settlement-with-u-s-sec.yaml) | other | 2023-02-09 |  |  |
| [2023-02_localbitcoins-to-shut-down.yaml](other/2023-02_localbitcoins-to-shut-down.yaml) | other | 2023-02-09 |  |  |
| [2023-02_paxos-faces-investigation-over-stablecoin-offerings.yaml](other/2023-02_paxos-faces-investigation-over-stablecoin-offerings.yaml) | other | 2023-02-09 |  |  |
| [2023-02_umami-finance-rug-pull.yaml](data-leak/2023-02_umami-finance-rug-pull.yaml) | data-leak | 2023-02-09 |  |  |
| [2023-02_metabirkins-creator-loses-trademark-infringement-lawsuit.yaml](other/2023-02_metabirkins-creator-loses-trademark-infringement-lawsuit.yaml) | other | 2023-02-08 |  |  |
| [2023-02_dookey-dash-game-tournament-ends-amidst-allegations-of-widespread-cheating.yaml](other/2023-02_dookey-dash-game-tournament-ends-amidst-allegations-of-widespread-cheating.yaml) | other | 2023-02-08 |  |  |
| [2023-02_coin-cloud-bankruptcy.yaml](other/2023-02_coin-cloud-bankruptcy.yaml) | other | 2023-02-07 |  |  |
| [2023-02_webaverse-theft.yaml](data-leak/2023-02_webaverse-theft.yaml) | data-leak | 2023-02-06 |  |  |
| [2023-02_binance-suspends-usd-bank-transfers.yaml](other/2023-02_binance-suspends-usd-bank-transfers.yaml) | other | 2023-02-06 |  |  |
| [2023-02_reddit-blackcat.yaml](data-leak/2023-02_reddit-blackcat.yaml) | data-leak | 2023-02-05 |  |  |
| [2023-02_logan-paul-slapped-with-a-class-action-over-cryptozoo-rugpull.yaml](other/2023-02_logan-paul-slapped-with-a-class-action-over-cryptozoo-rugpull.yaml) | other | 2023-02-03 |  |  |
| [2023-02_orion-protocol-hack.yaml](data-leak/2023-02_orion-protocol-hack.yaml) | data-leak | 2023-02-02 |  |  |
| [2023-02_applied-materials-rise-interactive.yaml](supply-chain/2023-02_applied-materials-rise-interactive.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_sling-tv-dish-network-corporation.yaml](supply-chain/2023-02_sling-tv-dish-network-corporation.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_atlassian-envoy.yaml](supply-chain/2023-02_atlassian-envoy.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_bonq-exploit.yaml](data-leak/2023-02_bonq-exploit.yaml) | data-leak | 2023-02-01 |  |  |
| [2023-02_volt-typhoon-lelwd-utility.yaml](other/2023-02_volt-typhoon-lelwd-utility.yaml) | other | 2023-02-01 |  |  |
| [2023-02_boost-mobile-dish-network-corporation.yaml](supply-chain/2023-02_boost-mobile-dish-network-corporation.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-02_sharp-healthcare-unknown.yaml](supply-chain/2023-02_sharp-healthcare-unknown.yaml) | supply-chain | 2023-02-01 |  |  |
| [2023-01_ftx-tries-to-claw-back-446-million-from-voyager.yaml](other/2023-01_ftx-tries-to-claw-back-446-million-from-voyager.yaml) | other | 2023-01-31 |  |  |
| [2023-01_ordinals-launch.yaml](other/2023-01_ordinals-launch.yaml) | other | 2023-01-31 |  |  |
| [2023-01_rally-sidechain-shuts-down.yaml](other/2023-01_rally-sidechain-shuts-down.yaml) | other | 2023-01-31 |  |  |
| [2023-01_tesla-lost-140-million-trading-bitcoin-in-2022.yaml](other/2023-01_tesla-lost-140-million-trading-bitcoin-in-2022.yaml) | other | 2023-01-31 |  |  |
| [2023-01_new-york-regulator-investigates-gemini.yaml](other/2023-01_new-york-regulator-investigates-gemini.yaml) | other | 2023-01-30 |  |  |
| [2023-03_hatch-bank-goanywhere-mft.yaml](supply-chain/2023-03_hatch-bank-goanywhere-mft.yaml) | supply-chain | 2023-01-30 | Cl0p | CVE-2023-0669 |
| [2023-02_community-health-systems-goanywhere-mft.yaml](supply-chain/2023-02_community-health-systems-goanywhere-mft.yaml) | supply-chain | 2023-01-28 | Cl0p | CVE-2023-0669 |
| [2023-01_azuki-twitter-hack.yaml](data-leak/2023-01_azuki-twitter-hack.yaml) | data-leak | 2023-01-27 |  |  |
| [2023-01_coinbase-fined-3-6-million-by-dutch-central-bank.yaml](other/2023-01_coinbase-fined-3-6-million-by-dutch-central-bank.yaml) | other | 2023-01-26 |  |  |
| [2023-01_kevin-rose-wallet-hack.yaml](data-leak/2023-01_kevin-rose-wallet-hack.yaml) | data-leak | 2023-01-25 |  |  |
| [2023-01_bithumb-executives-charged.yaml](other/2023-01_bithumb-executives-charged.yaml) | other | 2023-01-25 |  |  |
| [2023-01_fbi-pins-the-harmony-bridge-hack-on-north-korea.yaml](other/2023-01_fbi-pins-the-harmony-bridge-hack-on-north-korea.yaml) | other | 2023-01-24 |  |  |
| [2023-01_porsche-bungles-nft-roll-out.yaml](other/2023-01_porsche-bungles-nft-roll-out.yaml) | other | 2023-01-24 |  |  |
| [2023-01_gemini-lays-off-10-of-staff.yaml](other/2023-01_gemini-lays-off-10-of-staff.yaml) | other | 2023-01-23 |  |  |
| [2023-01_wormhole-hacker-becomes-the-third-largest-holder-of-steth.yaml](other/2023-01_wormhole-hacker-becomes-the-third-largest-holder-of-steth.yaml) | other | 2023-01-23 |  |  |
| [2023-01_binance-swift-floor-implemented.yaml](other/2023-01_binance-swift-floor-implemented.yaml) | other | 2023-01-21 |  |  |
| [2023-01_nexo-fined-45-million.yaml](other/2023-01_nexo-fined-45-million.yaml) | other | 2023-01-19 |  |  |
| [2023-01_genesis-bankruptcy.yaml](other/2023-01_genesis-bankruptcy.yaml) | other | 2023-01-19 |  |  |
| [2023-03_blue-shield-of-california-goanywhere-mft.yaml](supply-chain/2023-03_blue-shield-of-california-goanywhere-mft.yaml) | supply-chain | 2023-01-18 | Cl0p; Truebot web shell |  |
| [2023-01_goanywhere-clop.yaml](supply-chain/2023-01_goanywhere-clop.yaml) | supply-chain | 2023-01-18 |  | CVE-2023-0669 |
| [2023-06_intellihartx-llc-goanywhere-mft.yaml](supply-chain/2023-06_intellihartx-llc-goanywhere-mft.yaml) | supply-chain | 2023-01-18 | Cl0p; Truebot web shell |  |
| [2023-04_brightline-health-goanywhere-mft.yaml](supply-chain/2023-04_brightline-health-goanywhere-mft.yaml) | supply-chain | 2023-01-18 | Cl0p; Truebot web shell |  |
| [2023-04_santa-clara-family-health-plan-goanywhere-mft.yaml](supply-chain/2023-04_santa-clara-family-health-plan-goanywhere-mft.yaml) | supply-chain | 2023-01-18 | Cl0p; Truebot web shell |  |
| [2023-01_bitzlato-exchange-founder-charged.yaml](other/2023-01_bitzlato-exchange-founder-charged.yaml) | other | 2023-01-18 |  |  |
| [2023-04_nationsbenefits-holding-llc-goanywhere-mft.yaml](supply-chain/2023-04_nationsbenefits-holding-llc-goanywhere-mft.yaml) | supply-chain | 2023-01-18 | Cl0p; Truebot web shell |  |
| [2023-01_western-sydney-uni-m365.yaml](data-leak/2023-01_western-sydney-uni-m365.yaml) | data-leak | 2023-01-17 |  |  |
| [2023-01_three-arrows-capital-founders-seek-funding-for-exchange.yaml](other/2023-01_three-arrows-capital-founders-seek-funding-for-exchange.yaml) | other | 2023-01-16 |  |  |
| [2023-01_nft-god-wallet-drain.yaml](data-leak/2023-01_nft-god-wallet-drain.yaml) | data-leak | 2023-01-13 |  |  |
| [2023-01_lendhub-hack.yaml](data-leak/2023-01_lendhub-hack.yaml) | data-leak | 2023-01-12 |  |  |
| [2023-01_ftx-liquidators-get-liquidated.yaml](other/2023-01_ftx-liquidators-get-liquidated.yaml) | other | 2023-01-12 |  |  |
| [2023-01_sec-charges-gemini-and-genesis.yaml](other/2023-01_sec-charges-gemini-and-genesis.yaml) | other | 2023-01-12 |  |  |
| [2023-01_nexo-raided-by-bulgarian-authorities.yaml](other/2023-01_nexo-raided-by-bulgarian-authorities.yaml) | other | 2023-01-12 |  |  |
| [2023-01_coinbase-performs-more-layoffs.yaml](other/2023-01_coinbase-performs-more-layoffs.yaml) | other | 2023-01-10 |  |  |
| [2023-01_royal-mail-lockbit.yaml](ransomware/2023-01_royal-mail-lockbit.yaml) | ransomware | 2023-01-10 | LockBit 3.0 |  |
| [2023-01_genesis-lays-off-another-30-of-staff.yaml](other/2023-01_genesis-lays-off-another-30-of-staff.yaml) | other | 2023-01-05 |  |  |
| [2023-01_huobi-lays-off-employees.yaml](other/2023-01_huobi-lays-off-employees.yaml) | other | 2023-01-05 |  |  |
| [2023-01_mutant-ape-planet-rug-pull.yaml](other/2023-01_mutant-ape-planet-rug-pull.yaml) | other | 2023-01-05 |  |  |
| [2023-01_new-york-attorney-general-sues-celsius-ceo-alex-mashinksy.yaml](other/2023-01_new-york-attorney-general-sues-celsius-ceo-alex-mashinksy.yaml) | other | 2023-01-05 |  |  |
| [2023-03_forever21-employee-breach.yaml](data-leak/2023-03_forever21-employee-breach.yaml) | data-leak | 2023-01-05 |  |  |
| [2023-01_silvergate-bank-takes-718-million-loss-liquidating-debt-during-ftx-collapse.yaml](other/2023-01_silvergate-bank-takes-718-million-loss-liquidating-debt-during-ftx-collapse.yaml) | other | 2023-01-05 |  |  |
| [2023-01_coinbase-settles-with-new-york-regulators.yaml](other/2023-01_coinbase-settles-with-new-york-regulators.yaml) | other | 2023-01-04 |  |  |
| [2023-01_logan-paul-threatens-to-sue-coffeezilla.yaml](other/2023-01_logan-paul-threatens-to-sue-coffeezilla.yaml) | other | 2023-01-04 |  |  |
| [2023-01_fanatics-ditches-candy-digital.yaml](other/2023-01_fanatics-ditches-candy-digital.yaml) | other | 2023-01-04 |  |  |
| [2023-01_magic-eden-lists-fake-nfts.yaml](data-leak/2023-01_magic-eden-lists-fake-nfts.yaml) | data-leak | 2023-01-04 |  |  |
| [2023-01_cryptonovo-nft-theft.yaml](data-leak/2023-01_cryptonovo-nft-theft.yaml) | data-leak | 2023-01-04 |  |  |
| [2023-01_nft-marketplaces-display-porn.yaml](data-leak/2023-01_nft-marketplaces-display-porn.yaml) | data-leak | 2023-01-03 |  |  |
| [2023-01_wyre-shuts-down.yaml](other/2023-01_wyre-shuts-down.yaml) | other | 2023-01-03 |  |  |
| [2023-01_gmx-whale-wallet-drain.yaml](data-leak/2023-01_gmx-whale-wallet-drain.yaml) | data-leak | 2023-01-03 |  |  |
| [2023-01_dnp3-gambled-with-investor-funds.yaml](other/2023-01_dnp3-gambled-with-investor-funds.yaml) | other | 2023-01-03 |  |  |
| [2023-01_nikhil-gopalani-nft-theft.yaml](data-leak/2023-01_nikhil-gopalani-nft-theft.yaml) | data-leak | 2023-01-02 |  |  |
| [2023-01_gemini-founder-writes-open-letter-to-barry-silbert.yaml](other/2023-01_gemini-founder-writes-open-letter-to-barry-silbert.yaml) | other | 2023-01-02 |  |  |
| [2023-01_klm-flying-blue.yaml](supply-chain/2023-01_klm-flying-blue.yaml) | supply-chain | 2023-01-01 |  |  |
| [2023-01_fanduels-mailchimp.yaml](supply-chain/2023-01_fanduels-mailchimp.yaml) | supply-chain | 2023-01-01 |  |  |
| [2024-10_salt-typhoon-telecoms.yaml](other/2024-10_salt-typhoon-telecoms.yaml) | other | 2023-01-01 |  |  |
| [2024-10_salt-typhoon-lumen-verizon-att-telecom.yaml](other/2024-10_salt-typhoon-lumen-verizon-att-telecom.yaml) | other | 2023-01-01 | Demodex (kernel-mode rootkit) |  |
| [2023-01_luke-dashjr-wallet-hack.yaml](data-leak/2023-01_luke-dashjr-wallet-hack.yaml) | data-leak | 2023-01-01 |  |  |
| [2023-01_nissan-north-america-unknown.yaml](supply-chain/2023-01_nissan-north-america-unknown.yaml) | supply-chain | 2023-01-01 |  |  |
| [2023-01_solana-foundation-mailchimp.yaml](supply-chain/2023-01_solana-foundation-mailchimp.yaml) | supply-chain | 2023-01-01 |  |  |
| [2023-01_datadog-circleci.yaml](supply-chain/2023-01_datadog-circleci.yaml) | supply-chain | 2023-01-01 |  |  |
| [2023-01_university-of-colorado-hospital-authority-diligent-corporation.yaml](supply-chain/2023-01_university-of-colorado-hospital-authority-diligent-corporation.yaml) | supply-chain | 2023-01-01 |  |  |
| [2022-12_covario-bankruptcy.yaml](other/2022-12_covario-bankruptcy.yaml) | other | 2022-12-29 |  |  |
| [2022-12_tax-loss-harvesting-tool-launched.yaml](other/2022-12_tax-loss-harvesting-tool-launched.yaml) | other | 2022-12-29 |  |  |
| [2022-12_3commas-api-key-leak.yaml](data-leak/2022-12_3commas-api-key-leak.yaml) | data-leak | 2022-12-28 |  |  |
| [2022-12_alameda-wallets-sell-off-tokens.yaml](other/2022-12_alameda-wallets-sell-off-tokens.yaml) | other | 2022-12-28 |  |  |
| [2022-12_midas-investments-collapse.yaml](other/2022-12_midas-investments-collapse.yaml) | other | 2022-12-27 |  |  |
| [2022-12_avraham-eisenberg-arrested.yaml](other/2022-12_avraham-eisenberg-arrested.yaml) | other | 2022-12-27 |  |  |
| [2022-12_bitkeep-hack.yaml](data-leak/2022-12_bitkeep-hack.yaml) | data-leak | 2022-12-26 |  |  |
| [2022-12_btc-com-hack.yaml](data-leak/2022-12_btc-com-hack.yaml) | data-leak | 2022-12-26 |  |  |
| [2022-12_pytorch-nightly-dependency-confusion.yaml](supply-chain/2022-12_pytorch-nightly-dependency-confusion.yaml) | supply-chain | 2022-12-25 | triton (malicious PyPI packag… |  |
| [2024-08_toyota-240gb-dark-web.yaml](data-leak/2024-08_toyota-240gb-dark-web.yaml) | data-leak | 2022-12-25 |  |  |
| [2022-12_rubic-hack-2.yaml](data-leak/2022-12_rubic-hack-2.yaml) | data-leak | 2022-12-25 |  |  |
| [2022-12_rubic-hack-35-2.yaml](data-leak/2022-12_rubic-hack-35-2.yaml) | data-leak | 2022-12-25 |  |  |
| [2022-12_defrost-finance-rug-pull.yaml](other/2022-12_defrost-finance-rug-pull.yaml) | other | 2022-12-23 |  |  |
| [2022-12_aax-executives-arrested.yaml](other/2022-12_aax-executives-arrested.yaml) | other | 2022-12-23 |  |  |
| [2022-12_kotiota-barred-from-releasing-pok-mon-nfts.yaml](other/2022-12_kotiota-barred-from-releasing-pok-mon-nfts.yaml) | other | 2022-12-22 |  |  |
| [2022-12_core-scientific-bankruptcy.yaml](other/2022-12_core-scientific-bankruptcy.yaml) | other | 2022-12-21 |  |  |
| [2022-12_swan-bitcoin-releases-home-equity-bitcoin-product.yaml](other/2022-12_swan-bitcoin-releases-home-equity-bitcoin-product.yaml) | other | 2022-12-21 |  |  |
| [2022-12_caroline-ellison-and-gary-wang-plead-guilty.yaml](other/2022-12_caroline-ellison-and-gary-wang-plead-guilty.yaml) | other | 2022-12-21 |  |  |
| [2022-12_paxful-delists-ether.yaml](other/2022-12_paxful-delists-ether.yaml) | other | 2022-12-21 |  |  |
| [2022-12_waves-loses-peg.yaml](other/2022-12_waves-loses-peg.yaml) | other | 2022-12-20 |  |  |
| [2022-12_auros-bankruptcy.yaml](other/2022-12_auros-bankruptcy.yaml) | other | 2022-12-20 |  |  |
| [2022-12_sevenseason-nft-theft.yaml](data-leak/2022-12_sevenseason-nft-theft.yaml) | data-leak | 2022-12-17 |  |  |
| [2022-12_quadrigacx-unauthorized-transfer.yaml](other/2022-12_quadrigacx-unauthorized-transfer.yaml) | other | 2022-12-16 |  |  |
| [2022-12_circleci-secrets-breach.yaml](credential-theft/2022-12_circleci-secrets-breach.yaml) | credential-theft | 2022-12-16 |  |  |
| [2022-12_mazars-group-stops-crypto-audits.yaml](other/2022-12_mazars-group-stops-crypto-audits.yaml) | other | 2022-12-16 |  |  |
| [2022-12_raydium-hack.yaml](data-leak/2022-12_raydium-hack.yaml) | data-leak | 2022-12-16 |  |  |
| [2022-12_donald-trump-launches-nfts.yaml](other/2022-12_donald-trump-launches-nfts.yaml) | other | 2022-12-15 |  |  |
| [2022-12_binance-withdrawals-surge.yaml](other/2022-12_binance-withdrawals-surge.yaml) | other | 2022-12-13 |  |  |
| [2022-12_argo-blockchain-warns-of-bankruptcy.yaml](other/2022-12_argo-blockchain-warns-of-bankruptcy.yaml) | other | 2022-12-12 |  |  |
| [2022-12_sam-bankman-fried-arrested.yaml](other/2022-12_sam-bankman-fried-arrested.yaml) | other | 2022-12-12 |  |  |
| [2022-12_doj-considers-criminal-charges-for-binance.yaml](other/2022-12_doj-considers-criminal-charges-for-binance.yaml) | other | 2022-12-12 |  |  |
| [2022-12_decentraland-adds-landlords.yaml](other/2022-12_decentraland-adds-landlords.yaml) | other | 2022-12-11 |  |  |
| [2022-12_lodestar-finance-attack.yaml](data-leak/2022-12_lodestar-finance-attack.yaml) | data-leak | 2022-12-10 |  |  |
| [2022-12_the-block-ceo-resigns.yaml](other/2022-12_the-block-ceo-resigns.yaml) | other | 2022-12-09 |  |  |
| [2022-12_i-the-block-i-ceo-resigns.yaml](other/2022-12_i-the-block-i-ceo-resigns.yaml) | other | 2022-12-09 |  |  |
| [2022-12_digital-surge-enters-voluntary-administration.yaml](other/2022-12_digital-surge-enters-voluntary-administration.yaml) | other | 2022-12-08 |  |  |
| [2022-12_celebrity-class-action-filed.yaml](other/2022-12_celebrity-class-action-filed.yaml) | other | 2022-12-08 |  |  |
| [2022-12_vanessa-sierra-rug-pull.yaml](other/2022-12_vanessa-sierra-rug-pull.yaml) | other | 2022-12-08 |  |  |
| [2022-12_ftx-nfts-break.yaml](other/2022-12_ftx-nfts-break.yaml) | other | 2022-12-07 |  |  |
| [2022-12_koinly-layoffs.yaml](other/2022-12_koinly-layoffs.yaml) | other | 2022-12-06 |  |  |
| [2022-12_orthogonal-trading-insolvency.yaml](other/2022-12_orthogonal-trading-insolvency.yaml) | other | 2022-12-05 |  |  |
| [2022-12_swyftx-layoffs.yaml](other/2022-12_swyftx-layoffs.yaml) | other | 2022-12-05 |  |  |
| [2022-12_bybit-layoffs.yaml](other/2022-12_bybit-layoffs.yaml) | other | 2022-12-04 |  |  |
| [2022-12_activision-smishing-employee-data.yaml](data-leak/2022-12_activision-smishing-employee-data.yaml) | data-leak | 2022-12-04 |  |  |
| [2022-12_aax-customers-search-for-executives.yaml](other/2022-12_aax-customers-search-for-executives.yaml) | other | 2022-12-03 |  |  |
| [2022-12_genesis-owes-gemini.yaml](other/2022-12_genesis-owes-gemini.yaml) | other | 2022-12-03 |  |  |
| [2022-12_rackspace-play-ransomware.yaml](ransomware/2022-12_rackspace-play-ransomware.yaml) | ransomware | 2022-12-02 | Play ransomware | CVE-2022-41080, CVE-2022-41082 |
| [2022-12_st-luke-s-health-adelanto-healthcare-ventures.yaml](supply-chain/2022-12_st-luke-s-health-adelanto-healthcare-ventures.yaml) | supply-chain | 2022-12-01 |  |  |
| [2022-12_ankr-hack.yaml](data-leak/2022-12_ankr-hack.yaml) | data-leak | 2022-12-01 |  |  |
| [2022-12_sobeys-empire-co.yaml](supply-chain/2022-12_sobeys-empire-co.yaml) | supply-chain | 2022-12-01 |  |  |
| [2023-01_commuteair-jenkins-aws-s3.yaml](credential-theft/2023-01_commuteair-jenkins-aws-s3.yaml) | credential-theft | 2022-12-01 |  |  |
| [2022-12_helio-attack.yaml](data-leak/2022-12_helio-attack.yaml) | data-leak | 2022-12-01 |  |  |
| [2022-11_kraken-fined.yaml](other/2022-11_kraken-fined.yaml) | other | 2022-11-30 |  |  |
| [2022-11_kraken-layoffs.yaml](other/2022-11_kraken-layoffs.yaml) | other | 2022-11-30 |  |  |
| [2022-11_lastpass-devops-keylogger.yaml](credential-theft/2022-11_lastpass-devops-keylogger.yaml) | credential-theft | 2022-11-30 | Keylogger (via vulnerable Ple… |  |
| [2022-11_auros-misses-loan-payment.yaml](other/2022-11_auros-misses-loan-payment.yaml) | other | 2022-11-30 |  |  |
| [2022-11_maersk-and-ibm-shutter-blockchain-project.yaml](other/2022-11_maersk-and-ibm-shutter-blockchain-project.yaml) | other | 2022-11-30 |  |  |
| [2022-11_bitso-layoffs.yaml](other/2022-11_bitso-layoffs.yaml) | other | 2022-11-29 |  |  |
| [2022-11_block-subsidiary-announces-and-cancels-plans-to-trademark-web5.yaml](other/2022-11_block-subsidiary-announces-and-cancels-plans-to-trademark-web5.yaml) | other | 2022-11-29 |  |  |
| [2022-11_blockfi-bankruptcy.yaml](other/2022-11_blockfi-bankruptcy.yaml) | other | 2022-11-28 |  |  |
| [2022-11_elon-statue-fails-to-impress.yaml](other/2022-11_elon-statue-fails-to-impress.yaml) | other | 2022-11-26 |  |  |
| [2023-01_t-mobile-api.yaml](data-leak/2023-01_t-mobile-api.yaml) | data-leak | 2022-11-25 |  |  |
| [2022-11_150-companies-want-binance-bailout.yaml](other/2022-11_150-companies-want-binance-bailout.yaml) | other | 2022-11-25 |  |  |
| [2022-11_coinlist-halts-withdrawals.yaml](other/2022-11_coinlist-halts-withdrawals.yaml) | other | 2022-11-24 |  |  |
| [2022-11_lemon-cash-layoffs.yaml](other/2022-11_lemon-cash-layoffs.yaml) | other | 2022-11-24 |  |  |
| [2022-11_new-york-bans-new-mining-operations.yaml](other/2022-11_new-york-bans-new-mining-operations.yaml) | other | 2022-11-22 |  |  |
| [2022-11_iris-energy-defaults-on-loan.yaml](other/2022-11_iris-energy-defaults-on-loan.yaml) | other | 2022-11-22 |  |  |
| [2022-11_genesis-warns-of-bankruptcy.yaml](other/2022-11_genesis-warns-of-bankruptcy.yaml) | other | 2022-11-21 |  |  |
| [2022-11_grayscale-bitcoin-trust-declines.yaml](other/2022-11_grayscale-bitcoin-trust-declines.yaml) | other | 2022-11-19 |  |  |
| [2022-11_hoo-vanishes.yaml](other/2022-11_hoo-vanishes.yaml) | other | 2022-11-18 |  |  |
| [2022-11_coinhouse-halts-savings-accounts.yaml](other/2022-11_coinhouse-halts-savings-accounts.yaml) | other | 2022-11-17 |  |  |
| [2022-11_australian-securities-exchange-scraps-blockchain-project.yaml](other/2022-11_australian-securities-exchange-scraps-blockchain-project.yaml) | other | 2022-11-17 |  |  |
| [2022-11_nestcoin-layoffs.yaml](other/2022-11_nestcoin-layoffs.yaml) | other | 2022-11-16 |  |  |
| [2022-11_ftx-celebrities-class-action-filed.yaml](other/2022-11_ftx-celebrities-class-action-filed.yaml) | other | 2022-11-16 |  |  |
| [2022-11_gemini-halts-withdrawals.yaml](other/2022-11_gemini-halts-withdrawals.yaml) | other | 2022-11-16 |  |  |
| [2022-11_genesis-halts-withdrawals.yaml](other/2022-11_genesis-halts-withdrawals.yaml) | other | 2022-11-16 |  |  |
| [2022-11_digital-surge-halts-withdrawals.yaml](other/2022-11_digital-surge-halts-withdrawals.yaml) | other | 2022-11-15 |  |  |
| [2022-11_blockfi-layoffs.yaml](other/2022-11_blockfi-layoffs.yaml) | other | 2022-11-15 |  |  |
| [2022-11_coachella-nfts-stop-working.yaml](other/2022-11_coachella-nfts-stop-working.yaml) | other | 2022-11-15 |  |  |
| [2022-11_salt-halts-withdrawals.yaml](other/2022-11_salt-halts-withdrawals.yaml) | other | 2022-11-15 |  |  |
| [2022-11_binance-announces-industry-recovery-fund.yaml](other/2022-11_binance-announces-industry-recovery-fund.yaml) | other | 2022-11-14 |  |  |
| [2022-11_ikigai-asset-management-reveals-ftx-exposure.yaml](other/2022-11_ikigai-asset-management-reveals-ftx-exposure.yaml) | other | 2022-11-14 |  |  |
| [2022-11_huobi-reveals-ftx-exposure.yaml](other/2022-11_huobi-reveals-ftx-exposure.yaml) | other | 2022-11-13 |  |  |
| [2022-11_flare-token-hack.yaml](data-leak/2022-11_flare-token-hack.yaml) | data-leak | 2022-11-13 |  |  |
| [2022-11_aax-halts-withdrawals.yaml](other/2022-11_aax-halts-withdrawals.yaml) | other | 2022-11-13 |  |  |
| [2022-11_defiai-hack.yaml](data-leak/2022-11_defiai-hack.yaml) | data-leak | 2022-11-12 |  |  |
| [2022-11_crypto-com-admits-erroneous-transfer.yaml](other/2022-11_crypto-com-admits-erroneous-transfer.yaml) | other | 2022-11-12 |  |  |
| [2022-11_bahamas-securities-commission-denies-telling-ftx-to-open-withdrawals.yaml](other/2022-11_bahamas-securities-commission-denies-telling-ftx-to-open-withdrawals.yaml) | other | 2022-11-12 |  |  |
| [2022-11_tokensoft-intentionally-publishes-user-data.yaml](other/2022-11_tokensoft-intentionally-publishes-user-data.yaml) | other | 2022-11-12 |  |  |
| [2022-11_ftx-aws-secrets-compromise.yaml](credential-theft/2022-11_ftx-aws-secrets-compromise.yaml) | credential-theft | 2022-11-11 |  |  |
| [2022-11_ftx-collapse.yaml](other/2022-11_ftx-collapse.yaml) | other | 2022-11-11 |  |  |
| [2022-11_ftx-hack.yaml](data-leak/2022-11_ftx-hack.yaml) | data-leak | 2022-11-11 |  |  |
| [2022-11_dfx-finance-attack.yaml](data-leak/2022-11_dfx-finance-attack.yaml) | data-leak | 2022-11-10 |  |  |
| [2022-11_users-circumvent-ftx-withdrawal-halt.yaml](other/2022-11_users-circumvent-ftx-withdrawal-halt.yaml) | other | 2022-11-10 |  |  |
| [2022-11_blockfi-halts-withdrawals.yaml](other/2022-11_blockfi-halts-withdrawals.yaml) | other | 2022-11-10 |  |  |
| [2022-11_securities-commission-of-the-bahamas-freezes-ftx-assets.yaml](other/2022-11_securities-commission-of-the-bahamas-freezes-ftx-assets.yaml) | other | 2022-11-10 |  |  |
| [2022-11_bo-shen-wallet-compromise.yaml](data-leak/2022-11_bo-shen-wallet-compromise.yaml) | data-leak | 2022-11-10 |  |  |
| [2022-11_binance-rescinds-ftx-bailout.yaml](other/2022-11_binance-rescinds-ftx-bailout.yaml) | other | 2022-11-09 |  |  |
| [2022-11_binance-offers-ftx-bailout.yaml](other/2022-11_binance-offers-ftx-bailout.yaml) | other | 2022-11-08 |  |  |
| [2022-11_lbry-violated-securities-laws.yaml](other/2022-11_lbry-violated-securities-laws.yaml) | other | 2022-11-07 |  |  |
| [2022-11_i-coindesk-i-publishes-alameda-research-balance-sheet.yaml](other/2022-11_i-coindesk-i-publishes-alameda-research-balance-sheet.yaml) | other | 2022-11-07 |  |  |
| [2022-11_stolen-silk-road-bitcoins-seized.yaml](data-leak/2022-11_stolen-silk-road-bitcoins-seized.yaml) | data-leak | 2022-11-07 |  |  |
| [2022-11_coindesk-publishes-alameda-research-balance-sheet.yaml](other/2022-11_coindesk-publishes-alameda-research-balance-sheet.yaml) | other | 2022-11-07 |  |  |
| [2022-11_pando-hack.yaml](data-leak/2022-11_pando-hack.yaml) | data-leak | 2022-11-06 |  |  |
| [2022-11_telegram-repossesses-usernames.yaml](other/2022-11_telegram-repossesses-usernames.yaml) | other | 2022-11-05 |  |  |
| [2022-11_monkey-drainer-phishing-attack.yaml](data-leak/2022-11_monkey-drainer-phishing-attack.yaml) | data-leak | 2022-11-04 |  |  |
| [2022-11_gala-games-hack.yaml](other/2022-11_gala-games-hack.yaml) | other | 2022-11-03 |  |  |
| [2022-11_rubic-hack-35-1.yaml](data-leak/2022-11_rubic-hack-35-1.yaml) | data-leak | 2022-11-02 |  |  |
| [2022-11_iris-energy-close-to-defaulting-on-loans.yaml](other/2022-11_iris-energy-close-to-defaulting-on-loans.yaml) | other | 2022-11-02 |  |  |
| [2022-11_skyward-finance-hack.yaml](data-leak/2022-11_skyward-finance-hack.yaml) | data-leak | 2022-11-02 |  |  |
| [2022-11_rubic-hack-1.yaml](data-leak/2022-11_rubic-hack-1.yaml) | data-leak | 2022-11-02 |  |  |
| [2022-11_solend-attack.yaml](data-leak/2022-11_solend-attack.yaml) | data-leak | 2022-11-02 |  |  |
| [2022-11_tpg-telecom-iinet-76k-australia.yaml](data-leak/2022-11_tpg-telecom-iinet-76k-australia.yaml) | data-leak | 2022-11-01 |  |  |
| [2022-11_deribit-hack.yaml](data-leak/2022-11_deribit-hack.yaml) | data-leak | 2022-11-01 |  |  |
| [2022-10_hodlnaut-founders-hide-records.yaml](other/2022-10_hodlnaut-founders-hide-records.yaml) | other | 2022-10-28 |  |  |
| [2022-10_friesdao-attack.yaml](data-leak/2022-10_friesdao-attack.yaml) | data-leak | 2022-10-27 |  |  |
| [2022-10_core-scientific-warns-of-bankruptcy.yaml](other/2022-10_core-scientific-warns-of-bankruptcy.yaml) | other | 2022-10-27 |  |  |
| [2022-10_team-finance-hack.yaml](data-leak/2022-10_team-finance-hack.yaml) | data-leak | 2022-10-27 |  |  |
| [2022-10_monkey-drainer-phishing-scam.yaml](data-leak/2022-10_monkey-drainer-phishing-scam.yaml) | data-leak | 2022-10-25 |  |  |
| [2022-10_quickswap-attack.yaml](data-leak/2022-10_quickswap-attack.yaml) | data-leak | 2022-10-23 |  |  |
| [2022-10_freeway-rug-pull.yaml](other/2022-10_freeway-rug-pull.yaml) | other | 2022-10-23 |  |  |
| [2022-10_layer2dao-hack.yaml](data-leak/2022-10_layer2dao-hack.yaml) | data-leak | 2022-10-23 |  |  |
| [2022-10_3commas-hack.yaml](data-leak/2022-10_3commas-hack.yaml) | data-leak | 2022-10-22 |  |  |
| [2022-10_i-lord-of-the-rings-i-nfts-announced.yaml](other/2022-10_i-lord-of-the-rings-i-nfts-announced.yaml) | other | 2022-10-21 |  |  |
| [2022-10_olympus-dao-hack.yaml](data-leak/2022-10_olympus-dao-hack.yaml) | data-leak | 2022-10-21 |  |  |
| [2022-10_lord-of-the-rings-nfts-announced.yaml](other/2022-10_lord-of-the-rings-nfts-announced.yaml) | other | 2022-10-21 |  |  |
| [2022-10_unstoppable-domains-disables-coin-extensions.yaml](other/2022-10_unstoppable-domains-disables-coin-extensions.yaml) | other | 2022-10-18 |  |  |
| [2022-10_roofstock-claims-to-have-sold-house-as-nft.yaml](other/2022-10_roofstock-claims-to-have-sold-house-as-nft.yaml) | other | 2022-10-18 |  |  |
| [2022-10_moola-market-attack.yaml](data-leak/2022-10_moola-market-attack.yaml) | data-leak | 2022-10-18 |  |  |
| [2022-10_bitbtc-vulnerability.yaml](data-leak/2022-10_bitbtc-vulnerability.yaml) | data-leak | 2022-10-18 |  |  |
| [2022-10_aptos-launches-slowly.yaml](other/2022-10_aptos-launches-slowly.yaml) | other | 2022-10-17 |  |  |
| [2022-10_bitkeep-swap-hack.yaml](data-leak/2022-10_bitkeep-swap-hack.yaml) | data-leak | 2022-10-17 |  |  |
| [2022-10_texas-securities-investigators-looking-into-ftx.yaml](other/2022-10_texas-securities-investigators-looking-into-ftx.yaml) | other | 2022-10-17 |  |  |
| [2022-10_syntropy-theft.yaml](data-leak/2022-10_syntropy-theft.yaml) | data-leak | 2022-10-15 |  |  |
| [2022-10_dao-maker-dodges-repayment-promises.yaml](other/2022-10_dao-maker-dodges-repayment-promises.yaml) | other | 2022-10-14 |  |  |
| [2022-10_advocate-aurora-health-meta-pixel.yaml](supply-chain/2022-10_advocate-aurora-health-meta-pixel.yaml) | data-leak | 2022-10-14 |  |  |
| [2022-10_earning-farm-attack.yaml](data-leak/2022-10_earning-farm-attack.yaml) | data-leak | 2022-10-14 |  |  |
| [2022-10_ethereum-censorship.yaml](other/2022-10_ethereum-censorship.yaml) | other | 2022-10-14 |  |  |
| [2022-10_blu3dao-accusations.yaml](other/2022-10_blu3dao-accusations.yaml) | other | 2022-10-13 |  |  |
| [2022-10_harassment-at-ethereum-conference.yaml](other/2022-10_harassment-at-ethereum-conference.yaml) | other | 2022-10-11 |  |  |
| [2022-10_qanx-bridge-hack-35-2.yaml](data-leak/2022-10_qanx-bridge-hack-35-2.yaml) | data-leak | 2022-10-11 |  |  |
| [2022-10_rabby-wallet-hack.yaml](data-leak/2022-10_rabby-wallet-hack.yaml) | data-leak | 2022-10-11 |  |  |
| [2022-10_yuga-labs-sec-investigation.yaml](other/2022-10_yuga-labs-sec-investigation.yaml) | other | 2022-10-11 |  |  |
| [2022-10_cnn-abandons-vault-nft-project.yaml](other/2022-10_cnn-abandons-vault-nft-project.yaml) | other | 2022-10-11 |  |  |
| [2022-10_mango-markets-exploit.yaml](data-leak/2022-10_mango-markets-exploit.yaml) | data-leak | 2022-10-11 |  |  |
| [2022-10_bittrex-fined.yaml](other/2022-10_bittrex-fined.yaml) | other | 2022-10-11 |  |  |
| [2022-10_stax-finance-hack.yaml](data-leak/2022-10_stax-finance-hack.yaml) | data-leak | 2022-10-11 |  |  |
| [2022-10_qanx-bridge-hack-2.yaml](data-leak/2022-10_qanx-bridge-hack-2.yaml) | data-leak | 2022-10-11 |  |  |
| [2022-11_killnet-ddos-nato-european-parliament.yaml](other/2022-11_killnet-ddos-nato-european-parliament.yaml) | other | 2022-10-10 |  |  |
| [2022-10_blockwater-technologies-insolvency.yaml](other/2022-10_blockwater-technologies-insolvency.yaml) | other | 2022-10-09 |  |  |
| [2022-10_mydeal-australia-2-2m.yaml](credential-theft/2022-10_mydeal-australia-2-2m.yaml) | credential-theft | 2022-10-09 |  |  |
| [2022-10_laszlo-btc-nft-theft.yaml](data-leak/2022-10_laszlo-btc-nft-theft.yaml) | data-leak | 2022-10-08 |  |  |
| [2022-10_decentraland-has-few-users.yaml](other/2022-10_decentraland-has-few-users.yaml) | other | 2022-10-07 |  |  |
| [2022-10_celsius-customer-info-exposed-in-bankruptcy-court.yaml](other/2022-10_celsius-customer-info-exposed-in-bankruptcy-court.yaml) | other | 2022-10-06 |  |  |
| [2022-10_binance-bridge-hack.yaml](data-leak/2022-10_binance-bridge-hack.yaml) | data-leak | 2022-10-06 |  |  |
| [2022-10_korea-freezes-crypto-reportedly-belonging-to-do-kwon.yaml](other/2022-10_korea-freezes-crypto-reportedly-belonging-to-do-kwon.yaml) | other | 2022-10-05 |  |  |
| [2022-10_zcash-spam-attack.yaml](other/2022-10_zcash-spam-attack.yaml) | other | 2022-10-05 |  |  |
| [2022-10_sovryn-attack.yaml](data-leak/2022-10_sovryn-attack.yaml) | data-leak | 2022-10-04 |  |  |
| [2022-10_hacked-account-seller-convicted.yaml](other/2022-10_hacked-account-seller-convicted.yaml) | other | 2022-10-03 |  |  |
| [2022-10_commonspirit-health-hive.yaml](ransomware/2022-10_commonspirit-health-hive.yaml) | ransomware | 2022-10-03 | Hive ransomware |  |
| [2022-10_kim-kardashian-fined-by-sec.yaml](other/2022-10_kim-kardashian-fined-by-sec.yaml) | other | 2022-10-03 |  |  |
| [2022-10_coinbase-outage.yaml](other/2022-10_coinbase-outage.yaml) | other | 2022-10-02 |  |  |
| [2022-10_somnia-pain-management-of-kentucky-not-disclosed.yaml](supply-chain/2022-10_somnia-pain-management-of-kentucky-not-disclosed.yaml) | supply-chain | 2022-10-01 |  |  |
| [2022-10_barracuda-esg-cve-2023-2868.yaml](supply-chain/2022-10_barracuda-esg-cve-2023-2868.yaml) | supply-chain | 2022-10-01 | SALTWATER, SEASPY, SEASIDE, S… | CVE-2023-2868 |
| [2022-10_transit-swap-hack.yaml](data-leak/2022-10_transit-swap-hack.yaml) | data-leak | 2022-10-01 |  |  |
| [2022-09_flip-xyz-fantasy-nft-trading.yaml](other/2022-09_flip-xyz-fantasy-nft-trading.yaml) | other | 2022-09-30 |  |  |
| [2022-09_solana-outage.yaml](other/2022-09_solana-outage.yaml) | other | 2022-09-30 |  |  |
| [2022-09_elon-musk-blockchain-twitter-ideas.yaml](other/2022-09_elon-musk-blockchain-twitter-ideas.yaml) | other | 2022-09-29 |  |  |
| [2022-09_crypto-executives-leave.yaml](other/2022-09_crypto-executives-leave.yaml) | other | 2022-09-28 |  |  |
| [2022-09_0xbadc0de-mev-bot-exploited.yaml](data-leak/2022-09_0xbadc0de-mev-bot-exploited.yaml) | data-leak | 2022-09-28 |  |  |
| [2022-09_collector-claims-to-burn-frida-kahlo-drawing.yaml](other/2022-09_collector-claims-to-burn-frida-kahlo-drawing.yaml) | other | 2022-09-28 |  |  |
| [2022-09_nexo-enforcement-actions.yaml](other/2022-09_nexo-enforcement-actions.yaml) | other | 2022-09-26 |  |  |
| [2022-09_jason-falovitch-nft-theft.yaml](data-leak/2022-09_jason-falovitch-nft-theft.yaml) | data-leak | 2022-09-25 |  |  |
| [2022-09_bitex-founder-charged.yaml](data-leak/2022-09_bitex-founder-charged.yaml) | data-leak | 2022-09-22 |  |  |
| [2022-09_irs-authorized-to-issue-john-doe-summons.yaml](other/2022-09_irs-authorized-to-issue-john-doe-summons.yaml) | other | 2022-09-22 |  |  |
| [2022-09_coinbase-tested-proprietary-trading.yaml](other/2022-09_coinbase-tested-proprietary-trading.yaml) | other | 2022-09-22 |  |  |
| [2022-09_ooki-dao-sued-by-cftc.yaml](other/2022-09_ooki-dao-sued-by-cftc.yaml) | other | 2022-09-22 |  |  |
| [2022-09_compute-north-bankruptcy.yaml](other/2022-09_compute-north-bankruptcy.yaml) | other | 2022-09-22 |  |  |
| [2022-09_wintermute-hack.yaml](data-leak/2022-09_wintermute-hack.yaml) | data-leak | 2022-09-20 |  |  |
| [2022-09_crypto-king-scam.yaml](other/2022-09_crypto-king-scam.yaml) | other | 2022-09-20 |  |  |
| [2022-09_sparkster-sec-settlement.yaml](other/2022-09_sparkster-sec-settlement.yaml) | other | 2022-09-19 |  |  |
| [2022-09_uk-fca-warns-against-ftx.yaml](other/2022-09_uk-fca-warns-against-ftx.yaml) | other | 2022-09-19 |  |  |
| [2022-09_cryptofx-pyramid-scheme.yaml](other/2022-09_cryptofx-pyramid-scheme.yaml) | other | 2022-09-19 |  |  |
| [2022-09_optus.yaml](data-leak/2022-09_optus.yaml) | data-leak | 2022-09-19 |  |  |
| [2022-09_lakeshowtj-nft-theft.yaml](data-leak/2022-09_lakeshowtj-nft-theft.yaml) | data-leak | 2022-09-18 |  |  |
| [2022-09_rockstar-games-gta6-leak.yaml](data-leak/2022-09_rockstar-games-gta6-leak.yaml) | data-leak | 2022-09-17 |  |  |
| [2022-09_gmx-price-manipulation-attack.yaml](other/2022-09_gmx-price-manipulation-attack.yaml) | other | 2022-09-17 |  |  |
| [2022-09_binance-bug-with-helium-token.yaml](other/2022-09_binance-bug-with-helium-token.yaml) | other | 2022-09-16 |  |  |
| [2022-09_gensler-says-proof-of-stake-crypto-could-be-securities.yaml](other/2022-09_gensler-says-proof-of-stake-crypto-could-be-securities.yaml) | other | 2022-09-15 |  |  |
| [2022-09_profanity-vanity-address-vulnerability.yaml](data-leak/2022-09_profanity-vanity-address-vulnerability.yaml) | data-leak | 2022-09-15 |  |  |
| [2022-09_uber-mfa-fatigue.yaml](credential-theft/2022-09_uber-mfa-fatigue.yaml) | credential-theft | 2022-09-15 |  |  |
| [2022-09_coinbase-rolls-out-politics-feature.yaml](other/2022-09_coinbase-rolls-out-politics-feature.yaml) | other | 2022-09-14 |  |  |
| [2022-09_ethereum-merge-double-your-money-scams.yaml](data-leak/2022-09_ethereum-merge-double-your-money-scams.yaml) | data-leak | 2022-09-14 |  |  |
| [2022-09_do-kwon-arrest-warrant-issued.yaml](other/2022-09_do-kwon-arrest-warrant-issued.yaml) | other | 2022-09-14 |  |  |
| [2022-09_starbucks-web3-loyalty-program.yaml](other/2022-09_starbucks-web3-loyalty-program.yaml) | other | 2022-09-12 |  |  |
| [2022-09_revolut-social-engineering-50k.yaml](credential-theft/2022-09_revolut-social-engineering-50k.yaml) | credential-theft | 2022-09-11 |  |  |
| [2022-09_revolut-social-engineering.yaml](credential-theft/2022-09_revolut-social-engineering.yaml) | credential-theft | 2022-09-11 |  |  |
| [2022-09_ubisoft-describes-previous-nft-projects-as-research.yaml](other/2022-09_ubisoft-describes-previous-nft-projects-as-research.yaml) | other | 2022-09-10 |  |  |
| [2022-09_algorand-foundation-exposure-to-hodlnaut.yaml](other/2022-09_algorand-foundation-exposure-to-hodlnaut.yaml) | other | 2022-09-09 |  |  |
| [2022-09_new-free-dao-exploit.yaml](data-leak/2022-09_new-free-dao-exploit.yaml) | data-leak | 2022-09-08 |  |  |
| [2022-09_queen-elizabeth-nfts.yaml](other/2022-09_queen-elizabeth-nfts.yaml) | other | 2022-09-08 |  |  |
| [2022-09_celsius-monopoly.yaml](other/2022-09_celsius-monopoly.yaml) | other | 2022-09-08 |  |  |
| [2022-09_shiba-inu-credential-leak.yaml](other/2022-09_shiba-inu-credential-leak.yaml) | other | 2022-09-08 |  |  |
| [2022-09_coinbase-tornado-cash-lawsuit.yaml](other/2022-09_coinbase-tornado-cash-lawsuit.yaml) | other | 2022-09-08 |  |  |
| [2022-09_vbit-technologies-ponzi-scheme.yaml](data-leak/2022-09_vbit-technologies-ponzi-scheme.yaml) | data-leak | 2022-09-07 |  |  |
| [2022-09_david-bowie-nft-announcement.yaml](other/2022-09_david-bowie-nft-announcement.yaml) | other | 2022-09-06 |  |  |
| [2022-09_avalanche-flash-loan-attacks.yaml](data-leak/2022-09_avalanche-flash-loan-attacks.yaml) | data-leak | 2022-09-06 |  |  |
| [2022-09_poolin-wallet-halts-withdrawals.yaml](other/2022-09_poolin-wallet-halts-withdrawals.yaml) | other | 2022-09-05 |  |  |
| [2022-09_binance-plans-to-convert-stablecoins-to-busd.yaml](other/2022-09_binance-plans-to-convert-stablecoins-to-busd.yaml) | other | 2022-09-05 |  |  |
| [2022-09_mark-hopkins-sentenced.yaml](other/2022-09_mark-hopkins-sentenced.yaml) | other | 2022-09-04 |  |  |
| [2022-09_islamic-state-launches-nfts.yaml](other/2022-09_islamic-state-launches-nfts.yaml) | other | 2022-09-04 |  |  |
| [2022-09_lausd-vice-society.yaml](ransomware/2022-09_lausd-vice-society.yaml) | ransomware | 2022-09-03 | Vice Society ransomware |  |
| [2022-09_rug-pull-finder-mint-gamed.yaml](other/2022-09_rug-pull-finder-mint-gamed.yaml) | other | 2022-09-02 |  |  |
| [2022-09_coinbase-bug.yaml](other/2022-09_coinbase-bug.yaml) | other | 2022-09-02 |  |  |
| [2022-09_kyberswap-hack-1.yaml](data-leak/2022-09_kyberswap-hack-1.yaml) | data-leak | 2022-09-01 |  |  |
| [2022-09_magento-fishpig.yaml](supply-chain/2022-09_magento-fishpig.yaml) | supply-chain | 2022-09-01 |  |  |
| [2022-09_humana-alight-com-choice-health-pre.yaml](supply-chain/2022-09_humana-alight-com-choice-health-pre.yaml) | supply-chain | 2022-09-01 |  |  |
| [2022-09_bill-murray-charity-proceeds-theft.yaml](data-leak/2022-09_bill-murray-charity-proceeds-theft.yaml) | data-leak | 2022-09-01 |  |  |
| [2022-09_anthem-mainehealth-alight-com-choice-health-pre.yaml](supply-chain/2022-09_anthem-mainehealth-alight-com-choice-health-pre.yaml) | supply-chain | 2022-09-01 |  |  |
| [2022-09_shadowfi-exploit.yaml](data-leak/2022-09_shadowfi-exploit.yaml) | data-leak | 2022-09-01 |  |  |
| [2022-09_2tm-layoffs.yaml](other/2022-09_2tm-layoffs.yaml) | other | 2022-09-01 |  |  |
| [2022-09_dydx-announces-and-cancels-liveness-checks-plan.yaml](other/2022-09_dydx-announces-and-cancels-liveness-checks-plan.yaml) | other | 2022-09-01 |  |  |
| [2022-08_helium-ditches-custom-blockchain.yaml](other/2022-08_helium-ditches-custom-blockchain.yaml) | other | 2022-08-31 |  |  |
| [2022-08_babylon-finance-shuts-down.yaml](other/2022-08_babylon-finance-shuts-down.yaml) | other | 2022-08-31 |  |  |
| [2022-08_snapchat-abandons-web3-plans.yaml](other/2022-08_snapchat-abandons-web3-plans.yaml) | other | 2022-08-31 |  |  |
| [2022-08_kyle-roche-withdraws-from-class-actions.yaml](other/2022-08_kyle-roche-withdraws-from-class-actions.yaml) | other | 2022-08-31 |  |  |
| [2022-08_dc-attorney-general-sues-michael-saylor-and-microstrategy.yaml](other/2022-08_dc-attorney-general-sues-michael-saylor-and-microstrategy.yaml) | other | 2022-08-31 |  |  |
| [2022-08_thodex-ceo-arrested.yaml](other/2022-08_thodex-ceo-arrested.yaml) | other | 2022-08-30 |  |  |
| [2022-08_hacktivists-release-passport-nfts.yaml](other/2022-08_hacktivists-release-passport-nfts.yaml) | other | 2022-08-30 |  |  |
| [2022-08_compound-finance-ceth-bug.yaml](other/2022-08_compound-finance-ceth-bug.yaml) | other | 2022-08-30 |  |  |
| [2022-08_bitkub-cto-fined-for-insider-trading.yaml](other/2022-08_bitkub-cto-fined-for-insider-trading.yaml) | other | 2022-08-30 |  |  |
| [2022-08_crypto-com-wants-accidental-transfer-back.yaml](other/2022-08_crypto-com-wants-accidental-transfer-back.yaml) | other | 2022-08-30 |  |  |
| [2022-08_optifi-accidentally-closes-contract.yaml](other/2022-08_optifi-accidentally-closes-contract.yaml) | other | 2022-08-29 |  |  |
| [2022-08_ragnarok-treasury-mismanagement.yaml](other/2022-08_ragnarok-treasury-mismanagement.yaml) | other | 2022-08-26 |  |  |
| [2022-08_kyle-roche-accused-of-unethical-behavior.yaml](other/2022-08_kyle-roche-accused-of-unethical-behavior.yaml) | other | 2022-08-26 |  |  |
| [2022-10_medibank.yaml](ransomware/2022-10_medibank.yaml) | ransomware | 2022-08-25 | BlogXX / REvil variant |  |
| [2022-08_coinswitch-offices-searched.yaml](other/2022-08_coinswitch-offices-searched.yaml) | other | 2022-08-25 |  |  |
| [2022-08_eth-link-domain-at-risk.yaml](other/2022-08_eth-link-domain-at-risk.yaml) | other | 2022-08-25 |  |  |
| [2022-08_pokemonfi-rug-pull.yaml](other/2022-08_pokemonfi-rug-pull.yaml) | other | 2022-08-24 |  |  |
| [2022-08_cameron-redman-accused-of-crypto-twitter-hacks.yaml](data-leak/2022-08_cameron-redman-accused-of-crypto-twitter-hacks.yaml) | data-leak | 2022-08-24 |  |  |
| [2022-08_sudorare-rug-pull.yaml](other/2022-08_sudorare-rug-pull.yaml) | other | 2022-08-23 |  |  |
| [2022-08_transaction-reversal-scheme-perpetrators-charged.yaml](other/2022-08_transaction-reversal-scheme-perpetrators-charged.yaml) | other | 2022-08-23 |  |  |
| [2022-08_ethereum-nodes-at-risk-of-being-booted-from-hosting-provider.yaml](other/2022-08_ethereum-nodes-at-risk-of-being-booted-from-hosting-provider.yaml) | other | 2022-08-23 |  |  |
| [2022-08_plex-15m-user-breach.yaml](data-leak/2022-08_plex-15m-user-breach.yaml) | data-leak | 2022-08-23 |  |  |
| [2022-08_benddao-bank-run.yaml](other/2022-08_benddao-bank-run.yaml) | other | 2022-08-22 |  |  |
| [2022-08_0x47df5-nft-theft.yaml](data-leak/2022-08_0x47df5-nft-theft.yaml) | data-leak | 2022-08-20 |  |  |
| [2022-08_opensea-listing-bug.yaml](other/2022-08_opensea-listing-bug.yaml) | other | 2022-08-20 |  |  |
| [2022-08_swyftx-layoffs.yaml](other/2022-08_swyftx-layoffs.yaml) | other | 2022-08-19 |  |  |
| [2022-08_fdic-cease-and-desist-letters.yaml](other/2022-08_fdic-cease-and-desist-letters.yaml) | other | 2022-08-19 |  |  |
| [2022-08_hodlnaut-lied.yaml](other/2022-08_hodlnaut-lied.yaml) | other | 2022-08-19 |  |  |
| [2022-08_benddao-liquidation-risk.yaml](other/2022-08_benddao-liquidation-risk.yaml) | other | 2022-08-19 |  |  |
| [2022-08_degentown-rug-pull.yaml](other/2022-08_degentown-rug-pull.yaml) | other | 2022-08-18 |  |  |
| [2022-08_divorcee-wants-do-over.yaml](other/2022-08_divorcee-wants-do-over.yaml) | other | 2022-08-18 |  |  |
| [2022-08_crypto-com-layoffs.yaml](other/2022-08_crypto-com-layoffs.yaml) | other | 2022-08-18 |  |  |
| [2022-08_south-korea-moves-to-block-unregistered-exchanges.yaml](other/2022-08_south-korea-moves-to-block-unregistered-exchanges.yaml) | other | 2022-08-18 |  |  |
| [2022-08_bribe-protocol-rug-pull.yaml](other/2022-08_bribe-protocol-rug-pull.yaml) | other | 2022-08-18 |  |  |
| [2022-08_trader-signs-malicious-message.yaml](data-leak/2022-08_trader-signs-malicious-message.yaml) | data-leak | 2022-08-18 |  |  |
| [2022-08_celer-network-bridge-hack.yaml](data-leak/2022-08_celer-network-bridge-hack.yaml) | data-leak | 2022-08-17 |  |  |
| [2022-08_husd-loses-peg.yaml](other/2022-08_husd-loses-peg.yaml) | other | 2022-08-17 |  |  |
| [2022-08_canadian-pension-manager-regrets-crypto-investments.yaml](other/2022-08_canadian-pension-manager-regrets-crypto-investments.yaml) | other | 2022-08-17 |  |  |
| [2022-08_genesis-layoffs-ceo-steps-down.yaml](other/2022-08_genesis-layoffs-ceo-steps-down.yaml) | other | 2022-08-17 |  |  |
| [2022-08_adam-neumann-gets-more-backing.yaml](other/2022-08_adam-neumann-gets-more-backing.yaml) | other | 2022-08-17 |  |  |
| [2022-08_binance-exec-claims-deepfake-scam.yaml](other/2022-08_binance-exec-claims-deepfake-scam.yaml) | other | 2022-08-17 |  |  |
| [2022-08_hodlnaut-collapse.yaml](other/2022-08_hodlnaut-collapse.yaml) | other | 2022-08-16 |  |  |
| [2022-08_dragonchain-sec-complaint.yaml](other/2022-08_dragonchain-sec-complaint.yaml) | other | 2022-08-16 |  |  |
| [2022-08_yuga-labs-v-ryder-ripps.yaml](other/2022-08_yuga-labs-v-ryder-ripps.yaml) | other | 2022-08-15 |  |  |
| [2022-08_eqonex-shuts-down-exchange.yaml](other/2022-08_eqonex-shuts-down-exchange.yaml) | other | 2022-08-15 |  |  |
| [2022-08_bitgo-plans-to-seek-damages-from-galaxy-digital.yaml](other/2022-08_bitgo-plans-to-seek-damages-from-galaxy-digital.yaml) | other | 2022-08-15 |  |  |
| [2022-08_bluebenx-hack-or-exit-scam.yaml](data-leak/2022-08_bluebenx-hack-or-exit-scam.yaml) | data-leak | 2022-08-14 |  |  |
| [2022-08_asec-ape-nft-theft.yaml](data-leak/2022-08_asec-ape-nft-theft.yaml) | data-leak | 2022-08-14 |  |  |
| [2022-08_acala-exploit.yaml](data-leak/2022-08_acala-exploit.yaml) | data-leak | 2022-08-14 |  |  |
| [2022-08_velodrome-theft-by-team-member.yaml](data-leak/2022-08_velodrome-theft-by-team-member.yaml) | data-leak | 2022-08-13 |  |  |
| [2022-08_fake-apecoin-scam.yaml](data-leak/2022-08_fake-apecoin-scam.yaml) | data-leak | 2022-08-13 |  |  |
| [2022-08_tornado-cash-developer-arrested.yaml](other/2022-08_tornado-cash-developer-arrested.yaml) | other | 2022-08-12 |  |  |
| [2022-08_martin-shkreli-hack.yaml](other/2022-08_martin-shkreli-hack.yaml) | other | 2022-08-12 |  |  |
| [2022-08_flipvolt-assets-frozen.yaml](other/2022-08_flipvolt-assets-frozen.yaml) | other | 2022-08-12 |  |  |
| [2022-08_bitboy-defamation-lawsuit.yaml](other/2022-08_bitboy-defamation-lawsuit.yaml) | other | 2022-08-12 |  |  |
| [2022-08_coinbase-insider-trading-report.yaml](other/2022-08_coinbase-insider-trading-report.yaml) | other | 2022-08-12 |  |  |
| [2022-08_ethermine-blocks-tornado-transactions.yaml](other/2022-08_ethermine-blocks-tornado-transactions.yaml) | other | 2022-08-11 |  |  |
| [2022-08_untamed-isles-squanders-kickstarter-funds-on-crypto.yaml](other/2022-08_untamed-isles-squanders-kickstarter-funds-on-crypto.yaml) | other | 2022-08-11 |  |  |
| [2022-08_mailchimp-bans-crypto-newsletters.yaml](other/2022-08_mailchimp-bans-crypto-newsletters.yaml) | other | 2022-08-11 |  |  |
| [2022-08_i-untamed-isles-i-squanders-kickstarter-funds-on-crypto.yaml](other/2022-08_i-untamed-isles-i-squanders-kickstarter-funds-on-crypto.yaml) | other | 2022-08-11 |  |  |
| [2022-08_opensea-requires-police-report-to-freeze-nfts.yaml](other/2022-08_opensea-requires-police-report-to-freeze-nfts.yaml) | other | 2022-08-10 |  |  |
| [2022-08_blur-finance-rug-pull.yaml](other/2022-08_blur-finance-rug-pull.yaml) | other | 2022-08-10 |  |  |
| [2022-08_renbridge-money-laundering-report.yaml](other/2022-08_renbridge-money-laundering-report.yaml) | other | 2022-08-10 |  |  |
| [2022-08_coinbase-doesn-t-send-notifications-during-crash.yaml](other/2022-08_coinbase-doesn-t-send-notifications-during-crash.yaml) | other | 2022-08-10 |  |  |
| [2022-08_hotbit-suspends-trading.yaml](other/2022-08_hotbit-suspends-trading.yaml) | other | 2022-08-10 |  |  |
| [2022-08_celsius-ceo-dumps-tokens.yaml](other/2022-08_celsius-ceo-dumps-tokens.yaml) | other | 2022-08-10 |  |  |
| [2022-08_nuri-insolvency.yaml](other/2022-08_nuri-insolvency.yaml) | other | 2022-08-09 |  |  |
| [2022-08_curve-finance-hack.yaml](data-leak/2022-08_curve-finance-hack.yaml) | data-leak | 2022-08-09 |  |  |
| [2022-08_coinflex-restructuring.yaml](other/2022-08_coinflex-restructuring.yaml) | other | 2022-08-09 |  |  |
| [2022-08_truth-in-advertising-letters.yaml](other/2022-08_truth-in-advertising-letters.yaml) | other | 2022-08-08 |  |  |
| [2022-08_lastpass.yaml](data-leak/2022-08_lastpass.yaml) | data-leak | 2022-08-08 |  | CVE-2020-5741 |
| [2022-08_hodlnaut-halts-withdrawals.yaml](other/2022-08_hodlnaut-halts-withdrawals.yaml) | other | 2022-08-08 |  |  |
| [2022-08_discord-compromises.yaml](data-leak/2022-08_discord-compromises.yaml) | data-leak | 2022-08-08 |  |  |
| [2022-08_ofac-sanctions-tornado-cash.yaml](other/2022-08_ofac-sanctions-tornado-cash.yaml) | other | 2022-08-08 |  |  |
| [2022-08_bored-ape-animation-scam.yaml](data-leak/2022-08_bored-ape-animation-scam.yaml) | data-leak | 2022-08-08 |  |  |
| [2022-08_riot-blockchain-curtailment.yaml](other/2022-08_riot-blockchain-curtailment.yaml) | other | 2022-08-08 |  |  |
| [2022-08_wazirx-ownership-dispute.yaml](other/2022-08_wazirx-ownership-dispute.yaml) | other | 2022-08-08 |  |  |
| [2022-08_xinjiang-victims-database-nfts.yaml](other/2022-08_xinjiang-victims-database-nfts.yaml) | other | 2022-08-07 |  |  |
| [2022-08_dragoma-rug-pull.yaml](other/2022-08_dragoma-rug-pull.yaml) | other | 2022-08-07 |  |  |
| [2022-08_saxon-james-musk-coin-rug-pull.yaml](other/2022-08_saxon-james-musk-coin-rug-pull.yaml) | other | 2022-08-07 |  |  |
| [2022-08_beanstalk-farms-tries-a-relaunch.yaml](other/2022-08_beanstalk-farms-tries-a-relaunch.yaml) | other | 2022-08-06 |  |  |
| [2022-08_steven-galanis-wallet-compromise.yaml](data-leak/2022-08_steven-galanis-wallet-compromise.yaml) | data-leak | 2022-08-06 |  |  |
| [2022-08_wazirx-assets-frozen.yaml](other/2022-08_wazirx-assets-frozen.yaml) | other | 2022-08-05 |  |  |
| [2022-08_uncle-maker-attack-identified.yaml](other/2022-08_uncle-maker-attack-identified.yaml) | other | 2022-08-05 |  |  |
| [2022-08_lastpass-doordash-okta-and-authy-twilio.yaml](supply-chain/2022-08_lastpass-doordash-okta-and-authy-twilio.yaml) | supply-chain | 2022-08-04 |  |  |
| [2022-08_macalinao-brothers-revealed-as-scammers.yaml](other/2022-08_macalinao-brothers-revealed-as-scammers.yaml) | other | 2022-08-04 |  |  |
| [2022-08_news-outlets-publish-wrong-recovery-address-after-nomad-hack.yaml](other/2022-08_news-outlets-publish-wrong-recovery-address-after-nomad-hack.yaml) | other | 2022-08-03 |  |  |
| [2022-08_zb-exchange-hack.yaml](data-leak/2022-08_zb-exchange-hack.yaml) | data-leak | 2022-08-03 |  |  |
| [2022-08_robinhood-layoffs.yaml](other/2022-08_robinhood-layoffs.yaml) | other | 2022-08-02 |  |  |
| [2022-08_michael-saylor-steps-down-as-ceo.yaml](other/2022-08_michael-saylor-steps-down-as-ceo.yaml) | other | 2022-08-02 |  |  |
| [2022-08_slope-wallet-attack.yaml](data-leak/2022-08_slope-wallet-attack.yaml) | data-leak | 2022-08-02 |  |  |
| [2022-08_coinshares-reports-terra-loss.yaml](other/2022-08_coinshares-reports-terra-loss.yaml) | other | 2022-08-02 |  |  |
| [2022-08_robinhood-fined.yaml](other/2022-08_robinhood-fined.yaml) | other | 2022-08-02 |  |  |
| [2022-08_sturm-ruger-company-freestyle-solutions.yaml](supply-chain/2022-08_sturm-ruger-company-freestyle-solutions.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_nomad-bridge-hack.yaml](data-leak/2022-08_nomad-bridge-hack.yaml) | data-leak | 2022-08-01 |  |  |
| [2022-08_forsage-pyramid-scheme-operators-charged.yaml](other/2022-08_forsage-pyramid-scheme-operators-charged.yaml) | other | 2022-08-01 |  |  |
| [2022-08_orange-business-services-orange-silicon-valley.yaml](supply-chain/2022-08_orange-business-services-orange-silicon-valley.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_national-women-s-soccer-league-players-out-money-due-to-voyager-bankruptcy.yaml](other/2022-08_national-women-s-soccer-league-players-out-money-due-to-voyager-bankruptcy.yaml) | other | 2022-08-01 |  |  |
| [2022-08_nomad-bridge-exploit.yaml](other/2022-08_nomad-bridge-exploit.yaml) | other | 2022-08-01 |  |  |
| [2022-08_signal-twilio.yaml](supply-chain/2022-08_signal-twilio.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_anesthesia-associates-of-el-paso-pa-not-disclosed.yaml](supply-chain/2022-08_anesthesia-associates-of-el-paso-pa-not-disclosed.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_digitalocean-edge-messari-decrypt-mailchimp.yaml](supply-chain/2022-08_digitalocean-edge-messari-decrypt-mailchimp.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_kiplepay-sdn-bhd-not-disclosed.yaml](supply-chain/2022-08_kiplepay-sdn-bhd-not-disclosed.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_lee-county-emergency-medical-services-intermedix-corporation.yaml](supply-chain/2022-08_lee-county-emergency-medical-services-intermedix-corporation.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_syracuse-pediatrics-tully-physical-therapy-st-joseph-s-medical-salvation-army-and-24-organizations-practice-resources-llc.yaml](supply-chain/2022-08_syracuse-pediatrics-tully-physical-therapy-st-joseph-s-medical-salvation-army-and-24-organizations-practice-resources-llc.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_dropil-operators-sentenced.yaml](other/2022-08_dropil-operators-sentenced.yaml) | other | 2022-08-01 |  |  |
| [2022-08_municipalities-of-eijsden-margraten-gulpen-wittem-kerkrade-meerssen-and-vaals-not-disclosed.yaml](supply-chain/2022-08_municipalities-of-eijsden-margraten-gulpen-wittem-kerkrade-meerssen-and-vaals-not-disclosed.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_reaper-farm-hack.yaml](data-leak/2022-08_reaper-farm-hack.yaml) | data-leak | 2022-08-01 |  |  |
| [2022-08_nhs-advanced.yaml](supply-chain/2022-08_nhs-advanced.yaml) | supply-chain | 2022-08-01 |  |  |
| [2022-08_doordash-0ktapus-vendor.yaml](data-leak/2022-08_doordash-0ktapus-vendor.yaml) | data-leak | 2022-08-01 |  |  |
| [2022-07_babel-finance-collapse.yaml](other/2022-07_babel-finance-collapse.yaml) | other | 2022-07-29 |  |  |
| [2022-07_coinflex-layoffs.yaml](other/2022-07_coinflex-layoffs.yaml) | other | 2022-07-29 |  |  |
| [2022-07_helium-caught-lying.yaml](other/2022-07_helium-caught-lying.yaml) | other | 2022-07-29 |  |  |
| [2022-07_nirvana-finance-hack.yaml](data-leak/2022-07_nirvana-finance-hack.yaml) | data-leak | 2022-07-28 |  |  |
| [2022-07_regulators-order-voyager-to-stop-saying-they-re-fdic-insured.yaml](other/2022-07_regulators-order-voyager-to-stop-saying-they-re-fdic-insured.yaml) | other | 2022-07-28 |  |  |
| [2022-07_spicedao-wraps-up.yaml](other/2022-07_spicedao-wraps-up.yaml) | other | 2022-07-27 |  |  |
| [2022-07_titanium-blockchain-infrastructure-services-ceo-pleads-guilty.yaml](other/2022-07_titanium-blockchain-infrastructure-services-ceo-pleads-guilty.yaml) | other | 2022-07-26 |  |  |
| [2022-07_ofac-investigating-kraken.yaml](other/2022-07_ofac-investigating-kraken.yaml) | other | 2022-07-26 |  |  |
| [2022-07_kucoin-announces-anti-fud-fund.yaml](other/2022-07_kucoin-announces-anti-fud-fund.yaml) | other | 2022-07-26 |  |  |
| [2022-07_nemus-earth-challenged-by-brazilian-authorities.yaml](other/2022-07_nemus-earth-challenged-by-brazilian-authorities.yaml) | other | 2022-07-25 |  |  |
| [2022-07_immutable-layoffs.yaml](other/2022-07_immutable-layoffs.yaml) | other | 2022-07-25 |  |  |
| [2022-07_martin-shkreli-starts-web3-project.yaml](other/2022-07_martin-shkreli-starts-web3-project.yaml) | other | 2022-07-25 |  |  |
| [2022-07_teddy-doge-rug-pull.yaml](other/2022-07_teddy-doge-rug-pull.yaml) | other | 2022-07-25 |  |  |
| [2022-07_audius-governance-attack.yaml](data-leak/2022-07_audius-governance-attack.yaml) | data-leak | 2022-07-23 |  |  |
| [2022-07_gamestop-nft-platform-hosts-9-11-nft.yaml](other/2022-07_gamestop-nft-platform-hosts-9-11-nft.yaml) | other | 2022-07-23 |  |  |
| [2022-07_celsius-customers-send-letters-to-bankruptcy-judge.yaml](other/2022-07_celsius-customers-send-letters-to-bankruptcy-judge.yaml) | other | 2022-07-22 |  |  |
| [2022-07_blockchain-com-layoffs.yaml](other/2022-07_blockchain-com-layoffs.yaml) | other | 2022-07-21 |  |  |
| [2022-07_my-big-coin-founder-convicted.yaml](other/2022-07_my-big-coin-founder-convicted.yaml) | other | 2022-07-21 |  |  |
| [2022-07_coinbase-tipster-charged.yaml](other/2022-07_coinbase-tipster-charged.yaml) | other | 2022-07-21 |  |  |
| [2022-07_zipmex-halts-withdrawals.yaml](other/2022-07_zipmex-halts-withdrawals.yaml) | other | 2022-07-20 |  |  |
| [2022-07_i-minecraft-i-disallows-nfts.yaml](other/2022-07_i-minecraft-i-disallows-nfts.yaml) | other | 2022-07-20 |  |  |
| [2022-07_tesla-announces-sale-of-their-bitcoin.yaml](other/2022-07_tesla-announces-sale-of-their-bitcoin.yaml) | other | 2022-07-20 |  |  |
| [2022-07_crypto-offices-raided-in-korean-investigation.yaml](other/2022-07_crypto-offices-raided-in-korean-investigation.yaml) | other | 2022-07-20 |  |  |
| [2022-07_blockchain-carbon-offset-company-starts-forest-fires.yaml](other/2022-07_blockchain-carbon-offset-company-starts-forest-fires.yaml) | other | 2022-07-20 |  |  |
| [2022-07_minecraft-disallows-nfts.yaml](other/2022-07_minecraft-disallows-nfts.yaml) | other | 2022-07-20 |  |  |
| [2022-07_franklin-joke-loss.yaml](other/2022-07_franklin-joke-loss.yaml) | other | 2022-07-20 |  |  |
| [2022-07_raccoon-network-and-freedom-protocol-rug-pull.yaml](other/2022-07_raccoon-network-and-freedom-protocol-rug-pull.yaml) | other | 2022-07-19 |  |  |
| [2022-07_sho-restaurant-announced.yaml](other/2022-07_sho-restaurant-announced.yaml) | other | 2022-07-19 |  |  |
| [2022-07_binance-faces-fine-in-the-netherlands.yaml](other/2022-07_binance-faces-fine-in-the-netherlands.yaml) | other | 2022-07-18 |  |  |
| [2022-07_bexplus-shuts-down.yaml](other/2022-07_bexplus-shuts-down.yaml) | other | 2022-07-18 |  |  |
| [2022-07_fbi-warns-of-malicious-crypto-apps.yaml](data-leak/2022-07_fbi-warns-of-malicious-crypto-apps.yaml) | data-leak | 2022-07-18 |  |  |
| [2022-07_gemini-layoffs.yaml](other/2022-07_gemini-layoffs.yaml) | other | 2022-07-18 |  |  |
| [2022-07_blockfi-layoffs.yaml](other/2022-07_blockfi-layoffs.yaml) | other | 2022-07-18 |  |  |
| [2022-07_skybridge-suspends-redemptions-from-crypto-exposed-fund.yaml](other/2022-07_skybridge-suspends-redemptions-from-crypto-exposed-fund.yaml) | other | 2022-07-18 |  |  |
| [2022-07_aex-shut-down-by-police.yaml](other/2022-07_aex-shut-down-by-police.yaml) | other | 2022-07-17 |  |  |
| [2022-07_premint-hack.yaml](data-leak/2022-07_premint-hack.yaml) | data-leak | 2022-07-17 |  |  |
| [2022-07_deekay-twitter-hack.yaml](data-leak/2022-07_deekay-twitter-hack.yaml) | data-leak | 2022-07-16 |  |  |
| [2022-07_coinbase-announces-shutdown-of-affiliate-marketing-program.yaml](other/2022-07_coinbase-announces-shutdown-of-affiliate-marketing-program.yaml) | other | 2022-07-15 |  |  |
| [2022-07_betty-boop-nft-announcement.yaml](other/2022-07_betty-boop-nft-announcement.yaml) | other | 2022-07-14 |  |  |
| [2022-07_boneheads-rug-pull.yaml](other/2022-07_boneheads-rug-pull.yaml) | other | 2022-07-14 |  |  |
| [2022-07_opensea-layoffs.yaml](other/2022-07_opensea-layoffs.yaml) | other | 2022-07-14 |  |  |
| [2022-07_john-mcafee-associate-fined.yaml](other/2022-07_john-mcafee-associate-fined.yaml) | other | 2022-07-13 |  |  |
| [2022-07_celsius-collapse.yaml](other/2022-07_celsius-collapse.yaml) | other | 2022-07-13 |  |  |
| [2022-07_binance-reportedly-violated-sanctions.yaml](other/2022-07_binance-reportedly-violated-sanctions.yaml) | other | 2022-07-11 |  |  |
| [2022-07_vauld-deficit-revealed.yaml](other/2022-07_vauld-deficit-revealed.yaml) | other | 2022-07-11 |  |  |
| [2022-07_citizen-finance-hack.yaml](data-leak/2022-07_citizen-finance-hack.yaml) | data-leak | 2022-07-11 |  |  |
| [2022-07_uniswap-phishing-attack.yaml](data-leak/2022-07_uniswap-phishing-attack.yaml) | data-leak | 2022-07-11 |  |  |
| [2022-07_omni-hack.yaml](data-leak/2022-07_omni-hack.yaml) | data-leak | 2022-07-10 |  |  |
| [2022-07_bifrost-hack.yaml](data-leak/2022-07_bifrost-hack.yaml) | data-leak | 2022-07-10 |  |  |
| [2022-07_coinflex-sues-roger-ver.yaml](other/2022-07_coinflex-sues-roger-ver.yaml) | other | 2022-07-09 |  |  |
| [2022-07_vauld-seeks-creditor-protection.yaml](other/2022-07_vauld-seeks-creditor-protection.yaml) | other | 2022-07-08 |  |  |
| [2022-07_three-arrows-capital-founders-abscond.yaml](other/2022-07_three-arrows-capital-founders-abscond.yaml) | other | 2022-07-08 |  |  |
| [2022-07_rogers-communications-network-outage.yaml](other/2022-07_rogers-communications-network-outage.yaml) | other | 2022-07-08 |  |  |
| [2022-07_blockchain-com-exposure-to-three-arrows-capital.yaml](other/2022-07_blockchain-com-exposure-to-three-arrows-capital.yaml) | other | 2022-07-08 |  |  |
| [2022-07_hypernet-labs-shuts-down.yaml](other/2022-07_hypernet-labs-shuts-down.yaml) | other | 2022-07-08 |  |  |
| [2022-07_former-celsius-asset-manager-accuses-them-of-ponzi-scheme.yaml](other/2022-07_former-celsius-asset-manager-accuses-them-of-ponzi-scheme.yaml) | other | 2022-07-07 |  |  |
| [2022-07_2gether-closes-accounts.yaml](other/2022-07_2gether-closes-accounts.yaml) | other | 2022-07-07 |  |  |
| [2022-07_reddit-nfts.yaml](other/2022-07_reddit-nfts.yaml) | other | 2022-07-07 |  |  |
| [2022-07_bitstamp-fails-to-announce-inactivity-fee.yaml](other/2022-07_bitstamp-fails-to-announce-inactivity-fee.yaml) | other | 2022-07-06 |  |  |
| [2022-07_uprise-collapse.yaml](other/2022-07_uprise-collapse.yaml) | other | 2022-07-06 |  |  |
| [2022-07_genesis-exposure-to-three-arrows-capital-and-babel-finance.yaml](other/2022-07_genesis-exposure-to-three-arrows-capital-and-babel-finance.yaml) | other | 2022-07-06 |  |  |
| [2022-07_voyager-digital-bankruptcy.yaml](other/2022-07_voyager-digital-bankruptcy.yaml) | other | 2022-07-06 |  |  |
| [2022-07_decentral-bank-bug.yaml](other/2022-07_decentral-bank-bug.yaml) | other | 2022-07-06 |  |  |
| [2022-07_us-office-of-government-ethics-issues-crypto-guidance.yaml](other/2022-07_us-office-of-government-ethics-issues-crypto-guidance.yaml) | other | 2022-07-05 |  |  |
| [2022-07_polium-announces-vaporware.yaml](other/2022-07_polium-announces-vaporware.yaml) | other | 2022-07-05 |  |  |
| [2022-07_vauld-halts-withdrawals.yaml](other/2022-07_vauld-halts-withdrawals.yaml) | other | 2022-07-04 |  |  |
| [2022-07_coinloin-limits-withdrawals.yaml](other/2022-07_coinloin-limits-withdrawals.yaml) | other | 2022-07-04 |  |  |
| [2022-07_british-army-social-media-accounts-hacked.yaml](data-leak/2022-07_british-army-social-media-accounts-hacked.yaml) | data-leak | 2022-07-03 |  |  |
| [2022-07_crema-finance-hack.yaml](data-leak/2022-07_crema-finance-hack.yaml) | data-leak | 2022-07-02 |  |  |
| [2022-07_meta-shuts-down-novi.yaml](other/2022-07_meta-shuts-down-novi.yaml) | other | 2022-07-01 |  |  |
| [2022-07_edfinancial-and-oklahoma-student-loan-authority-nelnet-servicing.yaml](supply-chain/2022-07_edfinancial-and-oklahoma-student-loan-authority-nelnet-servicing.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_toronto-symphony-orchestra-wordfly.yaml](supply-chain/2022-07_toronto-symphony-orchestra-wordfly.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_ankr-hack.yaml](data-leak/2022-07_ankr-hack.yaml) | data-leak | 2022-07-01 |  |  |
| [2022-07_quixotic-nft-marketplace-hack.yaml](data-leak/2022-07_quixotic-nft-marketplace-hack.yaml) | data-leak | 2022-07-01 |  |  |
| [2022-07_american-health-imaging-banner-medical-group-belle-point-dental-duck-creek-family-dental-partners-in-periodontics-and-652-organizations-professional-finance-company.yaml](supply-chain/2022-07_american-health-imaging-banner-medical-group-belle-point-dental-duck-creek-family-dental-partners-in-periodontics-and-652-organizations-professional-finance-company.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_arlington-skin-virtual-private-network-solu.yaml](supply-chain/2022-07_arlington-skin-virtual-private-network-solu.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_boeing-employees-credit-union-not-disclosed.yaml](supply-chain/2022-07_boeing-employees-credit-union-not-disclosed.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_celsius-customer-io.yaml](supply-chain/2022-07_celsius-customer-io.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_sound-health-and-wellness-trust-zenith-american-solutions.yaml](supply-chain/2022-07_sound-health-and-wellness-trust-zenith-american-solutions.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-07_voyager-digital-suspends-withdrawals.yaml](other/2022-07_voyager-digital-suspends-withdrawals.yaml) | other | 2022-07-01 |  |  |
| [2022-07_mid-westchester-anesthesia-services-not-disclosed.yaml](supply-chain/2022-07_mid-westchester-anesthesia-services-not-disclosed.yaml) | supply-chain | 2022-07-01 |  |  |
| [2022-06_titanium-blockchain-infrastructure-services-ceo-charged.yaml](other/2022-06_titanium-blockchain-infrastructure-services-ceo-charged.yaml) | other | 2022-06-30 |  |  |
| [2022-06_mirror-trading-international-charged.yaml](other/2022-06_mirror-trading-international-charged.yaml) | other | 2022-06-30 |  |  |
| [2022-06_blockfi-nears-acquisition-deal-with-ftx.yaml](other/2022-06_blockfi-nears-acquisition-deal-with-ftx.yaml) | other | 2022-06-30 |  |  |
| [2022-06_empiresx-ponzi-scheme.yaml](other/2022-06_empiresx-ponzi-scheme.yaml) | other | 2022-06-30 |  |  |
| [2022-06_coca-cola-launches-pride-nfts.yaml](other/2022-06_coca-cola-launches-pride-nfts.yaml) | other | 2022-06-30 |  |  |
| [2022-06_circle-society-owner-charged.yaml](other/2022-06_circle-society-owner-charged.yaml) | other | 2022-06-30 |  |  |
| [2022-06_baller-apes-rug-puller-charged.yaml](other/2022-06_baller-apes-rug-puller-charged.yaml) | other | 2022-06-30 |  |  |
| [2022-06_coinbase-provides-ice-with-analytics-tools.yaml](other/2022-06_coinbase-provides-ice-with-analytics-tools.yaml) | other | 2022-06-29 |  |  |
| [2022-06_sec-rejects-bitcoin-etf.yaml](other/2022-06_sec-rejects-bitcoin-etf.yaml) | other | 2022-06-29 |  |  |
| [2022-06_three-arrows-capital-collapse.yaml](other/2022-06_three-arrows-capital-collapse.yaml) | other | 2022-06-29 |  |  |
| [2022-06_w3itch-io-steals-website-code-and-games.yaml](other/2022-06_w3itch-io-steals-website-code-and-games.yaml) | other | 2022-06-29 |  |  |
| [2022-06_compass-mining-ceo-and-cfo-resign.yaml](other/2022-06_compass-mining-ceo-and-cfo-resign.yaml) | other | 2022-06-28 |  |  |
| [2022-06_xcarnival-hack.yaml](data-leak/2022-06_xcarnival-hack.yaml) | data-leak | 2022-06-26 |  |  |
| [2022-06_no-one-wants-chevrolet-s-nft.yaml](other/2022-06_no-one-wants-chevrolet-s-nft.yaml) | other | 2022-06-25 |  |  |
| [2022-06_bored-amp-hungry-crypto-payments-update.yaml](other/2022-06_bored-amp-hungry-crypto-payments-update.yaml) | other | 2022-06-24 |  |  |
| [2022-06_bitpanda-layoffs.yaml](other/2022-06_bitpanda-layoffs.yaml) | other | 2022-06-24 |  |  |
| [2022-06_bored-hungry-crypto-payments-update.yaml](other/2022-06_bored-hungry-crypto-payments-update.yaml) | other | 2022-06-24 |  |  |
| [2022-06_lummis-and-gillibrand-solicit-feedback-on-bill-via-github.yaml](other/2022-06_lummis-and-gillibrand-solicit-feedback-on-bill-via-github.yaml) | other | 2022-06-23 |  |  |
| [2022-06_coinflex-halts-withdrawals.yaml](other/2022-06_coinflex-halts-withdrawals.yaml) | other | 2022-06-23 |  |  |
| [2022-06_horizon-bridge-hack.yaml](data-leak/2022-06_horizon-bridge-hack.yaml) | data-leak | 2022-06-23 |  |  |
| [2022-06_invictus-capital-halts-withdrawals.yaml](other/2022-06_invictus-capital-halts-withdrawals.yaml) | other | 2022-06-22 |  |  |
| [2022-06_hostess-announces-twinkcoin-cakes.yaml](other/2022-06_hostess-announces-twinkcoin-cakes.yaml) | other | 2022-06-22 |  |  |
| [2022-06_bybit-settlement-kucoin-ban-in-ontario.yaml](other/2022-06_bybit-settlement-kucoin-ban-in-ontario.yaml) | other | 2022-06-22 |  |  |
| [2022-06_voyager-digital-limits-withdrawals.yaml](other/2022-06_voyager-digital-limits-withdrawals.yaml) | other | 2022-06-22 |  |  |
| [2022-06_blockfi-bailed-out-by-ftx.yaml](other/2022-06_blockfi-bailed-out-by-ftx.yaml) | other | 2022-06-21 |  |  |
| [2022-06_vauld-layoffs.yaml](other/2022-06_vauld-layoffs.yaml) | other | 2022-06-21 |  |  |
| [2022-06_terraforms-labs-employees-banned-from-leaving-korea.yaml](other/2022-06_terraforms-labs-employees-banned-from-leaving-korea.yaml) | other | 2022-06-20 |  |  |
| [2022-06_qanon-influencer-scams.yaml](data-leak/2022-06_qanon-influencer-scams.yaml) | data-leak | 2022-06-20 |  |  |
| [2022-06_bybit-plans-layoffs.yaml](other/2022-06_bybit-plans-layoffs.yaml) | other | 2022-06-20 |  |  |
| [2022-06_hoo-halts-withdrawals.yaml](other/2022-06_hoo-halts-withdrawals.yaml) | other | 2022-06-19 |  |  |
| [2022-06_lacoste-discord-hacked.yaml](data-leak/2022-06_lacoste-discord-hacked.yaml) | data-leak | 2022-06-19 |  |  |
| [2022-06_solend-dao-passes-proposal-to-take-over-account.yaml](other/2022-06_solend-dao-passes-proposal-to-take-over-account.yaml) | other | 2022-06-19 |  |  |
| [2022-06_bancor-pauses-impermanent-loss-protection.yaml](other/2022-06_bancor-pauses-impermanent-loss-protection.yaml) | other | 2022-06-19 |  |  |
| [2022-06_magic-internet-money-wobbles.yaml](other/2022-06_magic-internet-money-wobbles.yaml) | other | 2022-06-18 |  |  |
| [2022-06_babel-finance-halts-withdrawals.yaml](other/2022-06_babel-finance-halts-withdrawals.yaml) | other | 2022-06-17 |  |  |
| [2022-06_makerdao-halts-aave-dai-direct-deposit.yaml](other/2022-06_makerdao-halts-aave-dai-direct-deposit.yaml) | other | 2022-06-17 |  |  |
| [2022-06_three-arrows-capital-looks-for-bailout.yaml](other/2022-06_three-arrows-capital-looks-for-bailout.yaml) | other | 2022-06-17 |  |  |
| [2022-06_finblox-limits-withdrawals.yaml](other/2022-06_finblox-limits-withdrawals.yaml) | other | 2022-06-16 |  |  |
| [2022-06_inverse-finance-hack-35-2.yaml](data-leak/2022-06_inverse-finance-hack-35-2.yaml) | data-leak | 2022-06-16 |  |  |
| [2022-06_inverse-finance-hack-2.yaml](data-leak/2022-06_inverse-finance-hack-2.yaml) | data-leak | 2022-06-16 |  |  |
| [2022-06_aex-limits-withdrawals.yaml](other/2022-06_aex-limits-withdrawals.yaml) | other | 2022-06-16 |  |  |
| [2022-06_anna-delvey-plans-nfts.yaml](other/2022-06_anna-delvey-plans-nfts.yaml) | other | 2022-06-16 |  |  |
| [2022-06_8-blocks-capital-calls-to-freeze-three-arrows-capital-funds.yaml](other/2022-06_8-blocks-capital-calls-to-freeze-three-arrows-capital-funds.yaml) | other | 2022-06-15 |  |  |
| [2022-06_kraken-announces-new-culture.yaml](other/2022-06_kraken-announces-new-culture.yaml) | other | 2022-06-15 |  |  |
| [2022-06_blockfi-fined.yaml](other/2022-06_blockfi-fined.yaml) | other | 2022-06-14 |  |  |
| [2022-06_three-arrows-capital-insolvency.yaml](other/2022-06_three-arrows-capital-insolvency.yaml) | other | 2022-06-14 |  |  |
| [2022-06_axie-infinity-downplays-job-creation-claims.yaml](other/2022-06_axie-infinity-downplays-job-creation-claims.yaml) | other | 2022-06-14 |  |  |
| [2022-06_merit-dao-votes-to-renege-on-deal.yaml](other/2022-06_merit-dao-votes-to-renege-on-deal.yaml) | other | 2022-06-14 |  |  |
| [2022-06_coinbase-layoffs.yaml](other/2022-06_coinbase-layoffs.yaml) | other | 2022-06-14 |  |  |
| [2022-06_sec-insider-trading-probe.yaml](other/2022-06_sec-insider-trading-probe.yaml) | other | 2022-06-14 |  |  |
| [2022-06_known-origin-discord-compromise.yaml](data-leak/2022-06_known-origin-discord-compromise.yaml) | data-leak | 2022-06-14 |  |  |
| [2022-06_usdd-wobbles.yaml](other/2022-06_usdd-wobbles.yaml) | other | 2022-06-13 |  |  |
| [2022-06_nft-collector-sells-at-huge-loss.yaml](other/2022-06_nft-collector-sells-at-huge-loss.yaml) | other | 2022-06-13 |  |  |
| [2022-06_crypto-com-and-blockfi-layoffs.yaml](other/2022-06_crypto-com-and-blockfi-layoffs.yaml) | other | 2022-06-13 |  |  |
| [2022-06_binance-us-class-action-filed.yaml](other/2022-06_binance-us-class-action-filed.yaml) | other | 2022-06-13 |  |  |
| [2022-06_binance-stuck-transaction.yaml](other/2022-06_binance-stuck-transaction.yaml) | other | 2022-06-13 |  |  |
| [2022-06_celsius-pauses-withdrawals.yaml](other/2022-06_celsius-pauses-withdrawals.yaml) | other | 2022-06-12 |  |  |
| [2022-06_seaflower-hacking-group-identified.yaml](data-leak/2022-06_seaflower-hacking-group-identified.yaml) | data-leak | 2022-06-12 |  |  |
| [2022-06_steth-loses-peg.yaml](other/2022-06_steth-loses-peg.yaml) | other | 2022-06-12 |  |  |
| [2022-06_el-universal-twitter-account-hack.yaml](data-leak/2022-06_el-universal-twitter-account-hack.yaml) | data-leak | 2022-06-09 |  |  |
| [2022-06_i-el-universal-i-twitter-account-hack.yaml](data-leak/2022-06_i-el-universal-i-twitter-account-hack.yaml) | data-leak | 2022-06-09 |  |  |
| [2022-06_offline-cash-project-announcement.yaml](other/2022-06_offline-cash-project-announcement.yaml) | other | 2022-06-09 |  |  |
| [2022-06_madison-cawthorn-belatedly-reports-trades.yaml](other/2022-06_madison-cawthorn-belatedly-reports-trades.yaml) | other | 2022-06-08 |  |  |
| [2022-06_players-only-nft-rug-pull.yaml](other/2022-06_players-only-nft-rug-pull.yaml) | other | 2022-06-08 |  |  |
| [2022-06_baby-elon-coin-rug-pull.yaml](other/2022-06_baby-elon-coin-rug-pull.yaml) | other | 2022-06-08 |  |  |
| [2022-06_osmosis-chain-attack.yaml](other/2022-06_osmosis-chain-attack.yaml) | other | 2022-06-08 |  |  |
| [2022-06_optimism-tokens-sent-to-wrong-address.yaml](other/2022-06_optimism-tokens-sent-to-wrong-address.yaml) | other | 2022-06-08 |  |  |
| [2022-06_apollox-exchange-attack.yaml](data-leak/2022-06_apollox-exchange-attack.yaml) | data-leak | 2022-06-08 |  |  |
| [2022-06_gym-network-hack.yaml](data-leak/2022-06_gym-network-hack.yaml) | data-leak | 2022-06-08 |  |  |
| [2022-06_lummis-and-gillibrand-propose-crypto-bill.yaml](other/2022-06_lummis-and-gillibrand-propose-crypto-bill.yaml) | other | 2022-06-07 |  |  |
| [2022-06_sec-reportedly-reviewing-bnb-token.yaml](other/2022-06_sec-reportedly-reviewing-bnb-token.yaml) | other | 2022-06-06 |  |  |
| [2022-06_early-june-2022-discord-compromises.yaml](data-leak/2022-06_early-june-2022-discord-compromises.yaml) | data-leak | 2022-06-06 |  |  |
| [2022-06_i-grit-i-blockchain-game-demo-fails-to-impress.yaml](other/2022-06_i-grit-i-blockchain-game-demo-fails-to-impress.yaml) | other | 2022-06-06 |  |  |
| [2022-06_grit-blockchain-game-demo-fails-to-impress.yaml](other/2022-06_grit-blockchain-game-demo-fails-to-impress.yaml) | other | 2022-06-06 |  |  |
| [2022-06_reuters-binance-money-laundering-report.yaml](other/2022-06_reuters-binance-money-laundering-report.yaml) | other | 2022-06-06 |  |  |
| [2022-06_maiar-exchange-hack.yaml](data-leak/2022-06_maiar-exchange-hack.yaml) | data-leak | 2022-06-05 |  |  |
| [2022-06_bored-apes-discord-compromise.yaml](data-leak/2022-06_bored-apes-discord-compromise.yaml) | data-leak | 2022-06-04 |  |  |
| [2022-06_topshotkief-nft-theft.yaml](data-leak/2022-06_topshotkief-nft-theft.yaml) | data-leak | 2022-06-04 |  |  |
| [2022-06_new-york-crypto-mining-moratorium.yaml](other/2022-06_new-york-crypto-mining-moratorium.yaml) | other | 2022-06-03 |  |  |
| [2022-06_ftc-reports-329-million-in-crypto-scams-in-q1.yaml](other/2022-06_ftc-reports-329-million-in-crypto-scams-in-q1.yaml) | other | 2022-06-03 |  |  |
| [2022-06_timechain-collapse.yaml](other/2022-06_timechain-collapse.yaml) | other | 2022-06-03 |  |  |
| [2022-06_goblin-asses-project-preempted.yaml](other/2022-06_goblin-asses-project-preempted.yaml) | other | 2022-06-02 |  |  |
| [2022-06_gemini-sued-by-cftc.yaml](other/2022-06_gemini-sued-by-cftc.yaml) | other | 2022-06-02 |  |  |
| [2022-06_landlord-puts-security-deposit-into-bitcoin.yaml](other/2022-06_landlord-puts-security-deposit-into-bitcoin.yaml) | other | 2022-06-02 |  |  |
| [2022-06_gemini-layoffs.yaml](other/2022-06_gemini-layoffs.yaml) | other | 2022-06-02 |  |  |
| [2022-06_forest-tiger-pro-rug-pull.yaml](other/2022-06_forest-tiger-pro-rug-pull.yaml) | other | 2022-06-02 |  |  |
| [2022-06_coinbase-rescinds-job-offers.yaml](other/2022-06_coinbase-rescinds-job-offers.yaml) | other | 2022-06-02 |  |  |
| [2022-06_animoon-rug-pull.yaml](other/2022-06_animoon-rug-pull.yaml) | other | 2022-06-02 |  |  |
| [2022-06_bored-ape-typo.yaml](other/2022-06_bored-ape-typo.yaml) | other | 2022-06-01 |  |  |
| [2022-06_opensea-customer-io.yaml](supply-chain/2022-06_opensea-customer-io.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-06_letter-in-support-of-responsible-fintech-policy.yaml](other/2022-06_letter-in-support-of-responsible-fintech-policy.yaml) | other | 2022-06-01 |  |  |
| [2022-06_burman-zuckerbrod-ophthalmology-associates-fishman-vision-eyecare-leaders.yaml](supply-chain/2022-06_burman-zuckerbrod-ophthalmology-associates-fishman-vision-eyecare-leaders.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-06_blue-cross-and-blue-shield-of-massachusetts-lifeworks-us.yaml](supply-chain/2022-06_blue-cross-and-blue-shield-of-massachusetts-lifeworks-us.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-08_twilio-0ktapus.yaml](credential-theft/2022-08_twilio-0ktapus.yaml) | credential-theft | 2022-06-01 |  |  |
| [2022-06_marriott-social-engineering-20gb.yaml](credential-theft/2022-06_marriott-social-engineering-20gb.yaml) | credential-theft | 2022-06-01 |  |  |
| [2022-06_baptist-health-system-resolute-health-hospital-the-hospitals-of-providence-memorial-campus-valley-baptist-medical-center-brownsville-valley-baptist-medical-center-harlingen-conifer-revenue-cycle-soluti.yaml](supply-chain/2022-06_baptist-health-system-resolute-health-hospital-the-hospitals-of-providence-memorial-campus-valley-baptist-medical-center-brownsville-valley-baptist-medical-center-harlingen-conifer-revenue-cycle-soluti.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-06_opensea-insider-trader-arrested.yaml](other/2022-06_opensea-insider-trader-arrested.yaml) | other | 2022-06-01 |  |  |
| [2022-06_colorado-springs-utilities-not-disclosed.yaml](supply-chain/2022-06_colorado-springs-utilities-not-disclosed.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-06_priority-health-warner-norcross-judd.yaml](supply-chain/2022-06_priority-health-warner-norcross-judd.yaml) | supply-chain | 2022-06-01 |  |  |
| [2022-06_i-guardian-i-editor-impersonated.yaml](other/2022-06_i-guardian-i-editor-impersonated.yaml) | other | 2022-06-01 |  |  |
| [2022-06_guardian-editor-impersonated.yaml](other/2022-06_guardian-editor-impersonated.yaml) | other | 2022-06-01 |  |  |
| [2022-06_solana-outage.yaml](other/2022-06_solana-outage.yaml) | other | 2022-06-01 |  |  |
| [2022-05_toronto-comic-arts-festival-nft-artist-controversy.yaml](other/2022-05_toronto-comic-arts-festival-nft-artist-controversy.yaml) | other | 2022-05-30 |  |  |
| [2022-05_mirror-protocol-exploit.yaml](other/2022-05_mirror-protocol-exploit.yaml) | other | 2022-05-30 |  |  |
| [2022-05_bored-ape-typo.yaml](other/2022-05_bored-ape-typo.yaml) | other | 2022-05-30 |  |  |
| [2022-05_superlative-apes-rug-pull.yaml](other/2022-05_superlative-apes-rug-pull.yaml) | other | 2022-05-30 |  |  |
| [2022-05_luna-airdrop-goes-to-thief.yaml](other/2022-05_luna-airdrop-goes-to-thief.yaml) | other | 2022-05-28 |  |  |
| [2022-05_elon-musk-deepfake.yaml](data-leak/2022-05_elon-musk-deepfake.yaml) | data-leak | 2022-05-27 |  |  |
| [2022-05_pokemoney-rug-pull.yaml](other/2022-05_pokemoney-rug-pull.yaml) | other | 2022-05-27 |  |  |
| [2022-05_mirror-protocol-vulnerability.yaml](data-leak/2022-05_mirror-protocol-vulnerability.yaml) | data-leak | 2022-05-26 |  |  |
| [2022-05_solana-clock-drift.yaml](other/2022-05_solana-clock-drift.yaml) | other | 2022-05-26 |  |  |
| [2022-05_bitso-layoffs.yaml](other/2022-05_bitso-layoffs.yaml) | other | 2022-05-26 |  |  |
| [2022-05_terra-2-0-announcement.yaml](other/2022-05_terra-2-0-announcement.yaml) | other | 2022-05-25 |  |  |
| [2022-05_decentraworld-rug-pull.yaml](other/2022-05_decentraworld-rug-pull.yaml) | other | 2022-05-24 |  |  |
| [2022-05_cisco-yanluowang-mfa-fatigue.yaml](credential-theft/2022-05_cisco-yanluowang-mfa-fatigue.yaml) | credential-theft | 2022-05-24 |  |  |
| [2022-05_digital-ornithologist-nft-theft.yaml](data-leak/2022-05_digital-ornithologist-nft-theft.yaml) | data-leak | 2022-05-24 |  |  |
| [2022-05_adam-neumann-gets-into-crypto.yaml](other/2022-05_adam-neumann-gets-into-crypto.yaml) | other | 2022-05-24 |  |  |
| [2022-05_jonny-reid-wallet-compromise.yaml](other/2022-05_jonny-reid-wallet-compromise.yaml) | other | 2022-05-23 |  |  |
| [2022-05_beeple-twitter-hack.yaml](data-leak/2022-05_beeple-twitter-hack.yaml) | data-leak | 2022-05-22 |  |  |
| [2022-05_johnny-reid-wallet-hack.yaml](data-leak/2022-05_johnny-reid-wallet-hack.yaml) | data-leak | 2022-05-22 |  |  |
| [2022-05_milady-founders-controversy.yaml](other/2022-05_milady-founders-controversy.yaml) | other | 2022-05-22 |  |  |
| [2022-05_bdollar-exploit.yaml](data-leak/2022-05_bdollar-exploit.yaml) | data-leak | 2022-05-21 |  |  |
| [2022-05_humbl-class-action.yaml](other/2022-05_humbl-class-action.yaml) | other | 2022-05-20 |  |  |
| [2022-05_reptilian-renegades-rug-pull.yaml](other/2022-05_reptilian-renegades-rug-pull.yaml) | other | 2022-05-19 |  |  |
| [2022-05_stablegains-collapse.yaml](other/2022-05_stablegains-collapse.yaml) | other | 2022-05-19 |  |  |
| [2022-05_qan-bridge-hack-1.yaml](data-leak/2022-05_qan-bridge-hack-1.yaml) | data-leak | 2022-05-18 |  |  |
| [2022-05_qan-bridge-hack-35-1.yaml](data-leak/2022-05_qan-bridge-hack-35-1.yaml) | data-leak | 2022-05-18 |  |  |
| [2022-05_feminist-metaverse-token-exploit.yaml](data-leak/2022-05_feminist-metaverse-token-exploit.yaml) | data-leak | 2022-05-18 |  |  |
| [2022-05_terra-class-action-lawsuits-filed.yaml](other/2022-05_terra-class-action-lawsuits-filed.yaml) | other | 2022-05-18 |  |  |
| [2022-05_terraform-labs-legal-team-resigns.yaml](other/2022-05_terraform-labs-legal-team-resigns.yaml) | other | 2022-05-17 |  |  |
| [2022-05_seth-green-nft-theft.yaml](data-leak/2022-05_seth-green-nft-theft.yaml) | data-leak | 2022-05-17 |  |  |
| [2022-05_multiple-discords-compromised.yaml](data-leak/2022-05_multiple-discords-compromised.yaml) | data-leak | 2022-05-17 |  |  |
| [2022-05_scream-bad-debt.yaml](other/2022-05_scream-bad-debt.yaml) | other | 2022-05-16 |  |  |
| [2022-05_cz-tweets-about-binance-s-terra-luna-holdings.yaml](other/2022-05_cz-tweets-about-binance-s-terra-luna-holdings.yaml) | other | 2022-05-16 |  |  |
| [2022-05_jason-vorhees-charged.yaml](other/2022-05_jason-vorhees-charged.yaml) | other | 2022-05-16 |  |  |
| [2022-05_luna-foundation-guard-report.yaml](other/2022-05_luna-foundation-guard-report.yaml) | other | 2022-05-16 |  |  |
| [2022-05_people-want-accounting-of-terra-s-bitcoin-reserves.yaml](other/2022-05_people-want-accounting-of-terra-s-bitcoin-reserves.yaml) | other | 2022-05-15 |  |  |
| [2022-05_feed-every-gorilla-token-exploit.yaml](data-leak/2022-05_feed-every-gorilla-token-exploit.yaml) | data-leak | 2022-05-15 |  |  |
| [2022-05_dei-loses-peg.yaml](other/2022-05_dei-loses-peg.yaml) | other | 2022-05-15 |  |  |
| [2022-05_insurace-shortens-claims-window.yaml](other/2022-05_insurace-shortens-claims-window.yaml) | other | 2022-05-13 |  |  |
| [2022-05_crypto-com-reverses-luna-trades.yaml](other/2022-05_crypto-com-reverses-luna-trades.yaml) | other | 2022-05-13 |  |  |
| [2022-05_phishing-attack-via-etherscan-and-coingecko.yaml](data-leak/2022-05_phishing-attack-via-etherscan-and-coingecko.yaml) | data-leak | 2022-05-13 |  |  |
| [2022-05_spiritswap-domain-hijacking-attack.yaml](data-leak/2022-05_spiritswap-domain-hijacking-attack.yaml) | data-leak | 2022-05-13 |  |  |
| [2022-05_terra-blockchain-halted.yaml](other/2022-05_terra-blockchain-halted.yaml) | other | 2022-05-12 |  |  |
| [2022-05_eminifx-ceo-charged.yaml](other/2022-05_eminifx-ceo-charged.yaml) | other | 2022-05-12 |  |  |
| [2022-05_tether-loses-peg.yaml](other/2022-05_tether-loses-peg.yaml) | other | 2022-05-12 |  |  |
| [2022-05_terra-oracle-attacks.yaml](data-leak/2022-05_terra-oracle-attacks.yaml) | data-leak | 2022-05-12 |  |  |
| [2022-05_do-kwon-revealed-to-have-run-other-stablecoin-project.yaml](other/2022-05_do-kwon-revealed-to-have-run-other-stablecoin-project.yaml) | other | 2022-05-11 |  |  |
| [2022-05_luna-token-price-crashes.yaml](other/2022-05_luna-token-price-crashes.yaml) | other | 2022-05-11 |  |  |
| [2022-05_ruja-ignatova-added-to-most-wanted-list.yaml](other/2022-05_ruja-ignatova-added-to-most-wanted-list.yaml) | other | 2022-05-11 |  |  |
| [2022-05_bitprime-pauses-trading.yaml](other/2022-05_bitprime-pauses-trading.yaml) | other | 2022-05-11 |  |  |
| [2022-05_coinbase-adds-bankruptcy-language-to-quarterly-report.yaml](other/2022-05_coinbase-adds-bankruptcy-language-to-quarterly-report.yaml) | other | 2022-05-10 |  |  |
| [2022-05_michael-owen-launches-nfts.yaml](other/2022-05_michael-owen-launches-nfts.yaml) | other | 2022-05-09 |  |  |
| [2022-05_g-o-a-t-token-rug-pull.yaml](other/2022-05_g-o-a-t-token-rug-pull.yaml) | other | 2022-05-09 |  |  |
| [2022-05_azuki-founder-admits-to-rug-pulls.yaml](other/2022-05_azuki-founder-admits-to-rug-pulls.yaml) | other | 2022-05-09 |  |  |
| [2022-05_terra-luna-collapse.yaml](other/2022-05_terra-luna-collapse.yaml) | other | 2022-05-09 |  |  |
| [2022-05_fortress-protocol-hack.yaml](data-leak/2022-05_fortress-protocol-hack.yaml) | data-leak | 2022-05-08 |  |  |
| [2022-05_hunter-rug-pull.yaml](other/2022-05_hunter-rug-pull.yaml) | other | 2022-05-08 |  |  |
| [2022-05_cashera-rug-pull.yaml](other/2022-05_cashera-rug-pull.yaml) | other | 2022-05-08 |  |  |
| [2022-05_fury-of-the-fur-rug-pull.yaml](other/2022-05_fury-of-the-fur-rug-pull.yaml) | other | 2022-05-07 |  |  |
| [2022-05_coinbase-nft-marketplace-flops.yaml](other/2022-05_coinbase-nft-marketplace-flops.yaml) | other | 2022-05-07 |  |  |
| [2022-05_day-of-defeat-rug-pull.yaml](other/2022-05_day-of-defeat-rug-pull.yaml) | other | 2022-05-06 |  |  |
| [2022-05_ferrari-domain-hijacked.yaml](data-leak/2022-05_ferrari-domain-hijacked.yaml) | data-leak | 2022-05-06 |  |  |
| [2022-05_ofac-sanctions-blender.yaml](other/2022-05_ofac-sanctions-blender.yaml) | other | 2022-05-06 |  |  |
| [2022-05_opensea-discord-hack.yaml](data-leak/2022-05_opensea-discord-hack.yaml) | data-leak | 2022-05-06 |  |  |
| [2022-05_mining-capital-coin-ceo-indicted.yaml](other/2022-05_mining-capital-coin-ceo-indicted.yaml) | other | 2022-05-05 |  |  |
| [2022-05_pragma-rug-pull.yaml](other/2022-05_pragma-rug-pull.yaml) | other | 2022-05-05 |  |  |
| [2022-05_early-may-2022-double-your-money-scams.yaml](data-leak/2022-05_early-may-2022-double-your-money-scams.yaml) | data-leak | 2022-05-05 |  |  |
| [2022-05_ape-holders-can-use-multiple-slurp-juices-on-a-single-ape.yaml](other/2022-05_ape-holders-can-use-multiple-slurp-juices-on-a-single-ape.yaml) | other | 2022-05-04 |  |  |
| [2022-05_juno-sends-funds-to-wrong-address.yaml](other/2022-05_juno-sends-funds-to-wrong-address.yaml) | other | 2022-05-04 |  |  |
| [2022-05_mm-finance-hack.yaml](data-leak/2022-05_mm-finance-hack.yaml) | data-leak | 2022-05-04 |  |  |
| [2022-05_square-enix-sells-ip-to-get-into-blockchain-gaming.yaml](other/2022-05_square-enix-sells-ip-to-get-into-blockchain-gaming.yaml) | other | 2022-05-03 |  |  |
| [2022-05_nft-sales-down-92.yaml](other/2022-05_nft-sales-down-92.yaml) | other | 2022-05-03 |  |  |
| [2022-05_vatican-plans-metaverse-nft-gallery.yaml](other/2022-05_vatican-plans-metaverse-nft-gallery.yaml) | other | 2022-05-02 |  |  |
| [2022-05_k12-schools-in-ny-illuminate-education.yaml](supply-chain/2022-05_k12-schools-in-ny-illuminate-education.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-05_evergreenhealth-mycare.yaml](supply-chain/2022-05_evergreenhealth-mycare.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-05_juno-whale-threatens-to-sue.yaml](other/2022-05_juno-whale-threatens-to-sue.yaml) | other | 2022-05-01 |  |  |
| [2022-05_mangatoon-elasticsearch.yaml](supply-chain/2022-05_mangatoon-elasticsearch.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-05_hospitals-in-northern-california-partnership-healthplan-of-ca.yaml](supply-chain/2022-05_hospitals-in-northern-california-partnership-healthplan-of-ca.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-05_st-luke-s-kaye-smith.yaml](supply-chain/2022-05_st-luke-s-kaye-smith.yaml) | supply-chain | 2022-05-01 |  |  |
| [2022-05_wikimedia-foundation-stops-accepting-cryptocurrency-donations.yaml](other/2022-05_wikimedia-foundation-stops-accepting-cryptocurrency-donations.yaml) | other | 2022-05-01 |  |  |
| [2022-04_otherside-launch-spikes-gas-fees.yaml](other/2022-04_otherside-launch-spikes-gas-fees.yaml) | other | 2022-04-30 |  |  |
| [2022-04_teenage-mutant-ninja-turtles-project-buys-forged-contract.yaml](other/2022-04_teenage-mutant-ninja-turtles-project-buys-forged-contract.yaml) | other | 2022-04-30 |  |  |
| [2022-04_fei-protocol-hack.yaml](data-leak/2022-04_fei-protocol-hack.yaml) | data-leak | 2022-04-30 |  |  |
| [2022-04_saddle-finance-hack-2.yaml](data-leak/2022-04_saddle-finance-hack-2.yaml) | data-leak | 2022-04-30 |  |  |
| [2022-04_solana-outage.yaml](other/2022-04_solana-outage.yaml) | other | 2022-04-30 |  |  |
| [2022-04_otherside-phishing-sites.yaml](data-leak/2022-04_otherside-phishing-sites.yaml) | data-leak | 2022-04-30 |  |  |
| [2022-04_deus-finance-hack-35-2.yaml](data-leak/2022-04_deus-finance-hack-35-2.yaml) | data-leak | 2022-04-28 |  |  |
| [2022-04_nasgo-sec-charges.yaml](other/2022-04_nasgo-sec-charges.yaml) | other | 2022-04-28 |  |  |
| [2022-04_deus-finance-hack-2.yaml](data-leak/2022-04_deus-finance-hack-2.yaml) | data-leak | 2022-04-28 |  |  |
| [2022-04_fake-louis-vuitton-project.yaml](data-leak/2022-04_fake-louis-vuitton-project.yaml) | data-leak | 2022-04-27 |  |  |
| [2022-04_central-african-republic-adopts-bitcoin-as-legal-tender.yaml](other/2022-04_central-african-republic-adopts-bitcoin-as-legal-tender.yaml) | other | 2022-04-27 |  |  |
| [2022-04_madison-cawthorne-accused-of-insider-trading.yaml](other/2022-04_madison-cawthorne-accused-of-insider-trading.yaml) | other | 2022-04-26 |  |  |
| [2022-04_fidelity-announces-bitcoin-plans.yaml](other/2022-04_fidelity-announces-bitcoin-plans.yaml) | other | 2022-04-26 |  |  |
| [2022-04_metadocs-nft-project-launches.yaml](other/2022-04_metadocs-nft-project-launches.yaml) | other | 2022-04-25 |  |  |
| [2022-04_sam-bankman-fried-describes-yield-farming-as-a-ponzi-scheme.yaml](other/2022-04_sam-bankman-fried-describes-yield-farming-as-a-ponzi-scheme.yaml) | other | 2022-04-25 |  |  |
| [2022-05_yuma-regional-medical-center.yaml](ransomware/2022-05_yuma-regional-medical-center.yaml) | ransomware | 2022-04-25 |  |  |
| [2022-04_bored-apes-instagram-hack.yaml](data-leak/2022-04_bored-apes-instagram-hack.yaml) | data-leak | 2022-04-25 |  |  |
| [2022-04_reggie-fowler-pleads-guilty.yaml](other/2022-04_reggie-fowler-pleads-guilty.yaml) | other | 2022-04-25 |  |  |
| [2022-04_epoch-times-writers-send-crypto-mailer.yaml](other/2022-04_epoch-times-writers-send-crypto-mailer.yaml) | other | 2022-04-22 |  |  |
| [2022-04_akudreams-bug.yaml](other/2022-04_akudreams-bug.yaml) | other | 2022-04-22 |  |  |
| [2022-04_i-epoch-times-i-writers-send-crypto-mailer.yaml](other/2022-04_i-epoch-times-i-writers-send-crypto-mailer.yaml) | other | 2022-04-22 |  |  |
| [2022-04_binance-gives-putin-regime-user-data.yaml](other/2022-04_binance-gives-putin-regime-user-data.yaml) | other | 2022-04-22 |  |  |
| [2022-04_zeed-hack.yaml](data-leak/2022-04_zeed-hack.yaml) | data-leak | 2022-04-21 |  |  |
| [2022-04_binance-twitter-branded-hashtag-looks-like-a-swastika.yaml](other/2022-04_binance-twitter-branded-hashtag-looks-like-a-swastika.yaml) | other | 2022-04-20 |  |  |
| [2022-04_terra-google-ad-phishing.yaml](data-leak/2022-04_terra-google-ad-phishing.yaml) | data-leak | 2022-04-20 |  |  |
| [2022-04_rogue-society-rug-pull.yaml](other/2022-04_rogue-society-rug-pull.yaml) | other | 2022-04-20 |  |  |
| [2022-04_chedda-rug-pull.yaml](data-leak/2022-04_chedda-rug-pull.yaml) | data-leak | 2022-04-19 |  |  |
| [2022-04_0x-fxnction-wallet-compromise.yaml](data-leak/2022-04_0x-fxnction-wallet-compromise.yaml) | data-leak | 2022-04-19 |  |  |
| [2022-04_rich-bulls-club-rug-pull.yaml](other/2022-04_rich-bulls-club-rug-pull.yaml) | other | 2022-04-19 |  |  |
| [2022-04_atari-ends-business-relationship-with-token-partner.yaml](other/2022-04_atari-ends-business-relationship-with-token-partner.yaml) | other | 2022-04-18 |  |  |
| [2022-04_2omb-and-redemption-exploits.yaml](data-leak/2022-04_2omb-and-redemption-exploits.yaml) | data-leak | 2022-04-18 |  |  |
| [2022-04_metamask-icloud-backup-vulnerability.yaml](data-leak/2022-04_metamask-icloud-backup-vulnerability.yaml) | data-leak | 2022-04-18 |  |  |
| [2022-04_andre-cronje-calls-for-regulation.yaml](other/2022-04_andre-cronje-calls-for-regulation.yaml) | other | 2022-04-18 |  |  |
| [2022-04_rarible-vulnerability.yaml](other/2022-04_rarible-vulnerability.yaml) | other | 2022-04-18 |  |  |
| [2022-04_beanstalk-farms-hack.yaml](data-leak/2022-04_beanstalk-farms-hack.yaml) | data-leak | 2022-04-17 |  |  |
| [2022-04_moonbirds-sybil-attack.yaml](other/2022-04_moonbirds-sybil-attack.yaml) | other | 2022-04-16 |  |  |
| [2022-04_gem-cofounder-exposed-as-abuser.yaml](other/2022-04_gem-cofounder-exposed-as-abuser.yaml) | other | 2022-04-16 |  |  |
| [2022-04_rikkei-finance-hack.yaml](data-leak/2022-04_rikkei-finance-hack.yaml) | data-leak | 2022-04-15 |  |  |
| [2022-04_axie-infinity-hacked-linked-to-north-korea.yaml](other/2022-04_axie-infinity-hacked-linked-to-north-korea.yaml) | other | 2022-04-14 |  |  |
| [2022-04_unicorn-nodes-rug-pull.yaml](other/2022-04_unicorn-nodes-rug-pull.yaml) | other | 2022-04-14 |  |  |
| [2022-04_monero-holders-plan-bank-run.yaml](other/2022-04_monero-holders-plan-bank-run.yaml) | other | 2022-04-14 |  |  |
| [2022-04_archieverse-nft-announcement.yaml](other/2022-04_archieverse-nft-announcement.yaml) | other | 2022-04-14 |  |  |
| [2022-04_the-real-tarzann-rug-pull.yaml](other/2022-04_the-real-tarzann-rug-pull.yaml) | other | 2022-04-14 |  |  |
| [2022-04_nft-collector-gets-low-bids-for-jack-dorsey-tweet.yaml](other/2022-04_nft-collector-gets-low-bids-for-jack-dorsey-tweet.yaml) | other | 2022-04-13 |  |  |
| [2022-04_ethereum-delays-proof-of-stake.yaml](other/2022-04_ethereum-delays-proof-of-stake.yaml) | other | 2022-04-13 |  |  |
| [2022-04_rcmp-report-more-than-2-million-in-crypto-scams.yaml](data-leak/2022-04_rcmp-report-more-than-2-million-in-crypto-scams.yaml) | data-leak | 2022-04-13 |  |  |
| [2022-04_coinbase-class-action-lawsuit-filed.yaml](other/2022-04_coinbase-class-action-lawsuit-filed.yaml) | other | 2022-04-13 |  |  |
| [2022-04_texas-securities-commissioner-stops-metaverse-casino.yaml](other/2022-04_texas-securities-commissioner-stops-metaverse-casino.yaml) | other | 2022-04-13 |  |  |
| [2022-04_fake-skyverse-project.yaml](data-leak/2022-04_fake-skyverse-project.yaml) | data-leak | 2022-04-13 |  |  |
| [2022-04_elephant-money-hack.yaml](data-leak/2022-04_elephant-money-hack.yaml) | data-leak | 2022-04-12 |  |  |
| [2022-04_coinbase-insider-trading.yaml](other/2022-04_coinbase-insider-trading.yaml) | other | 2022-04-12 |  |  |
| [2022-04_celsius-ends-earn-product-in-us.yaml](other/2022-04_celsius-ends-earn-product-in-us.yaml) | other | 2022-04-12 |  |  |
| [2022-04_wikimedia-community-requests-an-end-to-crypto-donations.yaml](other/2022-04_wikimedia-community-requests-an-end-to-crypto-donations.yaml) | other | 2022-04-12 |  |  |
| [2022-04_pierce-brown-cancels-nft-project.yaml](other/2022-04_pierce-brown-cancels-nft-project.yaml) | other | 2022-04-12 |  |  |
| [2022-04_creat-future-hack.yaml](data-leak/2022-04_creat-future-hack.yaml) | data-leak | 2022-04-11 |  |  |
| [2022-04_ichi-cascading-liquidations.yaml](other/2022-04_ichi-cascading-liquidations.yaml) | other | 2022-04-11 |  |  |
| [2022-04_casper-nft-theft.yaml](data-leak/2022-04_casper-nft-theft.yaml) | data-leak | 2022-04-11 |  |  |
| [2022-04_bored-hungry-restaurant-opens.yaml](other/2022-04_bored-hungry-restaurant-opens.yaml) | other | 2022-04-09 |  |  |
| [2022-04_bored-amp-hungry-restaurant-opens.yaml](other/2022-04_bored-amp-hungry-restaurant-opens.yaml) | other | 2022-04-09 |  |  |
| [2022-04_gripnr-announcement.yaml](other/2022-04_gripnr-announcement.yaml) | other | 2022-04-08 |  |  |
| [2022-04_industroyer2-ukraine-blocked.yaml](other/2022-04_industroyer2-ukraine-blocked.yaml) | other | 2022-04-08 | Industroyer2; CaddyWiper; ORC… |  |
| [2022-04_wonderhero-bridge-hack.yaml](data-leak/2022-04_wonderhero-bridge-hack.yaml) | data-leak | 2022-04-07 |  |  |
| [2022-04_heroku-travis-oauth-token-theft.yaml](supply-chain/2022-04_heroku-travis-oauth-token-theft.yaml) | supply-chain | 2022-04-07 |  |  |
| [2022-04_starstream-hack.yaml](data-leak/2022-04_starstream-hack.yaml) | data-leak | 2022-04-07 |  |  |
| [2022-04_tyler-gaye-alleged-misappropriation.yaml](other/2022-04_tyler-gaye-alleged-misappropriation.yaml) | other | 2022-04-07 |  |  |
| [2022-04_i-star-trek-i-nft-announcement.yaml](other/2022-04_i-star-trek-i-nft-announcement.yaml) | other | 2022-04-06 |  |  |
| [2022-04_fake-revoke-cash-site.yaml](data-leak/2022-04_fake-revoke-cash-site.yaml) | data-leak | 2022-04-06 |  |  |
| [2022-04_star-trek-nft-announcement.yaml](other/2022-04_star-trek-nft-announcement.yaml) | other | 2022-04-06 |  |  |
| [2022-04_vaynersports-gas-fee-issue.yaml](other/2022-04_vaynersports-gas-fee-issue.yaml) | other | 2022-04-05 |  |  |
| [2022-04_michael-vasile-nft-theft.yaml](data-leak/2022-04_michael-vasile-nft-theft.yaml) | data-leak | 2022-04-05 |  |  |
| [2022-04_worldcoin-reports.yaml](other/2022-04_worldcoin-reports.yaml) | other | 2022-04-05 |  |  |
| [2022-04_ubisoft-abandons-tom-clancy-nft-game.yaml](other/2022-04_ubisoft-abandons-tom-clancy-nft-game.yaml) | other | 2022-04-05 |  |  |
| [2022-04_ubisoft-abandons-i-tom-clancy-i-nft-game.yaml](other/2022-04_ubisoft-abandons-i-tom-clancy-i-nft-game.yaml) | other | 2022-04-05 |  |  |
| [2022-04_bitcoin-seized-from-hacked-accounts-seller.yaml](other/2022-04_bitcoin-seized-from-hacked-accounts-seller.yaml) | other | 2022-04-04 |  |  |
| [2022-04_s27-nft-theft.yaml](data-leak/2022-04_s27-nft-theft.yaml) | data-leak | 2022-04-04 |  |  |
| [2022-04_robert-malone-announces-plans-to-dox-people-on-the-blockchain.yaml](other/2022-04_robert-malone-announces-plans-to-dox-people-on-the-blockchain.yaml) | other | 2022-04-04 |  |  |
| [2022-04_waves-stablecoin-loses-peg.yaml](other/2022-04_waves-stablecoin-loses-peg.yaml) | other | 2022-04-04 |  |  |
| [2022-04_r-place-nfts.yaml](other/2022-04_r-place-nfts.yaml) | other | 2022-04-04 |  |  |
| [2022-04_trezor-phishing-attack.yaml](data-leak/2022-04_trezor-phishing-attack.yaml) | data-leak | 2022-04-03 |  |  |
| [2022-04_inverse-finance-hack-1.yaml](data-leak/2022-04_inverse-finance-hack-1.yaml) | data-leak | 2022-04-02 |  |  |
| [2022-04_inverse-finance-hack-35-1.yaml](data-leak/2022-04_inverse-finance-hack-35-1.yaml) | data-leak | 2022-04-02 |  |  |
| [2022-04_jay-chou-nft-theft.yaml](data-leak/2022-04_jay-chou-nft-theft.yaml) | data-leak | 2022-04-01 |  |  |
| [2022-04_fake-bored-ape-airdrops.yaml](data-leak/2022-04_fake-bored-ape-airdrops.yaml) | data-leak | 2022-04-01 |  |  |
| [2022-04_waves-protocol-losses.yaml](other/2022-04_waves-protocol-losses.yaml) | other | 2022-04-01 |  |  |
| [2022-04_let-s-go-brandon-class-action-lawsuit-filed.yaml](other/2022-04_let-s-go-brandon-class-action-lawsuit-filed.yaml) | other | 2022-04-01 |  |  |
| [2022-04_multiple-discord-compromises.yaml](data-leak/2022-04_multiple-discord-compromises.yaml) | data-leak | 2022-04-01 |  |  |
| [2022-04_dis-chem-not-disclosed.yaml](supply-chain/2022-04_dis-chem-not-disclosed.yaml) | supply-chain | 2022-04-01 |  |  |
| [2022-04_blue-cross-blue-shield-of-arizona-clover-health-kaiser-permanente-point32health-upmc-health-plan-and-33-healthcare-organizations-onetouchpoint.yaml](supply-chain/2022-04_blue-cross-blue-shield-of-arizona-clover-health-kaiser-permanente-point32health-upmc-health-plan-and-33-healthcare-organizations-onetouchpoint.yaml) | supply-chain | 2022-04-01 |  |  |
| [2022-04_sunwing-airlines-airline-choice.yaml](supply-chain/2022-04_sunwing-airlines-airline-choice.yaml) | supply-chain | 2022-04-01 |  |  |
| [2022-03_opensea-insider-trader-opens-new-nft-platform.yaml](other/2022-03_opensea-insider-trader-opens-new-nft-platform.yaml) | other | 2022-03-31 |  |  |
| [2022-03_cosmic-cowgirls-rug-pull-accusations.yaml](other/2022-03_cosmic-cowgirls-rug-pull-accusations.yaml) | other | 2022-03-31 |  |  |
| [2022-03_ola-finance-hack.yaml](data-leak/2022-03_ola-finance-hack.yaml) | data-leak | 2022-03-30 |  |  |
| [2022-03_bored-bunny-rug-pull.yaml](other/2022-03_bored-bunny-rug-pull.yaml) | other | 2022-03-29 |  |  |
| [2022-03_axie-infinity-bridge-hack.yaml](data-leak/2022-03_axie-infinity-bridge-hack.yaml) | data-leak | 2022-03-29 |  |  |
| [2022-03_andrew-yang-stiffs-artist.yaml](other/2022-03_andrew-yang-stiffs-artist.yaml) | other | 2022-03-28 |  |  |
| [2022-03_cameron-moul-ne-nft-theft.yaml](data-leak/2022-03_cameron-moul-ne-nft-theft.yaml) | data-leak | 2022-03-28 |  |  |
| [2022-03_calvin-chan-nft-theft.yaml](data-leak/2022-03_calvin-chan-nft-theft.yaml) | data-leak | 2022-03-28 |  |  |
| [2022-03_pak-nft-transaction-failures.yaml](other/2022-03_pak-nft-transaction-failures.yaml) | other | 2022-03-28 |  |  |
| [2022-03_mkleo-twitter-account-hack.yaml](data-leak/2022-03_mkleo-twitter-account-hack.yaml) | data-leak | 2022-03-28 |  |  |
| [2022-03_taylorrichie-eth-nft-theft.yaml](data-leak/2022-03_taylorrichie-eth-nft-theft.yaml) | data-leak | 2022-03-27 |  |  |
| [2022-03_revest-finance-hack.yaml](data-leak/2022-03_revest-finance-hack.yaml) | data-leak | 2022-03-27 |  |  |
| [2022-03_coinbase-requires-kyc-from-more-users.yaml](other/2022-03_coinbase-requires-kyc-from-more-users.yaml) | other | 2022-03-26 |  |  |
| [2022-03_zenledger-fires-executive.yaml](other/2022-03_zenledger-fires-executive.yaml) | other | 2022-03-25 |  |  |
| [2022-03_mcg-health-1-1m-patients.yaml](supply-chain/2022-03_mcg-health-1-1m-patients.yaml) | data-leak | 2022-03-25 |  |  |
| [2022-03_roller-derby-community-rejects-nfts.yaml](other/2022-03_roller-derby-community-rejects-nfts.yaml) | other | 2022-03-24 |  |  |
| [2022-03_exxon-mobil-tests-bitcoin-mining.yaml](other/2022-03_exxon-mobil-tests-bitcoin-mining.yaml) | other | 2022-03-24 |  |  |
| [2022-03_frosties-scammers-charged.yaml](other/2022-03_frosties-scammers-charged.yaml) | other | 2022-03-24 |  |  |
| [2022-03_twitter-apecoin-phishing-scams.yaml](data-leak/2022-03_twitter-apecoin-phishing-scams.yaml) | data-leak | 2022-03-24 |  |  |
| [2022-03_pye-hack.yaml](data-leak/2022-03_pye-hack.yaml) | data-leak | 2022-03-24 |  |  |
| [2022-03_animator-wants-royalties-on-dance-moves.yaml](other/2022-03_animator-wants-royalties-on-dance-moves.yaml) | other | 2022-03-23 |  |  |
| [2022-03_caked-apes-lawsuits.yaml](other/2022-03_caked-apes-lawsuits.yaml) | other | 2022-03-23 |  |  |
| [2022-03_ronin-axie-infinity-lazarus-625m.yaml](credential-theft/2022-03_ronin-axie-infinity-lazarus-625m.yaml) | credential-theft | 2022-03-23 |  |  |
| [2022-03_cashio-hack.yaml](data-leak/2022-03_cashio-hack.yaml) | data-leak | 2022-03-23 |  |  |
| [2022-03_g2-esports-sues-nft-provider-bondly.yaml](other/2022-03_g2-esports-sues-nft-provider-bondly.yaml) | other | 2022-03-22 |  |  |
| [2022-03_veve-hack.yaml](data-leak/2022-03_veve-hack.yaml) | data-leak | 2022-03-22 |  |  |
| [2022-03_onering-hack.yaml](data-leak/2022-03_onering-hack.yaml) | data-leak | 2022-03-21 |  |  |
| [2022-03_neonexus-rug-pull.yaml](other/2022-03_neonexus-rug-pull.yaml) | other | 2022-03-21 |  |  |
| [2022-03_bored-apes-animation-scam.yaml](data-leak/2022-03_bored-apes-animation-scam.yaml) | data-leak | 2022-03-21 |  |  |
| [2022-03_arthur-0x-nft-theft.yaml](data-leak/2022-03_arthur-0x-nft-theft.yaml) | data-leak | 2022-03-21 |  |  |
| [2022-03_microsoft-lapsus-bing-cortana-source.yaml](credential-theft/2022-03_microsoft-lapsus-bing-cortana-source.yaml) | credential-theft | 2022-03-20 |  |  |
| [2022-03_nikki-freid-twitter-account-hacked.yaml](data-leak/2022-03_nikki-freid-twitter-account-hacked.yaml) | data-leak | 2022-03-19 |  |  |
| [2022-03_igobit-founder-convicted.yaml](other/2022-03_igobit-founder-convicted.yaml) | other | 2022-03-18 |  |  |
| [2022-03_australian-facebook-crypto-scams.yaml](data-leak/2022-03_australian-facebook-crypto-scams.yaml) | data-leak | 2022-03-18 |  |  |
| [2022-03_kaiju-kongz-shadiness.yaml](other/2022-03_kaiju-kongz-shadiness.yaml) | other | 2022-03-18 |  |  |
| [2022-03_people-borrow-bored-apes-to-claim-apecoin.yaml](data-leak/2022-03_people-borrow-bored-apes-to-claim-apecoin.yaml) | data-leak | 2022-03-18 |  |  |
| [2022-03_rare-bears-discord-hack.yaml](data-leak/2022-03_rare-bears-discord-hack.yaml) | data-leak | 2022-03-16 |  |  |
| [2022-03_apecoin-launches.yaml](other/2022-03_apecoin-launches.yaml) | other | 2022-03-16 |  |  |
| [2022-03_winamp-announces-nft-plans.yaml](other/2022-03_winamp-announces-nft-plans.yaml) | other | 2022-03-16 |  |  |
| [2022-03_binance-stops-operating-in-ontario.yaml](other/2022-03_binance-stops-operating-in-ontario.yaml) | other | 2022-03-16 |  |  |
| [2022-03_binance-pauses-polygon-withdrawals.yaml](other/2022-03_binance-pauses-polygon-withdrawals.yaml) | other | 2022-03-15 |  |  |
| [2022-03_deus-finance-hack-35-1.yaml](data-leak/2022-03_deus-finance-hack-35-1.yaml) | data-leak | 2022-03-15 |  |  |
| [2022-03_hundred-finance-and-agave-finance-hacks.yaml](data-leak/2022-03_hundred-finance-and-agave-finance-hacks.yaml) | data-leak | 2022-03-15 |  |  |
| [2022-03_nftbooks-project-launches.yaml](other/2022-03_nftbooks-project-launches.yaml) | other | 2022-03-15 |  |  |
| [2022-03_official-formula-1-blockchain-game-shuts-down.yaml](other/2022-03_official-formula-1-blockchain-game-shuts-down.yaml) | other | 2022-03-15 |  |  |
| [2022-03_deus-finance-hack-1.yaml](data-leak/2022-03_deus-finance-hack-1.yaml) | data-leak | 2022-03-15 |  |  |
| [2022-03_wizard-pass-discord-hack.yaml](data-leak/2022-03_wizard-pass-discord-hack.yaml) | data-leak | 2022-03-14 |  |  |
| [2022-03_invictus-dao-votes-to-close.yaml](other/2022-03_invictus-dao-votes-to-close.yaml) | other | 2022-03-14 |  |  |
| [2022-03_clipboard-malware.yaml](data-leak/2022-03_clipboard-malware.yaml) | data-leak | 2022-03-14 |  |  |
| [2022-03_latoken-takes-back-trader-s-profit.yaml](other/2022-03_latoken-takes-back-trader-s-profit.yaml) | other | 2022-03-12 |  |  |
| [2022-03_rare-pepes-lawsuit.yaml](other/2022-03_rare-pepes-lawsuit.yaml) | other | 2022-03-12 |  |  |
| [2022-03_uk-authorities-shut-down-bitcoin-atms.yaml](other/2022-03_uk-authorities-shut-down-bitcoin-atms.yaml) | other | 2022-03-11 |  |  |
| [2022-03_yuga-labs-monopoly-achieved.yaml](other/2022-03_yuga-labs-monopoly-achieved.yaml) | other | 2022-03-11 |  |  |
| [2022-03_socios-payments-controversy.yaml](other/2022-03_socios-payments-controversy.yaml) | other | 2022-03-11 |  |  |
| [2022-03_meundies-cancels-nft-underwear-plans.yaml](other/2022-03_meundies-cancels-nft-underwear-plans.yaml) | other | 2022-03-11 |  |  |
| [2022-03_fir-tree-capital-shorts-tether.yaml](other/2022-03_fir-tree-capital-shorts-tether.yaml) | other | 2022-03-11 |  |  |
| [2022-03_facebook-crypto-scammer.yaml](data-leak/2022-03_facebook-crypto-scammer.yaml) | data-leak | 2022-03-11 |  |  |
| [2022-03_yuga-labs-requests-kyc.yaml](other/2022-03_yuga-labs-requests-kyc.yaml) | other | 2022-03-10 |  |  |
| [2022-03_polygon-outage.yaml](other/2022-03_polygon-outage.yaml) | other | 2022-03-10 |  |  |
| [2022-03_etherrock-typo.yaml](other/2022-03_etherrock-typo.yaml) | other | 2022-03-10 |  |  |
| [2022-03_jeff-passan-twitter-account-hack.yaml](data-leak/2022-03_jeff-passan-twitter-account-hack.yaml) | data-leak | 2022-03-10 |  |  |
| [2022-03_juno-airdrop-vote-begins.yaml](other/2022-03_juno-airdrop-vote-begins.yaml) | other | 2022-03-10 |  |  |
| [2022-03_fantasm-finance-hack.yaml](data-leak/2022-03_fantasm-finance-hack.yaml) | data-leak | 2022-03-09 |  |  |
| [2022-03_ape-kids-football-club-tanks.yaml](other/2022-03_ape-kids-football-club-tanks.yaml) | other | 2022-03-09 |  |  |
| [2022-03_pirate-x-pirate-hack.yaml](data-leak/2022-03_pirate-x-pirate-hack.yaml) | data-leak | 2022-03-09 |  |  |
| [2022-03_limewire-nft-marketplace-annoucement.yaml](other/2022-03_limewire-nft-marketplace-annoucement.yaml) | other | 2022-03-09 |  |  |
| [2022-03_crypto-exchange-glitch-costs-user.yaml](other/2022-03_crypto-exchange-glitch-costs-user.yaml) | other | 2022-03-09 |  |  |
| [2022-03_empowercoin-indictment.yaml](data-leak/2022-03_empowercoin-indictment.yaml) | data-leak | 2022-03-08 |  |  |
| [2022-03_crypto-com-calls-back-loans.yaml](other/2022-03_crypto-com-calls-back-loans.yaml) | other | 2022-03-08 |  |  |
| [2022-03_ormeus-coin-founder-charged.yaml](data-leak/2022-03_ormeus-coin-founder-charged.yaml) | data-leak | 2022-03-08 |  |  |
| [2022-03_jake-paul-undisclosed-promotion-accusations.yaml](other/2022-03_jake-paul-undisclosed-promotion-accusations.yaml) | other | 2022-03-07 |  |  |
| [2022-03_august-sander-nft-ownership-dispute.yaml](other/2022-03_august-sander-nft-ownership-dispute.yaml) | other | 2022-03-07 |  |  |
| [2022-03_andre-cronje-and-anton-nell-leave-crypto.yaml](other/2022-03_andre-cronje-and-anton-nell-leave-crypto.yaml) | other | 2022-03-06 |  |  |
| [2022-03_bacon-protocol-hack.yaml](data-leak/2022-03_bacon-protocol-hack.yaml) | data-leak | 2022-03-05 |  |  |
| [2022-03_battlecatsarena-rug-pull.yaml](other/2022-03_battlecatsarena-rug-pull.yaml) | other | 2022-03-05 |  |  |
| [2022-03_tai-lopez-launches-nfts.yaml](other/2022-03_tai-lopez-launches-nfts.yaml) | other | 2022-03-04 |  |  |
| [2022-03_samsung-lapsus.yaml](data-leak/2022-03_samsung-lapsus.yaml) | data-leak | 2022-03-04 |  |  |
| [2022-03_neosvr-abandons-crypto.yaml](other/2022-03_neosvr-abandons-crypto.yaml) | other | 2022-03-04 |  |  |
| [2022-03_consensys-blocks-venezuelans.yaml](other/2022-03_consensys-blocks-venezuelans.yaml) | other | 2022-03-03 |  |  |
| [2022-03_ukraine-airdrop-spoofed.yaml](other/2022-03_ukraine-airdrop-spoofed.yaml) | other | 2022-03-03 |  |  |
| [2022-03_nemus-earth-launches.yaml](other/2022-03_nemus-earth-launches.yaml) | other | 2022-03-03 |  |  |
| [2022-03_opensea-blocks-iranians.yaml](other/2022-03_opensea-blocks-iranians.yaml) | other | 2022-03-03 |  |  |
| [2022-03_ukraine-cancels-airdrop.yaml](other/2022-03_ukraine-cancels-airdrop.yaml) | other | 2022-03-03 |  |  |
| [2022-03_brian-rose-and-david-icke-announce-nfts.yaml](other/2022-03_brian-rose-and-david-icke-announce-nfts.yaml) | other | 2022-03-02 |  |  |
| [2022-03_treasure-nft-marketplace-bug.yaml](other/2022-03_treasure-nft-marketplace-bug.yaml) | other | 2022-03-02 |  |  |
| [2022-03_okta-sykes-enterprises.yaml](supply-chain/2022-03_okta-sykes-enterprises.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_parler-nft-platform-launches.yaml](other/2022-03_parler-nft-platform-launches.yaml) | other | 2022-03-01 |  |  |
| [2022-03_highmark-quantum-group.yaml](supply-chain/2022-03_highmark-quantum-group.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_former-consensys-employees-demand-audit.yaml](other/2022-03_former-consensys-employees-demand-audit.yaml) | other | 2022-03-01 |  |  |
| [2022-03_rennline-freestyle-solutions.yaml](supply-chain/2022-03_rennline-freestyle-solutions.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_acro-not-disclosed.yaml](supply-chain/2022-03_acro-not-disclosed.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_oklahoma-s-department-of-human-services-okdhs-liberty-of-oklahoma.yaml](supply-chain/2022-03_oklahoma-s-department-of-human-services-okdhs-liberty-of-oklahoma.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_samsung-qualcomm-nvidia.yaml](supply-chain/2022-03_samsung-qualcomm-nvidia.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_central-maine-medical-center-shields-health-care-group-in.yaml](supply-chain/2022-03_central-maine-medical-center-shields-health-care-group-in.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_datahealth-not-disclosed.yaml](supply-chain/2022-03_datahealth-not-disclosed.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_malicious-fiverr-developer.yaml](data-leak/2022-03_malicious-fiverr-developer.yaml) | data-leak | 2022-03-01 |  |  |
| [2022-03_unc-lenoir-health-care-avera-health-chi-health-phelps-health-and-4-organizations-mcg-health.yaml](supply-chain/2022-03_unc-lenoir-health-care-avera-health-chi-health-phelps-health-and-4-organizations-mcg-health.yaml) | supply-chain | 2022-03-01 |  |  |
| [2022-03_hackers-demand-nvidia-removes-gpu-constraints.yaml](data-leak/2022-03_hackers-demand-nvidia-removes-gpu-constraints.yaml) | data-leak | 2022-03-01 |  |  |
| [2022-02_robert-armijo-nft-theft.yaml](data-leak/2022-02_robert-armijo-nft-theft.yaml) | data-leak | 2022-02-28 |  |  |
| [2022-02_elexir-finance-rug-pull.yaml](other/2022-02_elexir-finance-rug-pull.yaml) | other | 2022-02-28 |  |  |
| [2022-02_exchanges-refuse-requests-to-freeze-funds-from-ukrainian-vp.yaml](other/2022-02_exchanges-refuse-requests-to-freeze-funds-from-ukrainian-vp.yaml) | other | 2022-02-28 |  |  |
| [2022-02_randi-zuckerberg-music-video.yaml](other/2022-02_randi-zuckerberg-music-video.yaml) | other | 2022-02-28 |  |  |
| [2022-02_genomesdao-launch.yaml](other/2022-02_genomesdao-launch.yaml) | other | 2022-02-28 |  |  |
| [2022-02_gavin-wood-tries-to-use-ukraine-invasion-as-marketing-opportunity.yaml](other/2022-02_gavin-wood-tries-to-use-ukraine-invasion-as-marketing-opportunity.yaml) | other | 2022-02-27 |  |  |
| [2022-02_howlerz-fake-contract.yaml](data-leak/2022-02_howlerz-fake-contract.yaml) | data-leak | 2022-02-26 |  |  |
| [2022-02_starcatchers-insider-trading.yaml](other/2022-02_starcatchers-insider-trading.yaml) | other | 2022-02-26 |  |  |
| [2022-02_scammers-try-to-profit-off-ukraine-invasion.yaml](other/2022-02_scammers-try-to-profit-off-ukraine-invasion.yaml) | other | 2022-02-26 |  |  |
| [2022-02_doodles-phishing-attack.yaml](data-leak/2022-02_doodles-phishing-attack.yaml) | data-leak | 2022-02-26 |  |  |
| [2022-02_nelson-mandela-nft-announcement.yaml](other/2022-02_nelson-mandela-nft-announcement.yaml) | other | 2022-02-25 |  |  |
| [2022-02_associated-press-mishandles-controversy.yaml](other/2022-02_associated-press-mishandles-controversy.yaml) | other | 2022-02-25 |  |  |
| [2022-02_bitconnect-founder-indicted.yaml](data-leak/2022-02_bitconnect-founder-indicted.yaml) | data-leak | 2022-02-25 |  |  |
| [2022-02_pixelmon-rug-pull.yaml](data-leak/2022-02_pixelmon-rug-pull.yaml) | data-leak | 2022-02-25 |  |  |
| [2022-02_bitmex-founders-plead-guilty.yaml](other/2022-02_bitmex-founders-plead-guilty.yaml) | other | 2022-02-24 |  |  |
| [2022-02_cyberattacks-modern-armed-conflicts.yaml](other/2022-02_cyberattacks-modern-armed-conflicts.yaml) | other | 2022-02-24 | HermeticWiper, WhisperGate, C… | CVE-2022-24521 |
| [2022-02_associated-press-releases-nft-of-migrants.yaml](other/2022-02_associated-press-releases-nft-of-migrants.yaml) | other | 2022-02-24 |  |  |
| [2022-02_nvidia-gpu-utility-malware.yaml](data-leak/2022-02_nvidia-gpu-utility-malware.yaml) | data-leak | 2022-02-23 |  |  |
| [2022-02_space-crypto-tokenomics-flop.yaml](other/2022-02_space-crypto-tokenomics-flop.yaml) | other | 2022-02-23 |  |  |
| [2022-02_nvidia-lapsus-gpu-source-code.yaml](credential-theft/2022-02_nvidia-lapsus-gpu-source-code.yaml) | credential-theft | 2022-02-23 |  |  |
| [2022-02_nvidia-lapsus.yaml](data-leak/2022-02_nvidia-lapsus.yaml) | data-leak | 2022-02-23 |  |  |
| [2022-02_sotheby-s-cryptopunks-auction-canceled.yaml](other/2022-02_sotheby-s-cryptopunks-auction-canceled.yaml) | other | 2022-02-23 |  |  |
| [2022-02_de-aaron-fox-rug-pull.yaml](other/2022-02_de-aaron-fox-rug-pull.yaml) | other | 2022-02-23 |  |  |
| [2022-02_ocean-protocol-vulnerability.yaml](other/2022-02_ocean-protocol-vulnerability.yaml) | other | 2022-02-22 |  |  |
| [2022-02_journalist-claims-to-have-identified-the-dao-hacker.yaml](data-leak/2022-02_journalist-claims-to-have-identified-the-dao-hacker.yaml) | data-leak | 2022-02-22 |  |  |
| [2022-02_coinbase-takes-credit-for-ad.yaml](other/2022-02_coinbase-takes-credit-for-ad.yaml) | other | 2022-02-21 |  |  |
| [2022-02_atom-protocol-rug-pull.yaml](other/2022-02_atom-protocol-rug-pull.yaml) | other | 2022-02-20 |  |  |
| [2022-02_composable-finance-exec-unmasked-as-omar-zaki.yaml](other/2022-02_composable-finance-exec-unmasked-as-omar-zaki.yaml) | other | 2022-02-20 |  |  |
| [2022-02_opensea-phishing-attacks.yaml](data-leak/2022-02_opensea-phishing-attacks.yaml) | data-leak | 2022-02-19 |  |  |
| [2022-02_nishid-wasnik-cryptocurrency-scam.yaml](data-leak/2022-02_nishid-wasnik-cryptocurrency-scam.yaml) | data-leak | 2022-02-19 |  |  |
| [2022-02_bitconnect-lawsuit-continues.yaml](other/2022-02_bitconnect-lawsuit-continues.yaml) | other | 2022-02-18 |  |  |
| [2022-02_kickstarter-continues-blockchain-plans.yaml](other/2022-02_kickstarter-continues-blockchain-plans.yaml) | other | 2022-02-18 |  |  |
| [2022-02_generaci-n-zoe-raided.yaml](data-leak/2022-02_generaci-n-zoe-raided.yaml) | data-leak | 2022-02-18 |  |  |
| [2022-02_timothy-mckimmy-nft-theft.yaml](other/2022-02_timothy-mckimmy-nft-theft.yaml) | other | 2022-02-18 |  |  |
| [2022-02_crypto-chicks-art-theft-controversy.yaml](other/2022-02_crypto-chicks-art-theft-controversy.yaml) | other | 2022-02-18 |  |  |
| [2022-02_shl0ms-blows-up-lamborghini.yaml](other/2022-02_shl0ms-blows-up-lamborghini.yaml) | other | 2022-02-17 |  |  |
| [2022-02_andrew-yang-announces-dao.yaml](other/2022-02_andrew-yang-announces-dao.yaml) | other | 2022-02-17 |  |  |
| [2022-02_binance-halts-activities-in-israel.yaml](other/2022-02_binance-halts-activities-in-israel.yaml) | other | 2022-02-17 |  |  |
| [2022-02_safemoon-class-action-lawsuit-filed.yaml](other/2022-02_safemoon-class-action-lawsuit-filed.yaml) | other | 2022-02-17 |  |  |
| [2022-02_robness-harasses-journalist.yaml](other/2022-02_robness-harasses-journalist.yaml) | other | 2022-02-16 |  |  |
| [2022-02_chaosium-suspends-nft-plans.yaml](other/2022-02_chaosium-suspends-nft-plans.yaml) | other | 2022-02-16 |  |  |
| [2022-02_metadecks-unauthorized-nfts.yaml](other/2022-02_metadecks-unauthorized-nfts.yaml) | other | 2022-02-16 |  |  |
| [2022-02_gary-vee-calls-out-shadiness.yaml](other/2022-02_gary-vee-calls-out-shadiness.yaml) | other | 2022-02-16 |  |  |
| [2022-02_bnb42-rug-pull.yaml](other/2022-02_bnb42-rug-pull.yaml) | other | 2022-02-15 |  |  |
| [2022-02_helloimmorgan-fails-to-disclose-paid-promotions.yaml](other/2022-02_helloimmorgan-fails-to-disclose-paid-promotions.yaml) | other | 2022-02-15 |  |  |
| [2022-02_canadian-antivaxxxers-make-bitcoin-plans.yaml](other/2022-02_canadian-antivaxxxers-make-bitcoin-plans.yaml) | other | 2022-02-14 |  |  |
| [2022-02_belvedere-museum-auctions-scraps-of-painting.yaml](other/2022-02_belvedere-museum-auctions-scraps-of-painting.yaml) | other | 2022-02-14 |  |  |
| [2022-02_buildfinance-governance-attack.yaml](data-leak/2022-02_buildfinance-governance-attack.yaml) | data-leak | 2022-02-14 |  |  |
| [2022-02_lonely-ape-dating-club-prank.yaml](other/2022-02_lonely-ape-dating-club-prank.yaml) | other | 2022-02-14 |  |  |
| [2022-02_british-authorities-seize-nfts-in-tax-investigation.yaml](other/2022-02_british-authorities-seize-nfts-in-tax-investigation.yaml) | other | 2022-02-13 |  |  |
| [2022-02_jacked-ape-club-team-melts-down.yaml](other/2022-02_jacked-ape-club-team-melts-down.yaml) | other | 2022-02-13 |  |  |
| [2022-02_monero-mining-pool-approaches-51.yaml](other/2022-02_monero-mining-pool-approaches-51.yaml) | other | 2022-02-13 |  |  |
| [2022-02_coinbase-outage.yaml](other/2022-02_coinbase-outage.yaml) | other | 2022-02-13 |  |  |
| [2022-02_air-taxi-dao-founder-narrowly-escapes-scam.yaml](data-leak/2022-02_air-taxi-dao-founder-narrowly-escapes-scam.yaml) | data-leak | 2022-02-12 |  |  |
| [2022-02_titanreach-alleged-fund-misappropriation.yaml](other/2022-02_titanreach-alleged-fund-misappropriation.yaml) | other | 2022-02-11 |  |  |
| [2022-02_blockfi-sec-settlement.yaml](other/2022-02_blockfi-sec-settlement.yaml) | other | 2022-02-11 |  |  |
| [2022-02_jacked-ape-club-deception.yaml](other/2022-02_jacked-ape-club-deception.yaml) | other | 2022-02-11 |  |  |
| [2022-02_i-titanreach-i-alleged-fund-misappropriation.yaml](other/2022-02_i-titanreach-i-alleged-fund-misappropriation.yaml) | other | 2022-02-11 |  |  |
| [2022-02_lana-rhoades-rug-pull.yaml](other/2022-02_lana-rhoades-rug-pull.yaml) | other | 2022-02-11 |  |  |
| [2022-02_moviepass-announces-blockchain-plans.yaml](other/2022-02_moviepass-announces-blockchain-plans.yaml) | other | 2022-02-11 |  |  |
| [2022-02_mtgdao-legal-notice.yaml](other/2022-02_mtgdao-legal-notice.yaml) | other | 2022-02-10 |  |  |
| [2022-02_squiggles-attempted-rug-pull.yaml](other/2022-02_squiggles-attempted-rug-pull.yaml) | other | 2022-02-10 |  |  |
| [2022-02_atomic-wallet-vulnerabilities.yaml](other/2022-02_atomic-wallet-vulnerabilities.yaml) | other | 2022-02-10 |  |  |
| [2022-02_greenidge-generation-opens.yaml](other/2022-02_greenidge-generation-opens.yaml) | other | 2022-02-09 |  |  |
| [2022-02_bbc-article-about-scammer.yaml](other/2022-02_bbc-article-about-scammer.yaml) | other | 2022-02-09 |  |  |
| [2022-02_baby-musk-coin-rug-pull.yaml](other/2022-02_baby-musk-coin-rug-pull.yaml) | other | 2022-02-09 |  |  |
| [2022-02_skycoin-kidnapping-lawsuit.yaml](other/2022-02_skycoin-kidnapping-lawsuit.yaml) | other | 2022-02-09 |  |  |
| [2022-02_dego-finance.yaml](data-leak/2022-02_dego-finance.yaml) | data-leak | 2022-02-09 |  |  |
| [2022-02_canadian-antivaxxers-shill-bitcoin.yaml](other/2022-02_canadian-antivaxxers-shill-bitcoin.yaml) | other | 2022-02-09 |  |  |
| [2022-02_samsung-environmental-nft-project-announced.yaml](other/2022-02_samsung-environmental-nft-project-announced.yaml) | other | 2022-02-09 |  |  |
| [2022-02_coinbase-insider-trading.yaml](other/2022-02_coinbase-insider-trading.yaml) | other | 2022-02-08 |  |  |
| [2022-02_superfluid-hack.yaml](data-leak/2022-02_superfluid-hack.yaml) | data-leak | 2022-02-08 |  |  |
| [2022-02_alleged-bitfinex-launderers-arrested.yaml](data-leak/2022-02_alleged-bitfinex-launderers-arrested.yaml) | data-leak | 2022-02-08 |  |  |
| [2022-02_british-journal-of-photography-replaces-twitter-account.yaml](other/2022-02_british-journal-of-photography-replaces-twitter-account.yaml) | other | 2022-02-08 |  |  |
| [2022-02_ira-financial-hack.yaml](data-leak/2022-02_ira-financial-hack.yaml) | data-leak | 2022-02-08 |  |  |
| [2022-02_looksrare-cashout.yaml](other/2022-02_looksrare-cashout.yaml) | other | 2022-02-07 |  |  |
| [2022-02_superrare-community-manager-controversy.yaml](other/2022-02_superrare-community-manager-controversy.yaml) | other | 2022-02-07 |  |  |
| [2022-02_nft-music-stream-unauthorized-marketplace.yaml](other/2022-02_nft-music-stream-unauthorized-marketplace.yaml) | other | 2022-02-07 |  |  |
| [2022-02_earnhub-hack.yaml](other/2022-02_earnhub-hack.yaml) | other | 2022-02-07 |  |  |
| [2022-02_un-report-on-north-korean-hacking.yaml](other/2022-02_un-report-on-north-korean-hacking.yaml) | other | 2022-02-06 |  |  |
| [2022-02_balloonsville-rug-pull.yaml](other/2022-02_balloonsville-rug-pull.yaml) | other | 2022-02-06 |  |  |
| [2022-02_ratz-club-rug-pull.yaml](data-leak/2022-02_ratz-club-rug-pull.yaml) | data-leak | 2022-02-06 |  |  |
| [2022-02_ubisoft-gives-employees-nfts.yaml](other/2022-02_ubisoft-gives-employees-nfts.yaml) | other | 2022-02-06 |  |  |
| [2022-02_cent-nft-platform-shuts-down.yaml](other/2022-02_cent-nft-platform-shuts-down.yaml) | other | 2022-02-06 |  |  |
| [2022-02_meter-passport-bridge-hack.yaml](data-leak/2022-02_meter-passport-bridge-hack.yaml) | data-leak | 2022-02-05 |  |  |
| [2022-02_ens-leadership-controversy.yaml](other/2022-02_ens-leadership-controversy.yaml) | other | 2022-02-05 |  |  |
| [2022-02_borrower-loses-bitcoin.yaml](other/2022-02_borrower-loses-bitcoin.yaml) | other | 2022-02-04 |  |  |
| [2022-02_gumroad-nft-controversy.yaml](other/2022-02_gumroad-nft-controversy.yaml) | other | 2022-02-04 |  |  |
| [2022-02_traderjoe-twitter-support-phishing-attack.yaml](data-leak/2022-02_traderjoe-twitter-support-phishing-attack.yaml) | data-leak | 2022-02-04 |  |  |
| [2022-02_nike-sues-stockx-nft-reseller.yaml](other/2022-02_nike-sues-stockx-nft-reseller.yaml) | other | 2022-02-03 |  |  |
| [2022-02_klayswap-hack.yaml](data-leak/2022-02_klayswap-hack.yaml) | data-leak | 2022-02-03 |  |  |
| [2022-02_miamicoin-loss.yaml](other/2022-02_miamicoin-loss.yaml) | other | 2022-02-02 |  |  |
| [2022-02_wormhole-bridge-exploit.yaml](other/2022-02_wormhole-bridge-exploit.yaml) | other | 2022-02-02 |  |  |
| [2022-02_wormhole-bridge-hack.yaml](data-leak/2022-02_wormhole-bridge-hack.yaml) | data-leak | 2022-02-02 |  |  |
| [2022-02_hitpiece-unauthorized-marketplace.yaml](other/2022-02_hitpiece-unauthorized-marketplace.yaml) | other | 2022-02-01 |  |  |
| [2022-02_fortune-500-companies-morley-companies.yaml](supply-chain/2022-02_fortune-500-companies-morley-companies.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-02_australian-clinical-labs-medlab.yaml](data-leak/2022-02_australian-clinical-labs-medlab.yaml) | ransomware | 2022-02-01 |  |  |
| [2022-02_team17-announces-and-then-cancels-foray-into-nfts.yaml](other/2022-02_team17-announces-and-then-cancels-foray-into-nfts.yaml) | other | 2022-02-01 |  |  |
| [2022-02_covid-19-nft-spam.yaml](other/2022-02_covid-19-nft-spam.yaml) | other | 2022-02-01 |  |  |
| [2022-02_oklahoma-city-police-department-dna-solutions-inc.yaml](supply-chain/2022-02_oklahoma-city-police-department-dna-solutions-inc.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-02_internet-society-not-disclosed.yaml](supply-chain/2022-02_internet-society-not-disclosed.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-02_memorial-health-system-advent-health-partners.yaml](supply-chain/2022-02_memorial-health-system-advent-health-partners.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-02_not-disclosed-comprehensive-health-service.yaml](supply-chain/2022-02_not-disclosed-comprehensive-health-service.yaml) | supply-chain | 2022-02-01 |  |  |
| [2022-01_iloveponzi-nft-theft.yaml](data-leak/2022-01_iloveponzi-nft-theft.yaml) | data-leak | 2022-01-31 |  |  |
| [2022-01_gambling-addiction-posts.yaml](other/2022-01_gambling-addiction-posts.yaml) | other | 2022-01-31 |  |  |
| [2022-01_redditors-discover-tax-season.yaml](other/2022-01_redditors-discover-tax-season.yaml) | other | 2022-01-31 |  |  |
| [2022-01_wwf-nft-announcement.yaml](other/2022-01_wwf-nft-announcement.yaml) | other | 2022-01-31 |  |  |
| [2022-01_ice-poseidon-rug-pull.yaml](other/2022-01_ice-poseidon-rug-pull.yaml) | other | 2022-01-31 |  |  |
| [2022-01_realux-rug-pull.yaml](other/2022-01_realux-rug-pull.yaml) | other | 2022-01-31 |  |  |
| [2022-01_troy-baker-cancels-partnership-with-voiceverse.yaml](other/2022-01_troy-baker-cancels-partnership-with-voiceverse.yaml) | other | 2022-01-31 |  |  |
| [2022-01_qubit-bounty-negotiation.yaml](data-leak/2022-01_qubit-bounty-negotiation.yaml) | data-leak | 2022-01-30 |  |  |
| [2022-01_wonderland-shuts-down-despite-vote.yaml](other/2022-01_wonderland-shuts-down-despite-vote.yaml) | other | 2022-01-30 |  |  |
| [2022-01_colors-nfts.yaml](other/2022-01_colors-nfts.yaml) | other | 2022-01-30 |  |  |
| [2022-01_fake-bored-ape-nfts.yaml](data-leak/2022-01_fake-bored-ape-nfts.yaml) | data-leak | 2022-01-29 |  |  |
| [2022-01_trader-error.yaml](other/2022-01_trader-error.yaml) | other | 2022-01-29 |  |  |
| [2022-01_justin-bieber-acquires-bored-ape.yaml](other/2022-01_justin-bieber-acquires-bored-ape.yaml) | other | 2022-01-29 |  |  |
| [2022-01_opensea-listing-bug-continues.yaml](other/2022-01_opensea-listing-bug-continues.yaml) | other | 2022-01-28 |  |  |
| [2022-01_looksrare-wash-trading-report.yaml](other/2022-01_looksrare-wash-trading-report.yaml) | other | 2022-01-28 |  |  |
| [2022-01_khan-academy-wash-trading-controversy.yaml](other/2022-01_khan-academy-wash-trading-controversy.yaml) | other | 2022-01-28 |  |  |
| [2022-01_lazy-lion-ape-club-rug-pull.yaml](other/2022-01_lazy-lion-ape-club-rug-pull.yaml) | other | 2022-01-28 |  |  |
| [2022-01_ip-harvesting-nfts-created.yaml](other/2022-01_ip-harvesting-nfts-created.yaml) | other | 2022-01-27 |  |  |
| [2022-01_padawan-dao-treasury-loss.yaml](other/2022-01_padawan-dao-treasury-loss.yaml) | other | 2022-01-27 |  |  |
| [2022-01_wonderland-developer-exposed-as-michael-patryn.yaml](other/2022-01_wonderland-developer-exposed-as-michael-patryn.yaml) | other | 2022-01-27 |  |  |
| [2022-01_opensea-tries-to-limit-free-mints.yaml](other/2022-01_opensea-tries-to-limit-free-mints.yaml) | other | 2022-01-27 |  |  |
| [2022-01_qubit-finance-hack.yaml](data-leak/2022-01_qubit-finance-hack.yaml) | data-leak | 2022-01-27 |  |  |
| [2022-01_iqoniq-collapse.yaml](other/2022-01_iqoniq-collapse.yaml) | other | 2022-01-26 |  |  |
| [2022-01_melania-trump-wash-trades.yaml](other/2022-01_melania-trump-wash-trades.yaml) | other | 2022-01-26 |  |  |
| [2022-01_wegro-rug-pull.yaml](other/2022-01_wegro-rug-pull.yaml) | other | 2022-01-26 |  |  |
| [2022-01_mercenary-rug-pull.yaml](other/2022-01_mercenary-rug-pull.yaml) | other | 2022-01-26 |  |  |
| [2022-01_charles-goldie-nft-sale.yaml](other/2022-01_charles-goldie-nft-sale.yaml) | other | 2022-01-26 |  |  |
| [2022-01_let-s-go-brandon-coin-crashes.yaml](other/2022-01_let-s-go-brandon-coin-crashes.yaml) | other | 2022-01-26 |  |  |
| [2022-01_wonderland-cascading-liquidations.yaml](other/2022-01_wonderland-cascading-liquidations.yaml) | other | 2022-01-25 |  |  |
| [2022-01_blockverse-rug-pull.yaml](other/2022-01_blockverse-rug-pull.yaml) | other | 2022-01-25 |  |  |
| [2022-01_john-lennon-nft-announcement.yaml](other/2022-01_john-lennon-nft-announcement.yaml) | other | 2022-01-25 |  |  |
| [2022-01_metaslave-nft-project.yaml](other/2022-01_metaslave-nft-project.yaml) | other | 2022-01-25 |  |  |
| [2022-01_nayib-bukele-insults.yaml](other/2022-01_nayib-bukele-insults.yaml) | other | 2022-01-24 |  |  |
| [2022-01_opensea-listing-bug.yaml](data-leak/2022-01_opensea-listing-bug.yaml) | data-leak | 2022-01-24 |  |  |
| [2022-01_solfire-finance-rug-pull.yaml](other/2022-01_solfire-finance-rug-pull.yaml) | other | 2022-01-23 |  |  |
| [2022-01_cryptopunks-insider-trading.yaml](other/2022-01_cryptopunks-insider-trading.yaml) | other | 2022-01-23 |  |  |
| [2022-01_nft-conservation-fund-announcement.yaml](other/2022-01_nft-conservation-fund-announcement.yaml) | other | 2022-01-22 |  |  |
| [2022-01_bataclan-attack-victim-nft.yaml](other/2022-01_bataclan-attack-victim-nft.yaml) | other | 2022-01-22 |  |  |
| [2022-01_kurt-cobain-nft-announcement.yaml](other/2022-01_kurt-cobain-nft-announcement.yaml) | other | 2022-01-22 |  |  |
| [2022-01_solana-outage.yaml](other/2022-01_solana-outage.yaml) | other | 2022-01-21 |  |  |
| [2022-01_cryptobatz-phishing-attack.yaml](data-leak/2022-01_cryptobatz-phishing-attack.yaml) | data-leak | 2022-01-21 |  |  |
| [2022-01_mcdonalds-steals-artwork.yaml](other/2022-01_mcdonalds-steals-artwork.yaml) | other | 2022-01-20 |  |  |
| [2022-01_metamask-vulnerability.yaml](other/2022-01_metamask-vulnerability.yaml) | other | 2022-01-20 |  |  |
| [2022-01_opensea-outage.yaml](other/2022-01_opensea-outage.yaml) | other | 2022-01-20 |  |  |
| [2022-01_twitter-announces-nft-profile-pictures.yaml](other/2022-01_twitter-announces-nft-profile-pictures.yaml) | other | 2022-01-20 |  |  |
| [2022-01_multichain-hack-1.yaml](data-leak/2022-01_multichain-hack-1.yaml) | data-leak | 2022-01-19 |  |  |
| [2022-01_kingfund-finance-rug-pull.yaml](other/2022-01_kingfund-finance-rug-pull.yaml) | other | 2022-01-19 |  |  |
| [2022-01_red-cross-icrc-515k-vulnerable.yaml](data-leak/2022-01_red-cross-icrc-515k-vulnerable.yaml) | data-leak | 2022-01-18 | BEACON, GLASSTOKEN (custom ma… | CVE-2021-40539 |
| [2022-01_bnb-heroes-rug-pull.yaml](other/2022-01_bnb-heroes-rug-pull.yaml) | other | 2022-01-18 |  |  |
| [2022-01_mastercard-partners-with-coinbase.yaml](other/2022-01_mastercard-partners-with-coinbase.yaml) | other | 2022-01-18 |  |  |
| [2022-01_metabirkins-lawsuit.yaml](other/2022-01_metabirkins-lawsuit.yaml) | other | 2022-01-17 |  |  |
| [2022-01_crypto-com-hack.yaml](data-leak/2022-01_crypto-com-hack.yaml) | data-leak | 2022-01-17 |  |  |
| [2022-01_notasecretnft-project.yaml](other/2022-01_notasecretnft-project.yaml) | other | 2022-01-16 |  |  |
| [2022-01_okta-lapsus.yaml](credential-theft/2022-01_okta-lapsus.yaml) | credential-theft | 2022-01-16 | Mimikatz |  |
| [2022-01_cryptoburgers-hack.yaml](data-leak/2022-01_cryptoburgers-hack.yaml) | data-leak | 2022-01-16 |  |  |
| [2022-01_invertedculture-and-madhashers-rug-pulls.yaml](other/2022-01_invertedculture-and-madhashers-rug-pulls.yaml) | other | 2022-01-15 |  |  |
| [2022-01_spicedao-confusion.yaml](other/2022-01_spicedao-confusion.yaml) | other | 2022-01-15 |  |  |
| [2022-01_voiceverse-stolen-work-controversy.yaml](other/2022-01_voiceverse-stolen-work-controversy.yaml) | other | 2022-01-14 |  |  |
| [2022-01_chinese-rug-pull-arrest.yaml](data-leak/2022-01_chinese-rug-pull-arrest.yaml) | data-leak | 2022-01-14 |  |  |
| [2022-01_float-protocol-exploit.yaml](data-leak/2022-01_float-protocol-exploit.yaml) | data-leak | 2022-01-14 |  |  |
| [2022-01_fees-wtf-token-drop-disaster.yaml](other/2022-01_fees-wtf-token-drop-disaster.yaml) | other | 2022-01-13 |  |  |
| [2022-01_global-game-jam-sponsorship-controversy.yaml](other/2022-01_global-game-jam-sponsorship-controversy.yaml) | other | 2022-01-12 |  |  |
| [2022-01_big-daddy-ape-club-rug-pull.yaml](other/2022-01_big-daddy-ape-club-rug-pull.yaml) | other | 2022-01-11 |  |  |
| [2022-01_citydao-discord-hack.yaml](data-leak/2022-01_citydao-discord-hack.yaml) | data-leak | 2022-01-10 |  |  |
| [2022-01_associated-press-nft-marketplace-announcement.yaml](other/2022-01_associated-press-nft-marketplace-announcement.yaml) | other | 2022-01-10 |  |  |
| [2022-01_lympo-hack.yaml](data-leak/2022-01_lympo-hack.yaml) | data-leak | 2022-01-10 |  |  |
| [2022-01_doodled-dragons-rug-pull.yaml](other/2022-01_doodled-dragons-rug-pull.yaml) | other | 2022-01-09 |  |  |
| [2022-01_frosties-rug-pull.yaml](other/2022-01_frosties-rug-pull.yaml) | other | 2022-01-09 |  |  |
| [2022-01_rich-dwarves-tribe-rug-pull.yaml](other/2022-01_rich-dwarves-tribe-rug-pull.yaml) | other | 2022-01-09 |  |  |
| [2022-01_lcx-hack.yaml](data-leak/2022-01_lcx-hack.yaml) | data-leak | 2022-01-08 |  |  |
| [2022-01_ethereummax-class-action-filed.yaml](other/2022-01_ethereummax-class-action-filed.yaml) | other | 2022-01-07 |  |  |
| [2022-01_coinsuper-withdrawal-issues.yaml](other/2022-01_coinsuper-withdrawal-issues.yaml) | other | 2022-01-07 |  |  |
| [2022-01_flyfish-club-nft-restaurant-announced.yaml](other/2022-01_flyfish-club-nft-restaurant-announced.yaml) | other | 2022-01-07 |  |  |
| [2022-01_mozilla-foundation-pauses-crypto-donations.yaml](other/2022-01_mozilla-foundation-pauses-crypto-donations.yaml) | other | 2022-01-06 |  |  |
| [2022-01_crowdmachine-sec-lawsuit.yaml](other/2022-01_crowdmachine-sec-lawsuit.yaml) | other | 2022-01-06 |  |  |
| [2022-01_pudgy-penguin-attempted-rug-pull.yaml](other/2022-01_pudgy-penguin-attempted-rug-pull.yaml) | other | 2022-01-05 |  |  |
| [2022-01_kazakhstan-internet-shutdown-impacts-bitcoin-hashrate.yaml](other/2022-01_kazakhstan-internet-shutdown-impacts-bitcoin-hashrate.yaml) | other | 2022-01-05 |  |  |
| [2022-01_kosovo-temporarily-bans-crypto-mining.yaml](other/2022-01_kosovo-temporarily-bans-crypto-mining.yaml) | other | 2022-01-04 |  |  |
| [2022-01_aja-trier-art-thefts.yaml](other/2022-01_aja-trier-art-thefts.yaml) | other | 2022-01-04 |  |  |
| [2022-01_fart-jar-nfts-announced.yaml](other/2022-01_fart-jar-nfts-announced.yaml) | other | 2022-01-04 |  |  |
| [2022-01_franklin-exposed-for-undisclosed-shilling.yaml](other/2022-01_franklin-exposed-for-undisclosed-shilling.yaml) | other | 2022-01-04 |  |  |
| [2022-01_samsung-nft-tv-announcement.yaml](other/2022-01_samsung-nft-tv-announcement.yaml) | other | 2022-01-03 |  |  |
| [2022-01_sunflower-farm-game-ddoses-polygon.yaml](other/2022-01_sunflower-farm-game-ddoses-polygon.yaml) | other | 2022-01-03 |  |  |
| [2022-01_arbixfinance-rug-pull.yaml](other/2022-01_arbixfinance-rug-pull.yaml) | other | 2022-01-03 |  |  |
| [2022-01_polymarket-fined-and-shut-down-by-cftc.yaml](other/2022-01_polymarket-fined-and-shut-down-by-cftc.yaml) | other | 2022-01-03 |  |  |
| [2022-01_matt-damon-advertisement.yaml](other/2022-01_matt-damon-advertisement.yaml) | other | 2022-01-02 |  |  |
| [2022-01_entira-family-clinics-netgain.yaml](supply-chain/2022-01_entira-family-clinics-netgain.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-01_a-one-home-health-services-bend-transitional-care-infinity-rehab-salem-transitional-care-the-arbor-at-avamere-court-and-75-organizations-avamere-health-services.yaml](supply-chain/2022-01_a-one-home-health-services-bend-transitional-care-infinity-rehab-salem-transitional-care-the-arbor-at-avamere-court-and-75-organizations-avamere-health-services.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-10_football-australia-aws-s3-keys.yaml](credential-theft/2022-10_football-australia-aws-s3-keys.yaml) | credential-theft | 2022-01-01 |  |  |
| [2022-01_digiconomist-report.yaml](other/2022-01_digiconomist-report.yaml) | other | 2022-01-01 |  |  |
| [2022-01_carson-turner-nft-loss.yaml](other/2022-01_carson-turner-nft-loss.yaml) | other | 2022-01-01 |  |  |
| [2022-01_baptist-memorial-health-care-butler-health-systems-children-s-healthcare-of-atlanta-hoag-health-system-and-28-organizations-ciox-health.yaml](supply-chain/2022-01_baptist-memorial-health-care-butler-health-systems-children-s-healthcare-of-atlanta-hoag-health-system-and-28-organizations-ciox-health.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-01_good-samaritan-society-mission-healthcare-at-renton-prestige-care-rockwood-south-hill-kin-on-health-care-center-and-63-organizations-infinity-rehab.yaml](supply-chain/2022-01_good-samaritan-society-mission-healthcare-at-renton-prestige-care-rockwood-south-hill-kin-on-health-care-center-and-63-organizations-infinity-rehab.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-01_cryptobike-rug-pull.yaml](other/2022-01_cryptobike-rug-pull.yaml) | other | 2022-01-01 |  |  |
| [2022-01_tether-prints-1-billion.yaml](other/2022-01_tether-prints-1-billion.yaml) | other | 2022-01-01 |  |  |
| [2022-01_tinyman-hack.yaml](data-leak/2022-01_tinyman-hack.yaml) | data-leak | 2022-01-01 |  |  |
| [2022-11_whatsapp-487m-phone-scrape.yaml](data-leak/2022-11_whatsapp-487m-phone-scrape.yaml) | data-leak | 2022-01-01 |  |  |
| [2022-08_twitter-api-54m-accounts.yaml](data-leak/2022-08_twitter-api-54m-accounts.yaml) | data-leak | 2022-01-01 |  |  |
| [2022-01_square-enix-nft-announcement.yaml](other/2022-01_square-enix-nft-announcement.yaml) | other | 2022-01-01 |  |  |
| [2022-01_government-of-south-australia-frontier-software.yaml](supply-chain/2022-01_government-of-south-australia-frontier-software.yaml) | supply-chain | 2022-01-01 |  |  |
| [2022-01_pegasus-airlines-s3-65tb.yaml](data-leak/2022-01_pegasus-airlines-s3-65tb.yaml) | data-leak | 2022-01-01 |  |  |
| [2021-12_year-rug-pull.yaml](other/2021-12_year-rug-pull.yaml) | other | 2021-12-31 |  |  |
| [2021-12_todd-kramer-nft-theft.yaml](data-leak/2021-12_todd-kramer-nft-theft.yaml) | data-leak | 2021-12-30 |  |  |
| [2021-12_fake-baby-ape-social-club-nfts.yaml](data-leak/2021-12_fake-baby-ape-social-club-nfts.yaml) | data-leak | 2021-12-29 |  |  |
| [2021-12_metamask-fake-token-launch.yaml](data-leak/2021-12_metamask-fake-token-launch.yaml) | data-leak | 2021-12-28 |  |  |
| [2021-12_waka-flocka-nft-theft.yaml](data-leak/2021-12_waka-flocka-nft-theft.yaml) | data-leak | 2021-12-28 |  |  |
| [2021-12_maricoin-announced.yaml](other/2021-12_maricoin-announced.yaml) | other | 2021-12-28 |  |  |
| [2021-12_crypto-mining-in-georgia-crushes-electrical-grid.yaml](other/2021-12_crypto-mining-in-georgia-crushes-electrical-grid.yaml) | other | 2021-12-28 |  |  |
| [2021-12_metaswap-gas-rug-pull.yaml](other/2021-12_metaswap-gas-rug-pull.yaml) | other | 2021-12-27 |  |  |
| [2021-12_metadao-rug-pull.yaml](data-leak/2021-12_metadao-rug-pull.yaml) | data-leak | 2021-12-27 |  |  |
| [2021-12_cipher-punks-nfts-created-without-permission.yaml](other/2021-12_cipher-punks-nfts-created-without-permission.yaml) | other | 2021-12-26 |  |  |
| [2021-12_elon-musk-pumps-santa-floki.yaml](other/2021-12_elon-musk-pumps-santa-floki.yaml) | other | 2021-12-25 |  |  |
| [2021-12_bergpay-eth-nft-theft.yaml](data-leak/2021-12_bergpay-eth-nft-theft.yaml) | data-leak | 2021-12-25 |  |  |
| [2021-12_blockbusterdao-announced.yaml](other/2021-12_blockbusterdao-announced.yaml) | other | 2021-12-25 |  |  |
| [2021-12_mirror-governance-attack-attempted.yaml](data-leak/2021-12_mirror-governance-attack-attempted.yaml) | data-leak | 2021-12-24 |  |  |
| [2021-12_fr0zenbuffal0-nft-theft.yaml](data-leak/2021-12_fr0zenbuffal0-nft-theft.yaml) | data-leak | 2021-12-23 |  |  |
| [2021-12_fuck-joe-biden-coin-launch.yaml](other/2021-12_fuck-joe-biden-coin-launch.yaml) | other | 2021-12-23 |  |  |
| [2021-12_open-source-nfts-made-without-permission.yaml](other/2021-12_open-source-nfts-made-without-permission.yaml) | other | 2021-12-22 |  |  |
| [2021-12_monkey-kingdom-discord-hack.yaml](data-leak/2021-12_monkey-kingdom-discord-hack.yaml) | data-leak | 2021-12-21 |  |  |
| [2021-12_visor-finance-hack.yaml](data-leak/2021-12_visor-finance-hack.yaml) | data-leak | 2021-12-21 |  |  |
| [2021-12_bob-ross-nft-announcement.yaml](other/2021-12_bob-ross-nft-announcement.yaml) | other | 2021-12-21 |  |  |
| [2021-12_fractal-discord-hack.yaml](data-leak/2021-12_fractal-discord-hack.yaml) | data-leak | 2021-12-21 |  |  |
| [2021-12_bent-finance-hack.yaml](data-leak/2021-12_bent-finance-hack.yaml) | data-leak | 2021-12-20 |  |  |
| [2021-12_grim-finance-hack.yaml](data-leak/2021-12_grim-finance-hack.yaml) | data-leak | 2021-12-18 |  |  |
| [2021-12_chivo-wallet-bug.yaml](other/2021-12_chivo-wallet-bug.yaml) | other | 2021-12-18 |  |  |
| [2021-12_artist-may-need-to-close-online-gallery.yaml](other/2021-12_artist-may-need-to-close-online-gallery.yaml) | other | 2021-12-17 |  |  |
| [2021-12_adidas-sybil-attack.yaml](other/2021-12_adidas-sybil-attack.yaml) | other | 2021-12-17 |  |  |
| [2021-12_opensea-ignores-stolen-artwork-reports.yaml](other/2021-12_opensea-ignores-stolen-artwork-reports.yaml) | other | 2021-12-17 |  |  |
| [2021-12_bored-ape-owner-messages.yaml](other/2021-12_bored-ape-owner-messages.yaml) | other | 2021-12-16 |  |  |
| [2021-12_melania-trump-nft-announcement.yaml](other/2021-12_melania-trump-nft-announcement.yaml) | other | 2021-12-16 |  |  |
| [2021-12_i-s-t-a-l-k-e-r-2-i-nft-cancellation.yaml](other/2021-12_i-s-t-a-l-k-e-r-2-i-nft-cancellation.yaml) | other | 2021-12-16 |  |  |
| [2021-12_s-t-a-l-k-e-r-2-nft-cancellation.yaml](other/2021-12_s-t-a-l-k-e-r-2-nft-cancellation.yaml) | other | 2021-12-16 |  |  |
| [2021-12_crypto-miner-tweet.yaml](other/2021-12_crypto-miner-tweet.yaml) | other | 2021-12-15 |  |  |
| [2021-12_doodles-typo.yaml](other/2021-12_doodles-typo.yaml) | other | 2021-12-15 |  |  |
| [2021-12_hacked-aws-account-mines-monero.yaml](data-leak/2021-12_hacked-aws-account-mines-monero.yaml) | data-leak | 2021-12-14 |  |  |
| [2021-12_crypto-tracker-bugs.yaml](other/2021-12_crypto-tracker-bugs.yaml) | other | 2021-12-14 |  |  |
| [2021-12_laurent-correia-rug-pull.yaml](other/2021-12_laurent-correia-rug-pull.yaml) | other | 2021-12-14 |  |  |
| [2021-12_stan-lee-nft-announcement.yaml](other/2021-12_stan-lee-nft-announcement.yaml) | other | 2021-12-14 |  |  |
| [2021-12_seattle-kraken-nfts-announcement.yaml](other/2021-12_seattle-kraken-nfts-announcement.yaml) | other | 2021-12-13 |  |  |
| [2021-12_vulcan-forged-hack.yaml](data-leak/2021-12_vulcan-forged-hack.yaml) | data-leak | 2021-12-13 |  |  |
| [2021-12_george-floyd-nfts.yaml](other/2021-12_george-floyd-nfts.yaml) | other | 2021-12-13 |  |  |
| [2021-12_loish-art-thefts.yaml](other/2021-12_loish-art-thefts.yaml) | other | 2021-12-13 |  |  |
| [2021-12_bored-ape-typo.yaml](other/2021-12_bored-ape-typo.yaml) | other | 2021-12-13 |  |  |
| [2021-12_peter-molyneaux-game-announcement.yaml](other/2021-12_peter-molyneaux-game-announcement.yaml) | other | 2021-12-11 |  |  |
| [2021-12_ascendex-hacked.yaml](data-leak/2021-12_ascendex-hacked.yaml) | data-leak | 2021-12-11 |  |  |
| [2021-12_ukg-kronos-ransomware.yaml](ransomware/2021-12_ukg-kronos-ransomware.yaml) | ransomware | 2021-12-11 |  |  |
| [2021-12_kronos-ukg-blackcat-ransomware.yaml](ransomware/2021-12_kronos-ukg-blackcat-ransomware.yaml) | ransomware | 2021-12-11 |  |  |
| [2021-12_mcdonalds-nft-racial-slur-controversy.yaml](other/2021-12_mcdonalds-nft-racial-slur-controversy.yaml) | other | 2021-12-11 |  |  |
| [2021-12_cash-app-former-employee.yaml](data-leak/2021-12_cash-app-former-employee.yaml) | data-leak | 2021-12-10 |  |  |
| [2021-12_kickstarter-blockchain-announcement.yaml](other/2021-12_kickstarter-blockchain-announcement.yaml) | other | 2021-12-08 |  |  |
| [2021-12_dydx-outage.yaml](other/2021-12_dydx-outage.yaml) | other | 2021-12-08 |  |  |
| [2021-12_ubisoft-i-tom-clancy-i-nft-announcement.yaml](other/2021-12_ubisoft-i-tom-clancy-i-nft-announcement.yaml) | other | 2021-12-07 |  |  |
| [2021-12_ubisoft-tom-clancy-nft-announcement.yaml](other/2021-12_ubisoft-tom-clancy-nft-announcement.yaml) | other | 2021-12-07 |  |  |
| [2021-12_wildworks-nft-gaming-announcement.yaml](other/2021-12_wildworks-nft-gaming-announcement.yaml) | other | 2021-12-06 |  |  |
| [2021-12_8ight-finance-hack.yaml](data-leak/2021-12_8ight-finance-hack.yaml) | data-leak | 2021-12-06 |  |  |
| [2021-12_i-coindesk-i-olympusdao-article.yaml](other/2021-12_i-coindesk-i-olympusdao-article.yaml) | other | 2021-12-05 |  |  |
| [2021-12_coindesk-olympusdao-article.yaml](other/2021-12_coindesk-olympusdao-article.yaml) | other | 2021-12-05 |  |  |
| [2021-12_eye-care-leaders-ehr-3-6m.yaml](ransomware/2021-12_eye-care-leaders-ehr-3-6m.yaml) | ransomware | 2021-12-04 |  |  |
| [2021-12_bitmart-hack.yaml](data-leak/2021-12_bitmart-hack.yaml) | data-leak | 2021-12-04 |  |  |
| [2021-12_tether-prints-3-billion.yaml](other/2021-12_tether-prints-3-billion.yaml) | other | 2021-12-04 |  |  |
| [2021-12_bitmart-exchange-hack-196m.yaml](other/2021-12_bitmart-exchange-hack-196m.yaml) | other | 2021-12-04 |  |  |
| [2021-12_polygon-hack.yaml](data-leak/2021-12_polygon-hack.yaml) | data-leak | 2021-12-04 |  |  |
| [2021-12_wikipedia-nfts.yaml](other/2021-12_wikipedia-nfts.yaml) | other | 2021-12-03 |  |  |
| [2021-12_codex-launches.yaml](other/2021-12_codex-launches.yaml) | other | 2021-12-02 |  |  |
| [2021-12_ivars-auzins-sec-charges.yaml](other/2021-12_ivars-auzins-sec-charges.yaml) | other | 2021-12-02 |  |  |
| [2022-04_lincoln-college-closure.yaml](ransomware/2022-04_lincoln-college-closure.yaml) | ransomware | 2021-12-01 |  |  |
| [2021-12_twitter-api-5-4m-scrape.yaml](data-leak/2021-12_twitter-api-5-4m-scrape.yaml) | data-leak | 2021-12-01 |  |  |
| [2021-12_badgerdao-hack.yaml](data-leak/2021-12_badgerdao-hack.yaml) | data-leak | 2021-12-01 |  |  |
| [2021-12_log4shell.yaml](other/2021-12_log4shell.yaml) | other | 2021-12-01 | Conti (ransomware), various c… | CVE-2021-44228, CVE-2021-45046, CVE-202… |
| [2021-11_unvaxxed-sperm-launch.yaml](other/2021-11_unvaxxed-sperm-launch.yaml) | other | 2021-11-30 |  |  |
| [2021-11_monox-hack.yaml](data-leak/2021-11_monox-hack.yaml) | data-leak | 2021-11-30 |  |  |
| [2021-11_bored-apes-stolen-from-friesframe.yaml](data-leak/2021-11_bored-apes-stolen-from-friesframe.yaml) | data-leak | 2021-11-30 |  |  |
| [2021-11_snowdogdao-crash.yaml](other/2021-11_snowdogdao-crash.yaml) | other | 2021-11-26 |  |  |
| [2021-11_metaworld-serial-scammer.yaml](other/2021-11_metaworld-serial-scammer.yaml) | other | 2021-11-25 |  |  |
| [2021-11_senat-committee-stablecoin-letters.yaml](other/2021-11_senat-committee-stablecoin-letters.yaml) | other | 2021-11-23 |  |  |
| [2021-11_ryan-ginster-sec-charges.yaml](other/2021-11_ryan-ginster-sec-charges.yaml) | other | 2021-11-23 |  |  |
| [2021-11_i-wolf-game-i-bug.yaml](other/2021-11_i-wolf-game-i-bug.yaml) | other | 2021-11-22 |  |  |
| [2021-11_wolf-game-bug.yaml](other/2021-11_wolf-game-bug.yaml) | other | 2021-11-22 |  |  |
| [2021-11_nft-artist-steals-stormtrooper-art.yaml](other/2021-11_nft-artist-steals-stormtrooper-art.yaml) | other | 2021-11-22 |  |  |
| [2021-11_constitutiondao-fails.yaml](other/2021-11_constitutiondao-fails.yaml) | other | 2021-11-14 |  |  |
| [2021-11_right-click-save-this-nft.yaml](other/2021-11_right-click-save-this-nft.yaml) | other | 2021-11-13 |  |  |
| [2021-12_badgerdao-frontend-exploit.yaml](other/2021-12_badgerdao-frontend-exploit.yaml) | other | 2021-11-10 |  |  |
| [2022-01_red-cross-not-disclosed.yaml](supply-chain/2022-01_red-cross-not-disclosed.yaml) | supply-chain | 2021-11-09 |  | CVE-2021-40539 |
| [2021-11_filecoin-ponzi-scheme.yaml](other/2021-11_filecoin-ponzi-scheme.yaml) | other | 2021-11-06 |  |  |
| [2021-11_cryptoland-video.yaml](other/2021-11_cryptoland-video.yaml) | other | 2021-11-06 |  |  |
| [2021-11_fake-press-release-about-bitcoin-cash.yaml](other/2021-11_fake-press-release-about-bitcoin-cash.yaml) | other | 2021-11-05 |  |  |
| [2021-11_bzx-hack.yaml](data-leak/2021-11_bzx-hack.yaml) | data-leak | 2021-11-05 |  |  |
| [2021-11_blockchain-global-enters-liquidation.yaml](other/2021-11_blockchain-global-enters-liquidation.yaml) | other | 2021-11-03 |  |  |
| [2021-11_robinhood-social-engineering-7m.yaml](credential-theft/2021-11_robinhood-social-engineering-7m.yaml) | credential-theft | 2021-11-03 |  |  |
| [2021-11_vesper-finance-hack.yaml](data-leak/2021-11_vesper-finance-hack.yaml) | data-leak | 2021-11-02 |  |  |
| [2021-11_i-squid-game-i-rug-pull.yaml](other/2021-11_i-squid-game-i-rug-pull.yaml) | other | 2021-11-01 |  |  |
| [2021-11_squid-game-rug-pull.yaml](other/2021-11_squid-game-rug-pull.yaml) | other | 2021-11-01 |  |  |
| [2021-11_uber-eats-third-party-820k.yaml](supply-chain/2021-11_uber-eats-third-party-820k.yaml) | supply-chain | 2021-11-01 |  |  |
| [2021-11_qrs-clients-qrs.yaml](supply-chain/2021-11_qrs-clients-qrs.yaml) | supply-chain | 2021-11-01 |  |  |
| [2021-11_bxh-exchange-hack.yaml](data-leak/2021-11_bxh-exchange-hack.yaml) | data-leak | 2021-11-01 |  |  |
| [2021-10_monkey-jizz-rug-pull.yaml](other/2021-10_monkey-jizz-rug-pull.yaml) | other | 2021-10-31 |  |  |
| [2021-10_calvin-becerra-nft-theft.yaml](data-leak/2021-10_calvin-becerra-nft-theft.yaml) | data-leak | 2021-10-31 |  |  |
| [2021-10_anubisdao-rug-pull.yaml](other/2021-10_anubisdao-rug-pull.yaml) | other | 2021-10-29 |  |  |
| [2021-10_miss-universe-rug-pull.yaml](other/2021-10_miss-universe-rug-pull.yaml) | other | 2021-10-28 |  |  |
| [2021-10_tekashi-6ix9ine-rug-pull.yaml](other/2021-10_tekashi-6ix9ine-rug-pull.yaml) | other | 2021-10-28 |  |  |
| [2021-10_opensea-svg-vulnerability.yaml](data-leak/2021-10_opensea-svg-vulnerability.yaml) | data-leak | 2021-10-28 |  |  |
| [2021-10_c-r-e-a-m-hack-35-3.yaml](data-leak/2021-10_c-r-e-a-m-hack-35-3.yaml) | data-leak | 2021-10-27 |  |  |
| [2021-10_c-r-e-a-m-hack-3.yaml](data-leak/2021-10_c-r-e-a-m-hack-3.yaml) | data-leak | 2021-10-27 |  |  |
| [2021-10_cream-finance-flash-loan-130m.yaml](other/2021-10_cream-finance-flash-loan-130m.yaml) | other | 2021-10-27 |  |  |
| [2021-10_ryval-launch.yaml](other/2021-10_ryval-launch.yaml) | other | 2021-10-26 |  |  |
| [2021-10_ua-parser-js-npm-malware.yaml](supply-chain/2021-10_ua-parser-js-npm-malware.yaml) | supply-chain | 2021-10-22 | XMRig (Monero cryptominer), j… |  |
| [2021-10_realms-of-ruin-fails-to-launch.yaml](other/2021-10_realms-of-ruin-fails-to-launch.yaml) | other | 2021-10-21 |  |  |
| [2021-10_creaturetoadz-discord-hack.yaml](data-leak/2021-10_creaturetoadz-discord-hack.yaml) | data-leak | 2021-10-20 |  |  |
| [2021-10_indexed-finance-hack.yaml](data-leak/2021-10_indexed-finance-hack.yaml) | data-leak | 2021-10-14 |  |  |
| [2021-10_cox-communications-social-engineering.yaml](data-leak/2021-10_cox-communications-social-engineering.yaml) | data-leak | 2021-10-11 |  |  |
| [2021-10_twitch-source-code-leak.yaml](data-leak/2021-10_twitch-source-code-leak.yaml) | data-leak | 2021-10-06 |  |  |
| [2021-10_solana-towers-rug-pull.yaml](other/2021-10_solana-towers-rug-pull.yaml) | other | 2021-10-06 |  |  |
| [2021-10_evolved-apes-rug-pull.yaml](other/2021-10_evolved-apes-rug-pull.yaml) | other | 2021-10-05 |  |  |
| [2021-10_twitch-source-code-125gb-leak.yaml](data-leak/2021-10_twitch-source-code-125gb-leak.yaml) | data-leak | 2021-10-04 |  |  |
| [2021-10_anthem-humana-practicemax.yaml](supply-chain/2021-10_anthem-humana-practicemax.yaml) | supply-chain | 2021-10-01 |  |  |
| [2021-10_durham-regional-government-not-disclosed.yaml](supply-chain/2021-10_durham-regional-government-not-disclosed.yaml) | supply-chain | 2021-10-01 |  |  |
| [2021-10_fullerton-health-agape-connecting-people.yaml](supply-chain/2021-10_fullerton-health-agape-connecting-people.yaml) | supply-chain | 2021-10-01 |  |  |
| [2021-10_baller-ape-club-rug-pull.yaml](other/2021-10_baller-ape-club-rug-pull.yaml) | other | 2021-10-01 |  |  |
| [2021-09_compound-finance-bug.yaml](other/2021-09_compound-finance-bug.yaml) | other | 2021-09-30 |  |  |
| [2021-09_iconics-rug-pull.yaml](other/2021-09_iconics-rug-pull.yaml) | other | 2021-09-30 |  |  |
| [2021-09_german-government-blockchain-project-scrapped.yaml](other/2021-09_german-government-blockchain-project-scrapped.yaml) | other | 2021-09-23 |  |  |
| [2021-09_vee-finance-hack.yaml](data-leak/2021-09_vee-finance-hack.yaml) | data-leak | 2021-09-21 |  |  |
| [2021-09_pnetwork-hack.yaml](data-leak/2021-09_pnetwork-hack.yaml) | data-leak | 2021-09-20 |  |  |
| [2021-09_sushiswap-hack.yaml](supply-chain/2021-09_sushiswap-hack.yaml) | supply-chain | 2021-09-17 |  |  |
| [2021-09_opensea-insider-trading-allegation.yaml](other/2021-09_opensea-insider-trading-allegation.yaml) | other | 2021-09-15 |  |  |
| [2021-09_fake-press-release-about-litecoin.yaml](other/2021-09_fake-press-release-about-litecoin.yaml) | other | 2021-09-13 |  |  |
| [2021-09_gtv-media-group-sec-settlement.yaml](other/2021-09_gtv-media-group-sec-settlement.yaml) | other | 2021-09-13 |  |  |
| [2021-09_rivetz-corp-sec-charges.yaml](other/2021-09_rivetz-corp-sec-charges.yaml) | other | 2021-09-08 |  |  |
| [2021-09_ambulance-victoria-2241-staff.yaml](data-leak/2021-09_ambulance-victoria-2241-staff.yaml) | data-leak | 2021-09-07 |  |  |
| [2021-09_el-salvador-adopts-bitcoin.yaml](other/2021-09_el-salvador-adopts-bitcoin.yaml) | other | 2021-09-07 |  |  |
| [2021-11_godaddy-wordpress-hosting-1m.yaml](credential-theft/2021-11_godaddy-wordpress-hosting-1m.yaml) | credential-theft | 2021-09-06 |  |  |
| [2021-09_godaddy-wordpress-1-2m.yaml](data-leak/2021-09_godaddy-wordpress-1-2m.yaml) | data-leak | 2021-09-06 |  |  |
| [2021-08_c-r-e-a-m-hack-35-2.yaml](data-leak/2021-08_c-r-e-a-m-hack-35-2.yaml) | data-leak | 2021-08-30 |  |  |
| [2021-08_c-r-e-a-m-hack-2.yaml](data-leak/2021-08_c-r-e-a-m-hack-2.yaml) | data-leak | 2021-08-30 |  |  |
| [2021-08_xtoken-hack-35-2.yaml](data-leak/2021-08_xtoken-hack-35-2.yaml) | data-leak | 2021-08-29 |  |  |
| [2021-08_xtoken-hack-2.yaml](data-leak/2021-08_xtoken-hack-2.yaml) | data-leak | 2021-08-29 |  |  |
| [2021-08_sohrob-farudi-nft-theft.yaml](data-leak/2021-08_sohrob-farudi-nft-theft.yaml) | data-leak | 2021-08-25 |  |  |
| [2021-08_jeff-nicholas-nft-theft.yaml](data-leak/2021-08_jeff-nicholas-nft-theft.yaml) | data-leak | 2021-08-24 |  |  |
| [2021-08_apria-healthcare-1-87m.yaml](data-leak/2021-08_apria-healthcare-1-87m.yaml) | data-leak | 2021-08-22 |  |  |
| [2021-08_liquid-global-hack.yaml](data-leak/2021-08_liquid-global-hack.yaml) | data-leak | 2021-08-19 |  |  |
| [2021-08_microsoft-exchange-proxyshell.yaml](other/2021-08_microsoft-exchange-proxyshell.yaml) | other | 2021-08-13 | LockFile ransomware, Babuk ra… | CVE-2021-34473, CVE-2021-34523, CVE-202… |
| [2021-08_dao-maker-hack.yaml](data-leak/2021-08_dao-maker-hack.yaml) | data-leak | 2021-08-12 |  |  |
| [2021-08_poly-network-hack-1.yaml](data-leak/2021-08_poly-network-hack-1.yaml) | data-leak | 2021-08-11 |  |  |
| [2021-08_poly-network-defi-611m.yaml](other/2021-08_poly-network-defi-611m.yaml) | other | 2021-08-10 |  |  |
| [2021-08_fame-lady-squad-scam.yaml](other/2021-08_fame-lady-squad-scam.yaml) | other | 2021-08-10 |  |  |
| [2021-08_poloniex-sec-settlement.yaml](other/2021-08_poloniex-sec-settlement.yaml) | other | 2021-08-09 |  |  |
| [2021-08_azure-cosmos-db-chaosdb.yaml](other/2021-08_azure-cosmos-db-chaosdb.yaml) | other | 2021-08-09 |  |  |
| [2021-08_blockchain-credit-partners-sec-settlement.yaml](other/2021-08_blockchain-credit-partners-sec-settlement.yaml) | other | 2021-08-06 |  |  |
| [2021-08_deviantart-releases-theft-scanner.yaml](other/2021-08_deviantart-releases-theft-scanner.yaml) | other | 2021-08-06 |  |  |
| [2021-08_uulala-sec-settlement.yaml](other/2021-08_uulala-sec-settlement.yaml) | other | 2021-08-04 |  |  |
| [2021-08_eskenazi-health-vice-society.yaml](ransomware/2021-08_eskenazi-health-vice-society.yaml) | ransomware | 2021-08-04 | Vice Society ransomware |  |
| [2021-08_popsicle-finance-hack.yaml](data-leak/2021-08_popsicle-finance-hack.yaml) | data-leak | 2021-08-03 |  |  |
| [2021-08_american-airlines-ford-maryland-depa-microsoft.yaml](supply-chain/2021-08_american-airlines-ford-maryland-depa-microsoft.yaml) | supply-chain | 2021-08-01 |  |  |
| [2021-08_catholic-health-capturerx.yaml](supply-chain/2021-08_catholic-health-capturerx.yaml) | supply-chain | 2021-08-01 |  |  |
| [2021-09_roper-st-francis-healthcare.yaml](ransomware/2021-09_roper-st-francis-healthcare.yaml) | ransomware | 2021-08-01 |  |  |
| [2021-08_first-horizon-bank-not-disclosed.yaml](supply-chain/2021-08_first-horizon-bank-not-disclosed.yaml) | supply-chain | 2021-08-01 |  |  |
| [2024-09_tmobile-fcc-settlement.yaml](data-leak/2024-09_tmobile-fcc-settlement.yaml) | data-leak | 2021-08-01 |  |  |
| [2021-08_tmobile-john-binns-54m.yaml](data-leak/2021-08_tmobile-john-binns-54m.yaml) | data-leak | 2021-08-01 |  |  |
| [2021-07_finiko-ponzi-scheme.yaml](data-leak/2021-07_finiko-ponzi-scheme.yaml) | data-leak | 2021-07-31 |  |  |
| [2021-07_rune-thefts.yaml](other/2021-07_rune-thefts.yaml) | other | 2021-07-23 |  |  |
| [2021-07_norton-antivirus-mines-crypto.yaml](other/2021-07_norton-antivirus-mines-crypto.yaml) | other | 2021-07-20 |  |  |
| [2021-07_circle-isn-t-backed-as-they-claim.yaml](other/2021-07_circle-isn-t-backed-as-they-claim.yaml) | other | 2021-07-16 |  |  |
| [2021-07_kaseya-vsa-revil.yaml](supply-chain/2021-07_kaseya-vsa-revil.yaml) | supply-chain | 2021-07-02 | REvil / Sodinokibi | CVE-2021-30116 |
| [2021-07_morgan-stanley-guidehouse-accellion.yaml](supply-chain/2021-07_morgan-stanley-guidehouse-accellion.yaml) | supply-chain | 2021-07-01 | DEWMODE web shell |  |
| [2021-07_hospitals-practicefirst.yaml](supply-chain/2021-07_hospitals-practicefirst.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_msps-and-clients-including-visma-ess-kaseya.yaml](supply-chain/2021-07_msps-and-clients-including-visma-ess-kaseya.yaml) | supply-chain | 2021-07-01 | REvil (Sodinokibi) ransomware |  |
| [2021-07_spreadgroup-customers-spreadshirt-spreadshop-a.yaml](supply-chain/2021-07_spreadgroup-customers-spreadshirt-spreadshop-a.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_memorial-health-system-guidehouse.yaml](supply-chain/2021-07_memorial-health-system-guidehouse.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_jefferson-s-kimmel-cancer-center-elekta.yaml](supply-chain/2021-07_jefferson-s-kimmel-cancer-center-elekta.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-07_hospitals-clearbalance.yaml](supply-chain/2021-07_hospitals-clearbalance.yaml) | supply-chain | 2021-07-01 |  |  |
| [2021-06_stablemagnet-rug-pull.yaml](other/2021-06_stablemagnet-rug-pull.yaml) | other | 2021-06-23 |  |  |
| [2022-06_unc2903-imdsv1-aws-metadata.yaml](credential-theft/2022-06_unc2903-imdsv1-aws-metadata.yaml) | credential-theft | 2021-06-21 |  |  |
| [2021-06_titan-stablecoin-collapse.yaml](other/2021-06_titan-stablecoin-collapse.yaml) | other | 2021-06-16 |  |  |
| [2021-06_ea-games-lapsus-source-code.yaml](data-leak/2021-06_ea-games-lapsus-source-code.yaml) | data-leak | 2021-06-06 |  |  |
| [2021-06_amerigas-j-j-keller.yaml](supply-chain/2021-06_amerigas-j-j-keller.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-07_saudi-aramco-not-disclosed.yaml](supply-chain/2021-07_saudi-aramco-not-disclosed.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_latitude-financial-oaic-pre-breach.yaml](data-leak/2021-06_latitude-financial-oaic-pre-breach.yaml) | data-leak | 2021-06-01 |  |  |
| [2024-02_volt-typhoon-critical-infrastructure.yaml](other/2024-02_volt-typhoon-critical-infrastructure.yaml) | other | 2021-06-01 |  | CVE-2021-40539, CVE-2021-27860 |
| [2021-06_u-s-lawmakers-house-legislators-iconstituent.yaml](supply-chain/2021-06_u-s-lawmakers-house-legislators-iconstituent.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_ohio-medicaid-program-maximus.yaml](supply-chain/2021-06_ohio-medicaid-program-maximus.yaml) | supply-chain | 2021-06-01 |  |  |
| [2023-01_twitter-api-scrape.yaml](data-leak/2023-01_twitter-api-scrape.yaml) | data-leak | 2021-06-01 |  |  |
| [2021-06_blue-cross-blue-shield-of-kansas-cit-logicgate.yaml](supply-chain/2021-06_blue-cross-blue-shield-of-kansas-cit-logicgate.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_cancer-centers-of-southwest-oklahoma-elekta.yaml](supply-chain/2021-06_cancer-centers-of-southwest-oklahoma-elekta.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_harbor-regional-health-capturerx.yaml](supply-chain/2021-06_harbor-regional-health-capturerx.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-06_cvs-health-not-disclosed.yaml](supply-chain/2021-06_cvs-health-not-disclosed.yaml) | supply-chain | 2021-06-01 |  |  |
| [2021-05_jbs-foods-revil.yaml](ransomware/2021-05_jbs-foods-revil.yaml) | ransomware | 2021-05-30 | REvil (Sodinokibi) |  |
| [2021-05_jbs-foods.yaml](ransomware/2021-05_jbs-foods.yaml) | ransomware | 2021-05-30 | REvil / Sodinokibi |  |
| [2021-05_belt-finance-hack.yaml](data-leak/2021-05_belt-finance-hack.yaml) | data-leak | 2021-05-29 |  |  |
| [2021-05_sec-begins-investigating-bitconnect.yaml](other/2021-05_sec-begins-investigating-bitconnect.yaml) | other | 2021-05-28 |  |  |
| [2021-05_burgerswap-exploit.yaml](data-leak/2021-05_burgerswap-exploit.yaml) | data-leak | 2021-05-28 |  |  |
| [2021-05_bogged-finance-hack.yaml](data-leak/2021-05_bogged-finance-hack.yaml) | data-leak | 2021-05-23 |  |  |
| [2021-05_defi100-rug-pull.yaml](other/2021-05_defi100-rug-pull.yaml) | other | 2021-05-22 |  |  |
| [2021-05_pancakebunny-exploit.yaml](data-leak/2021-05_pancakebunny-exploit.yaml) | data-leak | 2021-05-19 |  |  |
| [2021-05_finnexus-rug-pull.yaml](other/2021-05_finnexus-rug-pull.yaml) | other | 2021-05-17 |  |  |
| [2021-05_bearn-hack.yaml](data-leak/2021-05_bearn-hack.yaml) | data-leak | 2021-05-16 |  |  |
| [2021-05_ireland-hse-conti-ransomware.yaml](ransomware/2021-05_ireland-hse-conti-ransomware.yaml) | ransomware | 2021-05-14 | Conti ransomware; Cobalt Stri… |  |
| [2021-05_xtoken-hack-35-1.yaml](data-leak/2021-05_xtoken-hack-35-1.yaml) | data-leak | 2021-05-12 |  |  |
| [2021-05_xtoken-hack-1.yaml](data-leak/2021-05_xtoken-hack-1.yaml) | data-leak | 2021-05-12 |  |  |
| [2021-05_rari-capital-exploit.yaml](data-leak/2021-05_rari-capital-exploit.yaml) | data-leak | 2021-05-08 |  |  |
| [2021-05_colonial-pipeline.yaml](ransomware/2021-05_colonial-pipeline.yaml) | ransomware | 2021-05-07 | DarkSide |  |
| [2021-05_value-defi-hack-35-2.yaml](data-leak/2021-05_value-defi-hack-35-2.yaml) | data-leak | 2021-05-07 |  |  |
| [2021-05_value-defi-hack-2.yaml](data-leak/2021-05_value-defi-hack-2.yaml) | data-leak | 2021-05-07 |  |  |
| [2021-05_value-defi-hack-35-1.yaml](data-leak/2021-05_value-defi-hack-35-1.yaml) | data-leak | 2021-05-05 |  |  |
| [2021-05_value-defi-hack-1.yaml](data-leak/2021-05_value-defi-hack-1.yaml) | data-leak | 2021-05-05 |  |  |
| [2021-05_university-of-houston-herff-jones.yaml](supply-chain/2021-05_university-of-houston-herff-jones.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_fasttrack-customers-fasttrack-recruitment.yaml](supply-chain/2021-05_fasttrack-customers-fasttrack-recruitment.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_u-s-government-blueforce.yaml](supply-chain/2021-05_u-s-government-blueforce.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_fox-s-clinic-the-alpine-center-for-diabetes-endocrinology-and-metabolism-aprima.yaml](supply-chain/2021-05_fox-s-clinic-the-alpine-center-for-diabetes-endocrinology-and-metabolism-aprima.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_japanese-government-the-ministry-of-land-infrastructure-transport-and-tourism-fujitsu.yaml](supply-chain/2021-05_japanese-government-the-ministry-of-land-infrastructure-transport-and-tourism-fujitsu.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_u-s-department-of-energy-fermilab.yaml](supply-chain/2021-05_u-s-department-of-energy-fermilab.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-06_linkedin-700m-api-scrape.yaml](data-leak/2021-06_linkedin-700m-api-scrape.yaml) | data-leak | 2021-05-01 |  |  |
| [2021-05_spartan-protocol-hack.yaml](data-leak/2021-05_spartan-protocol-hack.yaml) | data-leak | 2021-05-01 |  |  |
| [2021-05_canada-post-commport-communications.yaml](supply-chain/2021-05_canada-post-commport-communications.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-08_microsoft-power-apps-misconfiguration.yaml](data-leak/2021-08_microsoft-power-apps-misconfiguration.yaml) | data-leak | 2021-05-01 |  |  |
| [2021-05_ardagh-clients-ardagh.yaml](supply-chain/2021-05_ardagh-clients-ardagh.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-05_ac-health-systems-and-san-diego-family-care-sdfc-caresouth-carolina-health-center-partners-of-southern-california-netgain.yaml](supply-chain/2021-05_ac-health-systems-and-san-diego-family-care-sdfc-caresouth-carolina-health-center-partners-of-southern-california-netgain.yaml) | supply-chain | 2021-05-01 |  |  |
| [2021-04_nfts-thwart-domain-auction.yaml](other/2021-04_nfts-thwart-domain-auction.yaml) | other | 2021-04-28 |  |  |
| [2021-04_brenntag-darkside-chemicals.yaml](ransomware/2021-04_brenntag-darkside-chemicals.yaml) | ransomware | 2021-04-28 | DarkSide |  |
| [2021-04_uranium-finance-hack.yaml](data-leak/2021-04_uranium-finance-hack.yaml) | data-leak | 2021-04-28 |  |  |
| [2021-04_uranium-finance-bsc-50m-exploit.yaml](other/2021-04_uranium-finance-bsc-50m-exploit.yaml) | other | 2021-04-28 |  |  |
| [2021-05_scripps-health-conti.yaml](ransomware/2021-05_scripps-health-conti.yaml) | ransomware | 2021-04-26 | Conti ransomware |  |
| [2021-04_thodex-exit-scam.yaml](other/2021-04_thodex-exit-scam.yaml) | other | 2021-04-21 |  |  |
| [2021-04_museum-burns-cryptopunks.yaml](other/2021-04_museum-burns-cryptopunks.yaml) | other | 2021-04-21 |  |  |
| [2021-04_click-studios-customers-click-studios.yaml](supply-chain/2021-04_click-studios-customers-click-studios.yaml) | supply-chain | 2021-04-20 | Moserpass |  |
| [2021-04_easyfi-hack.yaml](data-leak/2021-04_easyfi-hack.yaml) | data-leak | 2021-04-19 |  |  |
| [2021-04_africrypt-exit-scam.yaml](other/2021-04_africrypt-exit-scam.yaml) | other | 2021-04-13 |  |  |
| [2021-07_reproductive-biology-associates-doppelpaymer.yaml](ransomware/2021-07_reproductive-biology-associates-doppelpaymer.yaml) | ransomware | 2021-04-07 | DoppelPaymer ransomware |  |
| [2021-04_tata-communications-bharti-airtel-and-dbs-bank-route-mobil.yaml](supply-chain/2021-04_tata-communications-bharti-airtel-and-dbs-bank-route-mobil.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_doctors-medical-center-medifie.yaml](supply-chain/2021-04_doctors-medical-center-medifie.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_biotel-heart-not-disclosed.yaml](supply-chain/2021-04_biotel-heart-not-disclosed.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_callx-customers-possibly-lendingtree-liberty-mutual-insurance-and-vivint-among-the-clients-callx.yaml](supply-chain/2021-04_callx-customers-possibly-lendingtree-liberty-mutual-insurance-and-vivint-among-the-clients-callx.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_upstox-not-disclosed.yaml](supply-chain/2021-04_upstox-not-disclosed.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_celcius-not-disclosed.yaml](supply-chain/2021-04_celcius-not-disclosed.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_wiener-kennedy-perkins-co-netgain-4th-party.yaml](supply-chain/2021-04_wiener-kennedy-perkins-co-netgain-4th-party.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_centene-subsidiaries-healthnet-chw-accellion.yaml](supply-chain/2021-04_centene-subsidiaries-healthnet-chw-accellion.yaml) | supply-chain | 2021-04-01 | DEWMODE web shell |  |
| [2021-04_atlassian-procter-gamble-godaddy-the-washington-post-codecov.yaml](supply-chain/2021-04_atlassian-procter-gamble-godaddy-the-washington-post-codecov.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_ftx-mobilecoin-exploit.yaml](data-leak/2021-04_ftx-mobilecoin-exploit.yaml) | data-leak | 2021-04-01 |  |  |
| [2021-04_department-of-health-and-human-services-uchicago-king-s-daughters-health-system-osf-healthcare-aspirus-uchicago-medicine-and-memorial-hermann-health-system-meddata.yaml](supply-chain/2021-04_department-of-health-and-human-services-uchicago-king-s-daughters-health-system-osf-healthcare-aspirus-uchicago-medicine-and-memorial-hermann-health-system-meddata.yaml) | supply-chain | 2021-04-01 |  |  |
| [2025-04_blue-shield-california-google-analytics.yaml](data-leak/2025-04_blue-shield-california-google-analytics.yaml) | data-leak | 2021-04-01 |  |  |
| [2021-04_ei2-i-vic-international.yaml](supply-chain/2021-04_ei2-i-vic-international.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_japanese-prime-minister-s-cabinet-office-soliton-filezen-application.yaml](supply-chain/2021-04_japanese-prime-minister-s-cabinet-office-soliton-filezen-application.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_park-mobile-not-disclosed.yaml](supply-chain/2021-04_park-mobile-not-disclosed.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_apple-quanta.yaml](supply-chain/2021-04_apple-quanta.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_peach-aviation-zipair-tokyo-air-belgium-sky-airlines-air-transat-vietravel-aero-k-airlines-salam-air-flysafair-air-india-express-wingo-radixx-subsidiary-of-sabre-c.yaml](supply-chain/2021-04_peach-aviation-zipair-tokyo-air-belgium-sky-airlines-air-transat-vietravel-aero-k-airlines-salam-air-flysafair-air-india-express-wingo-radixx-subsidiary-of-sabre-c.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_stanford-university-the-university-of-maryland-baltimore-and-the-university-of-california-at-berkeley-accellion.yaml](supply-chain/2021-04_stanford-university-the-university-of-maryland-baltimore-and-the-university-of-california-at-berkeley-accellion.yaml) | supply-chain | 2021-04-01 | DEWMODE web shell |  |
| [2021-04_subsidiaries-of-personal-touch-personal-touch-retirement-solutions-personal-touch-mortgage-administration-services-personal-touch-holding-corp.yaml](supply-chain/2021-04_subsidiaries-of-personal-touch-personal-touch-retirement-solutions-personal-touch-mortgage-administration-services-personal-touch-holding-corp.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_apple-valley-clinic-netgain.yaml](supply-chain/2021-04_apple-valley-clinic-netgain.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-04_illinois-dhs-medicaid-misconfiguration.yaml](data-leak/2021-04_illinois-dhs-medicaid-misconfiguration.yaml) | data-leak | 2021-04-01 |  |  |
| [2021-04_amazon-flipkart-myntra-swiggy-and-zomato-bizongo.yaml](supply-chain/2021-04_amazon-flipkart-myntra-swiggy-and-zomato-bizongo.yaml) | supply-chain | 2021-04-01 |  |  |
| [2021-03_nine-entertainment-conti.yaml](ransomware/2021-03_nine-entertainment-conti.yaml) | ransomware | 2021-03-28 | Conti ransomware |  |
| [2021-03_cna-financial-phoenix-cryptolocker.yaml](ransomware/2021-03_cna-financial-phoenix-cryptolocker.yaml) | ransomware | 2021-03-21 | Phoenix CryptoLocker (Evil Co… |  |
| [2021-03_cna-financial.yaml](ransomware/2021-03_cna-financial.yaml) | ransomware | 2021-03-21 | Phoenix CryptoLocker (WastedL… |  |
| [2021-03_turtledex-rug-pull.yaml](other/2021-03_turtledex-rug-pull.yaml) | other | 2021-03-19 |  |  |
| [2021-03_luxottica-eyecare-70m.yaml](data-leak/2021-03_luxottica-eyecare-70m.yaml) | data-leak | 2021-03-16 |  |  |
| [2021-08_renaissance-life-health-insurance-secure-administrative-so.yaml](supply-chain/2021-08_renaissance-life-health-insurance-secure-administrative-so.yaml) | supply-chain | 2021-03-15 | ransomware (variant unspecifi… |  |
| [2021-03_revil-acer-proxylogen-50m.yaml](ransomware/2021-03_revil-acer-proxylogen-50m.yaml) | ransomware | 2021-03-14 | REvil (Sodinokibi) ransomware | CVE-2021-26855 |
| [2021-03_roll-hack.yaml](data-leak/2021-03_roll-hack.yaml) | data-leak | 2021-03-14 |  |  |
| [2021-03_beeple-wash-trade.yaml](other/2021-03_beeple-wash-trade.yaml) | other | 2021-03-11 |  |  |
| [2021-03_dodo-hack.yaml](data-leak/2021-03_dodo-hack.yaml) | data-leak | 2021-03-09 |  |  |
| [2021-03_nft-artist-creates-rug-pull-collection.yaml](other/2021-03_nft-artist-creates-rug-pull-collection.yaml) | other | 2021-03-09 |  |  |
| [2021-03_indie-developer-steals-artwork.yaml](other/2021-03_indie-developer-steals-artwork.yaml) | other | 2021-03-09 |  |  |
| [2021-03_verkada-cameras-jenkins-credentials.yaml](credential-theft/2021-03_verkada-cameras-jenkins-credentials.yaml) | credential-theft | 2021-03-08 |  |  |
| [2021-03_paid-network-hack.yaml](data-leak/2021-03_paid-network-hack.yaml) | data-leak | 2021-03-05 |  |  |
| [2021-03_meerkat-defi-rug-pull.yaml](other/2021-03_meerkat-defi-rug-pull.yaml) | other | 2021-03-04 |  |  |
| [2021-03_royal-dutch-shell-accellion.yaml](supply-chain/2021-03_royal-dutch-shell-accellion.yaml) | supply-chain | 2021-03-01 | DEWMODE web shell |  |
| [2021-03_schools-jail-cells-hospital-icus-and-major-companies-like-tesla-nissan-equinox-cloudflare-verkada.yaml](supply-chain/2021-03_schools-jail-cells-hospital-icus-and-major-companies-like-tesla-nissan-equinox-cloudflare-verkada.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_israeli-likud-party-elector-software.yaml](supply-chain/2021-03_israeli-likud-party-elector-software.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_multicare-health-services-netgain.yaml](supply-chain/2021-03_multicare-health-services-netgain.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_european-banking-authority-microsoft.yaml](supply-chain/2021-03_european-banking-authority-microsoft.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_piedmont-health-services-peaktpa.yaml](supply-chain/2021-03_piedmont-health-services-peaktpa.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_poll-county-schools-pcs-revenue-systems.yaml](supply-chain/2021-03_poll-county-schools-pcs-revenue-systems.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_qualys-accellion.yaml](supply-chain/2021-03_qualys-accellion.yaml) | supply-chain | 2021-03-01 | DEWMODE web shell |  |
| [2021-03_calviva-health-health-net-community-solutio.yaml](supply-chain/2021-03_calviva-health-health-net-community-solutio.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_flagstar-bank-accellion.yaml](supply-chain/2021-03_flagstar-bank-accellion.yaml) | supply-chain | 2021-03-01 | DEWMODE web shell |  |
| [2021-03_trillium-community-health-plan-southern-illinois-university-school-of-medicine-accellion.yaml](supply-chain/2021-03_trillium-community-health-plan-southern-illinois-university-school-of-medicine-accellion.yaml) | supply-chain | 2021-03-01 | DEWMODE web shell |  |
| [2021-03_austin-isd-not-disclosed.yaml](supply-chain/2021-03_austin-isd-not-disclosed.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_armed-forces-communications-electronics-association-and-the-us-geospatial-intelligence-foundation-spargo.yaml](supply-chain/2021-03_armed-forces-communications-electronics-association-and-the-us-geospatial-intelligence-foundation-spargo.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-03_university-of-miami-health-accellion.yaml](supply-chain/2021-03_university-of-miami-health-accellion.yaml) | supply-chain | 2021-03-01 | DEWMODE web shell |  |
| [2021-03_wake-forest-baptist-health-lexington-medical-center-healthgrades.yaml](supply-chain/2021-03_wake-forest-baptist-health-lexington-medical-center-healthgrades.yaml) | supply-chain | 2021-03-01 |  |  |
| [2021-02_singapore-airlines-sita-580k.yaml](supply-chain/2021-02_singapore-airlines-sita-580k.yaml) | supply-chain | 2021-02-26 |  |  |
| [2021-02_air-india-sita-pss-breach.yaml](supply-chain/2021-02_air-india-sita-pss-breach.yaml) | supply-chain | 2021-02-26 |  |  |
| [2021-03_singapore-airlines-air-new-zealand-british-airways-american-airlines-lufthansa-malaysia-airlines-finnair-japan-airlines-united-airlines-sas-cathay-pacific-and-south-korean-airline-juju-air-star-alliance-sita.yaml](supply-chain/2021-03_singapore-airlines-air-new-zealand-british-airways-american-airlines-lufthansa-malaysia-airlines-finnair-japan-airlines-united-airlines-sas-cathay-pacific-and-south-korean-airline-juju-air-star-alliance-sita.yaml) | supply-chain | 2021-02-24 |  |  |
| [2021-05_guess-fashion-darkside.yaml](ransomware/2021-05_guess-fashion-darkside.yaml) | ransomware | 2021-02-19 | DarkSide |  |
| [2021-02_c-r-e-a-m-hack-1.yaml](data-leak/2021-02_c-r-e-a-m-hack-1.yaml) | data-leak | 2021-02-13 |  |  |
| [2021-02_c-r-e-a-m-hack-35-1.yaml](data-leak/2021-02_c-r-e-a-m-hack-35-1.yaml) | data-leak | 2021-02-13 |  |  |
| [2021-05_upmc-cole-hidalgo-medical-services-t-capturerx.yaml](supply-chain/2021-05_upmc-cole-hidalgo-medical-services-t-capturerx.yaml) | supply-chain | 2021-02-06 | Ransomware (strain not public… |  |
| [2021-02_oldsmar-florida-water-treatment-hack.yaml](other/2021-02_oldsmar-florida-water-treatment-hack.yaml) | other | 2021-02-05 |  |  |
| [2021-02_yearn-finance-hack-1.yaml](data-leak/2021-02_yearn-finance-hack-1.yaml) | data-leak | 2021-02-04 |  |  |
| [2021-02_tether-pays-penalty-to-new-york.yaml](other/2021-02_tether-pays-penalty-to-new-york.yaml) | other | 2021-02-03 |  |  |
| [2021-02_jamaican-government-amber-group.yaml](supply-chain/2021-02_jamaican-government-amber-group.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_fertility-clinics-incl-shady-grove-fertility-reproductive-science-center-san-francisco-ivf-florida-and-fertility-center-of-illinois-usf.yaml](supply-chain/2021-02_fertility-clinics-incl-shady-grove-fertility-reproductive-science-center-san-francisco-ivf-florida-and-fertility-center-of-illinois-usf.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_washington-state-auditor-singtel-university-of-colorado-bombardier-accellion.yaml](supply-chain/2021-02_washington-state-auditor-singtel-university-of-colorado-bombardier-accellion.yaml) | supply-chain | 2021-02-01 | DEWMODE web shell |  |
| [2021-02_ubiquiti-networks-not-disclosed.yaml](supply-chain/2021-02_ubiquiti-networks-not-disclosed.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_airbus-air-cara-bes-arcelormittal-bt-luxottica-kuehne-nagel-minist-re-de-la-justice-fran-ais-new-zealand-police-pwc-russia-salomon-sanofi-and-sephora-possibly-centreon.yaml](supply-chain/2021-02_airbus-air-cara-bes-arcelormittal-bt-luxottica-kuehne-nagel-minist-re-de-la-justice-fran-ais-new-zealand-police-pwc-russia-salomon-sanofi-and-sephora-possibly-centreon.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_beaumont-health-epic-software.yaml](supply-chain/2021-02_beaumont-health-epic-software.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_sitepoint-teespring-waydev.yaml](supply-chain/2021-02_sitepoint-teespring-waydev.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_ramsey-county-minnesota-family-health-division-netgain.yaml](supply-chain/2021-02_ramsey-county-minnesota-family-health-division-netgain.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_microsoft-365-exchange-infrastructure-mimecast.yaml](supply-chain/2021-02_microsoft-365-exchange-infrastructure-mimecast.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_city-of-kirkland-monroe-redmonde-seattle-lakewood-water-district-afts.yaml](supply-chain/2021-02_city-of-kirkland-monroe-redmonde-seattle-lakewood-water-district-afts.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_city-of-monroe-kirkland-redmond-automatic-funds-transfer-ser.yaml](supply-chain/2021-02_city-of-monroe-kirkland-redmond-automatic-funds-transfer-ser.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_goodwin-procter-qimr-berghofer-medical-research-institute-allens-jones-day-accellion.yaml](supply-chain/2021-02_goodwin-procter-qimr-berghofer-medical-research-institute-allens-jones-day-accellion.yaml) | supply-chain | 2021-02-01 | DEWMODE web shell |  |
| [2021-02_french-government-stormshield.yaml](supply-chain/2021-02_french-government-stormshield.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-02_defense-industry-wind-river-customers-wind-river-systems.yaml](supply-chain/2021-02_defense-industry-wind-river-customers-wind-river-systems.yaml) | supply-chain | 2021-02-01 |  |  |
| [2021-04_codecov-bash-uploader-supply-chain.yaml](supply-chain/2021-04_codecov-bash-uploader-supply-chain.yaml) | supply-chain | 2021-01-31 |  |  |
| [2021-01_codecov-bash-uploader.yaml](supply-chain/2021-01_codecov-bash-uploader.yaml) | supply-chain | 2021-01-31 |  |  |
| [2021-05_monday-com-rapid7-twilio-mercari-codecov.yaml](supply-chain/2021-05_monday-com-rapid7-twilio-mercari-codecov.yaml) | supply-chain | 2021-01-31 |  |  |
| [2021-01_popcornswap-rug-pulls.yaml](data-leak/2021-01_popcornswap-rug-pulls.yaml) | data-leak | 2021-01-28 |  |  |
| [2021-01_westrock-ransomware-ot.yaml](ransomware/2021-01_westrock-ransomware-ot.yaml) | ransomware | 2021-01-23 |  |  |
| [2021-01_sonicwall-customers-sonicwall.yaml](supply-chain/2021-01_sonicwall-customers-sonicwall.yaml) | supply-chain | 2021-01-22 |  | CVE-2021-20016 |
| [2021-01_saddle-finance-hack-1.yaml](data-leak/2021-01_saddle-finance-hack-1.yaml) | data-leak | 2021-01-19 |  |  |
| [2021-09_nrs-dotty-s.yaml](supply-chain/2021-09_nrs-dotty-s.yaml) | supply-chain | 2021-01-16 | unspecified malware |  |
| [2021-01_asic-accellion-fta-australia.yaml](supply-chain/2021-01_asic-accellion-fta-australia.yaml) | supply-chain | 2021-01-15 | Cl0p / DEWMODE web shell | CVE-2021-27101, CVE-2021-27102, CVE-202… |
| [2021-01_2020-eye-care-network-3-25m.yaml](data-leak/2021-01_2020-eye-care-network-3-25m.yaml) | data-leak | 2021-01-11 |  |  |
| [2021-01_parler-70tb-data-scraped-before-takedown.yaml](data-leak/2021-01_parler-70tb-data-scraped-before-takedown.yaml) | data-leak | 2021-01-09 |  |  |
| [2021-03_microsoft-exchange-proxylogon.yaml](other/2021-03_microsoft-exchange-proxylogon.yaml) | other | 2021-01-03 | China Chopper webshell / HAFN… | CVE-2021-26855, CVE-2021-26857, CVE-202… |
| [2021-01_bonobos-not-disclosed.yaml](supply-chain/2021-01_bonobos-not-disclosed.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_socialarks-214m-profiles.yaml](data-leak/2021-01_socialarks-214m-profiles.yaml) | data-leak | 2021-01-01 |  |  |
| [2021-01_north-korean-stock-investment-firms-not-disclosed.yaml](supply-chain/2021-01_north-korean-stock-investment-firms-not-disclosed.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_neopets-69m-live-access.yaml](data-leak/2021-01_neopets-69m-live-access.yaml) | data-leak | 2021-01-01 |  |  |
| [2021-01_omnitrax-broe-group.yaml](supply-chain/2021-01_omnitrax-broe-group.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_saskatchewan-hal-system-aspira.yaml](supply-chain/2021-01_saskatchewan-hal-system-aspira.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_facebook-instagram-linkedin-socialark.yaml](supply-chain/2021-01_facebook-instagram-linkedin-socialark.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_supply-chain-for-audi-bmw-mercedes-porsche-saab-volkswagen-and-volvo-across-north-america-namesouth.yaml](supply-chain/2021-01_supply-chain-for-audi-bmw-mercedes-porsche-saab-volkswagen-and-volvo-across-north-america-namesouth.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-01_united-parcel-service-ups-and-norfolk-southern-railroad-taylor-made-diagnostics-tmd.yaml](supply-chain/2021-01_united-parcel-service-ups-and-norfolk-southern-railroad-taylor-made-diagnostics-tmd.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-05_peloton-api-private-user-data-exposure.yaml](data-leak/2021-05_peloton-api-private-user-data-exposure.yaml) | data-leak | 2021-01-01 |  |  |
| [2021-01_defence-forces-para-military-forces-and-intelligence-agencies-of-india-elcom-innovations.yaml](supply-chain/2021-01_defence-forces-para-military-forces-and-intelligence-agencies-of-india-elcom-innovations.yaml) | supply-chain | 2021-01-01 |  |  |
| [2021-04_pulse-secure-apt5-defense-contractors.yaml](other/2021-04_pulse-secure-apt5-defense-contractors.yaml) | other | 2021-01-01 |  | CVE-2021-22893, CVE-2019-11510, CVE-202… |
| [2021-01_accellion-fta-clop.yaml](supply-chain/2021-01_accellion-fta-clop.yaml) | supply-chain | 2020-12-25 | DEWMODE webshell / FINTEAM | CVE-2021-27101, CVE-2021-27102, CVE-202… |
| [2021-01_new-zeland-reserve-bank-australian-securities-and-investments-commission-asic-acellion-software.yaml](supply-chain/2021-01_new-zeland-reserve-bank-australian-securities-and-investments-commission-asic-acellion-software.yaml) | supply-chain | 2020-12-23 | DEWMODE web shell | CVE-2021-27101, CVE-2021-27102, CVE-202… |
| [2021-01_ubiquiti-insider-threat.yaml](data-leak/2021-01_ubiquiti-insider-threat.yaml) | data-leak | 2020-12-10 |  |  |
| [2020-12_private-and-government-organizations-vietnam-certification-au.yaml](supply-chain/2020-12_private-and-government-organizations-vietnam-certification-au.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_microsoft-not-disclosed.yaml](supply-chain/2020-12_microsoft-not-disclosed.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_now-pensions-not-disclosed.yaml](supply-chain/2020-12_now-pensions-not-disclosed.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_mongolian-government-agencies-able-software.yaml](supply-chain/2020-12_mongolian-government-agencies-able-software.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-12_department-of-treasury-and-commerce--solarwinds.yaml](supply-chain/2020-12_department-of-treasury-and-commerce--solarwinds.yaml) | supply-chain | 2020-12-01 | SUNBURST, TEARDROP, RAINDROP |  |
| [2020-12_fireeye-customers-fireeye.yaml](supply-chain/2020-12_fireeye-customers-fireeye.yaml) | supply-chain | 2020-12-01 |  |  |
| [2020-11_customers-of-belden-belden.yaml](supply-chain/2020-11_customers-of-belden-belden.yaml) | supply-chain | 2020-11-12 |  |  |
| [2020-11_great-heart-academies-blackbaud.yaml](supply-chain/2020-11_great-heart-academies-blackbaud.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-11_wildworks-not-disclosed.yaml](supply-chain/2020-11_wildworks-not-disclosed.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-11_insurance-carriers-in-texas-colarodo-vertafore.yaml](supply-chain/2020-11_insurance-carriers-in-texas-colarodo-vertafore.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-11_first-federal-community-bank-rio-ban-abs.yaml](supply-chain/2020-11_first-federal-community-bank-rio-ban-abs.yaml) | supply-chain | 2020-11-01 |  |  |
| [2020-10_lazada-redmart-app-not-disclosed.yaml](supply-chain/2020-10_lazada-redmart-app-not-disclosed.yaml) | supply-chain | 2020-10-29 |  |  |
| [2020-10_uvm-health-network-doppelpaymer.yaml](ransomware/2020-10_uvm-health-network-doppelpaymer.yaml) | ransomware | 2020-10-28 | DoppelPaymer ransomware |  |
| [2020-10_university-vermont-health-doppelpaymer.yaml](ransomware/2020-10_university-vermont-health-doppelpaymer.yaml) | ransomware | 2020-10-28 | DoppelPaymer |  |
| [2020-10_harvest-finance-exploit.yaml](other/2020-10_harvest-finance-exploit.yaml) | other | 2020-10-26 |  |  |
| [2020-10_nitro-pdf-77m-users.yaml](data-leak/2020-10_nitro-pdf-77m-users.yaml) | data-leak | 2020-10-21 |  |  |
| [2020-10_gravatar-profile-scraping-167m.yaml](data-leak/2020-10_gravatar-profile-scraping-167m.yaml) | data-leak | 2020-10-03 |  |  |
| [2020-12_fireeye-solarwinds-red-team-tools.yaml](supply-chain/2020-12_fireeye-solarwinds-red-team-tools.yaml) | supply-chain | 2020-10-01 | SUNBURST; TEARDROP |  |
| [2020-10_rady-children-hospital-sonoma-valley-blackbaud.yaml](supply-chain/2020-10_rady-children-hospital-sonoma-valley-blackbaud.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_kylie-cosmetics-shopify.yaml](supply-chain/2020-10_kylie-cosmetics-shopify.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_jm-bullion-not-disclosed.yaml](supply-chain/2020-10_jm-bullion-not-disclosed.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_government-departments-and-the-austr-isentia.yaml](supply-chain/2020-10_government-departments-and-the-austr-isentia.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_city-of-odessa-click2gov.yaml](supply-chain/2020-10_city-of-odessa-click2gov.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_apple-google-amazon-citibank-nitro.yaml](supply-chain/2020-10_apple-google-amazon-citibank-nitro.yaml) | supply-chain | 2020-10-01 |  |  |
| [2020-10_broadvoice-customers-broadvoice.yaml](supply-chain/2020-10_broadvoice-customers-broadvoice.yaml) | supply-chain | 2020-09-28 |  |  |
| [2020-09_universal-health-services-ryuk.yaml](ransomware/2020-09_universal-health-services-ryuk.yaml) | ransomware | 2020-09-27 | Ryuk ransomware; TrickBot; Em… |  |
| [2020-09_kucoin-hack-281m-lazarus.yaml](other/2020-09_kucoin-hack-281m-lazarus.yaml) | other | 2020-09-25 |  |  |
| [2020-10_google-fragomen-del-rey-bernsen.yaml](supply-chain/2020-10_google-fragomen-del-rey-bernsen.yaml) | supply-chain | 2020-09-24 |  |  |
| [2021-09_cisco-webex-iam-compromise.yaml](credential-theft/2021-09_cisco-webex-iam-compromise.yaml) | credential-theft | 2020-09-24 |  |  |
| [2020-12_dental-practices-dental-care-alliance-dca.yaml](supply-chain/2020-12_dental-practices-dental-care-alliance-dca.yaml) | supply-chain | 2020-09-18 |  |  |
| [2020-09_dusseldorf-hospital-patient-death.yaml](ransomware/2020-09_dusseldorf-hospital-patient-death.yaml) | ransomware | 2020-09-09 | DoppelPaymer ransomware | CVE-2019-19781 |
| [2020-09_pell-city-valley-bank-not-disclosed.yaml](supply-chain/2020-09_pell-city-valley-bank-not-disclosed.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-09_buffalo-n-y-area-hospitals-innova-he-blackbaud.yaml](supply-chain/2020-09_buffalo-n-y-area-hospitals-innova-he-blackbaud.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-09_e-commerce-stores-adobe-magento-1.yaml](supply-chain/2020-09_e-commerce-stores-adobe-magento-1.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-09_phipps-conservatory-blackbaud.yaml](supply-chain/2020-09_phipps-conservatory-blackbaud.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-09_tribune-media-times-media-grup-view-media.yaml](supply-chain/2020-09_tribune-media-times-media-grup-view-media.yaml) | supply-chain | 2020-09-01 |  |  |
| [2020-11_spotify-credential-stuffing-350k.yaml](credential-theft/2020-11_spotify-credential-stuffing-350k.yaml) | credential-theft | 2020-09-01 |  |  |
| [2020-11_lenscrafters-target-optical-eyemed-a-luxottica.yaml](supply-chain/2020-11_lenscrafters-target-optical-eyemed-a-luxottica.yaml) | supply-chain | 2020-08-05 | Nefilim ransomware |  |
| [2020-08_razer-elasticsearch-100k.yaml](data-leak/2020-08_razer-elasticsearch-100k.yaml) | data-leak | 2020-08-01 |  |  |
| [2020-08_rochester-ymca-not-disclosed.yaml](supply-chain/2020-08_rochester-ymca-not-disclosed.yaml) | supply-chain | 2020-08-01 |  |  |
| [2020-08_jack-daniel-s-brown-forman.yaml](supply-chain/2020-08_jack-daniel-s-brown-forman.yaml) | supply-chain | 2020-08-01 |  |  |
| [2020-08_department-of-health-not-disclosed.yaml](supply-chain/2020-08_department-of-health-not-disclosed.yaml) | supply-chain | 2020-08-01 |  |  |
| [2020-07_garmin-wastedlocker-evil-corp.yaml](ransomware/2020-07_garmin-wastedlocker-evil-corp.yaml) | ransomware | 2020-07-23 | WastedLocker ransomware; Fake… |  |
| [2023-09_microsoft-ai-sas-token-38tb.yaml](data-leak/2023-09_microsoft-ai-sas-token-38tb.yaml) | data-leak | 2020-07-20 |  |  |
| [2020-07_gedmatch-dna-privacy-attack.yaml](other/2020-07_gedmatch-dna-privacy-attack.yaml) | other | 2020-07-19 |  |  |
| [2020-07_twitter-bitcoin-scam-vishing.yaml](credential-theft/2020-07_twitter-bitcoin-scam-vishing.yaml) | credential-theft | 2020-07-15 |  |  |
| [2020-07_freepik-flaticon-8-3m.yaml](data-leak/2020-07_freepik-flaticon-8-3m.yaml) | data-leak | 2020-07-01 |  |  |
| [2020-07_microsoft-ai-38tb-sas-token.yaml](data-leak/2020-07_microsoft-ai-38tb-sas-token.yaml) | data-leak | 2020-07-01 |  |  |
| [2020-07_promo-com-not-disclosed.yaml](supply-chain/2020-07_promo-com-not-disclosed.yaml) | supply-chain | 2020-07-01 |  |  |
| [2020-07_citrix-not-disclosed.yaml](supply-chain/2020-07_citrix-not-disclosed.yaml) | supply-chain | 2020-07-01 |  |  |
| [2020-07_angelo-gordon-co-graham-capital-mana-m-j-brunner.yaml](supply-chain/2020-07_angelo-gordon-co-graham-capital-mana-m-j-brunner.yaml) | supply-chain | 2020-07-01 |  |  |
| [2020-06_mednax-office365-phishing-1-3m.yaml](credential-theft/2020-06_mednax-office365-phishing-1-3m.yaml) | credential-theft | 2020-06-17 |  |  |
| [2020-06_drizly-github-rds-breach.yaml](credential-theft/2020-06_drizly-github-rds-breach.yaml) | credential-theft | 2020-06-12 |  |  |
| [2020-07_digital-bank-app-dave-waydev.yaml](supply-chain/2020-07_digital-bank-app-dave-waydev.yaml) | supply-chain | 2020-06-10 |  |  |
| [2020-06_san-francisco-employees-retirement-s-10up-inc.yaml](supply-chain/2020-06_san-francisco-employees-retirement-s-10up-inc.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-06_police-departments-netsentiel.yaml](supply-chain/2020-06_police-departments-netsentiel.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-06_mu-health-not-disclosed.yaml](supply-chain/2020-06_mu-health-not-disclosed.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-06_joomla-open-source-matters.yaml](supply-chain/2020-06_joomla-open-source-matters.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-06_wattpad-breach.yaml](data-leak/2020-06_wattpad-breach.yaml) | data-leak | 2020-06-01 |  |  |
| [2020-07_wattpad-shinyhunters-268m.yaml](credential-theft/2020-07_wattpad-shinyhunters-268m.yaml) | credential-theft | 2020-06-01 |  |  |
| [2020-06_keepnet-not-disclosed.yaml](supply-chain/2020-06_keepnet-not-disclosed.yaml) | supply-chain | 2020-06-01 |  |  |
| [2020-05_experian-south-africa.yaml](data-leak/2020-05_experian-south-africa.yaml) | data-leak | 2020-05-01 |  |  |
| [2020-05_florida-department-of-economic-oppor-not-disclosed.yaml](supply-chain/2020-05_florida-department-of-economic-oppor-not-disclosed.yaml) | supply-chain | 2020-05-01 |  |  |
| [2020-05_truecaller-not-disclosed.yaml](supply-chain/2020-05_truecaller-not-disclosed.yaml) | supply-chain | 2020-05-01 |  |  |
| [2020-05_bank-of-america-not-disclosed.yaml](supply-chain/2020-05_bank-of-america-not-disclosed.yaml) | supply-chain | 2020-05-01 |  |  |
| [2020-05_mns-healthcare-clients-management-and-network-s.yaml](supply-chain/2020-05_mns-healthcare-clients-management-and-network-s.yaml) | supply-chain | 2020-05-01 |  |  |
| [2020-04_cognizant-maze-ransomware.yaml](ransomware/2020-04_cognizant-maze-ransomware.yaml) | ransomware | 2020-04-18 | Maze |  |
| [2020-04_magellan-health.yaml](ransomware/2020-04_magellan-health.yaml) | ransomware | 2020-04-11 |  |  |
| [2020-04_magellan-health-ransomware.yaml](ransomware/2020-04_magellan-health-ransomware.yaml) | ransomware | 2020-04-11 |  |  |
| [2020-04_service-nsw-phishing-186k.yaml](credential-theft/2020-04_service-nsw-phishing-186k.yaml) | credential-theft | 2020-04-04 |  |  |
| [2020-04_mariott-not-disclosed.yaml](supply-chain/2020-04_mariott-not-disclosed.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-04_usenext-usenet-nl-not-disclosed.yaml](supply-chain/2020-04_usenext-usenet-nl-not-disclosed.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-04_nintendo-credential-stuffing-160k.yaml](credential-theft/2020-04_nintendo-credential-stuffing-160k.yaml) | credential-theft | 2020-04-01 |  |  |
| [2020-04_rigup-s-energy-sector-clients-rigup.yaml](supply-chain/2020-04_rigup-s-energy-sector-clients-rigup.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-04_cognizant-s-clients-cognizant.yaml](supply-chain/2020-04_cognizant-s-clients-cognizant.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-04_michigan-state-university-volusion.yaml](supply-chain/2020-04_michigan-state-university-volusion.yaml) | supply-chain | 2020-04-01 |  |  |
| [2020-04_zoom-credential-stuffing-530k.yaml](credential-theft/2020-04_zoom-credential-stuffing-530k.yaml) | credential-theft | 2020-04-01 |  |  |
| [2020-12_solarwinds-sunburst.yaml](supply-chain/2020-12_solarwinds-sunburst.yaml) | supply-chain | 2020-03-26 | SUNBURST / TEARDROP / SUNSPOT | CVE-2020-10148 |
| [2020-03_cam4-elasticsearch-10bn-records.yaml](data-leak/2020-03_cam4-elasticsearch-10bn-records.yaml) | data-leak | 2020-03-16 |  |  |
| [2020-03_execupharm-clop-ransomware.yaml](ransomware/2020-03_execupharm-clop-ransomware.yaml) | ransomware | 2020-03-13 | CLOP |  |
| [2020-03_first-republic-bank-aws-insider.yaml](data-leak/2020-03_first-republic-bank-aws-insider.yaml) | data-leak | 2020-03-11 |  |  |
| [2020-03_general-electric-canon-business-services.yaml](supply-chain/2020-03_general-electric-canon-business-services.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_radio-com-not-disclosed.yaml](supply-chain/2020-03_radio-com-not-disclosed.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_norwegian-cruise-line-phishing.yaml](data-leak/2020-03_norwegian-cruise-line-phishing.yaml) | data-leak | 2020-03-01 |  |  |
| [2020-03_amazon-ebay-shopify-stripe-paypal-not-disclosed.yaml](supply-chain/2020-03_amazon-ebay-shopify-stripe-paypal-not-disclosed.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-04_zoom-credential-stuffing-530k-accounts.yaml](credential-theft/2020-04_zoom-credential-stuffing-530k-accounts.yaml) | credential-theft | 2020-03-01 |  |  |
| [2020-04_nintendo-160k-account-takeover.yaml](credential-theft/2020-04_nintendo-160k-account-takeover.yaml) | credential-theft | 2020-03-01 |  |  |
| [2020-03_chubb-not-disclosed.yaml](supply-chain/2020-03_chubb-not-disclosed.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_t-mobile-not-disclosed.yaml](supply-chain/2020-03_t-mobile-not-disclosed.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_spacex-tesla-boeing-lockheed-martin-visser.yaml](supply-chain/2020-03_spacex-tesla-boeing-lockheed-martin-visser.yaml) | supply-chain | 2020-03-01 |  |  |
| [2020-03_t-mobile-200k-breach.yaml](credential-theft/2020-03_t-mobile-200k-breach.yaml) | credential-theft | 2020-02-19 |  |  |
| [2020-02_blackbaud-crm-ransomware.yaml](ransomware/2020-02_blackbaud-crm-ransomware.yaml) | ransomware | 2020-02-07 |  |  |
| [2020-07_university-of-manitoba-university-of-blackbaud.yaml](supply-chain/2020-07_university-of-manitoba-university-of-blackbaud.yaml) | supply-chain | 2020-02-07 | ransomware |  |
| [2020-07_blackbaud-crm-ransomware.yaml](supply-chain/2020-07_blackbaud-crm-ransomware.yaml) | supply-chain | 2020-02-07 |  |  |
| [2020-02_clearview-ai-client-list.yaml](data-leak/2020-02_clearview-ai-client-list.yaml) | data-leak | 2020-02-01 |  |  |
| [2020-02_tql-carriers-tql.yaml](supply-chain/2020-02_tql-carriers-tql.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_rutters-store-not-disclosed.yaml](supply-chain/2020-02_rutters-store-not-disclosed.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_nedbank-computer-facilities-pty.yaml](supply-chain/2020-02_nedbank-computer-facilities-pty.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_idaho-central-credit-union-not-disclosed.yaml](supply-chain/2020-02_idaho-central-credit-union-not-disclosed.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_community-care-physicians-bst.yaml](supply-chain/2020-02_community-care-physicians-bst.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_carson-city-click2gov.yaml](supply-chain/2020-02_carson-city-click2gov.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-02_brunswick-county-schools-interactive-medical-syst.yaml](supply-chain/2020-02_brunswick-county-schools-interactive-medical-syst.yaml) | supply-chain | 2020-02-01 |  |  |
| [2020-01_amazon-customers-amazon.yaml](supply-chain/2020-01_amazon-customers-amazon.yaml) | supply-chain | 2020-01-10 |  |  |
| [2020-09_national-general-allstate-insurance.yaml](data-leak/2020-09_national-general-allstate-insurance.yaml) | data-leak | 2020-01-01 |  |  |
| [2020-01_state-governments-of-u-s-not-disclosed.yaml](supply-chain/2020-01_state-governments-of-u-s-not-disclosed.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_easyjet-breach.yaml](data-leak/2020-01_easyjet-breach.yaml) | data-leak | 2020-01-01 |  |  |
| [2020-01_regus-applause.yaml](supply-chain/2020-01_regus-applause.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_estee-lauder-440m-elasticsearch.yaml](data-leak/2020-01_estee-lauder-440m-elasticsearch.yaml) | data-leak | 2020-01-01 |  |  |
| [2020-05_easyjet-9m-customers.yaml](data-leak/2020-05_easyjet-9m-customers.yaml) | data-leak | 2020-01-01 |  |  |
| [2020-01_medical-facilities-isofh.yaml](supply-chain/2020-01_medical-facilities-isofh.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_marijuana-dispensaries-amedicanna-di-thsuite.yaml](supply-chain/2020-01_marijuana-dispensaries-amedicanna-di-thsuite.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_instagram-social-captain.yaml](supply-chain/2020-01_instagram-social-captain.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_the-australian-p-n-bank-not-disclosed.yaml](supply-chain/2020-01_the-australian-p-n-bank-not-disclosed.yaml) | supply-chain | 2020-01-01 |  |  |
| [2020-01_marriott-employee-credentials-5-2m.yaml](credential-theft/2020-01_marriott-employee-credentials-5-2m.yaml) | credential-theft | 2020-01-01 |  |  |
| [2020-01_travelex-revil-pulse-secure.yaml](ransomware/2020-01_travelex-revil-pulse-secure.yaml) | ransomware | 2019-12-31 | REvil (Sodinokibi) ransomware | CVE-2019-11510 |
| [2019-12_city-of-marietta-click2gov.yaml](supply-chain/2019-12_city-of-marietta-click2gov.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_wyze-customer-wyze.yaml](supply-chain/2019-12_wyze-customer-wyze.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_city-of-sioux-click2gov.yaml](supply-chain/2019-12_city-of-sioux-click2gov.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_singapore-armed-forces-saf-hmi-institute-of-health.yaml](supply-chain/2019-12_singapore-armed-forces-saf-hmi-institute-of-health.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_nypd-fingerprint-database-not-disclosed.yaml](supply-chain/2019-12_nypd-fingerprint-database-not-disclosed.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-12_xerox-centurylink-nasdaq-general-ele-ipr-software.yaml](supply-chain/2019-12_xerox-centurylink-nasdaq-general-ele-ipr-software.yaml) | supply-chain | 2019-12-01 |  |  |
| [2019-11_t-mobile-prepaid-breach.yaml](data-leak/2019-11_t-mobile-prepaid-breach.yaml) | data-leak | 2019-11-22 |  |  |
| [2019-11_tenncare-magellan-health-system.yaml](supply-chain/2019-11_tenncare-magellan-health-system.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_macy-s-not-disclosed.yaml](supply-chain/2019-11_macy-s-not-disclosed.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_florida-blue-magellan-health-inc.yaml](supply-chain/2019-11_florida-blue-magellan-health-inc.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_facebook-and-twitter-one-audience.yaml](supply-chain/2019-11_facebook-and-twitter-one-audience.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_city-of-san-angelo-click2gov.yaml](supply-chain/2019-11_city-of-san-angelo-click2gov.yaml) | supply-chain | 2019-11-01 |  |  |
| [2020-02_health-share-of-oregon-gridworks.yaml](supply-chain/2020-02_health-share-of-oregon-gridworks.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_palo-alto-networks-not-disclosed.yaml](supply-chain/2019-11_palo-alto-networks-not-disclosed.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_pompano-beach-city-click2gov.yaml](supply-chain/2019-11_pompano-beach-city-click2gov.yaml) | supply-chain | 2019-11-01 |  |  |
| [2019-11_tmobile-prepaid-customers.yaml](credential-theft/2019-11_tmobile-prepaid-customers.yaml) | credential-theft | 2019-11-01 |  |  |
| [2019-11_the-city-of-charlottesville-not-disclosed.yaml](supply-chain/2019-11_the-city-of-charlottesville-not-disclosed.yaml) | supply-chain | 2019-11-01 |  |  |
| [2023-03_cerebral-health-tracking-pixels-3m.yaml](data-leak/2023-03_cerebral-health-tracking-pixels-3m.yaml) | data-leak | 2019-10-12 |  |  |
| [2023-03_cerebral-31m-health-data-meta-google-sharing.yaml](data-leak/2023-03_cerebral-31m-health-data-meta-google-sharing.yaml) | data-leak | 2019-10-01 |  |  |
| [2020-01_schools-active-network.yaml](supply-chain/2020-01_schools-active-network.yaml) | supply-chain | 2019-10-01 | JavaScript web skimmer |  |
| [2019-10_geisinger-health-plan-magellan-national-imagin.yaml](supply-chain/2019-10_geisinger-health-plan-magellan-national-imagin.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-10_gw-community-members-chegg.yaml](supply-chain/2019-10_gw-community-members-chegg.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-10_the-clark-county-school-district-pearson-clinical-assessm.yaml](supply-chain/2019-10_the-clark-county-school-district-pearson-clinical-assessm.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-10_unicredit-not-disclosed.yaml](supply-chain/2019-10_unicredit-not-disclosed.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-10_centurylink-not-disclosed.yaml](supply-chain/2019-10_centurylink-not-disclosed.yaml) | supply-chain | 2019-10-01 |  |  |
| [2019-09_malinda-air-not-disclosed.yaml](supply-chain/2019-09_malinda-air-not-disclosed.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_github-and-bitbucket-circlci.yaml](supply-chain/2019-09_github-and-bitbucket-circlci.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_doordash-not-disclosed.yaml](supply-chain/2019-09_doordash-not-disclosed.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_city-of-broken-arrow-deerfield-beach-click2gov.yaml](supply-chain/2019-09_city-of-broken-arrow-deerfield-beach-click2gov.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_ames-parking-ticket-payments-click2gov.yaml](supply-chain/2019-09_ames-parking-ticket-payments-click2gov.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-09_yves-rocher-aliznet.yaml](supply-chain/2019-09_yves-rocher-aliznet.yaml) | supply-chain | 2019-09-01 |  |  |
| [2019-08_mastercard-not-disclosed.yaml](supply-chain/2019-08_mastercard-not-disclosed.yaml) | supply-chain | 2019-08-19 |  |  |
| [2020-01_mercy-health-lorain-rcm-enterprise-services.yaml](supply-chain/2020-01_mercy-health-lorain-rcm-enterprise-services.yaml) | supply-chain | 2019-08-14 |  |  |
| [2019-08_wood-ranch-medical-closure-ransomware.yaml](ransomware/2019-08_wood-ranch-medical-closure-ransomware.yaml) | ransomware | 2019-08-10 |  |  |
| [2019-08_dekalb-school-district-428-wilmette--pearson-clinical-assessm.yaml](supply-chain/2019-08_dekalb-school-district-428-wilmette--pearson-clinical-assessm.yaml) | supply-chain | 2019-08-01 |  |  |
| [2021-06_volkswagen-group-of-america-shift-digital.yaml](supply-chain/2021-06_volkswagen-group-of-america-shift-digital.yaml) | supply-chain | 2019-08-01 |  |  |
| [2019-08_naperville-unit-district-203-indian--pearson-clinical-assessm.yaml](supply-chain/2019-08_naperville-unit-district-203-indian--pearson-clinical-assessm.yaml) | supply-chain | 2019-08-01 |  |  |
| [2019-08_biostar2-biometric-27m.yaml](data-leak/2019-08_biostar2-biometric-27m.yaml) | data-leak | 2019-08-01 |  |  |
| [2019-08_choice-hotels-mongodb-vendor.yaml](data-leak/2019-08_choice-hotels-mongodb-vendor.yaml) | data-leak | 2019-07-02 |  |  |
| [2020-10_dickey-s-barbecue-pit-not-disclosed.yaml](supply-chain/2020-10_dickey-s-barbecue-pit-not-disclosed.yaml) | supply-chain | 2019-07-01 | POS memory-scraping malware (… |  |
| [2019-07_mgm-resorts-cloud-10-6m.yaml](data-leak/2019-07_mgm-resorts-cloud-10-6m.yaml) | data-leak | 2019-07-01 |  |  |
| [2019-07_seven-eleven-japan-app-500k-stolen.yaml](data-leak/2019-07_seven-eleven-japan-app-500k-stolen.yaml) | data-leak | 2019-07-01 |  |  |
| [2020-01_mitsubishi-not-disclosed.yaml](supply-chain/2020-01_mitsubishi-not-disclosed.yaml) | supply-chain | 2019-06-28 |  | CVE-2019-18187 |
| [2019-06_bulgarian-nra-5m-taxpayers.yaml](data-leak/2019-06_bulgarian-nra-5m-taxpayers.yaml) | data-leak | 2019-06-01 |  |  |
| [2019-06_komodo-not-disclosed.yaml](supply-chain/2019-06_komodo-not-disclosed.yaml) | supply-chain | 2019-06-01 |  |  |
| [2019-07_sprint-samsung-add-a-line.yaml](data-leak/2019-07_sprint-samsung-add-a-line.yaml) | data-leak | 2019-06-01 |  |  |
| [2019-05_canva-gnosticplayers-137m.yaml](credential-theft/2019-05_canva-gnosticplayers-137m.yaml) | credential-theft | 2019-05-24 |  |  |
| [2019-05_canva-gnosticplayers.yaml](data-leak/2019-05_canva-gnosticplayers.yaml) | data-leak | 2019-05-24 |  |  |
| [2019-05_instagram-chtrbox.yaml](supply-chain/2019-05_instagram-chtrbox.yaml) | supply-chain | 2019-05-14 |  |  |
| [2019-05_binance-hack-7000-btc.yaml](other/2019-05_binance-hack-7000-btc.yaml) | other | 2019-05-07 |  |  |
| [2019-05_uniqlo-not.yaml](supply-chain/2019-05_uniqlo-not.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_forbes-not-disclosed.yaml](supply-chain/2019-05_forbes-not-disclosed.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-08_cable-one-not-disclosed.yaml](supply-chain/2019-08_cable-one-not-disclosed.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_stockx-sneaker-6-8m.yaml](data-leak/2019-05_stockx-sneaker-6-8m.yaml) | data-leak | 2019-05-01 |  |  |
| [2019-05_4-600-websites-picreel-and-alpaca-forms.yaml](supply-chain/2019-05_4-600-websites-picreel-and-alpaca-forms.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_webstorage-users-asus-webstorage.yaml](supply-chain/2019-05_webstorage-users-asus-webstorage.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_vag-ericsson-leica-man-toshiba-unicr-citycomp.yaml](supply-chain/2019-05_vag-ericsson-leica-man-toshiba-unicr-citycomp.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_bank-axis-icici-indusind-rbl-not-disclosed.yaml](supply-chain/2019-05_bank-axis-icici-indusind-rbl-not-disclosed.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-05_u-s-customs-and-border-protection-not-disclosed.yaml](supply-chain/2019-05_u-s-customs-and-border-protection-not-disclosed.yaml) | supply-chain | 2019-05-01 | ransomware (unnamed, targeted… |  |
| [2019-05_truecaller-not-disclosed.yaml](supply-chain/2019-05_truecaller-not-disclosed.yaml) | supply-chain | 2019-05-01 |  |  |
| [2019-04_docker-hub-oauth-tokens.yaml](data-leak/2019-04_docker-hub-oauth-tokens.yaml) | data-leak | 2019-04-25 |  |  |
| [2019-04_176-colleges-and-universities-prismrbs.yaml](supply-chain/2019-04_176-colleges-and-universities-prismrbs.yaml) | supply-chain | 2019-04-14 | Mirrorthief JavaScript card s… |  |
| [2019-06_westpac-bank-payid.yaml](supply-chain/2019-06_westpac-bank-payid.yaml) | supply-chain | 2019-04-07 |  |  |
| [2019-04_freedom-mobile-apptium-technologies.yaml](supply-chain/2019-04_freedom-mobile-apptium-technologies.yaml) | supply-chain | 2019-03-25 |  |  |
| [2019-07_capital-one-ssrf-imdsv1-106m.yaml](data-leak/2019-07_capital-one-ssrf-imdsv1-106m.yaml) | credential-theft | 2019-03-22 |  |  |
| [2019-03_norsk-hydro-lockergoga.yaml](ransomware/2019-03_norsk-hydro-lockergoga.yaml) | ransomware | 2019-03-19 | LockerGoga |  |
| [2019-05_boost-mobile-credential-stuffing.yaml](credential-theft/2019-05_boost-mobile-credential-stuffing.yaml) | credential-theft | 2019-03-14 |  |  |
| [2019-03_the-bank-of-queensland-landmark-white-limited.yaml](supply-chain/2019-03_the-bank-of-queensland-landmark-white-limited.yaml) | supply-chain | 2019-03-01 |  |  |
| [2019-03_rush-system-for-health-miramed.yaml](supply-chain/2019-03_rush-system-for-health-miramed.yaml) | supply-chain | 2019-03-01 |  |  |
| [2019-02_china-railway-not-disclosed.yaml](supply-chain/2019-02_china-railway-not-disclosed.yaml) | supply-chain | 2019-02-01 |  |  |
| [2019-02_medibank-third-party-pre-breach.yaml](supply-chain/2019-02_medibank-third-party-pre-breach.yaml) | data-leak | 2019-02-01 |  |  |
| [2020-05_bhim-wallet-app-csc-e-governance-service.yaml](supply-chain/2020-05_bhim-wallet-app-csc-e-governance-service.yaml) | supply-chain | 2019-02-01 |  |  |
| [2019-02_verifications-io-763m-emails.yaml](data-leak/2019-02_verifications-io-763m-emails.yaml) | data-leak | 2019-02-01 |  |  |
| [2019-01_141-airlines-that-partner-with-amade-amadeus.yaml](supply-chain/2019-01_141-airlines-that-partner-with-amade-amadeus.yaml) | supply-chain | 2019-01-15 |  |  |
| [2019-01_ascension-opticsml.yaml](supply-chain/2019-01_ascension-opticsml.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_tim-hortons-covert-location-tracking.yaml](data-leak/2019-01_tim-hortons-covert-location-tracking.yaml) | data-leak | 2019-01-01 |  |  |
| [2021-04_facebook-533m-phone-scrape.yaml](data-leak/2021-04_facebook-533m-phone-scrape.yaml) | data-leak | 2019-01-01 |  |  |
| [2024-03_att-dark-web-73million.yaml](data-leak/2024-03_att-dark-web-73million.yaml) | data-leak | 2019-01-01 |  |  |
| [2019-03_asus-shadowhammer-lazarus.yaml](supply-chain/2019-03_asus-shadowhammer-lazarus.yaml) | supply-chain | 2019-01-01 | ShadowHammer backdoor |  |
| [2019-01_city-of-saint-john-nb-click2gov.yaml](supply-chain/2019-01_city-of-saint-john-nb-click2gov.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_e-commerce-sites-that-partner-with-a-adverline.yaml](supply-chain/2019-01_e-commerce-sites-that-partner-with-a-adverline.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_hanover-county-click2gov.yaml](supply-chain/2019-01_hanover-county-click2gov.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_humana-lcp-corp.yaml](supply-chain/2019-01_humana-lcp-corp.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_localbitcoins-not-disclosed.yaml](supply-chain/2019-01_localbitcoins-not-disclosed.yaml) | supply-chain | 2019-01-01 |  |  |
| [2019-01_all-sites-that-use-php-pear-and-down-php-pear.yaml](supply-chain/2019-01_all-sites-that-use-php-pear-and-down-php-pear.yaml) | supply-chain | 2018-12-20 | Perl reverse shell backdoor |  |
| [2019-04_georgia-tech-1-3m-web-app.yaml](data-leak/2019-04_georgia-tech-1-3m-web-app.yaml) | data-leak | 2018-12-14 |  |  |
| [2018-12_quora-100m-users.yaml](data-leak/2018-12_quora-100m-users.yaml) | data-leak | 2018-12-03 |  |  |
| [2018-12_taobao-tmall-alipay-baidu-cloud-163--easy-programming-languag.yaml](supply-chain/2018-12_taobao-tmall-alipay-baidu-cloud-163--easy-programming-languag.yaml) | supply-chain | 2018-12-01 | Credential-stealing trojan ta… |  |
| [2018-12_baylor-scott-white-medical-center-fr-not-disclosed.yaml](supply-chain/2018-12_baylor-scott-white-medical-center-fr-not-disclosed.yaml) | supply-chain | 2018-12-01 |  |  |
| [2018-12_city-of-saint-john-click2gov.yaml](supply-chain/2018-12_city-of-saint-john-click2gov.yaml) | supply-chain | 2018-12-01 |  |  |
| [2018-12_redwood-eye-center-it-lighthouse.yaml](supply-chain/2018-12_redwood-eye-center-it-lighthouse.yaml) | supply-chain | 2018-12-01 |  |  |
| [2018-11_gate-io-cryptocurrency-exchange-statcounter.yaml](supply-chain/2018-11_gate-io-cryptocurrency-exchange-statcounter.yaml) | supply-chain | 2018-11-03 | Custom JavaScript Bitcoin add… |  |
| [2018-11_city-of-york-council-appware.yaml](supply-chain/2018-11_city-of-york-council-appware.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_huntsville-hospital-in-alabama-jobscience-inc.yaml](supply-chain/2018-11_huntsville-hospital-in-alabama-jobscience-inc.yaml) | supply-chain | 2018-11-01 |  |  |
| [2019-02_equifax-experian-and-transunion-image-i-nation-technolog.yaml](supply-chain/2019-02_equifax-experian-and-transunion-image-i-nation-technolog.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_the-australian-defence-department-not-disclosed.yaml](supply-chain/2018-11_the-australian-defence-department-not-disclosed.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_ontario-cannabis-store-canada-post.yaml](supply-chain/2018-11_ontario-cannabis-store-canada-post.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_bitpay-right9ctrl.yaml](supply-chain/2018-11_bitpay-right9ctrl.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_city-of-bakersfield-click2gov.yaml](supply-chain/2018-11_city-of-bakersfield-click2gov.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-11_el-centro-regional-medical-center-jobscience-inc.yaml](supply-chain/2018-11_el-centro-regional-medical-center-jobscience-inc.yaml) | supply-chain | 2018-11-01 |  |  |
| [2018-10_dunkin-donuts-credential-stuffing.yaml](credential-theft/2018-10_dunkin-donuts-credential-stuffing.yaml) | credential-theft | 2018-10-31 |  |  |
| [2018-11_nordstrom-not-disclosed.yaml](supply-chain/2018-11_nordstrom-not-disclosed.yaml) | supply-chain | 2018-10-09 |  |  |
| [2018-10_a-few-e-commerce-sites-customers-of--shopper-approved.yaml](supply-chain/2018-10_a-few-e-commerce-sites-customers-of--shopper-approved.yaml) | supply-chain | 2018-10-01 |  |  |
| [2018-10_many-major-companies-including-amazo-supermicro.yaml](supply-chain/2018-10_many-major-companies-including-amazo-supermicro.yaml) | supply-chain | 2018-10-01 |  |  |
| [2018-10_the-indio-water-authority-click2gov.yaml](supply-chain/2018-10_the-indio-water-authority-click2gov.yaml) | supply-chain | 2018-10-01 |  |  |
| [2018-10_vestacp-not-disclosed.yaml](supply-chain/2018-10_vestacp-not-disclosed.yaml) | supply-chain | 2018-10-01 |  |  |
| [2018-09_the-conservative-party-uk-crowdcomms.yaml](supply-chain/2018-09_the-conservative-party-uk-crowdcomms.yaml) | supply-chain | 2018-09-30 |  |  |
| [2018-09_all-platfroms-that-use-facebook-logi-facebook.yaml](supply-chain/2018-09_all-platfroms-that-use-facebook-logi-facebook.yaml) | supply-chain | 2018-09-25 |  |  |
| [2018-11_atrium-health-accudoc-solutions-inc.yaml](supply-chain/2018-11_atrium-health-accudoc-solutions-inc.yaml) | supply-chain | 2018-09-22 |  |  |
| [2018-11_event-stream-npm-malware.yaml](supply-chain/2018-11_event-stream-npm-malware.yaml) | supply-chain | 2018-09-09 | flatmap-stream (malicious dep… |  |
| [2018-09_perth-mint-not-disclosed.yaml](supply-chain/2018-09_perth-mint-not-disclosed.yaml) | supply-chain | 2018-09-01 |  |  |
| [2019-03_healthcare-institutions-including-bl-wolverine-solutions-grou.yaml](supply-chain/2019-03_healthcare-institutions-including-bl-wolverine-solutions-grou.yaml) | supply-chain | 2018-09-01 | Ransomware (variant not publi… |  |
| [2018-09_foosackly-not-disclosed.yaml](supply-chain/2018-09_foosackly-not-disclosed.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_wegmans-invermar.yaml](supply-chain/2018-09_wegmans-invermar.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_the-washoe-county-school-district-edmodo.yaml](supply-chain/2018-09_the-washoe-county-school-district-edmodo.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_university-of-lousville-health-fitness-corp.yaml](supply-chain/2018-09_university-of-lousville-health-fitness-corp.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_blue-cross-blue-shield-of-rhode-isla-not-disclosed.yaml](supply-chain/2018-09_blue-cross-blue-shield-of-rhode-isla-not-disclosed.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-09_e-commerce-sites-of-feedify-feedify.yaml](supply-chain/2018-09_e-commerce-sites-of-feedify-feedify.yaml) | supply-chain | 2018-09-01 |  |  |
| [2018-08_150-businesses-including-those-in-tr-medcall-healthcare-advis.yaml](supply-chain/2018-08_150-businesses-including-those-in-tr-medcall-healthcare-advis.yaml) | supply-chain | 2018-08-24 |  |  |
| [2018-08_air-canada-not-disclosed.yaml](supply-chain/2018-08_air-canada-not-disclosed.yaml) | supply-chain | 2018-08-22 |  |  |
| [2018-09_british-airways-still-in-investigation.yaml](supply-chain/2018-09_british-airways-still-in-investigation.yaml) | supply-chain | 2018-08-21 | Magecart web skimmer |  |
| [2018-08_british-airways-magecart.yaml](data-leak/2018-08_british-airways-magecart.yaml) | data-leak | 2018-08-21 | Magecart skimmer |  |
| [2018-08_t-mobile-api-2m.yaml](data-leak/2018-08_t-mobile-api-2m.yaml) | data-leak | 2018-08-20 |  |  |
| [2018-08_cosmos-bank-india-atm-cashout.yaml](other/2018-08_cosmos-bank-india-atm-cashout.yaml) | other | 2018-08-11 |  |  |
| [2018-12_bevmo-ncr-corp.yaml](supply-chain/2018-12_bevmo-ncr-corp.yaml) | supply-chain | 2018-08-02 | JavaScript payment card skimm… |  |
| [2019-06_quest-diagnostics-laboratory-corpora-american-medical-collect.yaml](supply-chain/2019-06_quest-diagnostics-laboratory-corpora-american-medical-collect.yaml) | supply-chain | 2018-08-01 | web payment page skimmer |  |
| [2019-07_american-esoteric-laboratories-sunri-american-medical-collect.yaml](supply-chain/2019-07_american-esoteric-laboratories-sunri-american-medical-collect.yaml) | supply-chain | 2018-08-01 | web payment page skimmer |  |
| [2018-08_south-korean-organizations-remote-support-solution.yaml](supply-chain/2018-08_south-korean-organizations-remote-support-solution.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-08_mention-not-disclosed.yaml](supply-chain/2018-08_mention-not-disclosed.yaml) | supply-chain | 2018-08-01 |  |  |
| [2019-03_amca-quest-labcorp-billing.yaml](data-leak/2019-03_amca-quest-labcorp-billing.yaml) | data-leak | 2018-08-01 |  |  |
| [2018-08_fiserv-affiliated-financial-institut-fiserv.yaml](supply-chain/2018-08_fiserv-affiliated-financial-institut-fiserv.yaml) | supply-chain | 2018-08-01 |  |  |
| [2019-07_clinical-pathology-laboratories-american-medical-collect.yaml](supply-chain/2019-07_clinical-pathology-laboratories-american-medical-collect.yaml) | supply-chain | 2018-08-01 | web payment page skimmer |  |
| [2019-05_amca-quest-labcorp-breach.yaml](supply-chain/2019-05_amca-quest-labcorp-breach.yaml) | supply-chain | 2018-08-01 |  |  |
| [2019-06_opko-health-american-medical-collect.yaml](supply-chain/2019-06_opko-health-american-medical-collect.yaml) | supply-chain | 2018-08-01 | web payment page skimmer |  |
| [2018-08_a-probably-mexican-government-healt--hova-health.yaml](supply-chain/2018-08_a-probably-mexican-government-healt--hova-health.yaml) | supply-chain | 2018-08-01 |  |  |
| [2018-12_managed-health-services-of-indiana-lcp-corp.yaml](supply-chain/2018-12_managed-health-services-of-indiana-lcp-corp.yaml) | supply-chain | 2018-07-30 |  |  |
| [2018-07_labcorp-samsam-ransomware.yaml](ransomware/2018-07_labcorp-samsam-ransomware.yaml) | ransomware | 2018-07-14 | SamSam ransomware |  |
| [2018-07_timehop-21m-social-tokens.yaml](credential-theft/2018-07_timehop-21m-social-tokens.yaml) | credential-theft | 2018-07-04 |  |  |
| [2018-10_department-of-defense-pentagon-not-disclosed.yaml](supply-chain/2018-10_department-of-defense-pentagon-not-disclosed.yaml) | supply-chain | 2018-07-01 |  |  |
| [2018-06_the-central-bank-of-the-bahamas-not-disclosed.yaml](supply-chain/2018-06_the-central-bank-of-the-bahamas-not-disclosed.yaml) | supply-chain | 2018-06-28 |  |  |
| [2018-06_singhealth-apt-breach.yaml](data-leak/2018-06_singhealth-apt-breach.yaml) | data-leak | 2018-06-27 | Custom RAT (remote access tro… |  |
| [2018-08_godaddy-amazon-s3-bucket.yaml](supply-chain/2018-08_godaddy-amazon-s3-bucket.yaml) | supply-chain | 2018-06-19 |  |  |
| [2018-06_reddit-not-disclosed.yaml](supply-chain/2018-06_reddit-not-disclosed.yaml) | supply-chain | 2018-06-14 |  |  |
| [2018-01_reddit-mailgun.yaml](supply-chain/2018-01_reddit-mailgun.yaml) | supply-chain | 2018-06-14 |  |  |
| [2018-06_flipboard-145m-users.yaml](data-leak/2018-06_flipboard-145m-users.yaml) | data-leak | 2018-06-02 |  |  |
| [2019-01_highmark-bcbs-aetna-emblem-health-hu-benefitmall.yaml](supply-chain/2019-01_highmark-bcbs-aetna-emblem-health-hu-benefitmall.yaml) | supply-chain | 2018-06-01 |  |  |
| [2018-06_exactis-elasticsearch-340m.yaml](data-leak/2018-06_exactis-elasticsearch-340m.yaml) | data-leak | 2018-06-01 |  |  |
| [2018-05_universal-music-group-agilisium.yaml](supply-chain/2018-05_universal-music-group-agilisium.yaml) | supply-chain | 2018-05-30 |  |  |
| [2018-05_banco-de-chile-swift-wiper.yaml](other/2018-05_banco-de-chile-swift-wiper.yaml) | other | 2018-05-24 | KillMBR wiper (custom variant… |  |
| [2018-06_whitbread-costa-coffee-premier-inn-pageup.yaml](supply-chain/2018-06_whitbread-costa-coffee-premier-inn-pageup.yaml) | supply-chain | 2018-05-23 | Unspecified malware on PageUp… |  |
| [2018-05_pageup-hr-platform-breach.yaml](supply-chain/2018-05_pageup-hr-platform-breach.yaml) | data-leak | 2018-05-23 |  |  |
| [2019-02_houzz-not-disclosed.yaml](supply-chain/2019-02_houzz-not-disclosed.yaml) | supply-chain | 2018-05-23 |  |  |
| [2018-05_pageup-hr-saas-australia.yaml](data-leak/2018-05_pageup-hr-saas-australia.yaml) | data-leak | 2018-05-23 |  |  |
| [2018-05_some-fortune-500-firms-corporation-service-comp.yaml](supply-chain/2018-05_some-fortune-500-firms-corporation-service-comp.yaml) | supply-chain | 2018-04-05 |  |  |
| [2018-09_chegg-s3-root-credentials.yaml](data-leak/2018-09_chegg-s3-root-credentials.yaml) | credential-theft | 2018-04-01 |  |  |
| [2018-03_unitypoint-health-bec-1-4m.yaml](credential-theft/2018-03_unitypoint-health-bec-1-4m.yaml) | credential-theft | 2018-03-14 |  |  |
| [2018-07_unitypoint-health-phishing-14m-patients.yaml](data-leak/2018-07_unitypoint-health-phishing-14m-patients.yaml) | data-leak | 2018-03-14 |  |  |
| [2018-03_cathay-pacific-9-4m-passengers.yaml](data-leak/2018-03_cathay-pacific-9-4m-passengers.yaml) | data-leak | 2018-03-01 |  |  |
| [2018-05_chili-s-grill-bar-not-disclosed.yaml](supply-chain/2018-05_chili-s-grill-bar-not-disclosed.yaml) | supply-chain | 2018-03-01 | POS RAM-scraping malware |  |
| [2019-10_nordvpn-not-disclosed.yaml](supply-chain/2019-10_nordvpn-not-disclosed.yaml) | supply-chain | 2018-03-01 |  |  |
| [2018-02_la-times-s3-cryptomining.yaml](other/2018-02_la-times-s3-cryptomining.yaml) | other | 2018-02-09 |  |  |
| [2018-02_under-armour-myfitnesspal.yaml](data-leak/2018-02_under-armour-myfitnesspal.yaml) | data-leak | 2018-02-01 |  |  |
| [2018-02_ticketmaster-inbenta-magecart.yaml](supply-chain/2018-02_ticketmaster-inbenta-magecart.yaml) | supply-chain | 2018-02-01 | Magecart skimmer |  |
| [2018-01_allscripts-samsam-ehr-outage.yaml](ransomware/2018-01_allscripts-samsam-ehr-outage.yaml) | ransomware | 2018-01-18 | SamSam ransomware |  |
| [2018-01_allscripts-ransomware-ehr-vendor.yaml](ransomware/2018-01_allscripts-ransomware-ehr-vendor.yaml) | ransomware | 2018-01-18 | SamSam ransomware |  |
| [2019-01_collection1-773m-credential-dump.yaml](credential-theft/2019-01_collection1-773m-credential-dump.yaml) | credential-theft | 2018-01-01 |  |  |
| [2018-01_healthengine-patient-data-lawyers.yaml](data-leak/2018-01_healthengine-patient-data-lawyers.yaml) | data-leak | 2018-01-01 |  |  |
| [2026-04_german-bka-revil-gandcrab-leader-unmasked.yaml](ransomware/2026-04_german-bka-revil-gandcrab-leader-unmasked.yaml) | ransomware | 2018-01-01 | REvil (Sodinokibi), GandCrab |  |
| [2018-01_western-union-not-disclosed.yaml](supply-chain/2018-01_western-union-not-disclosed.yaml) | supply-chain | 2018-01-01 |  |  |
| [2018-06_klook-sociaplus.yaml](supply-chain/2018-06_klook-sociaplus.yaml) | supply-chain | 2017-12-11 | JavaScript skimmer |  |
| [2017-12_nicehash-hack-4700-btc.yaml](other/2017-12_nicehash-hack-4700-btc.yaml) | other | 2017-12-06 |  |  |
| [2018-02_orlando-orthopaedic-center-not-disclosed.yaml](supply-chain/2018-02_orlando-orthopaedic-center-not-disclosed.yaml) | supply-chain | 2017-12-01 |  |  |
| [2018-02_applebee-s-not-disclosed.yaml](supply-chain/2018-02_applebee-s-not-disclosed.yaml) | supply-chain | 2017-11-23 | POS RAM-scraping malware |  |
| [2018-06_uc-san-diego-health-nuance-communications.yaml](supply-chain/2018-06_uc-san-diego-health-nuance-communications.yaml) | supply-chain | 2017-11-20 |  |  |
| [2017-10_domino-s-australia-a-former-supplier.yaml](supply-chain/2017-10_domino-s-australia-a-former-supplier.yaml) | supply-chain | 2017-10-01 |  |  |
| [2019-08_imperva-rds-snapshot-exposure.yaml](data-leak/2019-08_imperva-rds-snapshot-exposure.yaml) | credential-theft | 2017-10-01 |  |  |
| [2018-06_more-than-a-dozen-us-cities-click2gov.yaml](supply-chain/2018-06_more-than-a-dozen-us-cities-click2gov.yaml) | supply-chain | 2017-10-01 | SJavaWebManage web shell | CVE-2017-3248, CVE-2017-3506, CVE-2017-… |
| [2018-04_bestbuy-sears-kmart-delta-not-disclosed.yaml](supply-chain/2018-04_bestbuy-sears-kmart-delta-not-disclosed.yaml) | supply-chain | 2017-09-27 |  |  |
| [2018-06_ticketmaster-inbenta.yaml](supply-chain/2018-06_ticketmaster-inbenta.yaml) | supply-chain | 2017-09-01 | Magecart JavaScript card skim… |  |
| [2017-09_samsung-sony-asus-intel-vmware-o2-si-ccleaner.yaml](supply-chain/2017-09_samsung-sony-asus-intel-vmware-o2-si-ccleaner.yaml) | supply-chain | 2017-09-01 | Floxif backdoor (Stage 1); St… |  |
| [2017-08_panera-bread-plaintext-api.yaml](data-leak/2017-08_panera-bread-plaintext-api.yaml) | data-leak | 2017-08-01 |  |  |
| [2019-02_huddle-house-not-disclosed.yaml](supply-chain/2019-02_huddle-house-not-disclosed.yaml) | supply-chain | 2017-08-01 | POS RAM scraper (card track d… |  |
| [2017-07_hbo-game-of-thrones-15tb.yaml](data-leak/2017-07_hbo-game-of-thrones-15tb.yaml) | data-leak | 2017-07-31 |  |  |
| [2017-07_aetna-hiv-envelope-disclosure.yaml](data-leak/2017-07_aetna-hiv-envelope-disclosure.yaml) | data-leak | 2017-07-28 |  |  |
| [2017-07_hundreds-of-large-companies-around-t-netsarang.yaml](supply-chain/2017-07_hundreds-of-large-companies-around-t-netsarang.yaml) | supply-chain | 2017-07-01 | ShadowPad modular backdoor |  |
| [2017-06_many-ukrainen-companies-and-everal-g-medoc.yaml](supply-chain/2017-06_many-ukrainen-companies-and-everal-g-medoc.yaml) | supply-chain | 2017-06-27 | NotPetya (Petya variant / wip… | CVE-2017-0144, CVE-2017-0145 |
| [2017-06_notpetya-medoc-maersk-10b.yaml](supply-chain/2017-06_notpetya-medoc-maersk-10b.yaml) | supply-chain | 2017-06-27 | NotPetya (Petya variant / wip… | CVE-2017-0144 |
| [2017-06_uk-parliament-owa-brute-force.yaml](credential-theft/2017-06_uk-parliament-owa-brute-force.yaml) | credential-theft | 2017-06-23 |  |  |
| [2017-07_verizon-nice-systems.yaml](supply-chain/2017-07_verizon-nice-systems.yaml) | supply-chain | 2017-06-08 |  |  |
| [2017-08_triton-trisis-ics-safety-systems.yaml](other/2017-08_triton-trisis-ics-safety-systems.yaml) | other | 2017-06-01 | TRITON (TRISIS, HatMan) |  |
| [2017-06_verizon-nice-systems-s3-14m.yaml](supply-chain/2017-06_verizon-nice-systems-s3-14m.yaml) | data-leak | 2017-06-01 |  |  |
| [2017-06_deep-root-analytics-198m-voters.yaml](data-leak/2017-06_deep-root-analytics-198m-voters.yaml) | data-leak | 2017-06-01 |  |  |
| [2017-06_republican-national-committee-deep-root.yaml](supply-chain/2017-06_republican-national-committee-deep-root.yaml) | supply-chain | 2017-06-01 |  |  |
| [2017-05_onelogin-aws-decryption-breach.yaml](credential-theft/2017-05_onelogin-aws-decryption-breach.yaml) | credential-theft | 2017-05-31 |  |  |
| [2017-05_zomato-17m-users.yaml](data-leak/2017-05_zomato-17m-users.yaml) | data-leak | 2017-05-17 |  |  |
| [2017-07_equifax-not-disclosed.yaml](supply-chain/2017-07_equifax-not-disclosed.yaml) | supply-chain | 2017-05-13 |  | CVE-2017-5638 |
| [2017-05_wannacry-eternalblue-global.yaml](ransomware/2017-05_wannacry-eternalblue-global.yaml) | ransomware | 2017-05-12 | WannaCry (WannaCrypt, WannaCr… | CVE-2017-0144, CVE-2017-0145, CVE-2017-… |
| [2017-05_wannacry-nhs-attack.yaml](ransomware/2017-05_wannacry-nhs-attack.yaml) | ransomware | 2017-05-12 | WannaCry ransomware | CVE-2017-0144, CVE-2017-0145 |
| [2018-04_saks-lord-taylor-fin7-5m-cards.yaml](credential-theft/2018-04_saks-lord-taylor-fin7-5m-cards.yaml) | credential-theft | 2017-05-01 | BOOSTWRITE / POS malware (FIN… |  |
| [2017-05_companies-with-mac-user-employees-wh-handbrake.yaml](supply-chain/2017-05_companies-with-mac-user-employees-wh-handbrake.yaml) | supply-chain | 2017-05-01 | Proton RAT (Remote Access Tro… |  |
| [2017-05_saks-lord-taylor-fin7-pos.yaml](data-leak/2017-05_saks-lord-taylor-fin7-pos.yaml) | data-leak | 2017-05-01 | Carbanak POS RAM-scraping mal… |  |
| [2017-05_bell-canada-anonymous-1-9m.yaml](data-leak/2017-05_bell-canada-anonymous-1-9m.yaml) | data-leak | 2017-05-01 |  |  |
| [2017-11_forever-21-not-disclosed.yaml](supply-chain/2017-11_forever-21-not-disclosed.yaml) | supply-chain | 2017-04-03 | POS RAM-scraping malware (unn… |  |
| [2017-11_forever21-pos-malware.yaml](credential-theft/2017-11_forever21-pos-malware.yaml) | credential-theft | 2017-04-03 | POS malware |  |
| [2017-04_wonga-payday-loans-270k.yaml](data-leak/2017-04_wonga-payday-loans-270k.yaml) | data-leak | 2017-04-01 |  |  |
| [2017-04_chipotle-pos-malware.yaml](credential-theft/2017-04_chipotle-pos-malware.yaml) | credential-theft | 2017-03-24 | POS malware (Track data scrap… |  |
| [2017-03_chipotle-pos-malware.yaml](data-leak/2017-03_chipotle-pos-malware.yaml) | data-leak | 2017-03-24 | POS RAM scraping malware |  |
| [2017-10_hyatt-hotels-not-disclosed.yaml](supply-chain/2017-10_hyatt-hotels-not-disclosed.yaml) | supply-chain | 2017-03-18 | POS RAM-scraping malware (unn… |  |
| [2017-05_equifax.yaml](data-leak/2017-05_equifax.yaml) | data-leak | 2017-03-10 |  | CVE-2017-5638 |
| [2019-05_first-american-financial-idor-885m-docs.yaml](data-leak/2019-05_first-american-financial-idor-885m-docs.yaml) | data-leak | 2017-03-01 |  |  |
| [2017-05_macron-campaign-apt28-macronleaks.yaml](other/2017-05_macron-campaign-apt28-macronleaks.yaml) | other | 2017-01-01 |  |  |
| [2023-02_goodrx-ftc-health-data-advertising.yaml](data-leak/2023-02_goodrx-ftc-health-data-advertising.yaml) | data-leak | 2017-01-01 |  |  |
| [2018-01_aadhaar-india-1-billion-exposed.yaml](data-leak/2018-01_aadhaar-india-1-billion-exposed.yaml) | data-leak | 2017-01-01 |  |  |
| [2019-06_desjardins-insider.yaml](data-leak/2019-06_desjardins-insider.yaml) | data-leak | 2017-01-01 |  |  |
| [2019-01_desjardins-insider-breach.yaml](data-leak/2019-01_desjardins-insider-breach.yaml) | data-leak | 2017-01-01 |  |  |
| [2017-09_sonic-drive-in-pos-5m-cards.yaml](credential-theft/2017-09_sonic-drive-in-pos-5m-cards.yaml) | credential-theft | 2017-01-01 | POS malware |  |
| [2023-02_goodrx-health-data-meta-google-advertising.yaml](data-leak/2023-02_goodrx-health-data-meta-google-advertising.yaml) | data-leak | 2017-01-01 |  |  |
| [2017-03_brand-new-day-not-disclosed.yaml](supply-chain/2017-03_brand-new-day-not-disclosed.yaml) | supply-chain | 2016-12-22 |  |  |
| [2016-12_industroyer-ukraine-power-grid.yaml](other/2016-12_industroyer-ukraine-power-grid.yaml) | other | 2016-12-17 | Industroyer (CrashOverride); … |  |
| [2019-10_uber-slack-and-fcc-zendesk.yaml](supply-chain/2019-10_uber-slack-and-fcc-zendesk.yaml) | supply-chain | 2016-11-01 |  |  |
| [2016-11_three-mobile-uk-133k.yaml](data-leak/2016-11_three-mobile-uk-133k.yaml) | data-leak | 2016-11-01 |  |  |
| [2016-10_australian-red-cross-blood-service.yaml](data-leak/2016-10_australian-red-cross-blood-service.yaml) | data-leak | 2016-10-26 |  |  |
| [2017-02_arbys-pos-malware-355k-cards.yaml](credential-theft/2017-02_arbys-pos-malware-355k-cards.yaml) | credential-theft | 2016-10-25 | POS malware (Track 1/Track 2 … |  |
| [2016-10_australian-red-cross-donor-data.yaml](data-leak/2016-10_australian-red-cross-donor-data.yaml) | data-leak | 2016-10-25 |  |  |
| [2016-10_dailymotion-85m-accounts.yaml](data-leak/2016-10_dailymotion-85m-accounts.yaml) | data-leak | 2016-10-20 |  |  |
| [2017-10_uber-github.yaml](supply-chain/2017-10_uber-github.yaml) | supply-chain | 2016-10-13 |  |  |
| [2016-10_deloitte-email-breach.yaml](data-leak/2016-10_deloitte-email-breach.yaml) | data-leak | 2016-10-01 |  |  |
| [2016-10_adult-friendfinder-lfi-412m.yaml](data-leak/2016-10_adult-friendfinder-lfi-412m.yaml) | data-leak | 2016-10-01 |  |  |
| [2016-10_uber-cover-up.yaml](data-leak/2016-10_uber-cover-up.yaml) | data-leak | 2016-10-01 |  |  |
| [2016-10_uber-github-aws-credentials.yaml](credential-theft/2016-10_uber-github-aws-credentials.yaml) | credential-theft | 2016-10-01 |  |  |
| [2018-05_lifebridge-health-breach-538k-patients.yaml](data-leak/2018-05_lifebridge-health-breach-538k-patients.yaml) | data-leak | 2016-09-27 |  |  |
| [2017-02_cloudflare-cloudbleed-memory-leak.yaml](other/2017-02_cloudflare-cloudbleed-memory-leak.yaml) | data-leak | 2016-09-22 |  |  |
| [2017-02_new-jersey-diamond-institute-for-fer-not-disclosed.yaml](supply-chain/2017-02_new-jersey-diamond-institute-for-fer-not-disclosed.yaml) | supply-chain | 2016-08-28 |  |  |
| [2016-08_shadow-brokers-nsa-exploit-leak.yaml](other/2016-08_shadow-brokers-nsa-exploit-leak.yaml) | other | 2016-08-13 | EternalBlue; EternalRomance; … | CVE-2017-0144, CVE-2017-0145 |
| [2017-05_sabre-synxis-hospitality-1-3m-cards.yaml](credential-theft/2017-05_sabre-synxis-hospitality-1-3m-cards.yaml) | credential-theft | 2016-08-10 |  |  |
| [2017-07_hard-rock-hotels-casinos-sabre-corp-synxis.yaml](supply-chain/2017-07_hard-rock-hotels-casinos-sabre-corp-synxis.yaml) | supply-chain | 2016-08-10 |  |  |
| [2016-08_sabre-synxis-hotel-breach.yaml](supply-chain/2016-08_sabre-synxis-hotel-breach.yaml) | data-leak | 2016-08-10 |  |  |
| [2016-08_bitfinex-hack-119756-btc.yaml](other/2016-08_bitfinex-hack-119756-btc.yaml) | other | 2016-08-02 |  |  |
| [2017-04_ihg-intercontinental-pos-1200-locations.yaml](credential-theft/2017-04_ihg-intercontinental-pos-1200-locations.yaml) | credential-theft | 2016-08-01 | POS malware (Track data scrap… |  |
| [2016-07_datadog-aws-access-keys.yaml](credential-theft/2016-07_datadog-aws-access-keys.yaml) | credential-theft | 2016-07-07 |  |  |
| [2016-07_oracle-micros-carbanak.yaml](supply-chain/2016-07_oracle-micros-carbanak.yaml) | supply-chain | 2016-07-01 | Carbanak malware |  |
| [2016-07_dark-overlord-healthcare-extortion.yaml](data-leak/2016-07_dark-overlord-healthcare-extortion.yaml) | data-leak | 2016-07-01 |  |  |
| [2016-06_banner-health-pos-pivot.yaml](data-leak/2016-06_banner-health-pos-pivot.yaml) | data-leak | 2016-06-17 | POS RAM-scraping malware |  |
| [2016-06_banner-health-pos-pivot-3-7m.yaml](data-leak/2016-06_banner-health-pos-pivot-3-7m.yaml) | data-leak | 2016-06-17 | POS malware |  |
| [2016-05_newkirk-products-bcbs-health-id-cards.yaml](data-leak/2016-05_newkirk-products-bcbs-health-id-cards.yaml) | data-leak | 2016-05-21 |  |  |
| [2016-05_newkirk-products-health-id-cards.yaml](supply-chain/2016-05_newkirk-products-health-id-cards.yaml) | supply-chain | 2016-05-11 |  |  |
| [2016-03_comelec-philippines-55m-voters.yaml](data-leak/2016-03_comelec-philippines-55m-voters.yaml) | data-leak | 2016-03-27 |  |  |
| [2016-03_gru-dnc-podesta-election-hack.yaml](credential-theft/2016-03_gru-dnc-podesta-election-hack.yaml) | credential-theft | 2016-03-19 | X-Agent, X-Tunnel, Mimikatz, … |  |
| [2016-06_dnc-podesta-apt28-gru.yaml](other/2016-06_dnc-podesta-apt28-gru.yaml) | other | 2016-03-19 | X-Agent (Sofacy) keylogger/cr… |  |
| [2016-02_snapchat-ceo-fraud-payroll.yaml](credential-theft/2016-02_snapchat-ceo-fraud-payroll.yaml) | credential-theft | 2016-02-26 |  |  |
| [2016-02_bangladesh-bank-swift-heist-81m.yaml](other/2016-02_bangladesh-bank-swift-heist-81m.yaml) | other | 2016-02-04 | EVTDIAG, MSOUTC, MSOUTC (Laza… |  |
| [2016-02_bangladesh-bank-swift-81m.yaml](other/2016-02_bangladesh-bank-swift-81m.yaml) | other | 2016-02-04 | EVTDIAG; MSOUTC; MSOUTC (SWIF… |  |
| [2016-02_weebly-43m-users.yaml](data-leak/2016-02_weebly-43m-users.yaml) | data-leak | 2016-02-01 |  |  |
| [2016-01_centene-corporation-missing-hard-drives.yaml](data-leak/2016-01_centene-corporation-missing-hard-drives.yaml) | data-leak | 2016-01-07 |  |  |
| [2016-07_vitagene-s3-unprotected-buckets.yaml](credential-theft/2016-07_vitagene-s3-unprotected-buckets.yaml) | data-leak | 2016-01-01 |  |  |
| [2016-01_verizon-enterprise-1-5m.yaml](data-leak/2016-01_verizon-enterprise-1-5m.yaml) | data-leak | 2016-01-01 |  |  |
| [2018-10_fastcash-dprk-atm-cashout.yaml](other/2018-10_fastcash-dprk-atm-cashout.yaml) | other | 2016-01-01 | FASTCash implant (AIX trojan) |  |
| [2016-01_lifeboat-minecraft-7m.yaml](data-leak/2016-01_lifeboat-minecraft-7m.yaml) | data-leak | 2016-01-01 |  |  |
| [2015-12_blackenergy-ukraine-power-grid.yaml](other/2015-12_blackenergy-ukraine-power-grid.yaml) | other | 2015-12-23 | BlackEnergy3; KillDisk |  |
| [2015-11_vtech-children-learning-tablets.yaml](data-leak/2015-11_vtech-children-learning-tablets.yaml) | data-leak | 2015-11-14 |  |  |
| [2015-10_talktalk-sql-injection-157k.yaml](data-leak/2015-10_talktalk-sql-injection-157k.yaml) | data-leak | 2015-10-21 |  |  |
| [2015-10_21st-century-oncology-fbi.yaml](data-leak/2015-10_21st-century-oncology-fbi.yaml) | data-leak | 2015-10-03 |  |  |
| [2015-10_21st-century-oncology-fbi-2-2m.yaml](data-leak/2015-10_21st-century-oncology-fbi-2-2m.yaml) | data-leak | 2015-10-03 |  |  |
| [2016-05_wendys-pos-malware-1025-locations.yaml](credential-theft/2016-05_wendys-pos-malware-1025-locations.yaml) | credential-theft | 2015-10-01 | POS malware (two distinct str… |  |
| [2015-10_wendys-pos-malware-1025-locations.yaml](supply-chain/2015-10_wendys-pos-malware-1025-locations.yaml) | supply-chain | 2015-10-01 | Carbanak variant POS malware |  |
| [2015-09_experian-t-mobile-15m.yaml](supply-chain/2015-09_experian-t-mobile-15m.yaml) | supply-chain | 2015-09-01 |  |  |
| [2015-09_t-mobile-experian.yaml](supply-chain/2015-09_t-mobile-experian.yaml) | supply-chain | 2015-09-01 |  |  |
| [2015-12_hyatt-hotels-pos-malware-250-hotels.yaml](credential-theft/2015-12_hyatt-hotels-pos-malware-250-hotels.yaml) | credential-theft | 2015-08-13 | POS malware |  |
| [2015-07_ashley-madison-impact-team.yaml](data-leak/2015-07_ashley-madison-impact-team.yaml) | data-leak | 2015-07-12 |  |  |
| [2015-07_hacking-team-400gb-dump.yaml](data-leak/2015-07_hacking-team-400gb-dump.yaml) | data-leak | 2015-07-05 |  |  |
| [2015-06_lastpass-first-breach.yaml](data-leak/2015-06_lastpass-first-breach.yaml) | data-leak | 2015-06-12 |  |  |
| [2015-09_sam-s-club-costco-cvs-riteaid-walmar-pni-digital-media.yaml](supply-chain/2015-09_sam-s-club-costco-cvs-riteaid-walmar-pni-digital-media.yaml) | supply-chain | 2015-06-01 |  |  |
| [2015-05_medical-informatics-engineering-webchart.yaml](supply-chain/2015-05_medical-informatics-engineering-webchart.yaml) | data-leak | 2015-05-07 |  |  |
| [2015-05_bundestag-apt28-16gb-exfil.yaml](other/2015-05_bundestag-apt28-16gb-exfil.yaml) | other | 2015-04-01 |  |  |
| [2015-02_sally-beauty-pos-25k-cards.yaml](data-leak/2015-02_sally-beauty-pos-25k-cards.yaml) | data-leak | 2015-03-01 | POS RAM-scraping malware |  |
| [2015-01_centcom-twitter-youtube-isis-hijack.yaml](other/2015-01_centcom-twitter-youtube-isis-hijack.yaml) | other | 2015-01-12 |  |  |
| [2015-01_irs-get-transcript-100k.yaml](credential-theft/2015-01_irs-get-transcript-100k.yaml) | credential-theft | 2015-01-01 |  |  |
| [2015-05_irs-get-transcript-100k-ssn.yaml](data-leak/2015-05_irs-get-transcript-100k-ssn.yaml) | credential-theft | 2015-01-01 |  |  |
| [2015-04_tv5monde-apt28-broadcast-disruption.yaml](other/2015-04_tv5monde-apt28-broadcast-disruption.yaml) | other | 2015-01-01 |  |  |
| [2015-02_anthem-health-insurance-78m.yaml](data-leak/2015-02_anthem-health-insurance-78m.yaml) | data-leak | 2014-12-10 |  |  |
| [2015-01_morgan-stanley-insider-350k-clients.yaml](data-leak/2015-01_morgan-stanley-insider-350k-clients.yaml) | data-leak | 2014-12-01 |  |  |
| [2014-11_sony-pictures-wiper-lazarus.yaml](other/2014-11_sony-pictures-wiper-lazarus.yaml) | other | 2014-11-24 | Destover (wiper/backdoor) |  |
| [2014-11_browserstack-aws-access-key-forgotten.yaml](credential-theft/2014-11_browserstack-aws-access-key-forgotten.yaml) | credential-theft | 2014-11-09 |  |  |
| [2015-11_state-department-unclassified-email.yaml](data-leak/2015-11_state-department-unclassified-email.yaml) | data-leak | 2014-10-01 |  |  |
| [2014-09_ucla-health-4-5m-apt.yaml](data-leak/2014-09_ucla-health-4-5m-apt.yaml) | data-leak | 2014-09-01 |  |  |
| [2015-07_ucla-health.yaml](data-leak/2015-07_ucla-health.yaml) | data-leak | 2014-09-01 |  |  |
| [2014-09_kmart-sears-holdings-pos-malware.yaml](credential-theft/2014-09_kmart-sears-holdings-pos-malware.yaml) | credential-theft | 2014-09-01 | POS RAM-scraping malware (spe… |  |
| [2014-08_bell-canada-hacker-1-9m.yaml](data-leak/2014-08_bell-canada-hacker-1-9m.yaml) | data-leak | 2014-08-01 |  |  |
| [2018-11_marriott-starwood.yaml](supply-chain/2018-11_marriott-starwood.yaml) | supply-chain | 2014-07-29 | Remote Access Trojan (RAT); M… |  |
| [2015-06_opm-security-clearance-breach.yaml](data-leak/2015-06_opm-security-clearance-breach.yaml) | data-leak | 2014-07-01 |  |  |
| [2014-07_kbox-singapore-317k-pdpc.yaml](data-leak/2014-07_kbox-singapore-317k-pdpc.yaml) | data-leak | 2014-07-01 |  |  |
| [2014-07_lowe-s-safetyfirst-e-driver-fil.yaml](supply-chain/2014-07_lowe-s-safetyfirst-e-driver-fil.yaml) | supply-chain | 2014-07-01 |  |  |
| [2014-06_codespaces-aws-ransomware.yaml](other/2014-06_codespaces-aws-ransomware.yaml) | other | 2014-06-17 |  |  |
| [2014-06_dominos-pizza-europe-600k-customers.yaml](data-leak/2014-06_dominos-pizza-europe-600k-customers.yaml) | data-leak | 2014-06-13 |  |  |
| [2014-10_jpmorgan-chase-co-not-disclosed.yaml](supply-chain/2014-10_jpmorgan-chase-co-not-disclosed.yaml) | supply-chain | 2014-06-01 |  |  |
| [2014-08_jpmorgan-chase-83m-accounts.yaml](data-leak/2014-08_jpmorgan-chase-83m-accounts.yaml) | data-leak | 2014-06-01 |  |  |
| [2015-05_carefirst-bcbs-apt-1-1m.yaml](data-leak/2015-05_carefirst-bcbs-apt-1-1m.yaml) | data-leak | 2014-06-01 |  |  |
| [2014-06_jpmorgan-chase-76m-households.yaml](data-leak/2014-06_jpmorgan-chase-76m-households.yaml) | data-leak | 2014-06-01 |  |  |
| [2014-06_dominos-pizza-france-belgium.yaml](data-leak/2014-06_dominos-pizza-france-belgium.yaml) | data-leak | 2014-06-01 |  |  |
| [2014-06_carefirst-bcbs-china-apt.yaml](data-leak/2014-06_carefirst-bcbs-china-apt.yaml) | data-leak | 2014-06-01 |  |  |
| [2014-05_uber-github-aws-50k-drivers.yaml](credential-theft/2014-05_uber-github-aws-50k-drivers.yaml) | credential-theft | 2014-05-12 |  |  |
| [2014-05_premera-blue-cross-apt.yaml](data-leak/2014-05_premera-blue-cross-apt.yaml) | data-leak | 2014-05-05 |  |  |
| [2015-01_premera-blue-cross.yaml](data-leak/2015-01_premera-blue-cross.yaml) | data-leak | 2014-05-05 |  |  |
| [2014-04_heartbleed-openssl-cve-2014-0160.yaml](other/2014-04_heartbleed-openssl-cve-2014-0160.yaml) | other | 2014-04-07 |  | CVE-2014-0160 |
| [2014-08_community-health-systems-apt18-heartbleed.yaml](data-leak/2014-08_community-health-systems-apt18-heartbleed.yaml) | data-leak | 2014-04-01 |  | CVE-2014-0160 |
| [2014-04_staples-pos-malware.yaml](data-leak/2014-04_staples-pos-malware.yaml) | data-leak | 2014-04-01 | POS RAM-scraping malware |  |
| [2014-04_community-health-systems-apt.yaml](data-leak/2014-04_community-health-systems-apt.yaml) | data-leak | 2014-04-01 | Custom Mimikatz variant |  |
| [2014-04_boston-medical-mdf-transcription-servic.yaml](supply-chain/2014-04_boston-medical-mdf-transcription-servic.yaml) | supply-chain | 2014-04-01 |  |  |
| [2014-09_home-depot-blackpos-56m.yaml](data-leak/2014-09_home-depot-blackpos-56m.yaml) | data-leak | 2014-04-01 | BlackPOS (Kaptoxa) RAM-scraper |  |
| [2014-09_staples-pos-1-16m-cards.yaml](data-leak/2014-09_staples-pos-1-16m-cards.yaml) | data-leak | 2014-04-01 | POS RAM-scraping malware |  |
| [2014-03_opm-personnel-files-4-2m-earlier-breach.yaml](data-leak/2014-03_opm-personnel-files-4-2m-earlier-breach.yaml) | data-leak | 2014-03-01 | PlugX RAT |  |
| [2014-02_university-of-maryland-310k.yaml](data-leak/2014-02_university-of-maryland-310k.yaml) | data-leak | 2014-02-18 |  |  |
| [2014-03_kickstarter-user-data-breach.yaml](data-leak/2014-03_kickstarter-user-data-breach.yaml) | data-leak | 2014-02-12 |  |  |
| [2014-02_faa-employee-data-45k.yaml](data-leak/2014-02_faa-employee-data-45k.yaml) | data-leak | 2014-02-01 |  |  |
| [2014-05_ebay-employee-credentials-145m.yaml](data-leak/2014-05_ebay-employee-credentials-145m.yaml) | credential-theft | 2014-02-01 |  |  |
| [2014-11_usps-china-apt-800k-employees.yaml](data-leak/2014-11_usps-china-apt-800k-employees.yaml) | data-leak | 2014-01-01 |  |  |
| [2014-01_morrisons-insider-100k-employees.yaml](data-leak/2014-01_morrisons-insider-100k-employees.yaml) | data-leak | 2014-01-01 |  |  |
| [2021-06_mercedes-benz-usa-not-disclosed.yaml](supply-chain/2021-06_mercedes-benz-usa-not-disclosed.yaml) | supply-chain | 2014-01-01 |  |  |
| [2014-06_indiana-university-146k-ssn-exposure.yaml](data-leak/2014-06_indiana-university-146k-ssn-exposure.yaml) | data-leak | 2014-01-01 |  |  |
| [2018-11_marriott-starwood.yaml](data-leak/2018-11_marriott-starwood.yaml) | data-leak | 2014-01-01 | Remote Access Trojan (name un… |  |
| [2017-05_bronx-lebanon-hospital-center-in-new-ihealth-innovations.yaml](supply-chain/2017-05_bronx-lebanon-hospital-center-in-new-ihealth-innovations.yaml) | supply-chain | 2014-01-01 |  |  |
| [2013-12_excellus-bcbs-apt.yaml](data-leak/2013-12_excellus-bcbs-apt.yaml) | data-leak | 2013-12-23 |  |  |
| [2015-09_excellus-bcbs-apt-10m.yaml](data-leak/2015-09_excellus-bcbs-apt-10m.yaml) | data-leak | 2013-12-01 |  |  |
| [2013-11_target-blackpos.yaml](other/2013-11_target-blackpos.yaml) | other | 2013-11-15 | BlackPOS / Kaptoxa |  |
| [2023-05_toyota-connected-cloud-misconfiguration-2m.yaml](data-leak/2023-05_toyota-connected-cloud-misconfiguration-2m.yaml) | data-leak | 2013-11-06 |  |  |
| [2013-11_toyota-connected-gps-10year-exposure.yaml](data-leak/2013-11_toyota-connected-gps-10year-exposure.yaml) | data-leak | 2013-11-06 |  |  |
| [2013-11_target-fazio-mechanical-service.yaml](supply-chain/2013-11_target-fazio-mechanical-service.yaml) | supply-chain | 2013-11-01 | BlackPOS (Kaptoxa) RAM-scrapi… |  |
| [2013-11_cupid-media-42m-plaintext.yaml](data-leak/2013-11_cupid-media-42m-plaintext.yaml) | data-leak | 2013-11-01 |  |  |
| [2015-04_att-insider-callcenter-fcc.yaml](data-leak/2015-04_att-insider-callcenter-fcc.yaml) | data-leak | 2013-11-01 |  |  |
| [2021-02_florida-healthy-kids-corporation-fhkc-jelly-bean-communications-de.yaml](supply-chain/2021-02_florida-healthy-kids-corporation-fhkc-jelly-bean-communications-de.yaml) | supply-chain | 2013-11-01 |  |  |
| [2015-10_scottrade-4-6m-customers.yaml](data-leak/2015-10_scottrade-4-6m-customers.yaml) | data-leak | 2013-10-01 |  |  |
| [2013-09_pf-changs-pos-malware.yaml](credential-theft/2013-09_pf-changs-pos-malware.yaml) | credential-theft | 2013-09-01 | POS malware (FIN6) |  |
| [2013-09_pf-changs-pos-malware-2m-cards.yaml](credential-theft/2013-09_pf-changs-pos-malware-2m-cards.yaml) | credential-theft | 2013-09-01 | POS RAM-scraping malware |  |
| [2013-10_adobe-source-code-153m.yaml](data-leak/2013-10_adobe-source-code-153m.yaml) | data-leak | 2013-08-01 |  |  |
| [2013-07_rt-jones-capital-not-disclosed.yaml](supply-chain/2013-07_rt-jones-capital-not-disclosed.yaml) | supply-chain | 2013-07-22 |  |  |
| [2013-12_neiman-marcus-pos-malware-350k-cards.yaml](data-leak/2013-12_neiman-marcus-pos-malware-350k-cards.yaml) | data-leak | 2013-07-16 | POS RAM-scraping malware |  |
| [2013-07_advocate-health-care-stolen-computers.yaml](data-leak/2013-07_advocate-health-care-stolen-computers.yaml) | data-leak | 2013-07-15 |  |  |
| [2013-07_advocate-medical-4m-stolen-laptops.yaml](data-leak/2013-07_advocate-medical-4m-stolen-laptops.yaml) | data-leak | 2013-07-15 |  |  |
| [2016-09_yahoo-3-billion-accounts.yaml](data-leak/2016-09_yahoo-3-billion-accounts.yaml) | credential-theft | 2013-07-01 |  |  |
| [2018-03_facebook-cambridge-analytica-87m.yaml](data-leak/2018-03_facebook-cambridge-analytica-87m.yaml) | data-leak | 2013-06-01 |  |  |
| [2013-05_michaels-stores-pos-malware.yaml](data-leak/2013-05_michaels-stores-pos-malware.yaml) | data-leak | 2013-05-08 | POS RAM-scraping malware |  |
| [2013-01_michaels-stores-pos-malware-26m-cards.yaml](credential-theft/2013-01_michaels-stores-pos-malware-26m-cards.yaml) | credential-theft | 2013-05-08 | POS RAM-scraping malware |  |
| [2013-01_michaels-stores-pos-malware.yaml](credential-theft/2013-01_michaels-stores-pos-malware.yaml) | credential-theft | 2013-05-08 | POS malware (Track data scrap… |  |
| [2013-05_tumblr-65m-accounts-discovered-2016.yaml](data-leak/2013-05_tumblr-65m-accounts-discovered-2016.yaml) | data-leak | 2013-05-01 |  |  |
| [2013-04_livingsocial-50m-accounts.yaml](data-leak/2013-04_livingsocial-50m-accounts.yaml) | data-leak | 2013-04-26 |  |  |
| [2013-04_livingsocial-50m-customers.yaml](data-leak/2013-04_livingsocial-50m-customers.yaml) | data-leak | 2013-04-01 |  |  |
| [2013-02_evernote-50m-breach.yaml](data-leak/2013-02_evernote-50m-breach.yaml) | data-leak | 2013-02-28 |  |  |
| [2013-02_goodwill-ck-systems-pos.yaml](supply-chain/2013-02_goodwill-ck-systems-pos.yaml) | supply-chain | 2013-02-01 | POS RAM-scraping malware |  |
| [2013-10_imgur-breach-17m-accounts-discovered-2017.yaml](data-leak/2013-10_imgur-breach-17m-accounts-discovered-2017.yaml) | data-leak | 2013-01-01 |  |  |
| [2020-11_hotels-customers-of-prestige-softwar-prestige-software.yaml](supply-chain/2020-11_hotels-customers-of-prestige-softwar-prestige-software.yaml) | supply-chain | 2013-01-01 |  |  |
| [2012-12_schnucks-markets-pos-malware-24m-cards.yaml](credential-theft/2012-12_schnucks-markets-pos-malware-24m-cards.yaml) | credential-theft | 2012-12-01 | POS RAM-scraping malware |  |
| [2013-01_howard-university-hospital-stolen-laptop-34k.yaml](data-leak/2013-01_howard-university-hospital-stolen-laptop-34k.yaml) | data-leak | 2012-11-01 |  |  |
| [2015-05_penn-state-cs-apt-18k.yaml](data-leak/2015-05_penn-state-cs-apt-18k.yaml) | data-leak | 2012-09-01 |  |  |
| [2012-10_south-carolina-revenue-dept-3-8m-ssn.yaml](data-leak/2012-10_south-carolina-revenue-dept-3-8m-ssn.yaml) | data-leak | 2012-08-27 |  |  |
| [2012-08_blizzard-battle-net-14m.yaml](data-leak/2012-08_blizzard-battle-net-14m.yaml) | data-leak | 2012-08-04 |  |  |
| [2012-09_barnes-noble-pos-skimmers.yaml](credential-theft/2012-09_barnes-noble-pos-skimmers.yaml) | credential-theft | 2012-08-01 |  |  |
| [2016-08_dropbox-credential-reuse-68m.yaml](credential-theft/2016-08_dropbox-credential-reuse-68m.yaml) | credential-theft | 2012-07-01 |  |  |
| [2012-07_disqus-breach-17m-accounts-discovered-2017.yaml](data-leak/2012-07_disqus-breach-17m-accounts-discovered-2017.yaml) | data-leak | 2012-07-01 |  |  |
| [2012-07_disqus-17m-breach-disclosed-2017.yaml](data-leak/2012-07_disqus-17m-breach-disclosed-2017.yaml) | data-leak | 2012-07-01 |  |  |
| [2012-06_south-carolina-dhhs-medicaid-228k.yaml](data-leak/2012-06_south-carolina-dhhs-medicaid-228k.yaml) | data-leak | 2012-06-14 |  |  |
| [2012-09_barnes-noble-pos-skimmers-63-stores.yaml](credential-theft/2012-09_barnes-noble-pos-skimmers-63-stores.yaml) | credential-theft | 2012-06-01 |  |  |
| [2012-06_linkedin-unsalted-sha1-117m.yaml](data-leak/2012-06_linkedin-unsalted-sha1-117m.yaml) | credential-theft | 2012-05-01 |  |  |
| [2012-06_eharmony-passwords-unsalted.yaml](credential-theft/2012-06_eharmony-passwords-unsalted.yaml) | credential-theft | 2012-05-01 |  |  |
| [2012-06_eharmony-15m-passwords-leaked.yaml](credential-theft/2012-06_eharmony-15m-passwords-leaked.yaml) | credential-theft | 2012-05-01 |  |  |
| [2012-03_lastfm-43m-passwords-breach.yaml](credential-theft/2012-03_lastfm-43m-passwords-breach.yaml) | credential-theft | 2012-03-01 |  |  |
| [2012-01_zappos-24m-customers.yaml](data-leak/2012-01_zappos-24m-customers.yaml) | data-leak | 2012-01-15 |  |  |
| [2012-03_global-payments-card-processor.yaml](data-leak/2012-03_global-payments-card-processor.yaml) | data-leak | 2012-01-01 |  |  |
| [2012-01_facebook-plaintext-passwords-600m.yaml](data-leak/2012-01_facebook-plaintext-passwords-600m.yaml) | data-leak | 2012-01-01 |  |  |
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
| [2008-03_hannaford-pos-malware-4m.yaml](data-leak/2008-03_hannaford-pos-malware-4m.yaml) | data-leak | 2007-12-01 |  |  |
| [2009-01_heartland-payment-systems-130m.yaml](data-leak/2009-01_heartland-payment-systems-130m.yaml) | data-leak | 2007-12-01 |  |  |
| [2006-08_aol-search-data-leak-650k.yaml](data-leak/2006-08_aol-search-data-leak-650k.yaml) | data-leak | 2006-08-04 |  |  |
| [2006-05_veterans-affairs-laptop-26m.yaml](data-leak/2006-05_veterans-affairs-laptop-26m.yaml) | data-leak | 2006-05-03 |  |  |
| [2005-10_samy-worm-myspace-xss.yaml](other/2005-10_samy-worm-myspace-xss.yaml) | other | 2005-10-04 | Samy worm (JavaScript XSS wor… |  |
| [2005-10_samy-worm-myspace-xss-1m-friends.yaml](other/2005-10_samy-worm-myspace-xss-1m-friends.yaml) | other | 2005-10-04 | Samy worm (JS/Samy) |  |
| [2005-08_zotob-worm-windows2000-cnn-nyt-dhs.yaml](other/2005-08_zotob-worm-windows2000-cnn-nyt-dhs.yaml) | other | 2005-08-13 | Zotob (W32/Zotob, also Tpbot,… | CVE-2005-1983 |
| [2005-08_zotob-worm-ms05-039.yaml](other/2005-08_zotob-worm-ms05-039.yaml) | other | 2005-08-13 | Zotob (IRCBot variant) | CVE-2005-1983 |
| [2007-01_tjx-wardriving-wifi-94m.yaml](data-leak/2007-01_tjx-wardriving-wifi-94m.yaml) | data-leak | 2005-07-01 |  |  |
| [2005-02_paris-hilton-tmobile-sidekick-hack.yaml](data-leak/2005-02_paris-hilton-tmobile-sidekick-hack.yaml) | data-leak | 2005-02-19 |  |  |
| [2005-03_dsw-designer-shoe-warehouse-14m-cards.yaml](data-leak/2005-03_dsw-designer-shoe-warehouse-14m-cards.yaml) | data-leak | 2005-01-01 |  |  |
| [2005-03_dsw-designer-shoe-warehouse.yaml](data-leak/2005-03_dsw-designer-shoe-warehouse.yaml) | credential-theft | 2005-01-01 |  |  |
| [2004-01_mydoom-worm-fastest-email.yaml](other/2004-01_mydoom-worm-fastest-email.yaml) | other | 2004-01-26 | MyDoom (W32/Mydoom, Novarg, M… |  |
| [2005-06_cardsystems-sql-injection-40m.yaml](data-leak/2005-06_cardsystems-sql-injection-40m.yaml) | data-leak | 2004-01-01 |  |  |
| [2005-02_choicepoint-fraud-163k.yaml](data-leak/2005-02_choicepoint-fraud-163k.yaml) | data-leak | 2004-01-01 |  |  |
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
# ── Core fields (always present) ───────────────────────────────────────────────
source_name: "Publication or organization reporting the breach"
source_url: "https://example.com/direct-link-to-report"
date_of_breach: "YYYY-MM-DD"          # also accepts YYYY-MM or YYYY
date_of_disclosure: "YYYY-MM-DD"      # empty string "" if unknown
category: "ransomware | data-leak | supply-chain | credential-theft | other"
notes: "Narrative summary of the incident including timeline, scope, threat actor attribution, and any known impact."

# ── Traditional breach fields ───────────────────────────────────────────────────
date_of_customer_notification: ""     # YYYY-MM-DD or "" if unknown
initial_attack_vector: "CWE-NNN: Short description, or free-text description of the attack method"
cve: []                               # list of CVE/GHSA IDs, e.g. ["CVE-2024-3094"], empty if none
vendor_product: "Vendor Product Name" # affected vendor or product
software_package: ""                  # package name for software supply chain incidents, "" otherwise
malware: ""                           # malware family name if identified, "" otherwise
supply_chain_claimed: false           # true if a third-party vendor relationship was the attack vector

# ── Crypto / Web3 fields ───────────────────────────────────────────────────────
blockchain: "ethereum"                # blockchain(s) involved, e.g. "ethereum, solana"; omit if not applicable
financial_loss_usd: 0                 # numeric USD value of funds lost; omit if not applicable
financial_recovered_usd: 0           # numeric USD value recovered after the incident; omit if not applicable
affected_count: 0                    # number of affected wallets, users, or individuals; omit if not applicable
```

## Folders

- `ransomware/` — ransomware incidents
- `data-leak/` — customer data exposure
- `supply-chain/` — supply chain attacks
- `credential-theft/` — credential compromise
- `other/` — uncategorized or multi-category
