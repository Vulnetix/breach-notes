#!/usr/bin/env python3
"""
Rewrite BlackKite stub supply-chain records with comprehensive research-backed notes.
Writes clean YAML directly without round-tripping through yaml.dump.
"""
import os, re, sys
from pathlib import Path

DATA_DIR = Path("/home/chris/GitHub/breach-notes/data/supply-chain")

def clean(s):
    """Fix encoding artifacts."""
    if not s: return ''
    s = str(s)
    for bad, good in [
        ('\u00e2\u0080\u0099', "'"), ('\u00e2\u0080\u0093', '–'),
        ('\u00e2\u0080\u0094', '—'), ('\u00e2\u0080\u009c', '"'),
        ('\u00e2\u0080\u009d', '"'), ('â\x80\x99', "'"),
        ('â\x80\x93', '–'), ('â\x80\x94', '—'),
        ('â\x80\x9c', '"'), ('â\x80\x9d', '"'),
    ]:
        s = s.replace(bad, good)
    return s.strip()

def yaml_str(s, indent=0):
    """Safely format a string value for YAML."""
    s = clean(str(s)) if s else ''
    if not s: return '""'
    # Use block scalar for long strings
    if len(s) > 200 or '\n' in s:
        lines = s.replace('\\n', '\n').split('\n')
        prefix = ' ' * (indent + 2)
        body = ('\n' + prefix).join(l.rstrip() for l in lines)
        return f'|-\n{prefix}{body}'
    # Escape for plain string
    if any(c in s for c in [':', '#', '[', ']', '{', '}', '&', '*', '!', '|', '>', "'", '"', '%', '@', '`']):
        escaped = s.replace('"', '\\"')
        return f'"{escaped}"'
    return s

def write_yaml(path, d):
    """Write a breach record as clean YAML."""
    lines = []
    simple_fields = [
        'source_name', 'source_url', 'date_of_breach',
        'date_of_disclosure', 'date_of_customer_notification',
        'category', 'initial_attack_vector',
    ]
    for f in simple_fields:
        v = clean(d.get(f, ''))
        lines.append(f'{f}: {yaml_str(v, len(f))}')
    
    lines.append('cve: []')
    
    vp = clean(d.get('vendor_product', ''))
    lines.append(f'vendor_product: {yaml_str(vp, 14)}')
    lines.append('software_package: ""')
    
    malware = clean(d.get('malware', ''))
    lines.append(f'malware: {yaml_str(malware, 7)}')
    
    sc = 'true' if d.get('supply_chain_claimed', True) else 'false'
    lines.append(f'supply_chain_claimed: {sc}')
    
    notes = clean(d.get('notes', ''))
    if len(notes) > 200:
        # Block scalar
        wrapped = []
        words = notes.split()
        line = ''
        for w in words:
            if len(line) + len(w) + 1 > 110:
                wrapped.append(line)
                line = w
            else:
                line = (line + ' ' + w).strip()
        if line: wrapped.append(line)
        body = '\n  '.join(wrapped)
        lines.append(f'notes: |-\n  {body}')
    else:
        lines.append(f'notes: {yaml_str(notes, 6)}')
    
    with open(path, 'w') as f:
        f.write('\n'.join(lines) + '\n')


# ─── Comprehensive research database ──────────────────────────────────────────
# Pattern → full incident details
KNOWN = [

# ══ 2013 ══
("RT Jones Capital", {
    "source_name": "RT Jones Capital Equities — SEC First Cybersecurity Enforcement, Third-Party Web Hosting Breach",
    "source_url": "https://www.sec.gov/news/pressrelease/2015-202.html",
    "date_of_breach": "2013-07-01",
    "initial_attack_vector": "RT Jones Capital stored client PII on a third-party hosted website that was compromised; the firm had no policies to assess vendor cybersecurity, no encryption of stored PII, and no incident response plan",
    "vendor_product": "Third-party web hosting provider (unnamed)",
    "notes": "RT Jones Capital Equities Management, a St. Louis-based registered investment adviser, stored PII for approximately 100,000 clients and prospects on a third-party web server. In July 2013 that server was attacked and the data compromised. In September 2015 the SEC issued a cease-and-desist and imposed a $75,000 civil penalty — the first SEC enforcement action against a registered investment adviser solely for cybersecurity failures under Rule 30(a) of Regulation S-P (the Safeguards Rule). The SEC found no policies to assess vendor cybersecurity, no PII encryption, and no incident response plan. No client suffered financial harm.",
}),

("Target.*Fazio|Fazio.*Target", {
    "source_name": "Target Corporation BlackPOS Breach via Fazio Mechanical HVAC Vendor — 70M Customers, 40M Cards",
    "source_url": "https://krebsonsecurity.com/2014/02/target-hackers-broke-in-via-hvac-company/",
    "date_of_breach": "2013-11-27",
    "initial_attack_vector": "Attackers infected Fazio Mechanical Services (HVAC contractor) with Citadel credential-stealing malware, harvesting network credentials Fazio used for remote monitoring of Target's refrigeration and HVAC systems; pivoted from vendor portal to Target's POS network and deployed BlackPOS (Kaptoxa) RAM-scraping malware",
    "vendor_product": "Fazio Mechanical Services (HVAC contractor) — vendor portal / POS network",
    "malware": "BlackPOS (Kaptoxa); Citadel credential stealer (on vendor systems)",
    "notes": "Between 27 November and 15 December 2013, attackers breached Target Corporation via Fazio Mechanical Services, an HVAC contractor with remote access to Target's systems for monitoring heating and refrigeration. Citadel malware on Fazio's computers harvested network credentials. Attackers pivoted to Target's POS network and installed BlackPOS RAM-scraping malware on approximately 1,800 store terminals, capturing 40 million payment cards and exfiltrating personal data of 70 million customers during peak holiday shopping. Target paid $18.5M to settle with 47 state AGs, $10M in consumer class action, and over $200M in total breach-related costs. CEO Gregg Steinhafel resigned. Accelerated US EMV chip adoption and PCI DSS network segmentation requirements.",
}),

("Boston Medical.*MDF|MDF Transcription", {
    "source_name": "Boston Medical Center Patient Records Breach via MDF Transcription Services",
    "source_url": "https://www.bostonglobe.com/business/2014/04/29/boston-medical-center-fires-vendor-after-data-breach/",
    "date_of_breach": "2014-04-01",
    "initial_attack_vector": "MDF Transcription Services, contracted by Boston Medical Center for medical transcription, improperly posted patient records to a publicly accessible, unauthenticated internet server; records were discoverable via search engines",
    "vendor_product": "MDF Transcription Services",
    "notes": "In April 2014, Boston Medical Center discovered that MDF Transcription Services had posted approximately 15,000 patient records — including diagnoses, procedures, and clinical notes — to a publicly accessible website with no authentication. BMC immediately terminated the contract, filed an HHS OCR HIPAA breach notification, notified patients, and reported to law enforcement. The breach illustrated the risk of business associates lacking adequate data handling controls for internet-facing systems. BMC implemented enhanced vendor security assessments following the incident.",
}),

("Lowe.*SafetyFirst|SafetyFirst.*Lowe", {
    "source_name": "Lowe's Driver Records Breach via SafetyFirst E-Driver File Platform",
    "source_url": "https://www.csoonline.com/article/2158122/identity-management/vendor-error-forces-lowes-to-issue-breach-notification-letters.html",
    "date_of_breach": "2014-07-01",
    "initial_attack_vector": "SafetyFirst's E-Driver File online driver qualification database — used by Lowe's to store commercial driver records — had a vulnerability or misconfiguration exposing driver SSNs, birth dates, and driver's licence numbers",
    "vendor_product": "SafetyFirst E-Driver File (fleet driver qualification management)",
    "notes": "In July 2014, Lowe's Companies issued breach notification letters after driver qualification records stored in SafetyFirst's E-Driver File platform were exposed. Data included Social Security numbers, dates of birth, driver's licence numbers, and related PII for current and former Lowe's commercial vehicle drivers. SafetyFirst provides fleet safety and driver qualification management services. Affected individuals received notification and credit monitoring offers.",
}),

("JPMorgan.*Corporate Challenge|Corporate Challenge.*JPMorgan", {
    "source_name": "JPMorgan Chase Corporate Challenge Race Registration Third-Party Breach",
    "source_url": "https://www.wsj.com/articles/j-p-morgan-found-hackers-after-finding-breach-of-race-website-1414766443",
    "date_of_breach": "2014-06-01",
    "initial_attack_vector": "Attackers (same Russian criminal group responsible for the JPMorgan Chase 76M-household breach) compromised a third-party race registration website used for JPMorgan's Corporate Challenge charity running events, discovering credentials that aided the broader network breach",
    "vendor_product": "Corporate Challenge race registration platform (third-party)",
    "notes": "In 2014, the same Russian criminal group responsible for JPMorgan Chase's main corporate network breach (76 million households) also compromised a third-party website hosting JPMorgan's Corporate Challenge race registrations. The race site, used by thousands of employees for charity running events in multiple cities, stored employee personal information. The breach was discovered during forensic investigation of the broader JPMorgan hack. The attackers were later identified as linked to Gery Shalon's organized crime network, which operated multiple fraud schemes using stolen financial data.",
}),

# ══ 2015 ══
("PNI Digital Media|Sam.*Club.*Costco.*CVS", {
    "source_name": "PNI Digital Media Supply Chain Breach — Sam's Club, Costco, CVS, Rite Aid, Walmart Canada Photo Centers",
    "source_url": "https://www.scmagazine.com/pni-digital-media-cvs-and-costco-warn-of-pii-compromise-in-photo-center-attack/article/533792/",
    "date_of_breach": "2015-07-01",
    "initial_attack_vector": "Attackers compromised PNI Digital Media — the technology platform provider powering photo printing kiosks and online ordering for multiple major retailers — installing payment card skimming malware that collected customer payment data across all retailers simultaneously",
    "vendor_product": "PNI Digital Media (photo center software and payment processing)",
    "malware": "Payment card skimming malware",
    "notes": "In 2015, PNI Digital Media — a Victoria, BC company powering photo printing services for Costco, Sam's Club, CVS Pharmacy, Rite Aid, Walmart Canada, and Tesco UK — was compromised by attackers who installed payment card skimming malware on the PNI platform. All major retail clients were simultaneously affected. Costco suspended online photo services; CVS took down its photo site; Sam's Club, Rite Aid, and Walmart Canada issued notifications. PNI had been acquired by Shutterfly in 2014. The breach demonstrated the concentration risk of B2B technology platforms serving competing retail brands — one vendor breach simultaneously exposed millions of customers across the industry.",
}),

("T-Mobile.*Experian.*2015|Experian.*T-Mobile.*2015|2015.*T-Mobile.*Experian", {
    "source_name": "T-Mobile / Experian Credit Application Server Breach — 15 Million Customers",
    "source_url": "https://www.t-mobile.com/customers/experian-data-breach-faq",
    "date_of_breach": "2015-09-01",
    "initial_attack_vector": "Unknown attacker accessed Experian's server that processed T-Mobile postpaid credit applications; the specific intrusion vector was not publicly disclosed by Experian",
    "vendor_product": "Experian Decision Analytics (T-Mobile credit check server)",
    "notes": "In September 2015, Experian's server processing T-Mobile credit applications was breached, exposing data for approximately 15 million people who applied for T-Mobile postpaid service from September 2013 to September 2015. Stolen data included names, addresses, Social Security numbers, dates of birth, driver's licence and passport numbers. T-Mobile CEO John Legere publicly criticised Experian. Connecticut AG opened an investigation. Experian offered 2 years of credit monitoring. Multiple class actions were filed against both companies.",
}),

# ══ 2017 ══
("Handbrake.*Mac|Mac.*Handbrake", {
    "source_name": "HandBrake macOS Download Mirror Compromised — Proton RAT Supply Chain Attack",
    "source_url": "https://www.macrumors.com/2017/05/07/handbrake-app-security-warning-servers-hacked/",
    "date_of_breach": "2017-05-02",
    "initial_attack_vector": "Attackers compromised the HandBrake macOS download mirror server and replaced the legitimate HandBrake 1.0.7 DMG installer with a trojanized version containing the Proton macOS RAT; users who downloaded from the compromised mirror between 2-6 May 2017 received malware",
    "vendor_product": "HandBrake video transcoder (mirror download server)",
    "malware": "Proton RAT for macOS",
    "notes": "Between 2-6 May 2017, attackers compromised HandBrake's macOS download mirror server and replaced the legitimate installer with a Proton RAT-infected version. HandBrake is a widely used free video transcoding app. The Proton RAT collected macOS Keychain passwords, browser credentials, SSH keys, and GPG keys. HandBrake estimated ~50% of mirror downloads during the window were malicious. Corporate victim Panic Software confirmed infection. Users were instructed to change all saved passwords and invalidate SSH/GPG keys. An early and notable macOS supply chain attack via trusted open-source download infrastructure.",
}),

("NetSarang|ShadowPad.*NetSarang|NetSarang.*ShadowPad", {
    "source_name": "NetSarang ShadowPad Supply Chain Backdoor — Winnti Group, 100+ Large Corporations",
    "source_url": "https://www.kaspersky.com/about/press-releases/2017_shadowpad-how-attackers-hide-backdoor-in-software-used-by-hundreds-of-large-companies-around-the-world",
    "date_of_breach": "2017-07-17",
    "initial_attack_vector": "BRONZE ATLAS / Winnti Group compromised NetSarang's build pipeline and inserted the ShadowPad modular backdoor into a legitimately code-signed server management software library (nssock2.dll) distributed with Xmanager, Xshell, Xftp, and Xlpd",
    "vendor_product": "NetSarang Xmanager / Xshell / Xftp (server management suite)",
    "malware": "ShadowPad modular backdoor",
    "notes": "In July 2017, Kaspersky Lab discovered that NetSarang's server management software suite had been trojanized with ShadowPad — a sophisticated modular backdoor attributed to BRONZE ATLAS / Winnti Group (China-linked APT). NetSarang products are used by ~500,000 enterprises globally. The compromised .nls library (nssock2.dll) was included in legitimately signed builds and distributed via NetSarang's official website for 17 days. Active infections were detected at a Hong Kong financial institution. NetSarang released a clean version on 4 August 2017. Victims included financial services, pharmaceutical, telecom, and government organizations. ShadowPad became a recurring tool in subsequent Winnti supply chain operations.",
}),

("CCleaner|Piriform.*CCleaner", {
    "source_name": "CCleaner Supply Chain Backdoor — BARIUM/Winnti, 2.27 Million Users, Stage 2 Intel/Samsung/Sony",
    "source_url": "https://www.wired.com/story/inside-the-unnerving-supply-chain-attack-that-corrupted-ccleaner/",
    "date_of_breach": "2017-08-15",
    "initial_attack_vector": "BARIUM/Winnti Group compromised Piriform's software build infrastructure and injected the Floxif backdoor into CCleaner 5.33 for Windows; the trojanized version was digitally signed with Piriform's legitimate code-signing certificate and distributed via official channels",
    "vendor_product": "Piriform CCleaner 5.33 (PC optimization utility, Windows)",
    "malware": "Floxif backdoor (Stage 1); GhostRat-variant (Stage 2 for high-value targets)",
    "notes": "Between 15 August and 12 September 2017, Piriform (Avast subsidiary) distributed a backdoored CCleaner 5.33 to 2.27 million Windows users. Stage 1 (Floxif) collected system info; Stage 2 was delivered only to ~40 machines at targeted tech companies including Samsung, Sony, VMware, Intel, O2, Singtel, and Fujitsu. Discovered by Cisco Talos and disclosed 18 September 2017. The malicious version bore a valid Piriform digital signature. Attribution to BARIUM/Winnti based on shared code with known Chinese APT tools. Piriform had been acquired by Avast just weeks before the attack. Demonstrated the risk of acquiring companies with already-compromised build infrastructure.",
}),

("Deep Root.*Republican|Republican.*Deep Root", {
    "source_name": "Republican National Committee Deep Root Analytics S3 Bucket Exposure — 198 Million Voter Records",
    "source_url": "https://gizmodo.com/gop-data-firm-accidentally-leaks-personal-details-of-ne-1796211612",
    "date_of_breach": "2017-06-01",
    "initial_attack_vector": "Deep Root Analytics — a data firm contracted by the Republican National Committee — misconfigured an Amazon S3 bucket to be publicly accessible without authentication, exposing voter analytics data for nearly every US registered voter",
    "vendor_product": "Deep Root Analytics (AWS S3 bucket)",
    "notes": "In June 2017, UpGuard's Chris Vickery discovered a publicly accessible S3 bucket belonging to Deep Root Analytics, a political data firm contracted by the RNC. The bucket contained 1.1TB of data on approximately 198 million Americans — nearly every registered US voter — including names, addresses, dates of birth, phone numbers, party affiliation, and detailed political scoring on 46 issues including gun control and stem cell research. The data had been compiled for campaign microtargeting. Deep Root secured the bucket after notification. The incident highlighted risks in political data broker practices and S3 misconfiguration at analytics firms handling mass voter data.",
}),

("Equifax.*2017|2017.*Equifax", {
    "source_name": "Equifax Apache Struts Breach — 147 Million Americans, SSNs, $575M FTC Settlement",
    "source_url": "https://www.consumer.ftc.gov/blog/2017/09/equifax-data-breach-what-do",
    "date_of_breach": "2017-05-13",
    "initial_attack_vector": "Equifax failed to patch a critical Apache Struts vulnerability (CVE-2017-5638) in their ACIS online dispute portal despite a patch being available for months; the unpatched vulnerability allowed attackers to gain remote code execution and access Equifax's internal systems",
    "vendor_product": "Apache Struts (CVE-2017-5638) in Equifax's ACIS dispute portal",
    "malware": "",
    "notes": "Between 13 May and 30 July 2017, attackers exploited CVE-2017-5638 in Apache Struts on Equifax's ACIS online dispute portal. Equifax had been warned about the vulnerability in March 2017 but failed to patch it. Attackers spent 78 days undetected, exfiltrating personal data of approximately 147.9 million Americans including names, SSNs, dates of birth, addresses, driver's licence numbers, and ~200,000 credit card numbers. CEO Richard Smith resigned. Equifax paid $575M to the FTC (largest ever data security settlement at the time), $380.5M to consumers, and reached settlements with all 50 state AGs totalling $690M+. Congress held multiple hearings. The breach is the definitive case study in failure to apply critical security patches in a timely manner.",
}),

("Sabre.*SynXis|Hard Rock.*Sabre|SynXis", {
    "source_name": "Sabre Hospitality SynXis Central Reservations Breach — Hard Rock and 36,000 Hotels",
    "source_url": "https://threatpost.com/sabre-corp-investigating-breach-of-reservation-system/125405/",
    "date_of_breach": "2017-08-10",
    "initial_attack_vector": "Unknown attacker used a compromised credential for an authorized SynXis user to access Sabre Hospitality Solutions' SynXis Central Reservations system, then accessed payment card data and PII for hotel guests",
    "vendor_product": "Sabre Hospitality Solutions SynXis Central Reservations",
    "notes": "Between August 2016 and March 2017, an unauthorized actor used compromised credentials to access Sabre's SynXis Central Reservations system — the dominant hotel reservation platform used by approximately 36,000 hotel properties globally. Stolen data included payment card Track 1/Track 2 data and guest PII. Affected properties included Hard Rock Hotels & Casinos (11 hotels), Trump Hotels, Loews Hotels, Kimpton Hotels, Four Seasons, and many others. Sabre notified affected hotel clients in May 2017; hotels notified their guests. Class-action lawsuits filed against multiple hotel chains. Demonstrated the concentration risk of hospitality reservation platforms.",
}),

("Verizon.*NICE|NICE.*Verizon", {
    "source_name": "Verizon 14 Million Customer Data Exposure via NICE Systems AWS S3 Misconfiguration",
    "source_url": "https://thehackernews.com/2017/07/over-14-million-verizon-customers-data.html",
    "date_of_breach": "2017-06-01",
    "initial_attack_vector": "NICE Systems — contracted by Verizon for call center analytics — misconfigured an Amazon S3 bucket storing approximately 14 million Verizon customer call records to be publicly accessible without authentication; discovered by UpGuard researcher Dan O'Sullivan",
    "vendor_product": "NICE Systems AWS S3 bucket (Verizon customer data)",
    "notes": "In July 2017, UpGuard researchers discovered a publicly accessible Amazon S3 bucket belonging to NICE Systems containing approximately 14 million Verizon customer records including names, addresses, account numbers, and PINs (used for customer service authentication). NICE Systems was contracted to analyze Verizon's call center customer service interactions. Verizon disputed the full PIN exposure but acknowledged the misconfiguration. PIN exposure would have enabled account takeover via social engineering of Verizon customer service. Verizon and NICE worked to secure the bucket after notification. Demonstrated risk of call center analytics vendors handling sensitive authentication data.",
}),

("Forever 21.*2017|2017.*Forever 21", {
    "source_name": "Forever 21 POS Malware Breach — 8 Months of Payment Card Theft at Store Locations",
    "source_url": "https://threatpost.com/forever-21-says-pos-systems-exposed-customer-data-for-8-months/129271/",
    "date_of_breach": "2017-03-01",
    "initial_attack_vector": "POS malware infected point-of-sale terminals at Forever 21 stores nationwide; the malware activated when the point-to-point encryption (P2PE) protection was not active on specific terminals, capturing payment card data during those windows",
    "vendor_product": "Third-party POS system vendor (unnamed)",
    "malware": "POS memory-scraping malware",
    "notes": "Between approximately March and October 2017, POS malware operated at Forever 21 store locations — one of the largest US fashion retail chains. Uniquely, the malware only captured card data when the point-to-point encryption (P2PE) protection on terminals was not active, meaning it targeted specific terminals at specific times. Thousands of store locations may have been affected over the 8-month period. Credit card data (numbers, expiration dates, verification codes, cardholder names) was stolen. Forever 21 disclosed the breach in November 2017 after payment card brands alerted them. Law enforcement and a third-party forensics firm assisted with investigation.",
}),

("Hyatt.*2017|2017.*Hyatt", {
    "source_name": "Hyatt Hotels Second POS Malware Breach — 41 Hotels, Third-Party Payment Systems",
    "source_url": "https://threatpost.com/hyatt-hit-by-credit-card-breach-again/128440/",
    "date_of_breach": "2017-01-01",
    "initial_attack_vector": "POS malware was installed on point-of-sale systems at 41 Hyatt hotel locations; Hyatt had previously suffered a POS malware breach in 2015-2016, suggesting persistent vulnerability in its payment processing infrastructure or third-party POS service provider",
    "vendor_product": "Third-party POS system vendor at Hyatt locations",
    "malware": "POS RAM-scraping malware",
    "notes": "In October 2017, Hyatt Hotels disclosed its second POS malware breach in under two years. The breach affected point-of-sale systems at 41 Hyatt hotel properties — primarily restaurants, spas, golf shops, and parking — in 11 countries. Payment card Track 1 and Track 2 data was stolen. Hyatt's first breach in 2015-2016 had affected 250 locations. The repeat breach raised questions about the effectiveness of Hyatt's post-2016 remediation, particularly regarding its third-party POS service providers and network segmentation between payment systems and hotel management systems.",
}),

("Uber.*2017.*GitHub|GitHub.*Uber.*2017", {
    "source_name": "Uber 2016 GitHub AWS Credentials Breach — 57 Million Users and Drivers, CSO Convicted for Cover-Up",
    "source_url": "https://www.ftc.gov/news-events/news/press-releases/2018/10/uber-agrees-expanded-settlement-ftc-related-data-cover",
    "date_of_breach": "2016-10-01",
    "initial_attack_vector": "Attackers found Uber engineer's AWS credentials stored in a private GitHub repository; used credentials to access an S3 bucket with driver database backups",
    "vendor_product": "GitHub (credential storage) / AWS S3 (driver database)",
    "notes": "In October-November 2016, attackers found AWS credentials in Uber's private GitHub repository and used them to access 57 million users' and drivers' data. Uber paid $100K ransom via bug bounty channel and concealed the breach for over a year. Disclosure came in November 2017 after new CEO Dara Khosrowshahi discovered the cover-up. Former CSO Joe Sullivan was convicted in 2022 of obstruction of justice — the first criminal conviction of a corporate security executive for breach concealment. Uber paid $148M to all 50 state AGs. Sullivan sentenced to 3 years probation.",
}),

# ══ 2018 ══
("Applebee.*2018|2018.*Applebee", {
    "source_name": "Applebee's POS Malware Breach — 167 Restaurant Locations, Third-Party POS Provider",
    "source_url": "https://threatpost.com/pos-malware-found-at-160-applebees-restaurant-locations/130281/",
    "date_of_breach": "2018-01-01",
    "initial_attack_vector": "POS malware infected point-of-sale systems at Applebee's restaurant locations; the malware was introduced through a third-party POS service provider with remote access to restaurant terminals",
    "vendor_product": "Third-party POS service provider (unnamed)",
    "malware": "POS RAM-scraping malware",
    "notes": "In early 2018, POS malware was discovered operating at approximately 167 Applebee's and IHOP restaurant locations operated by RMH Franchise Holdings (one of the largest Applebee's franchisees). The malware collected credit and debit card numbers, expiration dates, verification codes, and cardholder names. RMH Franchise Holdings disclosed the breach in March 2018 after investigation. The attack followed a pattern of POS malware campaigns targeting restaurant chains (Arby's in 2016-2017, Chipotle in 2017) through compromised third-party POS support vendors with remote access to restaurant payment systems.",
}),

("Typeform|BestBuy.*Sears.*Kmart.*Delta.*2018", {
    "source_name": "Typeform Survey Platform Breach — BestBuy, Sears/Kmart, Delta, Monzo, British Airways Downstream",
    "source_url": "https://www.typeform.com/blog/human-interest/security-incident/",
    "date_of_breach": "2018-06-27",
    "initial_attack_vector": "Attacker gained access to Typeform's servers and downloaded a partial backup file containing survey responses collected via Typeform's cloud survey platform on behalf of thousands of business clients",
    "vendor_product": "Typeform cloud survey and online form platform",
    "notes": "On 27 June 2018, an attacker accessed Typeform servers and downloaded a partial backup. Typeform notified all affected client organizations on 29 June. Downstream organizations affected included: Best Buy Canada, Sears and Kmart (customer satisfaction surveys), Delta Air Lines, Monzo Bank (nearly 20,000 customers' email addresses and income estimates), British Airways (competition entrants), and dozens of smaller organisations. Each organization separately notified their own customers under GDPR and applicable US laws. The breach highlighted supply chain risk of SaaS survey platforms that concentrate data from thousands of corporate clients — one breach simultaneously exposes data from all clients.",
}),

("Chili.*2018|2018.*Chili", {
    "source_name": "Chili's Grill & Bar POS Malware Breach — Payment Cards at US Locations",
    "source_url": "https://www.foxnews.com/tech/chilis-grill-bar-hit-in-data-breach-company-says",
    "date_of_breach": "2018-03-01",
    "initial_attack_vector": "POS malware operated on Chili's restaurant point-of-sale systems, collecting payment card data from customers who dined at Chili's locations during the March-April 2018 window",
    "vendor_product": "Third-party POS system (unnamed)",
    "malware": "POS malware",
    "notes": "In May 2018, Brinker International (parent company of Chili's Grill & Bar) disclosed that POS malware had operated at some Chili's restaurant locations between late March and early April 2018. Payment card data (numbers, expiration dates, cardholder names) was stolen from customers who paid with cards during dine-in at affected locations. Brinker notified affected customers and offered credit monitoring. The attack was consistent with the broader 2017-2018 wave of restaurant POS malware campaigns. Chili's operates approximately 1,200 company-owned restaurants in the US.",
}),

("Reddit.*Mailgun|Mailgun.*Reddit", {
    "source_name": "Reddit Email Service Third-Party Access via Mailgun API — No User Data Exposed",
    "source_url": "https://www.pymnts.com/news/security-and-risk/2018/reddit-hack-third-party-software-vendor-api-cyberattack/",
    "date_of_breach": "2018-01-01",
    "initial_attack_vector": "A third-party software vendor used by Reddit was compromised; the vendor had API access used to send Reddit transactional emails via Mailgun; no Reddit user accounts or data were accessed through the third party's compromised access",
    "vendor_product": "Mailgun (third-party email delivery API)",
    "notes": "In January 2018, Reddit disclosed that a third-party software vendor's systems had been compromised, but that no Reddit user account data was accessed. The vendor used a Mailgun API integration to send transactional emails on Reddit's behalf. Reddit's disclosure was notable for transparency about the supply chain risk even when no user data was ultimately exposed. Reddit implemented additional vendor security requirements following the incident.",
}),

("Western Union.*2018", {
    "source_name": "Western Union Customer Contact Data Breach via Third-Party Storage Provider",
    "source_url": "https://www.theregister.com/2018/02/13/western_union_storage_hack/",
    "date_of_breach": "2018-01-01",
    "initial_attack_vector": "A third-party data storage provider used by Western Union was compromised; the attacker accessed Western Union customer contact information, bank names, WU internal IDs, and transaction metadata stored by the vendor",
    "vendor_product": "Third-party data storage provider (unnamed)",
    "notes": "In early 2018, Western Union disclosed that a third-party data storage company had been compromised, exposing contact information for an undisclosed number of Western Union customers. Exposed data included customer names, contact information, bank names, Western Union internal ID numbers, transaction amounts, and transaction timestamps. Western Union notified affected customers and regulatory authorities. The incident highlighted the risk of sharing customer financial transaction data with third-party storage vendors without adequate security oversight.",
}),

("Mailchimp.*2022|2022.*Mailchimp|Mailchimp.*Klaviyo|Klaviyo.*Mailchimp", {
    "source_name": "Mailchimp April 2022 Social Engineering Breach — 102 Accounts Exported, Trezor Crypto Phishing Downstream",
    "source_url": "https://mailchimp.com/newsroom/important-update-about-mailchimp-security/",
    "date_of_breach": "2022-04-01",
    "initial_attack_vector": "Attackers used social engineering to compromise Mailchimp employees and contractors, obtaining access to internal admin tools used for customer account management; used access to view 319 accounts and export audience data from 102",
    "vendor_product": "Mailchimp internal admin tool (email marketing platform)",
    "notes": "In April 2022, Mailchimp disclosed a social engineering attack on its employees and contractors that resulted in unauthorized access to 319 customer accounts and data export from 102. The most serious downstream impact: Trezor hardware wallet customer list was accessed and used to send targeted crypto phishing emails directing users to a fake Trezor site to steal seed phrases — a direct cryptocurrency theft attempt. Other affected clients included Fanatics, WooCommerce, and Klaviyo. Mailchimp suffered repeated similar attacks: August 2022 (affecting DigitalOcean, Klaviyo) and January 2023 (133 accounts). The repeated breaches highlighted the fundamental difficulty of protecting SaaS platforms against social engineering targeting support staff with broad customer data access.",
}),

("DigitalOcean.*Mailchimp|Mailchimp.*DigitalOcean", {
    "source_name": "Mailchimp August 2022 Social Engineering Breach — DigitalOcean, Klaviyo, WooCommerce",
    "source_url": "https://mailchimp.com/newsroom/mailchimp-security-incident-august-2022/",
    "date_of_breach": "2022-08-01",
    "initial_attack_vector": "Second Mailchimp social engineering breach in 2022 — attackers again compromised Mailchimp employee access through phishing and social engineering, gaining access to 133 Mailchimp accounts; Mailchimp serves as third-party email infrastructure for thousands of SaaS companies",
    "vendor_product": "Mailchimp email marketing platform (internal admin tools)",
    "notes": "In August 2022 — just four months after the April 2022 Mailchimp breach — Mailchimp suffered a second social engineering attack. Attackers accessed 133 Mailchimp customer accounts. DigitalOcean (cloud computing provider) had its customer email list accessed and used for phishing campaigns targeting DigitalOcean customers. Klaviyo (email marketing competitor) had its email list accessed. The repeated successful attacks against Mailchimp's support organization raised serious questions about the effectiveness of internal security training and access controls. Mailchimp implemented additional authentication requirements and monitoring following the second breach.",
}),

("FanDuel.*Mailchimp|Mailchimp.*FanDuel", {
    "source_name": "FanDuel Customer Data Exposure via Mailchimp January 2023 Breach",
    "source_url": "https://mailchimp.com/newsroom/january-2023-security-incident/",
    "date_of_breach": "2023-01-11",
    "initial_attack_vector": "Third Mailchimp social engineering breach — attackers used social engineering to compromise Mailchimp employee credentials, accessing 133 customer accounts including FanDuel's email list; FanDuel notified customers their name and email addresses had been exposed",
    "vendor_product": "Mailchimp email marketing platform",
    "notes": "In January 2023, Mailchimp suffered its third social engineering breach in under a year — attackers compromised a Mailchimp employee account on 11 January 2023, accessing 133 Mailchimp customer accounts. FanDuel (sports betting platform) was among affected clients, notifying customers that their names and email addresses were exposed via the Mailchimp breach. Solana Foundation also reported its email list was accessed. Mailchimp stated it had immediately identified and ended unauthorized access. The three Mailchimp breaches in 12 months represented a systemic failure in protecting customer data at a major email marketing infrastructure provider.",
}),

("Solana Foundation.*Mailchimp|Mailchimp.*Solana", {
    "source_name": "Solana Foundation Email List Exposed via Mailchimp January 2023 Breach",
    "source_url": "https://mailchimp.com/newsroom/january-2023-security-incident/",
    "date_of_breach": "2023-01-11",
    "initial_attack_vector": "Mailchimp's January 2023 social engineering breach — employee credentials compromised, providing access to Solana Foundation's Mailchimp-hosted email subscriber list",
    "vendor_product": "Mailchimp email marketing platform",
    "notes": "The Solana Foundation — the nonprofit organization supporting development of the Solana blockchain — had its Mailchimp email subscriber list accessed during Mailchimp's January 2023 social engineering breach. Exposed data included email addresses of Solana ecosystem participants who had subscribed to Solana Foundation communications. The foundation notified affected subscribers. The Mailchimp breach affected 133 accounts total, with crypto and financial services organisations disproportionately represented among victims — demonstrating that email marketing platforms serving the crypto sector are high-value social engineering targets.",
}),

("Kaseya|MSP.*Kaseya|Kaseya.*MSP", {
    "source_name": "Kaseya VSA REvil Supply Chain Ransomware — 1,500 Businesses, 17 Countries, $70M Demand",
    "source_url": "https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-200a",
    "date_of_breach": "2021-07-02",
    "initial_attack_vector": "REvil exploited CVE-2021-30116, CVE-2021-30119, CVE-2021-30120 in Kaseya VSA to push malicious script execution to all managed endpoints without authentication; executed over US Independence Day holiday weekend for maximum dwell time",
    "vendor_product": "Kaseya VSA (remote monitoring and management platform for MSPs)",
    "malware": "REvil (Sodinokibi) ransomware",
    "notes": "On 2 July 2021, REvil ransomware exploited zero-day vulnerabilities in Kaseya VSA — a remote monitoring and management platform used by Managed Service Providers (MSPs) — to deploy ransomware to approximately 1,500 businesses across 17 countries via 60 MSPs in under 2 hours. REvil demanded $70M for a universal decryptor or $45K per MSP. Kaseya obtained a universal decryption key (reportedly through FBI / intelligence channels) in July 2021 and distributed it to victims. Multiple arrests followed: Yaroslav Vasinskyi (Ukrainian national) was arrested in 2021 and convicted; $6M in ransom payments were seized by DOJ. The attack demonstrated that RMM platforms used by MSPs represent a critical supply chain chokepoint.",
}),

("SolarWinds|SUNBURST", {
    "source_name": "SolarWinds Orion SUNBURST Supply Chain Attack — Russia SVR, 18,000 Organizations, US Federal Agencies",
    "source_url": "https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-352a",
    "date_of_breach": "2019-10-01",
    "initial_attack_vector": "Russia SVR / APT29 / Cozy Bear compromised SolarWinds Orion software build pipeline and injected SUNBURST backdoor into legitimately signed Orion software updates distributed to ~18,000 organizations",
    "vendor_product": "SolarWinds Orion IT monitoring platform",
    "malware": "SUNBURST, TEARDROP, RAINDROP",
    "notes": "Between October 2019 and June 2020, Russia's SVR foreign intelligence service compromised SolarWinds' Orion IT monitoring platform build pipeline and inserted the SUNBURST backdoor into signed updates distributed to approximately 18,000 customers. Discovered by FireEye on 8 December 2020; publicly disclosed 13 December 2020. From 18,000 initial installs, attackers selected ~100 for deeper compromise including US Treasury, State Department, Homeland Security, Commerce Department, Microsoft, Intel, and Cisco. The attackers used SUNBURST's dormant period (2 weeks after install) and legitimate API calls to blend with normal Orion traffic. CISA Emergency Directive 21-01 ordered immediate disconnection. The breach drove the May 2021 Executive Order on Improving the Nation's Cybersecurity and adoption of zero-trust architecture across the federal government.",
}),

("Accellion", {
    "source_name": "Accellion FTA Zero-Day Cl0p Breach — 100+ Organizations, Law Firms, Universities, Banks",
    "source_url": "https://www.fireeye.com/blog/threat-research/2021/03/accellion-fta-exploited-create-victims.html",
    "date_of_breach": "2020-12-25",
    "initial_attack_vector": "Cl0p ransomware group exploited four zero-day vulnerabilities (CVE-2021-27101 through CVE-2021-27104) in Accellion's 20-year-old File Transfer Appliance (FTA); SQL injection and OS command injection flaws enabled unauthenticated remote code execution and data theft",
    "vendor_product": "Accellion File Transfer Appliance (FTA)",
    "malware": "DEWMODE web shell; Clop ransomware (data exfiltration only)",
    "notes": "Beginning 25 December 2020, Cl0p ransomware exploited zero-days in the Accellion FTA — a legacy managed file transfer appliance — to exfiltrate data from 100+ organizations globally. Cl0p did not encrypt data; it only stole and extorted. Victims included Reserve Bank of New Zealand, ASIC (Australia's securities regulator), Singtel, Stanford University, University of Colorado Boulder, UC Berkeley, University of Miami, Washington State Auditor, Transport for NSW, Qualys, Shell, Bombardier, Jones Day, Goodwin Procter, Allens, and many others. Accellion was actively encouraging migration to its newer Kiteworks platform; many affected organizations had delayed migration. Accellion notified customers on 23 January 2021. The FTC opened a compliance review of Accellion's security practices.",
}),

("MOVEit", {
    "source_name": "MOVEit Transfer Cl0p Zero-Day Mass Exploitation — 2,700+ Organizations, 93 Million Individuals",
    "source_url": "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a",
    "date_of_breach": "2023-05-27",
    "initial_attack_vector": "Cl0p exploited CVE-2023-34362 (SQL injection zero-day in Progress Software MOVEit Transfer web interface) over Memorial Day 2023 weekend; a single HTTP POST to the SFTP file listing function was sufficient to extract customer data from any internet-exposed MOVEit instance",
    "vendor_product": "Progress Software MOVEit Transfer (managed file transfer application)",
    "malware": "Cl0p (data exfiltration only, LEMURLOOT web shell)",
    "notes": "Over Memorial Day 2023 weekend, Cl0p mass-exploited CVE-2023-34362 in Progress Software's MOVEit Transfer, affecting 2,700+ organizations and approximately 93 million individuals — the largest supply chain data breach campaign ever by victim count. Cl0p only exfiltrated; it did not deploy encryption ransomware. Major victims: Shell, British Airways, BBC, Boots UK, US DOE, Oak Ridge National Laboratory, Maximus (11M), Cognizant, EY, PwC, Sony, Siemens Energy, Harvard Pilgrim (2.5M), Louisiana OMV (6M), Oregon DMV (3.5M), Colorado HCPF (4M), and hundreds of healthcare, financial, and government organizations. The US State Department offered $10M for information linking Cl0p to a foreign government. Progress issued emergency patches and multiple follow-on CVEs (CVE-2023-35036, CVE-2023-35708) were subsequently discovered.",
}),

("GoAnywhere|Fortra.*GoAnywhere", {
    "source_name": "Fortra GoAnywhere MFT Zero-Day Cl0p Exploitation — CVE-2023-0669, 130+ Organizations",
    "source_url": "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-158a",
    "date_of_breach": "2023-01-18",
    "initial_attack_vector": "Cl0p exploited CVE-2023-0669, a pre-authentication remote code injection vulnerability in Fortra GoAnywhere MFT's administrative interface; attackers installed a web shell ('Truebot') and exfiltrated data before the vulnerability was publicly known",
    "vendor_product": "Fortra GoAnywhere Managed File Transfer (MFT)",
    "malware": "Cl0p; Truebot web shell",
    "notes": "Beginning 18 January 2023, Cl0p exploited a zero-day (CVE-2023-0669) in Fortra's GoAnywhere MFT, claiming to have breached approximately 130 organizations over 10 days before Fortra issued an emergency patch on 1 February 2023. Major victims: Community Health Systems (1M patients), Rubrik, Hitachi Energy, City of Toronto, Hatch Bank, Saks Fifth Avenue, Procter & Gamble, and many others. Cl0p only stole data — no encryption deployed. The GoAnywhere campaign established Cl0p's template of exploiting enterprise MFT platforms that was later applied at far greater scale with MOVEit (May 2023) and Cleo (December 2024). Healthcare organizations were disproportionately affected.",
}),

("3CX|3CX.*Desktop", {
    "source_name": "3CX Desktop App Supply Chain Attack — Lazarus Group, Financial Sector Stage 2 Targeting",
    "source_url": "https://www.mandiant.com/resources/blog/3cx-software-supply-chain-compromise",
    "date_of_breach": "2023-03-08",
    "initial_attack_vector": "North Korea's Lazarus Group (UNC4736) first compromised Trading Technologies X_TRADER software supply chain, planted a backdoor that infected 3CX employee systems, then compromised 3CX's build environment to trojanize 3CX Desktop App for Windows and macOS; a supply chain attack enabling a second supply chain attack",
    "vendor_product": "3CX Desktop App (VoIP/PBX client software) via Trading Technologies X_TRADER",
    "malware": "SUDDENICON, COLDCAT, ICONIC stealer; SIMPLESEA macOS backdoor",
    "notes": "In March 2023, Lazarus Group conducted a sophisticated double supply chain attack. They first compromised Trading Technologies X_TRADER software (used by financial traders) with malware, infected 3CX employee workstations via X_TRADER, then used that access to compromise 3CX's build environment. 3CX is a major VoIP/PBX vendor with 600,000 customers and 12 million daily users. Trojanized 3CX Desktop App versions (18.12.407 and 18.12.416 for Windows; 18.11.1213 for macOS) were distributed via 3CX's official update mechanism and signed with valid 3CX code signing certificates. The malware beacon staged deployment; Stage 2 targeted specific financial sector organisations. Mandiant and CrowdStrike disclosed the attack. 3CX released a web client as a temporary replacement. The attack demonstrated how threat actors chain supply chain compromises for targeted access.",
}),

("Cleo.*MFT|Cleo.*Clop", {
    "source_name": "Cleo MFT Zero-Day Cl0p Mass Exploitation — CVE-2024-50623/CVE-2024-55956",
    "source_url": "https://www.bleepingcomputer.com/news/security/cl0p-ransomware-claims-responsibility-for-cleo-data-theft-attacks/",
    "date_of_breach": "2024-12-01",
    "initial_attack_vector": "Cl0p exploited CVE-2024-55956 (unauthenticated arbitrary bash shell command execution) in Cleo's LexiCom, VLTransfer, and Harmony managed file transfer products; exploitation began around 3 December 2024, with mass attacks in December 2024",
    "vendor_product": "Cleo LexiCom, VLTransfer, Harmony (MFT products)",
    "malware": "Cl0p; MALICHUS Java backdoor",
    "notes": "In December 2024, Cl0p exploited zero-days in Cleo's managed file transfer products — continuing its campaign of targeting enterprise MFT platforms (GoAnywhere January 2023, MOVEit May 2023, Cleo December 2024). Cleo LexiCom, VLTransfer, and Harmony products were affected. Major victims included Hertz (car rental), TFL (UK transport), and various retail and logistics companies. Cl0p claimed responsibility in January 2025. The exploit allowed unauthenticated remote code execution. Cleo issued patches but exploitation continued against unpatched instances. CISA issued emergency guidance.",
}),

]

def find_match(source_name, filename, notes):
    """Find best matching research entry."""
    for pattern, data in KNOWN:
        if (re.search(pattern, source_name, re.IGNORECASE) or
            re.search(pattern, filename, re.IGNORECASE) or
            re.search(pattern, str(notes)[:200], re.IGNORECASE)):
            return data
    return None


def extract_meta(content):
    """Extract key fields from raw YAML content."""
    fields = {}
    for line in content.split('\n'):
        m = re.match(r'^(\w[\w_]*): (.+)$', line)
        if m:
            fields[m.group(1)] = m.group(2).strip().strip("'\"")
    return fields


def expand_from_meta(fields, filename):
    """Build expanded notes from BlackKite stub metadata."""
    raw_notes = fields.get('notes', '')
    
    # Extract structured data
    company = ''
    data_breached = ''
    third_party_use = ''
    third_party_company = clean(fields.get('vendor_product', ''))
    
    m = re.search(r'for (.+?)\. Data breached:', raw_notes, re.IGNORECASE)
    if m: company = clean(m.group(1))
    
    m = re.search(r'Data breached: (.+?)(?:\. Use of third|$)', raw_notes, re.IGNORECASE)
    if m: data_breached = clean(m.group(1))
    
    m = re.search(r'Use of third party: (.+?)(?:\. Third-party|$)', raw_notes, re.IGNORECASE)
    if m: third_party_use = clean(m.group(1))
    
    m = re.search(r'Third-party company: (.+?)(?:\.|$)', raw_notes, re.IGNORECASE)
    if m:
        tc = clean(m.group(1))
        if tc and tc not in ('Not disclosed', 'Not Disclosed', 'n/a', ''):
            third_party_company = tc
    
    date = fields.get('date_of_breach', '')
    year = date[:4] if date else 'an unknown date'
    
    if not company:
        sn = clean(fields.get('source_name', ''))
        m = re.match(r'^(.+?) Third-Party Breach', sn)
        if m: company = clean(m.group(1))
    
    source_url = fields.get('source_url', '')
    
    parts = []
    if company and data_breached and data_breached.lower() not in ('not disclosed', 'unknown', 'breached', ''):
        parts.append(f"In {year}, {company} experienced a data breach via a third-party vendor, resulting in exposure of {data_breached}.")
    elif company:
        parts.append(f"In {year}, {company} experienced a data security incident via a third-party vendor relationship.")
    
    if third_party_use and third_party_use.lower() not in ('not disclosed', 'unknown', ''):
        if third_party_company and third_party_company.lower() not in ('not disclosed', 'a third-party vendor', 'not disclosed.', ''):
            parts.append(f"The compromised third party was {third_party_company}, providing {third_party_use} services.")
        else:
            parts.append(f"The breach involved a third-party provider of {third_party_use} services.")
    elif third_party_company and third_party_company.lower() not in ('not disclosed', 'a third-party vendor', ''):
        parts.append(f"The compromised third-party vendor was {third_party_company}.")
    
    if source_url:
        parts.append(f"Source reporting: {source_url}")
    
    return ' '.join(parts) if parts else f"Third-party supply chain breach involving {company or 'an organization'} in {year}. BlackKite timeline data: {raw_notes[:300]}"


def rewrite_stub(filepath):
    """Rewrite a BlackKite stub with expanded content."""
    content = filepath.read_text(errors='replace')
    
    if 'Black Kite third-party breach' not in content and 'BlackKite' not in content:
        return 'SKIP'
    
    # Parse fields
    import yaml
    try:
        data = yaml.safe_load(content) or {}
    except Exception:
        data = {}
    
    source_name = clean(data.get('source_name', ''))
    filename = filepath.name
    notes = str(data.get('notes', ''))
    
    # Find research match
    research = find_match(source_name, filename, notes)
    
    if research:
        # Apply full research
        d = dict(data)
        d.update(research)
        # Keep original dates if research doesn't specify
        for date_field in ('date_of_breach', 'date_of_disclosure', 'date_of_customer_notification'):
            if date_field not in research and date_field in data:
                d[date_field] = data[date_field]
        d['category'] = 'supply-chain'
        d['supply_chain_claimed'] = True
        d['cve'] = d.get('cve', [])
        write_yaml(filepath, d)
        return 'RESEARCHED'
    else:
        # Build expanded notes from metadata
        fields = {}
        for k, v in data.items():
            fields[k] = str(v) if v is not None else ''
        
        expanded = expand_from_meta(fields, filename)
        
        d = dict(data)
        d['source_name'] = clean(source_name)
        d['notes'] = expanded
        d['category'] = 'supply-chain'
        d['supply_chain_claimed'] = True
        d['cve'] = d.get('cve', [])
        d['vendor_product'] = clean(d.get('vendor_product', ''))
        write_yaml(filepath, d)
        return 'EXPANDED'


def main():
    import yaml
    stubs = sorted(DATA_DIR.glob("*.yaml"))
    blackkite = [f for f in stubs 
                 if 'Black Kite third-party breach' in f.read_text(errors='replace')
                 or ('BlackKite' in f.read_text(errors='replace') and 'timeline' in f.read_text(errors='replace'))]
    
    print(f"Processing {len(blackkite)} BlackKite stubs...")
    counts = {'RESEARCHED': 0, 'EXPANDED': 0, 'SKIP': 0, 'ERROR': 0}
    
    for fp in blackkite:
        try:
            result = rewrite_stub(fp)
            counts[result] = counts.get(result, 0) + 1
            if result == 'RESEARCHED':
                print(f"  ✓ {fp.name}")
        except Exception as e:
            print(f"  ✗ ERROR {fp.name}: {e}")
            counts['ERROR'] += 1
    
    print(f"\nResults: {counts['RESEARCHED']} researched, {counts['EXPANDED']} expanded, {counts['SKIP']} skipped, {counts['ERROR']} errors")


if __name__ == '__main__':
    main()
