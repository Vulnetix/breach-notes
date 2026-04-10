#!/usr/bin/env python3
"""
Import incident-like articles from DataBreachToday article sitemaps.

Run:
  uv run --with pyyaml --with requests --with beautifulsoup4 \
    python scripts/import-databreachtoday.py --max-new 300
"""

from __future__ import annotations

import argparse
import re
import time
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
    "incident",
]

URL_HINT_TERMS = [
    "breach",
    "ransomware",
    "hack",
    "leak",
    "stolen",
    "compromise",
    "malware",
    "extortion",
    "phishing",
    "cyberattack",
    "cyber-attack",
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


def get(session: requests.Session, url: str, retries: int = 2) -> Optional[str]:
    for attempt in range(retries):
        try:
            resp = session.get(url, timeout=25)
            if resp.status_code == 200:
                return resp.text
            if resp.status_code in (403, 429):
                time.sleep(0.8 + attempt)
                continue
        except Exception:
            time.sleep(0.8 + attempt)
    return None


def parse_date(text: str) -> Optional[str]:
    text = (text or "").strip()
    try:
        return datetime.strptime(text, "%B %d, %Y").strftime("%Y-%m-%d")
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


def collect_article_urls(session: requests.Session) -> list[str]:
    html = get(session, SITEMAP_INDEX)
    if not html:
        return []

    sitemap_urls = sorted(set(re.findall(r"https://www\.databreachtoday\.com/articles-sitemap\d+\.html", html)))

    article_urls: set[str] = set()
    for sitemap in sitemap_urls:
        page = get(session, sitemap)
        if not page:
            continue
        urls = re.findall(r"https://www\.databreachtoday\.com/[^\"<]+-a-\d+", page)
        article_urls.update(urls)
        time.sleep(0.15)

    def extract_id(url: str) -> int:
        m = re.search(r"-a-(\d+)$", url)
        return int(m.group(1)) if m else 0

    # Pre-filter by URL slug terms so we do not fetch all 20k articles.
    filtered = []
    for url in article_urls:
        slug = url.split('.com/', 1)[1].rsplit('-a-', 1)[0].lower()
        if any(term in slug for term in URL_HINT_TERMS):
            filtered.append(url)

    return sorted(filtered, key=extract_id, reverse=True)


def should_keep(title: str, description: str) -> bool:
    hay = f"{title} {description}".lower()
    return any(term in hay for term in INCIDENT_TERMS)


def parse_article(html: str) -> tuple[str, str, Optional[str]]:
    soup = BeautifulSoup(html, "html.parser")

    title = ""
    t = soup.select_one("h1.article-title")
    if t:
        title = t.get_text(" ", strip=True)
    if not title:
        og = soup.find("meta", attrs={"property": "og:title"})
        if og and og.get("content"):
            title = og["content"].strip()
    if not title and soup.title:
        title = soup.title.get_text(" ", strip=True).replace(" - DataBreachToday", "")

    description = ""
    d = soup.find("meta", attrs={"name": "description"})
    if d and d.get("content"):
        description = d["content"].strip()

    date_text = None
    byline_date = soup.select_one("span.article-byline span.text-nowrap")
    if byline_date:
        date_text = byline_date.get_text(" ", strip=True)

    return title, description, parse_date(date_text or "")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-new", type=int, default=300)
    parser.add_argument("--max-fetch", type=int, default=3000)
    args = parser.parse_args()

    session = requests.Session()
    session.headers.update({"User-Agent": UA})

    existing_urls = load_existing_source_urls()
    article_urls = collect_article_urls(session)

    added = 0
    fetched = 0
    skipped = 0

    for url in article_urls:
        if added >= args.max_new or fetched >= args.max_fetch:
            break

        normalized = normalize_url(url)
        if normalized in existing_urls:
            skipped += 1
            continue

        page = get(session, url)
        fetched += 1
        if fetched % 100 == 0:
            print(f"Fetched {fetched} article pages, current added={added}, skipped={skipped}")
        if not page:
            skipped += 1
            continue

        title, description, date_str = parse_article(page)
        if not title or not date_str:
            skipped += 1
            continue

        if not should_keep(title, description):
            skipped += 1
            continue

        article_id_match = re.search(r"-a-(\d+)$", url)
        article_id = int(article_id_match.group(1)) if article_id_match else 0

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

        out_path = build_filename(category, date_str, title, article_id)
        out_path.write_text(yaml.safe_dump(record, sort_keys=False, allow_unicode=True), encoding="utf-8")

        existing_urls.add(normalized)
        added += 1

        if added % 25 == 0:
            print(f"Added {added} entries so far...")

        time.sleep(0.08)

    print(
        f"DataBreachToday import complete: added={added}, fetched={fetched}, skipped={skipped}, "
        f"candidate_urls={len(article_urls)}"
    )


if __name__ == "__main__":
    main()
