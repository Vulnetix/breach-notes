#!/usr/bin/env python3
"""
Import HIPAA breach notifications from the HHS OCR "Wall of Shame" portal.
https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf

The portal lists all HIPAA breaches affecting ≥500 individuals.
We navigate the JSF session flow, then paginate through all records.
Only Hacking/IT Incidents with ≥500 individuals are imported as incidents;
other types (Loss, Theft of device, Paper) are skipped unless ≥10,000 individuals.

Run:
  uv run --with pyyaml --with requests --with beautifulsoup4 \
    python scripts/import-hhs-ocr.py
"""

from __future__ import annotations

import re
import time
import html as html_module
from datetime import datetime
from pathlib import Path

import requests
import yaml

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
SOURCE_PORTAL = "https://ocrportal.hhs.gov"
UA = "Mozilla/5.0 (compatible; breach-notes-importer/1.0)"

# Minimum individuals to include for non-hacking breach types
HACK_MIN = 500
OTHER_MIN = 10_000


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value[:80] or "unknown"


def normalize_url(url: str) -> str:
    return re.sub(r"/$", "", (url or "").strip())


def clean_html(s: str) -> str:
    s = re.sub(r"<[^>]+>", "", s)
    return html_module.unescape(s).strip()


def load_existing_names() -> set[str]:
    """Return a set of lower-case entity names already in our dataset."""
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
        if sn:
            names.add(sn)
        # Also index by first 60 chars of source_name (after stripping common suffixes)
        core = re.sub(r"\s*\(hipaa breach.*\).*$", "", sn, flags=re.I).strip()
        if core:
            names.add(core)
    return names


def parse_rows(html_text: str) -> list[dict]:
    """Extract breach rows from an HTML/XML response body."""
    rows = re.findall(r'data-ri="\d+".*?</tr>', html_text, re.DOTALL)
    results = []
    for row in rows:
        cells = re.findall(r"<td[^>]*>(.*?)</td>", row, re.DOTALL)
        if len(cells) < 8:
            continue
        record = {
            "name": clean_html(cells[1]),
            "state": clean_html(cells[2]),
            "covered_entity_type": clean_html(cells[3]),
            "individuals": clean_html(cells[4]).replace(",", ""),
            "date_submitted": clean_html(cells[5]),  # MM/DD/YYYY
            "breach_type": clean_html(cells[6]),
            "location": clean_html(cells[7]),
        }
        if len(cells) > 8:
            record["under_investigation"] = clean_html(cells[8])
        results.append(record)
    return results


def infer_category(breach_type: str, location: str) -> str:
    bt = breach_type.lower()
    lo = location.lower()
    if "ransomware" in bt or "ransomware" in lo:
        return "ransomware"
    if "hacking" in bt or "it incident" in bt:
        return "data-leak"
    if "unauthorized" in bt:
        return "data-leak"
    return "data-leak"


def infer_vector(breach_type: str, location: str) -> str:
    bt = breach_type.lower()
    lo = location.lower()
    if "hacking" in bt:
        if "email" in lo:
            return "Phishing or business email compromise targeting healthcare email accounts"
        if "network server" in lo:
            return "Hacking/IT incident targeting network server infrastructure"
        if "electronic medical record" in lo:
            return "Unauthorized access to electronic medical record system"
        return f"Hacking/IT incident ({location})"
    if "unauthorized access" in bt:
        return f"Unauthorized access or disclosure ({location})"
    if "ransomware" in bt:
        return "Ransomware attack on healthcare systems"
    if "loss" in bt:
        return f"Loss of device or media containing PHI ({location})"
    if "theft" in bt:
        return f"Theft of device or media containing PHI ({location})"
    return f"{breach_type} ({location})"


def build_filename(category: str, date_str: str, name: str) -> Path:
    prefix = date_str[:7]
    base = f"{prefix}_{slugify(name)}-hipaa-breach"
    path = DATA_DIR / category / f"{base}.yaml"
    if not path.exists():
        return path
    i = 2
    while True:
        p = DATA_DIR / category / f"{base}-{i}.yaml"
        if not p.exists():
            return p
        i += 1


def to_record(row: dict, submission_date: str) -> dict:
    name = row["name"]
    state = row["state"]
    entity_type = row["covered_entity_type"]
    individuals = row["individuals"]
    breach_type = row["breach_type"]
    location = row["location"]
    is_ba = "business associate" in entity_type.lower()

    category = infer_category(breach_type, location)
    vector = infer_vector(breach_type, location)

    notes = (
        f"{name} ({state}), a {entity_type}, submitted a HIPAA breach notification to the "
        f"HHS Office for Civil Rights (OCR) on {submission_date} for a breach affecting "
        f"{individuals} individuals. Breach type: {breach_type}. "
        f"Information location: {location}. "
        f"{'This was reported by a Business Associate on behalf of a covered entity. ' if is_ba else ''}"
        f"Source: HHS OCR Breach Portal (HIPAA Breach Notification Rule, 45 CFR §164.400–414). "
        f"The OCR portal lists all breaches of unsecured protected health information (PHI) "
        f"affecting 500 or more individuals."
    )

    return {
        "source_name": f"{name} HIPAA Breach Notification ({submission_date[:7] if len(submission_date) >= 7 else submission_date})",
        "source_url": "https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf",
        "date_of_breach": "",
        "date_of_disclosure": submission_date,
        "date_of_customer_notification": "",
        "category": category,
        "initial_attack_vector": vector,
        "cve": [],
        "vendor_product": name,
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": is_ba,
        "notes": notes,
    }


def make_session() -> tuple[requests.Session, str]:
    """Establish a fresh session and navigate to the report page. Returns (session, view_state)."""
    s = requests.Session()
    s.headers.update({"User-Agent": UA})

    # Step 1: GET breach_report.jsf → redirects to breach_frontpage.jsf
    r1 = s.get(f"{SOURCE_PORTAL}/ocr/breach/breach_report.jsf", timeout=30, allow_redirects=True)
    vs = re.findall(r'value="([-\d:]+)"', r1.text)
    vs = vs[-1] if vs else ""

    # Step 2: POST "View HIPAA Breach Reports" button (j_idt39)
    r2 = s.post(
        f"{SOURCE_PORTAL}/ocr/breach/breach_frontpage.jsf",
        data={
            "ocrForm": "ocrForm",
            "javax.faces.ViewState": vs,
            "ocrForm:j_idt39": "ocrForm:j_idt39",
        },
        timeout=30,
        allow_redirects=True,
    )

    # Step 3: GET breach_report_hip.jsf (may have been followed by allow_redirects)
    if "breach_report_hip" not in r2.url:
        r3 = s.get(f"{SOURCE_PORTAL}/ocr/breach/breach_report_hip.jsf", timeout=30)
    else:
        r3 = r2

    vs4 = re.findall(r'value="([-\d:]+)"', r3.text)
    vs4 = vs4[-1] if vs4 else ""
    return s, r3.text, vs4


def fetch_page(session: requests.Session, vs: str, first: int, rows: int = 100) -> str:
    r = session.post(
        f"{SOURCE_PORTAL}/ocr/breach/breach_report_hip.jsf",
        headers={
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Faces-Request": "partial/ajax",
            "X-Requested-With": "XMLHttpRequest",
        },
        data=(
            "javax.faces.partial.ajax=true"
            "&javax.faces.source=ocrForm%3AreportResultTable"
            "&javax.faces.partial.execute=ocrForm%3AreportResultTable"
            "&javax.faces.partial.render=ocrForm%3AreportResultTable"
            "&ocrForm%3AreportResultTable=ocrForm%3AreportResultTable"
            "&ocrForm%3AreportResultTable_pagination=true"
            f"&ocrForm%3AreportResultTable_first={first}"
            f"&ocrForm%3AreportResultTable_rows={rows}"
            "&ocrForm%3AreportResultTable_encodeFeature=true"
            "&ocrForm=ocrForm"
            f"&javax.faces.ViewState={requests.utils.quote(vs)}"
        ),
        timeout=60,
    )
    return r.text


def parse_date_mdy(date_str: str) -> str:
    """Convert MM/DD/YYYY to YYYY-MM-DD."""
    try:
        return datetime.strptime(date_str.strip(), "%m/%d/%Y").strftime("%Y-%m-%d")
    except Exception:
        return date_str


def should_include(row: dict) -> bool:
    bt = row["breach_type"].lower()
    try:
        n = int(row["individuals"])
    except ValueError:
        return False
    if n < HACK_MIN:
        return False
    is_hack = "hacking" in bt or "it incident" in bt or "ransomware" in bt or "unauthorized" in bt
    if is_hack:
        return n >= HACK_MIN
    # Non-hacking (Loss, Theft of device, etc.) — only include large ones
    return n >= OTHER_MIN


def main() -> None:
    print("Establishing HHS OCR session...")
    session, page1_html, vs = make_session()

    if not vs:
        print("ERROR: could not obtain ViewState from report page")
        return

    # Get total count
    rc_match = re.search(r"rowCount:(\d+)", page1_html)
    total = int(rc_match.group(1)) if rc_match else 0
    print(f"Total records on portal: {total}")

    existing_names = load_existing_names()
    all_rows: list[dict] = parse_rows(page1_html)

    page = 1
    first = 100
    while first < total:
        print(f"Fetching page {page + 1} (rows {first}–{min(first+100, total)})...")
        page_html = fetch_page(session, vs, first)
        if "<redirect" in page_html[:200]:
            print("  Session expired, re-establishing...")
            session, page1_html, vs = make_session()
            page_html = fetch_page(session, vs, first)
        new_rows = parse_rows(page_html)
        all_rows.extend(new_rows)
        first += 100
        page += 1
        time.sleep(0.4)

    print(f"Fetched {len(all_rows)} total rows from portal")

    added = skipped_existing = skipped_threshold = 0

    for row in all_rows:
        if not should_include(row):
            skipped_threshold += 1
            continue

        name_lower = row["name"].lower()
        core = re.sub(r"\s*\(hipaa breach.*\).*$", "", name_lower, flags=re.I).strip()

        if name_lower in existing_names or core in existing_names:
            skipped_existing += 1
            continue

        date_submitted = parse_date_mdy(row["date_submitted"])
        category = infer_category(row["breach_type"], row["location"])
        record = to_record(row, date_submitted)

        out_path = build_filename(category, date_submitted, row["name"])
        out_path.write_text(
            yaml.safe_dump(record, sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )

        existing_names.add(name_lower)
        if core:
            existing_names.add(core)
        added += 1

        if added % 50 == 0:
            print(f"  Added {added} records so far...")

    print(
        f"\nHHS OCR import complete:"
        f"  added={added}"
        f"  skipped_already_covered={skipped_existing}"
        f"  skipped_below_threshold={skipped_threshold}"
        f"  total_portal_records={len(all_rows)}"
    )


if __name__ == "__main__":
    main()
