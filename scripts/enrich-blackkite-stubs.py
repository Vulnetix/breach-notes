#!/usr/bin/env python3
"""
Enrich Black Kite-generated supply-chain stubs using public reporting at source_url.

This script finds records whose notes start with:
  "Black Kite third-party breach timeline entry for ..."

It then attempts to fetch and extract article metadata + summary text and rewrites
notes to include sourced context plus the original Black Kite timeline details.

Run:
  uv run --with pyyaml --with requests --with beautifulsoup4 \
    python scripts/enrich-blackkite-stubs.py

Optional:
  --limit N       Process at most N stub files
  --no-write      Dry run (show summary only)
"""

from __future__ import annotations

import argparse
import json
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

import requests
import yaml
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "supply-chain"
STUB_PREFIX = "Black Kite third-party breach timeline entry for "

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text


def parse_stub_details(notes: str) -> tuple[str, str, str]:
    m = re.search(
        r"Data breached:\s*(.*?)\.\s*Use of third party:\s*(.*?)\.\s*Third-party company:\s*(.*?)\.?$",
        notes,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not m:
        return "Unknown", "Unknown", "Third-party vendor"
    return clean_text(m.group(1)), clean_text(m.group(2)), clean_text(m.group(3))


def normalize_date(value: str) -> str:
    value = (value or "").strip()
    if not value:
        return ""

    value = value.replace("Z", "+00:00")
    # Trim timezone abbreviations if present (e.g., "GMT")
    value = re.sub(r"\s+[A-Z]{2,5}$", "", value)

    for candidate in [value, value.split("T")[0], value.split(" ")[0]]:
        try:
            dt = datetime.fromisoformat(candidate)
            return dt.date().isoformat()
        except Exception:
            pass

    for fmt in (
        "%Y-%m-%d",
        "%B %d, %Y",
        "%b %d, %Y",
        "%d %B %Y",
        "%d %b %Y",
    ):
        try:
            dt = datetime.strptime(value, fmt)
            return dt.date().isoformat()
        except Exception:
            continue

    m = re.search(r"(20\d{2}-\d{2}-\d{2})", value)
    return m.group(1) if m else ""


def find_meta_content(soup: BeautifulSoup, keys: list[tuple[str, str]]) -> str:
    for attr, key in keys:
        tag = soup.find("meta", attrs={attr: key})
        if tag and tag.get("content"):
            return clean_text(tag.get("content", ""))
    return ""


def extract_ldjson_published(soup: BeautifulSoup) -> str:
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = script.string or script.get_text() or ""
        raw = raw.strip()
        if not raw:
            continue
        try:
            data = json.loads(raw)
        except Exception:
            continue

        stack = [data]
        while stack:
            node = stack.pop()
            if isinstance(node, dict):
                for k, v in node.items():
                    lk = str(k).lower()
                    if lk in {"datepublished", "datecreated", "datemodified", "uploadDate".lower()} and isinstance(v, str):
                        normalized = normalize_date(v)
                        if normalized:
                            return normalized
                    if isinstance(v, (dict, list)):
                        stack.append(v)
            elif isinstance(node, list):
                stack.extend(node)

    return ""


def extract_paragraphs_from_html(soup: BeautifulSoup) -> list[str]:
    selectors = [
        "article p",
        "main p",
        ".article-content p",
        ".post-content p",
        ".entry-content p",
    ]

    paragraphs: list[str] = []
    seen: set[str] = set()

    for sel in selectors:
        for p in soup.select(sel):
            txt = clean_text(p.get_text(" ", strip=True))
            if len(txt) < 60:
                continue
            low = txt.lower()
            if any(x in low for x in ["cookie", "subscribe", "advertisement", "newsletter"]):
                continue
            if txt in seen:
                continue
            seen.add(txt)
            paragraphs.append(txt)
        if len(paragraphs) >= 4:
            break

    if not paragraphs:
        for p in soup.find_all("p"):
            txt = clean_text(p.get_text(" ", strip=True))
            if len(txt) < 60:
                continue
            if txt in seen:
                continue
            seen.add(txt)
            paragraphs.append(txt)
            if len(paragraphs) >= 4:
                break

    return paragraphs


def compose_summary(description: str, paragraphs: list[str], max_chars: int = 700) -> str:
    parts: list[str] = []
    total = 0

    if description and len(description.split()) >= 8:
        description = description.rstrip(". ") + "."
        parts.append(description)
        total += len(description) + 1

    for p in paragraphs:
        if description and p[:80].lower() in description.lower():
            continue
        sentence = p.rstrip(". ") + "."
        if total + len(sentence) > max_chars:
            break
        parts.append(sentence)
        total += len(sentence) + 1
        if len(parts) >= 3:
            break

    return clean_text(" ".join(parts))


def parse_jina_markdown(md: str) -> list[str]:
    # Strip common markdown/link noise
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)
    md = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"`([^`]*)`", r"\1", md)

    lines = [clean_text(line) for line in md.splitlines()]
    lines = [ln for ln in lines if ln]

    cleaned: list[str] = []
    for ln in lines:
        if ln.startswith("#"):
            continue
        if ln.startswith("* ") or ln.startswith("*   "):
            continue
        if len(ln) < 60:
            continue
        low = ln.lower()
        if any(x in low for x in ["all rights reserved", "cookie", "sign up", "advertise"]):
            continue
        cleaned.append(ln)
        if len(cleaned) >= 4:
            break

    return cleaned


def fetch_with_jina(session: requests.Session, source_url: str) -> dict[str, str]:
    jina_url = "https://r.jina.ai/http://" + re.sub(r"^https?://", "", source_url.strip())

    # Throttle to avoid 429
    time.sleep(1.15)

    for attempt in range(5):
        try:
            r = session.get(jina_url, headers={"User-Agent": HEADERS["User-Agent"]}, timeout=60)
        except Exception:
            if attempt == 4:
                return {}
            time.sleep(2 + attempt)
            continue

        if r.status_code == 429:
            time.sleep(4 + attempt * 3)
            continue
        if r.status_code != 200:
            return {}

        text = r.text
        title = ""
        published = ""

        m_title = re.search(r"^Title:\s*(.+)$", text, flags=re.MULTILINE)
        if m_title:
            title = clean_text(m_title.group(1))

        m_pub = re.search(r"^Published Time:\s*(.+)$", text, flags=re.MULTILINE)
        if m_pub:
            published = normalize_date(m_pub.group(1))

        md = ""
        marker = "Markdown Content:"
        idx = text.find(marker)
        if idx != -1:
            md = text[idx + len(marker):].strip()

        paragraphs = parse_jina_markdown(md)
        summary = compose_summary("", paragraphs)

        return {
            "title": title,
            "published": published,
            "summary": summary,
            "method": "jina",
        }

    return {}


def fetch_source_context(session: requests.Session, source_url: str) -> dict[str, str]:
    try:
        r = session.get(source_url, headers=HEADERS, timeout=45, allow_redirects=True)
    except Exception:
        return fetch_with_jina(session, source_url)

    if r.status_code != 200 or "html" not in r.headers.get("Content-Type", "").lower():
        return fetch_with_jina(session, source_url)

    soup = BeautifulSoup(r.text, "html.parser")

    title = find_meta_content(
        soup,
        [
            ("property", "og:title"),
            ("name", "twitter:title"),
        ],
    )
    if not title and soup.title and soup.title.string:
        title = clean_text(soup.title.string)

    description = find_meta_content(
        soup,
        [
            ("property", "og:description"),
            ("name", "description"),
            ("name", "twitter:description"),
        ],
    )

    published = find_meta_content(
        soup,
        [
            ("property", "article:published_time"),
            ("name", "article:published_time"),
            ("name", "pubdate"),
            ("name", "date"),
            ("itemprop", "datePublished"),
        ],
    )
    normalized_published = normalize_date(published)
    if not normalized_published:
        t = soup.find("time")
        if t and t.get("datetime"):
            normalized_published = normalize_date(t.get("datetime", ""))
    if not normalized_published:
        normalized_published = extract_ldjson_published(soup)

    paragraphs = extract_paragraphs_from_html(soup)
    summary = compose_summary(description, paragraphs)

    if not summary:
        fallback = fetch_with_jina(session, source_url)
        if fallback:
            if not title:
                title = fallback.get("title", "")
            if not normalized_published:
                normalized_published = fallback.get("published", "")
            summary = fallback.get("summary", "")
            return {
                "title": title,
                "published": normalized_published,
                "summary": summary,
                "method": "direct+jina",
            }

    return {
        "title": title,
        "published": normalized_published,
        "summary": summary,
        "method": "direct",
    }


def build_notes(summary: str, data_breached: str, use_of_3p: str, third_party: str) -> str:
    bits: list[str] = []

    summary = clean_text(summary)
    if summary:
        if not summary.endswith((".", "!", "?")):
            summary += "."
        bits.append(summary)

    bits.append(
        "Black Kite timeline context: "
        f"Data breached: {data_breached or 'Unknown'}. "
        f"Use of third party: {use_of_3p or 'Unknown'}. "
        f"Third-party company: {third_party or 'Third-party vendor'}."
    )

    return clean_text(" ".join(bits))


def iter_stub_files() -> list[Path]:
    paths: list[Path] = []
    for p in sorted(DATA_DIR.glob("*.yaml")):
        try:
            doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        notes = str(doc.get("notes", ""))
        if notes.startswith(STUB_PREFIX):
            paths.append(p)
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich Black Kite stub records")
    parser.add_argument("--limit", type=int, default=0, help="Process at most N files")
    parser.add_argument("--no-write", action="store_true", help="Do not write changes")
    args = parser.parse_args()

    stub_paths = iter_stub_files()
    if args.limit and args.limit > 0:
        stub_paths = stub_paths[: args.limit]

    print(f"Found {len(stub_paths)} Black Kite stubs to process")

    session = requests.Session()
    processed = 0
    updated = 0
    with_summary = 0
    with_published = 0
    failures = 0

    for path in stub_paths:
        processed += 1
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            failures += 1
            print(f"[FAIL] parse error: {path}")
            continue

        source_url = clean_text(str(doc.get("source_url", "")))
        old_notes = str(doc.get("notes", ""))
        data_breached, use_of_3p, third_party = parse_stub_details(old_notes)

        context: dict[str, str] = {}
        if source_url:
            context = fetch_source_context(session, source_url)

        summary = clean_text(context.get("summary", ""))
        published = clean_text(context.get("published", ""))

        if summary:
            with_summary += 1
        if published:
            with_published += 1

        new_notes = build_notes(summary, data_breached, use_of_3p, third_party)

        changed = False
        if new_notes and new_notes != old_notes:
            doc["notes"] = new_notes
            changed = True

        # Improve disclosure date when we can extract a full date.
        if published:
            old_disclosure = clean_text(str(doc.get("date_of_disclosure", "")))
            if old_disclosure != published:
                doc["date_of_disclosure"] = published
                changed = True

        if changed:
            updated += 1
            if not args.no_write:
                path.write_text(
                    yaml.safe_dump(doc, sort_keys=False, allow_unicode=True),
                    encoding="utf-8",
                )

        if processed % 25 == 0:
            print(
                f"Progress: {processed}/{len(stub_paths)} | updated={updated} "
                f"summary={with_summary} published={with_published} failures={failures}"
            )

    print("---")
    print(
        f"Done. processed={processed} updated={updated} "
        f"with_summary={with_summary} with_published={with_published} failures={failures}"
    )


if __name__ == "__main__":
    main()
