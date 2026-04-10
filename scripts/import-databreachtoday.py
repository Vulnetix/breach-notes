#!/usr/bin/env python3
"""
Import incident-focused entries from DataBreachToday article sitemaps.

Run:
  uv run --with pyyaml --with requests --with beautifulsoup4 \
    python scripts/import-databreachtoday.py --max-new 250
"""

from __future__ import annotations

import argparse
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests
import yaml
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
SITEMAP_INDEX = "https://www.databreachtoday.com/sitemap.html"
UA = "Mozilla/5.0 (compatible; breach-notes-importer/1.0)"

INCIDENT_TERMS = [
    "breach",
    "ransomware",
    "hacked",
    "hack",
    "leak",
    "stolen",
    "compromise",
    "compromised",
    "cyberattack",
    "cyber attack",
    "malware",
    "extortion",
    "data theft",
    "phishing",
]


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "incident"


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


def fetch_text(session: requests.Session, url: str, timeout: int = 20) -> Optional[str]:
    try:
        r = session.get(url, timeout=timeout)
        if r.status_code == 200:
            return r.text
    except Exception:
        return None
    return None


def parse_date(date_text: str) -> Optional[str]:
    date_text = (date_text or "").strip()
    try:
        return datetime.strptime(date_text, "%B %d, %Y").strftime("%Y-%m-%d")
    except Exception:
        return None


def infer_category(text: str, url: str) -> tuple[str, bool, str]:
    hay = f"{text} {url}".lower()
    supply_chain = any(x in hay for x in ["third-party", "third party", "vendor", "supply chain", "moveit"])

    if any(x in hay for x in ["ransomware", "lockbit", "clop", "conti", "blackcat", "alphv", "bianlian"]):
        return "ransomware", supply_chain, "Ransomware intrusion"
    if supply_chain:
        return "supply-chain", True, "Third-party / vendor compromise"
    if any(x in hay for x in ["credential", "password", "phishing", "account", "token", "login"]):
        return "credential-theft", supply_chain, "Credential theft or account compromise"
    if any(x in hay for x in ["breach", "leak", "stolen", "exposed", "compromise", "hack"]):
        return "data-leak", supply_chain, "Unauthorized access / data exposure"
    return "other", supply_chain, "Cybersecurity incident under investigation"


def build_filename(category: str, date_str: str, title: str, article_id: int) -> Path:
    prefix = date_str[:7]
    base = f"{prefix}_{slugify(title)[:70]}"
    path = DATA_DIR / category / f"{base}.yaml"
    if not path.exists():
        return path

    alt = DATA_DIR / category / f"{base}-a{article_id}.yaml"
    if not alt.exists():
        return alt

    i = 2
    while True:
        p = DATA_DIR / category / f"{base}-a{article_id}-{i}.yaml"
        if not p.exists():
            return p
        i += 1


def article_id(url: str) -> int:
    m = re.search(r"-a-(\d+)$", url)
    return int(m.group(1)) if m else 0


def collect_candidates(session: requests.Session) -> list[tuple[str, str]]:
    html = fetch_text(session, SITEMAP_INDEX, timeout=30)
    if not html:
        return []

    sitemap_urls = sorted(set(re.findall(r"https://www\.databreachtoday\.com/articles-sitemap\d+\.html", html)))

    pairs: list[tuple[str, str]] = []
    for idx, sitemap in enumerate(sitemap_urls, start=1):
        page = fetch_text(session, sitemap, timeout=30)
        if not page:
            continue

        entries = re.findall(r'<a href="(https://www\.databreachtoday\.com/[^\"]+-a-\d+)">([^<]+)</a>', page)
        for url, title in entries:
            low = title.lower()
            if any(term in low for term in INCIDENT_TERMS):
                pairs.append((url, title.strip()))

        print(f"Sitemap {idx}/{len(sitemap_urls)} parsed, candidate count={len(pairs)}")
        time.sleep(0.1)

    dedup = {(u, t) for u, t in pairs}
    return sorted(dedup, key=lambda x: article_id(x[0]), reverse=True)


def fetch_article_metadata(session: requests.Session, url: str) -> Optional[dict]:
    html = fetch_text(session, url, timeout=20)
    if not html:
        return None

    soup = BeautifulSoup(html, "html.parser")

    title = ""
    t = soup.select_one("h1.article-title")
    if t:
        title = t.get_text(" ", strip=True)
    if not title:
        meta_title = soup.find("meta", attrs={"property": "og:title"})
        if meta_title and meta_title.get("content"):
            title = meta_title["content"].strip()

    if not title:
        return None

    description = ""
    d = soup.find("meta", attrs={"name": "description"})
    if d and d.get("content"):
        description = d["content"].strip()

    byline_date = soup.select_one("span.article-byline span.text-nowrap")
    date = parse_date(byline_date.get_text(" ", strip=True) if byline_date else "")
    if not date:
        return None

    return {
        "url": url,
        "title": title,
        "description": description,
        "date": date,
        "article_id": article_id(url),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-new", type=int, default=250)
    parser.add_argument("--max-candidates", type=int, default=800)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    session = requests.Session()
    session.headers.update({"User-Agent": UA})

    existing_urls = load_existing_source_urls()
    candidates = collect_candidates(session)

    candidates = [(u, t) for (u, t) in candidates if normalize_url(u) not in existing_urls]
    candidates = candidates[: args.max_candidates]

    print(f"Fetching metadata for {len(candidates)} candidate articles...")

    added = 0
    processed = 0

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {ex.submit(fetch_article_metadata, session, url): (url, title) for url, title in candidates}

        for fut in as_completed(futures):
            processed += 1
            result = fut.result()
            if not result:
                if processed % 100 == 0:
                    print(f"Processed {processed}/{len(candidates)} (added={added})")
                continue

            url = result["url"]
            normalized = normalize_url(url)
            if normalized in existing_urls:
                continue

            title = result["title"]
            description = result["description"]
            date_str = result["date"]

            category, supply_chain, vector = infer_category(f"{title} {description}", url)

            record = {
                "source_name": f"{title} (DataBreachToday)",
                "source_url": url,
                "date_of_breach": date_str,
                "date_of_disclosure": date_str,
                "date_of_customer_notification": "",
                "category": category,
                "initial_attack_vector": vector,
                "cve": re.findall(r"CVE-\d{4}-\d{4,7}", f"{title} {description}", flags=re.I),
                "vendor_product": "",
                "software_package": "",
                "malware": "",
                "supply_chain_claimed": bool(supply_chain),
                "notes": f"{description}\n\nSource: DataBreachToday article coverage.",
            }

            out_path = build_filename(category, date_str, title, result["article_id"])
            out_path.write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True), encoding="utf-8")

            existing_urls.add(normalized)
            added += 1

            if added % 25 == 0:
                print(f"Added {added} records...")

            if added >= args.max_new:
                break

            if processed % 100 == 0:
                print(f"Processed {processed}/{len(candidates)} (added={added})")

    print(f"DataBreachToday import complete: added={added}, processed={processed}, candidates={len(candidates)}")


if __name__ == "__main__":
    main()
