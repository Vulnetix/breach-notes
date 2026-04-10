#!/usr/bin/env python3
"""
Enrich BlackKite-derived supply-chain records with details from source reporting.

Targets records that still look templated/generic (legacy BlackKite stub notes,
BlackKite marker text, or the generic initial_attack_vector placeholder), then:
  - fetches source_url content (direct fetch, with r.jina.ai fallback)
  - extracts a concise summary + publish date where possible
  - rewrites notes with richer context
  - updates date_of_disclosure when a better publication date is found

Run:
  uv run --with pyyaml --with requests --with beautifulsoup4 \
    python scripts/enrich-blackkite-stubs.py

Options:
  --limit N       process at most N candidates
  --offset N      skip first N candidates
  --no-write      dry run
"""

from __future__ import annotations

import argparse
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "supply-chain"

LEGACY_PREFIX = "Black Kite third-party breach timeline entry for "
GENERIC_MARKER = "Source: BlackKite third-party breach timeline."
GENERIC_VECTOR = "Compromise of third-party service provider / vendor relationship"

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

BLOCK_TERMS = [
    "access denied",
    "enable javascript",
    "request rate has exceeded",
    "captcha",
    "cloudflare",
    "verify you are human",
    "bot detection",
    "temporarily unavailable",
]

_last_jina_call = 0.0


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def looks_like_block_page(text: str) -> bool:
    low = (text or "").lower()
    return any(term in low for term in BLOCK_TERMS)


def normalize_date(value: str) -> str:
    value = clean_text(value)
    if not value:
        return ""

    value = value.replace("Z", "+00:00")
    value = re.sub(r"\s+[A-Z]{2,5}$", "", value)

    # Common exact parses
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
            return clean_text(tag["content"])
    return ""


def extract_ldjson_published(soup: BeautifulSoup) -> str:
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = (script.string or script.get_text() or "").strip()
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
                    if isinstance(v, (dict, list)):
                        stack.append(v)
                    elif isinstance(v, str):
                        if str(k).lower() in {"datepublished", "datecreated", "datemodified", "uploaddate"}:
                            out = normalize_date(v)
                            if out:
                                return out
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

    def push(txt: str) -> None:
        txt = clean_text(txt)
        if len(txt) < 70:
            return
        low = txt.lower()
        if looks_like_block_page(low):
            return
        if any(x in low for x in ["cookie", "subscribe", "newsletter", "advertisement"]):
            return
        if txt in seen:
            return
        seen.add(txt)
        paragraphs.append(txt)

    for sel in selectors:
        for p in soup.select(sel):
            push(p.get_text(" ", strip=True))
        if len(paragraphs) >= 5:
            break

    if not paragraphs:
        for p in soup.find_all("p"):
            push(p.get_text(" ", strip=True))
            if len(paragraphs) >= 5:
                break

    return paragraphs[:5]


def compose_summary(description: str, paragraphs: list[str], max_chars: int = 850) -> str:
    parts: list[str] = []
    total = 0

    description = clean_text(description)
    if description and len(description.split()) >= 8 and not looks_like_block_page(description):
        sentence = description.rstrip(". ") + "."
        parts.append(sentence)
        total += len(sentence) + 1

    for p in paragraphs:
        if description and p[:90].lower() in description.lower():
            continue
        sentence = p.rstrip(". ") + "."
        if total + len(sentence) > max_chars:
            break
        parts.append(sentence)
        total += len(sentence) + 1
        if len(parts) >= 3:
            break

    summary = clean_text(" ".join(parts))
    if looks_like_block_page(summary):
        return ""
    return summary


def parse_jina_markdown(md: str) -> list[str]:
    md = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", md)
    md = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"`([^`]*)`", r"\1", md)

    lines = [clean_text(line) for line in md.splitlines()]
    lines = [ln for ln in lines if ln]

    out: list[str] = []
    for ln in lines:
        if ln.startswith("#"):
            continue
        if ln.startswith("* ") or ln.startswith("*   "):
            continue
        if len(ln) < 70:
            continue
        low = ln.lower()
        if looks_like_block_page(low):
            continue
        if any(x in low for x in ["all rights reserved", "sign up", "advertise", "newsletter"]):
            continue
        out.append(ln)
        if len(out) >= 5:
            break

    return out


def fetch_with_jina(session: requests.Session, source_url: str) -> dict[str, str]:
    global _last_jina_call

    jina_url = "https://r.jina.ai/http://" + re.sub(r"^https?://", "", source_url.strip())

    # Gentle throttle to avoid 429 from r.jina.ai
    wait = max(0.0, 1.3 - (time.time() - _last_jina_call))
    if wait > 0:
        time.sleep(wait)

    for attempt in range(5):
        try:
            r = session.get(jina_url, headers={"User-Agent": HEADERS["User-Agent"]}, timeout=65)
        except Exception:
            if attempt == 4:
                return {}
            time.sleep(2 + attempt)
            continue
        finally:
            _last_jina_call = time.time()

        if r.status_code == 429:
            time.sleep(5 + attempt * 4)
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
        r = session.get(source_url, headers=HEADERS, timeout=50, allow_redirects=True)
    except Exception:
        return fetch_with_jina(session, source_url)

    content_type = r.headers.get("Content-Type", "").lower()
    if r.status_code != 200 or "html" not in content_type or looks_like_block_page(r.text[:5000]):
        return fetch_with_jina(session, source_url)

    soup = BeautifulSoup(r.text, "html.parser")

    title = find_meta_content(soup, [("property", "og:title"), ("name", "twitter:title")])
    if not title and soup.title and soup.title.string:
        title = clean_text(soup.title.string)

    description = find_meta_content(
        soup,
        [("property", "og:description"), ("name", "description"), ("name", "twitter:description")],
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
    published = normalize_date(published)

    if not published:
        t = soup.find("time")
        if t and t.get("datetime"):
            published = normalize_date(t.get("datetime", ""))
    if not published:
        published = extract_ldjson_published(soup)

    paragraphs = extract_paragraphs_from_html(soup)
    summary = compose_summary(description, paragraphs)

    if not summary:
        fallback = fetch_with_jina(session, source_url)
        if fallback:
            return {
                "title": title or fallback.get("title", ""),
                "published": published or fallback.get("published", ""),
                "summary": clean_text(fallback.get("summary", "")),
                "method": "direct+jina",
            }

    return {
        "title": title,
        "published": published,
        "summary": summary,
        "method": "direct",
    }


def parse_blackkite_context(doc: dict) -> tuple[str, str, str, str]:
    """
    Return (company, data_breached, use_of_3p, third_party).
    """
    notes = str(doc.get("notes", ""))
    source_name = clean_text(str(doc.get("source_name", "")))
    vendor_product = clean_text(str(doc.get("vendor_product", ""))) or "Third-party vendor"

    company = source_name.split(" Third-Party Breach")[0] if " Third-Party Breach" in source_name else source_name
    data_breached = "Unknown"
    use_of_3p = "Unknown"
    third_party = vendor_product

    # Legacy direct BlackKite stub text
    m = re.search(
        r"Data breached:\s*(.*?)\.\s*Use of third party:\s*(.*?)\.\s*Third-party company:\s*(.*?)\.?$",
        notes,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if m:
        data_breached = clean_text(m.group(1))
        use_of_3p = clean_text(m.group(2))
        third_party = clean_text(m.group(3)) or third_party
        return company, data_breached, use_of_3p, third_party

    # Generic converted template
    m = re.search(r"resulting in exposure of\s*(.*?)\.\s", notes, flags=re.IGNORECASE | re.DOTALL)
    if m:
        data_breached = clean_text(m.group(1))

    m = re.search(
        r"The compromised third party was\s*(.*?),\s*which provided\s*(.*?)\s*services\.",
        notes,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if m:
        third_party = clean_text(m.group(1)) or third_party
        use_of_3p = clean_text(m.group(2)) or use_of_3p
    else:
        m2 = re.search(
            r"The breach occurred through a third-party vendor providing\s*(.*?)\s*services\.",
            notes,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if m2:
            use_of_3p = clean_text(m2.group(1))

    return company, data_breached, use_of_3p, third_party


def is_blackkite_candidate(doc: dict) -> bool:
    notes = str(doc.get("notes", ""))
    vec = clean_text(str(doc.get("initial_attack_vector", "")))

    if notes.startswith(LEGACY_PREFIX):
        return True
    if GENERIC_MARKER in notes:
        return True
    if vec == GENERIC_VECTOR and str(doc.get("category", "")) == "supply-chain":
        return True
    return False


def is_placeholder_date(value: str) -> bool:
    value = clean_text(value)
    return bool(re.match(r"^\d{4}-\d{2}-01$", value))


def is_plausible_disclosure_date(doc: dict, published: str) -> bool:
    published = clean_text(published)
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", published):
        return False

    pub_year = int(published[:4])
    this_year = datetime.now(timezone.utc).year
    if pub_year > this_year + 1:
        return False

    breach = clean_text(str(doc.get("date_of_breach", "")))
    if re.match(r"^\d{4}-\d{2}-\d{2}$", breach):
        breach_year = int(breach[:4])
        if pub_year < breach_year - 1 or pub_year > breach_year + 2:
            return False

    return True


def build_notes(summary: str, data_breached: str, use_of_3p: str, third_party: str) -> str:
    bits: list[str] = []

    summary = clean_text(summary)
    if summary:
        if not summary.endswith((".", "!", "?")):
            summary += "."
        bits.append(summary)

    if data_breached and data_breached.lower() != "unknown":
        bits.append(f"Reported impact included: {data_breached}.")
    if use_of_3p and use_of_3p.lower() != "unknown":
        bits.append(f"Third-party involvement: {use_of_3p}.")
    if third_party and third_party.lower() not in {"", "unknown", "third-party vendor", "not disclosed"}:
        bits.append(f"Third-party company: {third_party}.")

    if not bits:
        bits.append("BlackKite timeline indicates a third-party/vendor-related breach; detailed reporting was not accessible automatically.")

    return clean_text(" ".join(bits))


def iter_candidate_paths() -> list[Path]:
    out: list[Path] = []
    for p in sorted(DATA_DIR.glob("*.yaml")):
        try:
            doc = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        if is_blackkite_candidate(doc):
            out.append(p)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich BlackKite-derived records")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--no-write", action="store_true")
    args = parser.parse_args()

    paths = iter_candidate_paths()
    total_candidates = len(paths)

    if args.offset > 0:
        paths = paths[args.offset :]
    if args.limit > 0:
        paths = paths[: args.limit]

    print(f"Candidates found: {total_candidates}; processing: {len(paths)}")

    session = requests.Session()

    processed = 0
    updated = 0
    with_summary = 0
    with_published = 0
    source_failures = 0

    for path in paths:
        processed += 1

        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        except Exception:
            source_failures += 1
            print(f"[FAIL] parse: {path}")
            continue

        source_url = clean_text(str(doc.get("source_url", "")))
        old_notes = str(doc.get("notes", ""))

        company, data_breached, use_of_3p, third_party = parse_blackkite_context(doc)

        context = {}
        if source_url:
            context = fetch_source_context(session, source_url)

        title = clean_text(context.get("title", ""))
        summary = clean_text(context.get("summary", ""))
        published = clean_text(context.get("published", ""))

        if title and summary and title.lower() not in summary.lower():
            summary = f"{title}. {summary}"

        if summary:
            with_summary += 1
        if published:
            with_published += 1

        new_notes = build_notes(summary, data_breached, use_of_3p, third_party)

        changed = False
        if new_notes and new_notes != old_notes:
            doc["notes"] = new_notes
            changed = True

        # Update disclosure date only when we got a plausible full date and
        # the existing value looks like a placeholder.
        if published and is_plausible_disclosure_date(doc, published):
            old_disclosure = clean_text(str(doc.get("date_of_disclosure", "")))
            if (not old_disclosure or is_placeholder_date(old_disclosure)) and old_disclosure != published:
                doc["date_of_disclosure"] = published
                changed = True

        # Keep company name from source_name if possible; we do not rewrite naming fields here.
        _ = company

        if changed:
            updated += 1
            if not args.no_write:
                path.write_text(
                    yaml.safe_dump(doc, sort_keys=False, allow_unicode=True),
                    encoding="utf-8",
                )

        if processed % 25 == 0:
            print(
                f"Progress: {processed}/{len(paths)} | updated={updated} "
                f"summary={with_summary} published={with_published} fail={source_failures}"
            )

    print("---")
    print(
        f"Done. processed={processed} updated={updated} "
        f"with_summary={with_summary} with_published={with_published} failures={source_failures}"
    )


if __name__ == "__main__":
    main()
