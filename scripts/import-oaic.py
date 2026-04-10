#!/usr/bin/env python3
"""
Import Australian mandatory data breach notifications from OAIC.

Sources:
  1. OAIC Investigation & Inquiry Reports — named entities
     https://www.oaic.gov.au/privacy/privacy-assessments-and-decisions/privacy-decisions/Investigation-inquiry-reports
  2. OAIC Enforceable Undertakings — named entities
     https://www.oaic.gov.au/privacy/privacy-assessments-and-decisions/privacy-decisions/enforceable-undertakings
  3. OAIC Named incidents from the NDB quarterly reports (curated list)

Run:
  uv run --with pyyaml --with requests --with beautifulsoup4 \
    python scripts/import-oaic.py
"""

from __future__ import annotations

import re
import time
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
UA = "Mozilla/5.0 (compatible; breach-notes-importer/1.0)"

OAIC_BASE = "https://www.oaic.gov.au"
INVESTIGATION_INDEX = f"{OAIC_BASE}/privacy/privacy-assessments-and-decisions/privacy-decisions/Investigation-inquiry-reports"
UNDERTAKINGS_INDEX = f"{OAIC_BASE}/privacy/privacy-assessments-and-decisions/privacy-decisions/enforceable-undertakings"


# Manually curated large Australian breaches named in OAIC NDB quarterly reports
# that may not have their own investigation/undertaking page.
# (entity, date, individuals_approx, source_url, category, vector, notes)
OAIC_NDB_NAMED = [
    {
        "source_name": "Service NSW Data Breach — Phishing Attack (3.8M Records)",
        "source_url": "https://www.oaic.gov.au/privacy/notifiable-data-breaches/notifiable-data-breaches-publications/notifiable-data-breaches-report-july-to-december-2020",
        "date_of_breach": "2020-03-01",
        "date_of_disclosure": "2020-04-22",
        "category": "credential-theft",
        "initial_attack_vector": "Phishing emails targeting 47 Service NSW staff email accounts, exposing 3.8 million documents containing personal information of approximately 186,000 customers",
        "cve": [],
        "vendor_product": "Service NSW",
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": False,
        "notes": (
            "In March 2020, 47 Service NSW staff email accounts were compromised through "
            "phishing attacks. The breach exposed 3.8 million documents containing personal "
            "information of approximately 186,000 customers, including identity documents, "
            "medical information, and financial records. Service NSW notified the OAIC under "
            "the Notifiable Data Breaches scheme. The NSW Information and Privacy Commission "
            "also investigated. Service NSW invested $45 million AUD in remediation. "
            "Notified to OAIC and reported publicly April 2020."
        ),
    },
    {
        "source_name": "Canva Data Breach — 139 Million Users (2019)",
        "source_url": "https://www.oaic.gov.au/privacy/notifiable-data-breaches",
        "date_of_breach": "2019-05-24",
        "date_of_disclosure": "2019-05-24",
        "category": "data-leak",
        "initial_attack_vector": "SQL injection or credential-based attack on Canva's user database exposing usernames, email addresses, bcrypt-hashed passwords and partial payment card data",
        "cve": [],
        "vendor_product": "Canva",
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": False,
        "notes": (
            "On 24 May 2019, Canva — the Australian graphic design platform — suffered a breach "
            "exposing data of approximately 139 million users globally. The attacker (known as "
            "GnosticPlayers) accessed usernames, real names, email addresses, city/country, and "
            "bcrypt-hashed passwords. Google tokens used for login were exposed in plaintext. "
            "Approximately 78 million users had Gmail addresses. Canva detected the breach in "
            "real time during the attack and forced password resets. Notified to OAIC under NDB scheme."
        ),
    },
    {
        "source_name": "Coles Group Flybuys / Loyalty Member Credential Stuffing Breach",
        "source_url": "https://www.oaic.gov.au/privacy/notifiable-data-breaches/notifiable-data-breaches-publications",
        "date_of_breach": "2020-01-01",
        "date_of_disclosure": "2020-03-01",
        "category": "credential-theft",
        "initial_attack_vector": "Credential stuffing attack against the Flybuys loyalty program, exploiting reused credentials from prior third-party breaches",
        "cve": [],
        "vendor_product": "Flybuys (Coles Group / Wesfarmers)",
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": False,
        "notes": (
            "The Flybuys loyalty program (Coles Group / Wesfarmers joint venture) was targeted "
            "by credential stuffing attacks in early 2020, where attackers used lists of usernames "
            "and passwords from prior breaches to access customer accounts. Affected customers had "
            "Flybuys points stolen or redeemed fraudulently. Notified to OAIC under NDB scheme. "
            "Representative of a broader wave of credential stuffing attacks against Australian "
            "loyalty programs in 2020."
        ),
    },
    {
        "source_name": "MediBEST / Australian Clinical Labs (Medlab Pathology) Data Breach — 223,000 Patients",
        "source_url": "https://www.oaic.gov.au/privacy/privacy-assessments-and-decisions/privacy-decisions/Investigation-inquiry-reports",
        "date_of_breach": "2022-02-01",
        "date_of_disclosure": "2022-11-01",
        "category": "data-leak",
        "initial_attack_vector": "Ransomware attack on Medlab Pathology (Australian Clinical Labs subsidiary) with delayed disclosure of 9+ months",
        "cve": [],
        "vendor_product": "Australian Clinical Labs / Medlab Pathology",
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": False,
        "notes": (
            "In February 2022, Medlab Pathology (a subsidiary of Australian Clinical Labs, one of "
            "Australia's largest pathology providers) suffered a ransomware attack. The breach was "
            "not disclosed publicly until November 2022 — more than 9 months after it occurred — "
            "triggering serious OAIC scrutiny. Approximately 223,000 patients and 2,500 health "
            "professionals had data exposed including highly sensitive pathology and health information. "
            "The delay in notification was a significant regulatory concern and OAIC investigated. "
            "Australian Clinical Labs paid a $1.8 million settlement fine in 2024."
        ),
    },
    {
        "source_name": "Dymocks Booksellers Data Breach — 836,000 Customers",
        "source_url": "https://www.oaic.gov.au/privacy/notifiable-data-breaches",
        "date_of_breach": "2023-07-18",
        "date_of_disclosure": "2023-09-06",
        "category": "data-leak",
        "initial_attack_vector": "Data theft from Dymocks customer loyalty and CRM database; breach originated via a third-party system",
        "cve": [],
        "vendor_product": "Dymocks Booksellers",
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": True,
        "notes": (
            "In September 2023 Dymocks Booksellers notified 836,000 Australian customers that "
            "their data had been stolen and published on criminal forums. The breach occurred "
            "in or around July 2023. Exposed data included names, dates of birth, email and "
            "postal addresses, gender, and membership details. Dymocks attributed the breach "
            "to a third-party system compromise. Notified to OAIC under NDB scheme."
        ),
    },
    {
        "source_name": "HWL Ebsworth Legal — BlackCat/ALPHV Ransomware — 65 Government Agencies",
        "source_url": "https://www.oaic.gov.au/privacy/notifiable-data-breaches",
        "date_of_breach": "2023-04-28",
        "date_of_disclosure": "2023-06-07",
        "category": "ransomware",
        "initial_attack_vector": "BlackCat/ALPHV ransomware group breached HWL Ebsworth law firm, exfiltrating 3.6TB of data affecting 65 Australian government agencies and dozens of corporate clients",
        "cve": [],
        "vendor_product": "HWL Ebsworth Lawyers",
        "software_package": "",
        "malware": "BlackCat/ALPHV ransomware",
        "supply_chain_claimed": True,
        "notes": (
            "On 28 April 2023, the BlackCat (ALPHV) ransomware group breached HWL Ebsworth, "
            "one of Australia's largest law firms. The attackers exfiltrated approximately 3.6TB "
            "of data containing sensitive documents from 65 Australian government agencies, "
            "including the Australian Federal Police, Australian Taxation Office, National Australia "
            "Bank, Westpac, ASIC, and the Department of Home Affairs. After HWL Ebsworth refused "
            "to pay the ransom, BlackCat published the data on its dark web leak site in June 2023. "
            "Multiple NDB notifications were lodged with OAIC. The breach triggered the Australian "
            "Signals Directorate (ASD/ACSC) advisory and an OAIC investigation."
        ),
    },
    {
        "source_name": "TPG Telecom / iiNet Hosted Exchange — 15,000 Business Customer Credentials",
        "source_url": "https://www.oaic.gov.au/privacy/notifiable-data-breaches",
        "date_of_breach": "2022-12-13",
        "date_of_disclosure": "2022-12-13",
        "category": "credential-theft",
        "initial_attack_vector": "Credential stuffing attack against TPG's hosted Exchange email service used by approximately 15,000 iiNet and Westnet business customers",
        "cve": [],
        "vendor_product": "TPG Telecom / iiNet Hosted Exchange",
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": False,
        "notes": (
            "In December 2022, TPG Telecom disclosed that its iiNet and Westnet hosted Exchange "
            "email service for approximately 15,000 business customers had been breached via "
            "credential stuffing. Attackers scanned for accounts used to store cryptocurrency "
            "and financial data. TPG engaged CrowdStrike and notified OAIC under NDB. TPG is "
            "Australia's third-largest telco and the breach raised concerns about business email "
            "security practices for SMBs hosted on telecoms providers."
        ),
    },
    {
        "source_name": "Medibank Private Ransomware — 9.7 Million Customers (2022)",
        "source_url": "https://www.oaic.gov.au/privacy/privacy-assessments-and-decisions/privacy-decisions",
        "date_of_breach": "2022-10-13",
        "date_of_disclosure": "2022-10-26",
        "category": "ransomware",
        "initial_attack_vector": "REvil/REvil-affiliated threat actor accessed Medibank network via stolen contractor credentials (purchased on a Russian dark web forum); used legitimate remote access tool to pivot across the network before exfiltrating data",
        "cve": [],
        "vendor_product": "Medibank Private",
        "software_package": "",
        "malware": "REvil/affiliated ransomware",
        "supply_chain_claimed": False,
        "notes": (
            "In October 2022 Medibank Private, Australia's largest private health insurer, "
            "suffered its most significant cybersecurity breach in Australian corporate history. "
            "Threat actors accessed the network using stolen credentials of a high-privilege "
            "user purchased from a Russian cybercriminal forum. They exfiltrated data belonging "
            "to 9.7 million current and former customers, including 5.1 million Medibank customers, "
            "2.8 million ahm customers, and 1.8 million international customers. The stolen data "
            "included names, birthdates, addresses, phone numbers, email addresses, Medicare numbers, "
            "and highly sensitive health claims data. The attacker demanded AUD $9.7 million ransom "
            "(AUD $1 per customer). Medibank refused. The data was published in batches on a dark "
            "web blog in November 2022. The OAIC launched a formal investigation. The Australian "
            "Federal Police attributed the breach to a Russia-based threat actor with links to the "
            "REvil ransomware group. In 2024, OAIC found Medibank failed to adequately protect data "
            "and Federal Court proceedings were commenced."
        ),
    },
    {
        "source_name": "Optus Data Breach — 9.8 Million Customers (2022)",
        "source_url": "https://www.oaic.gov.au/privacy/privacy-assessments-and-decisions/privacy-decisions",
        "date_of_breach": "2022-09-22",
        "date_of_disclosure": "2022-09-22",
        "category": "data-leak",
        "initial_attack_vector": "Unauthenticated API endpoint on a developer/test environment exposed customer PII without authentication; attacker queried sequentially to exfiltrate 9.8 million records",
        "cve": [],
        "vendor_product": "Optus (Singtel subsidiary)",
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": False,
        "notes": (
            "In September 2022, Optus — Australia's second-largest telecommunications provider — "
            "suffered a massive data breach exposing personal information of 9.8 million current "
            "and former customers. An unauthenticated API endpoint on a developer environment, "
            "accessible from the public internet, allowed an attacker to iterate through customer "
            "records without authentication. Exposed data included names, dates of birth, phone "
            "numbers, email addresses, home addresses, and government identity document numbers "
            "(passport, driver's licence, Medicare numbers). The attacker initially demanded "
            "AUD $1 million in Monero ransom before releasing 10,200 records publicly and then "
            "deleting the demand. OAIC opened a formal investigation. The Australian government "
            "subsequently changed laws to allow telcos to share breach data with banks. Optus "
            "paid AUD $140 million in legal settlements and remediation costs."
        ),
    },
    {
        "source_name": "Latitude Financial Services Data Breach — 14 Million Records (2023)",
        "source_url": "https://www.oaic.gov.au/privacy/privacy-assessments-and-decisions/privacy-decisions",
        "date_of_breach": "2023-03-16",
        "date_of_disclosure": "2023-03-27",
        "category": "data-leak",
        "initial_attack_vector": "Attacker used stolen employee credentials to access Latitude's IT systems, pivoting through a service provider to steal 14 million identity documents and personal records",
        "cve": [],
        "vendor_product": "Latitude Financial Services",
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": True,
        "notes": (
            "In March 2023, Latitude Financial Services — a major Australian consumer finance "
            "company — suffered Australia's largest financial services data breach. An attacker "
            "used stolen employee login credentials to pivot through a third-party service provider "
            "and access 14 million records. The breach exposed approximately 7.9 million Australian "
            "and New Zealand driver's licence numbers, 6.1 million more records including dates of "
            "birth, addresses, and phone numbers, and 53,000 passport numbers. The attacker demanded "
            "ransom; Latitude refused. OAIC and the Australian Securities and Investments Commission "
            "(ASIC) both launched investigations. Latitude faced class action litigation. The "
            "Australian government paid AUD $1 million compensation to affected customers on Latitude's behalf. "
            "OAIC found Latitude failed to protect personal information and ordered remediation."
        ),
    },
    {
        "source_name": "MediSecure E-Prescription Service Ransomware — 12.9 Million Australians",
        "source_url": "https://www.oaic.gov.au/privacy/notifiable-data-breaches",
        "date_of_breach": "2024-04-01",
        "date_of_disclosure": "2024-05-16",
        "category": "ransomware",
        "initial_attack_vector": "Ransomware attack on MediSecure, a government-contracted Australian e-prescription delivery service, resulting in exfiltration of health prescription data for 12.9 million Australians",
        "cve": [],
        "vendor_product": "MediSecure",
        "software_package": "",
        "malware": "Ransomware (group not publicly identified)",
        "supply_chain_claimed": True,
        "notes": (
            "In April/May 2024, MediSecure — a company that provided secure electronic prescription "
            "delivery services under Australian government contract — suffered a ransomware attack. "
            "MediSecure disclosed the breach on 16 May 2024. The attack affected approximately "
            "12.9 million Australians, covering prescriptions dispensed between March 2019 and "
            "November 2023 via the MediSecure platform. A 6.5TB dataset containing prescription "
            "history, patient and prescriber details was stolen. The data included Medicare numbers, "
            "prescription information, and health identifiers. MediSecure entered voluntary "
            "administration in June 2024 as a result of the breach. The Australian Digital Health "
            "Agency confirmed no current prescription data was affected as MediSecure had been "
            "replaced by eRx as the national provider. The Australian Signals Directorate (ASD) "
            "and OAIC both investigated."
        ),
    },
    {
        "source_name": "St Vincent's Health Australia — Cyberattack (2023)",
        "source_url": "https://www.oaic.gov.au/privacy/notifiable-data-breaches",
        "date_of_breach": "2023-12-19",
        "date_of_disclosure": "2024-01-03",
        "category": "data-leak",
        "initial_attack_vector": "Cyberattack on St Vincent's Health Australia IT systems by unknown threat actor, with data stolen from the network",
        "cve": [],
        "vendor_product": "St Vincent's Health Australia",
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": False,
        "notes": (
            "In December 2023, St Vincent's Health Australia — one of the country's largest "
            "not-for-profit health and aged care providers operating hospitals in NSW, VIC, and QLD — "
            "detected a cyberattack in which data was stolen from its network. St Vincent's announced "
            "the attack on 3 January 2024. The full extent of data stolen was not immediately "
            "determined, but the attack affected patient and operational data. The Australian Cyber "
            "Security Centre (ACSC) and OAIC were notified. St Vincent's engaged forensic specialists "
            "to investigate. The attack was notable given St Vincent's serves vulnerable populations "
            "including aged care and mental health patients."
        ),
    },
]


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:90] or "oaic-breach"


def normalize_url(url: str) -> str:
    return re.sub(r"/$", "", (url or "").strip())


def load_existing_source_urls() -> set[str]:
    urls: set[str] = set()
    for path in DATA_DIR.glob("**/*.yaml"):
        if path.name == "recent-breaches.yaml":
            continue
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        src = normalize_url(str(doc.get("source_url", "")))
        if src:
            urls.add(src)
    return urls


def load_existing_names() -> set[str]:
    names: set[str] = set()
    for path in DATA_DIR.glob("**/*.yaml"):
        if path.name == "recent-breaches.yaml":
            continue
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        sn = str(doc.get("source_name", "")).lower()
        notes = str(doc.get("notes", "")).lower()
        vendor = str(doc.get("vendor_product", "")).lower()
        names.add(sn)
        names.add(vendor)
    return names


def build_path(category: str, date_str: str, name: str) -> Path:
    prefix = date_str[:7] if date_str and len(date_str) >= 7 else "0000-00"
    base = f"{prefix}_{slugify(name)}-oaic"
    p = DATA_DIR / category / f"{base}.yaml"
    if not p.exists():
        return p
    i = 2
    while True:
        alt = DATA_DIR / category / f"{base}-{i}.yaml"
        if not alt.exists():
            return alt
        i += 1


def fetch_investigation_pages(session: requests.Session) -> list[dict]:
    """Fetch OAIC investigation report index and individual report pages."""
    records: list[dict] = []

    for index_url in [INVESTIGATION_INDEX, UNDERTAKINGS_INDEX]:
        r = session.get(index_url, timeout=30)
        if r.status_code != 200:
            continue
        soup = BeautifulSoup(r.text, "html.parser")
        links = [
            a["href"] for a in soup.find_all("a", href=True)
            if "/privacy/privacy-assessments-and-decisions/privacy-decisions/" in a["href"]
            and a["href"] != index_url
            and "Investigation-inquiry-reports" in a["href"] or "enforceable-undertakings" in a["href"]
        ]
        # De-dup
        links = list(set(links))

        for link in links:
            url = link if link.startswith("http") else OAIC_BASE + link
            try:
                pr = session.get(url, timeout=30)
                if pr.status_code != 200:
                    continue
                psoup = BeautifulSoup(pr.text, "html.parser")

                title = ""
                h1 = psoup.find("h1")
                if h1:
                    title = h1.get_text(strip=True)
                if not title:
                    continue

                # Get date from meta or content
                date_str = ""
                pub_date = psoup.find("meta", attrs={"name": "publishedDate"})
                if pub_date and pub_date.get("content"):
                    try:
                        from datetime import datetime as dt
                        d = dt.strptime(pub_date["content"].strip(), "%d %B %Y")
                        date_str = d.strftime("%Y-%m-%d")
                    except Exception:
                        pass

                # Extract description/body
                body = ""
                main = psoup.find("main") or psoup.find("div", class_="content") or psoup.find("article")
                if main:
                    # Get first few paragraphs
                    paras = [p.get_text(" ", strip=True) for p in main.find_all("p")[:5] if p.get_text(strip=True)]
                    body = " ".join(paras)[:800]

                records.append({
                    "title": title,
                    "url": url,
                    "date": date_str,
                    "body": body,
                })
                time.sleep(0.3)
            except Exception as e:
                print(f"  Error fetching {url}: {e}")

    return records


def main() -> None:
    existing_urls = load_existing_source_urls()
    existing_names = load_existing_names()
    added = skipped = 0

    session = requests.Session()
    session.headers.update({"User-Agent": UA})

    # Part 1: Curated OAIC NDB named incidents
    print(f"Processing {len(OAIC_NDB_NAMED)} curated OAIC NDB named incidents...")
    for rec in OAIC_NDB_NAMED:
        sn_lower = rec["source_name"].lower()
        vendor_lower = rec.get("vendor_product", "").lower()

        if normalize_url(rec["source_url"]) in existing_urls:
            # Source URL alone is not enough - many point to index pages
            # Check by vendor name instead
            pass

        if vendor_lower in existing_names or any(
            vendor_lower and vendor_lower in n for n in existing_names
        ):
            print(f"  Skipping (exists): {rec['source_name'][:60]}")
            skipped += 1
            continue

        category = rec["category"]
        date_str = rec["date_of_breach"]
        out_path = build_path(category, date_str, rec["source_name"])
        out_path.write_text(yaml.safe_dump(rec, sort_keys=False, allow_unicode=True), encoding="utf-8")
        existing_names.add(sn_lower)
        existing_names.add(vendor_lower)
        print(f"  Created: {out_path.name}")
        added += 1

    # Part 2: OAIC investigation report pages
    print(f"\nFetching OAIC investigation/undertaking index pages...")
    try:
        investigation_recs = fetch_investigation_pages(session)
        print(f"  Found {len(investigation_recs)} investigation pages")
        for irec in investigation_recs:
            title_lower = irec["title"].lower()
            if any(title_lower in n or n in title_lower for n in existing_names if n):
                skipped += 1
                continue
            if normalize_url(irec["url"]) in existing_urls:
                skipped += 1
                continue

            # Try to infer category
            cat = "data-leak"
            for kw, c in [("ransomware", "ransomware"), ("phishing", "credential-theft"),
                          ("credential", "credential-theft"), ("supply chain", "supply-chain")]:
                if kw in irec["body"].lower() or kw in irec["title"].lower():
                    cat = c
                    break

            date_str = irec["date"] or "2020-01-01"

            record = {
                "source_name": f"{irec['title']} (OAIC Investigation)",
                "source_url": irec["url"],
                "date_of_breach": date_str,
                "date_of_disclosure": date_str,
                "date_of_customer_notification": "",
                "category": cat,
                "initial_attack_vector": "See OAIC investigation report",
                "cve": [],
                "vendor_product": irec["title"],
                "software_package": "",
                "malware": "",
                "supply_chain_claimed": False,
                "notes": irec["body"] + f"\n\nSource: OAIC Investigation Report — {irec['url']}",
            }
            out_path = build_path(cat, date_str, irec["title"])
            out_path.write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True), encoding="utf-8")
            existing_urls.add(normalize_url(irec["url"]))
            existing_names.add(title_lower)
            print(f"  Created: {out_path.name}")
            added += 1
    except Exception as e:
        print(f"  Error fetching investigation pages: {e}")

    print(f"\nOAIC import complete: added={added}, skipped={skipped}")


if __name__ == "__main__":
    main()
