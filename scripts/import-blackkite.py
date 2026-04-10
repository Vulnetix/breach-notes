#!/usr/bin/env python3
"""
Import third-party breach incidents from Black Kite's public timeline page.

Run:
  uv run --with pyyaml --with requests python scripts/import-blackkite.py
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

import requests
import yaml

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
SOURCE_URL = "https://blackkite.com/data-breaches-caused-by-third-parties/"
MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}


def slugify(value: str) -> str:
    value = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return value or "unknown"


def normalize_url(url: str) -> str:
    if not url:
        return ""
    return re.sub(r"/$", "", url.strip())


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


def fetch_blackkite_entries() -> list[dict[str, Any]]:
    resp = requests.get(
        SOURCE_URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; breach-notes-importer/1.0)"},
        timeout=60,
    )
    resp.raise_for_status()

    html = resp.text
    match = re.search(r'yearSections\\":(\[.*?\])\}\]\]', html)
    if not match:
        raise RuntimeError("Could not locate yearSections payload on Black Kite page")

    escaped_json = match.group(1)
    payload = bytes(escaped_json, "utf-8").decode("unicode_escape")
    year_sections = json.loads(payload)

    rows: list[dict[str, Any]] = []
    for year_block in year_sections:
        year = str(year_block.get("year", "")).strip()
        for entry in year_block.get("entries", []):
            rows.append(
                {
                    "year": year,
                    "month": str(entry.get("date", "")).strip(),
                    "company": str(entry.get("company", "")).strip(),
                    "company_link": str(entry.get("companyLink", "")).strip(),
                    "data_breached": str(entry.get("dataBreached", "")).strip(),
                    "use_of_3rd_party": str(entry.get("useOf3rdParty", "")).strip(),
                    "third_party_company": str(entry.get("thirdPartyCompany", "")).strip(),
                }
            )
    return rows


def build_filename(year: str, month: str, company: str, vendor: str) -> Path:
    month_num = MONTHS.get(month.lower(), 1)
    prefix = f"{year}-{month_num:02d}"
    base = f"{prefix}_{slugify(company)}-{slugify(vendor)[:28]}".strip("-")
    path = DATA_DIR / "supply-chain" / f"{base}.yaml"

    if not path.exists():
        return path

    i = 2
    while True:
        alt = DATA_DIR / "supply-chain" / f"{base}-{i}.yaml"
        if not alt.exists():
            return alt
        i += 1


def to_record(entry: dict[str, Any]) -> dict[str, Any]:
    year = entry["year"]
    month_name = entry["month"]
    month_num = MONTHS.get(month_name.lower(), 1)
    date_str = f"{year}-{month_num:02d}-01"

    company = entry["company"] or "Unknown Organization"
    vendor = entry["third_party_company"] or "Third-party vendor"
    source_url = entry["company_link"] or SOURCE_URL

    notes = (
        f"Black Kite third-party breach timeline entry for {company}. "
        f"Data breached: {entry['data_breached'] or 'Unknown'}. "
        f"Use of third party: {entry['use_of_3rd_party'] or 'Unknown'}. "
        f"Third-party company: {vendor}."
    )

    return {
        "source_name": f"{company} Third-Party Breach ({month_name} {year})",
        "source_url": source_url,
        "date_of_breach": date_str,
        "date_of_disclosure": date_str,
        "date_of_customer_notification": "",
        "category": "supply-chain",
        "initial_attack_vector": "Compromise of third-party service provider / vendor relationship",
        "cve": [],
        "vendor_product": vendor,
        "software_package": "",
        "malware": "",
        "supply_chain_claimed": True,
        "notes": notes,
    }


def main() -> None:
    os.chdir(BASE_DIR)
    existing_urls = load_existing_source_urls()
    rows = fetch_blackkite_entries()

    added = 0
    skipped = 0

    for entry in rows:
        if not entry["year"] or not entry["company"]:
            skipped += 1
            continue

        source_url = normalize_url(entry["company_link"])
        if source_url and source_url in existing_urls:
            skipped += 1
            continue

        record = to_record(entry)
        out_path = build_filename(
            entry["year"],
            entry["month"],
            entry["company"],
            entry["third_party_company"],
        )

        out_path.write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True), encoding="utf-8")
        added += 1
        if source_url:
            existing_urls.add(source_url)

    print(f"Black Kite import complete: added={added}, skipped={skipped}, total_rows={len(rows)}")


if __name__ == "__main__":
    main()
