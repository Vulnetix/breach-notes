#!/usr/bin/env python3
"""
Enrich existing web3isgoinggreat.com YAML files with structured fields
derived from the web3 JSON metadata and body text analysis.

Fields added/updated:
  - financial_loss_usd       (from scamAmountDetails.total)
  - financial_recovered_usd  (from scamAmountDetails.recovered)
  - initial_attack_vector    (derived from collection + filters + body)
  - vendor_product           (from title / shortTitle)
  - blockchain               (from filters.blockchain)
  - supply_chain_claimed     (true for supply-chain category)
  - affected_count           (extracted from body text if present)

Usage:
  uv run --with pyyaml --with requests --with beautifulsoup4 python scripts/enrich-web3isgoinggreat.py
"""

import re
import html
import os
import sys
import time
import json
import yaml
import requests
from bs4 import BeautifulSoup

# ─── helpers ────────────────────────────────────────────────────────────────

def clean_html(raw):
    if not raw:
        return ""
    text = re.sub(r'<[^>]+>', '', raw)
    text = html.unescape(text)
    text = text.replace('\xa0', ' ')
    return text.strip()

def slugify(text):
    text = clean_html(text)
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def fetch_page(cursor=None):
    url = "https://www.web3isgoinggreat.com/web1"
    if cursor:
        url += f"?cursor={cursor}&direction=next"
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
    except Exception as e:
        print(f"  WARN fetch {url}: {e}")
        return [], None
    soup = BeautifulSoup(r.text, 'html.parser')
    tag = soup.find('script', id='__NEXT_DATA__')
    if not tag:
        return [], None
    pp = json.loads(tag.string)['props']['pageProps']
    entries = pp['entries']
    has_next = pp['hasNext']
    cursor_next = entries[-1]['id'] if entries and has_next else None
    return entries, cursor_next

def fetch_all_entries():
    all_entries = []
    cursor = None
    page = 0
    while True:
        page += 1
        entries, cursor = fetch_page(cursor)
        all_entries.extend(entries)
        print(f"  page {page}: {len(entries)} entries (total {len(all_entries)})", flush=True)
        if not cursor:
            break
        time.sleep(0.3)
    return all_entries

# ─── attack vector derivation ────────────────────────────────────────────────

COLLECTION_VECTORS = {
    'flash-loan-attack':   'Flash loan attack on smart contract',
    'rug-pull':            'Exit scam / rug pull',
    'north-korea':         'Nation-state attack (Lazarus/DPRK) — private key or social engineering compromise',
    'domain-attack':       'DNS hijacking / domain takeover (front-end compromise)',
    'address-poisoning':   'Address poisoning attack',
    'oracle-manipulation': 'Oracle price manipulation',
    'withdrawal-limit':    'Withdrawal halt / insolvency',
    'supply-chain-attack': 'Software supply chain attack',
    'ai':                  'AI-assisted attack or AI-generated exploit',
    'zachxbt':             'On-chain theft (attributed by zachxbt)',
    'typos':               'User error / fat-finger trade',
}

BODY_PATTERNS = [
    (r'flash[\s-]loan',                    'Flash loan attack on smart contract'),
    (r'reentrancy',                         'Reentrancy attack on smart contract'),
    (r'oracle[\s\w]*(?:manipulat|attack)',  'Oracle price manipulation'),
    (r'access control',                     'Smart contract access control vulnerability'),
    (r'private[\s-]key[\s\w]*(?:leak|compromise|stolen|exfiltrat)',
                                            'Private key compromise'),
    (r'seed phrase',                        'Seed phrase / wallet compromise'),
    (r'phishing',                           'Phishing attack'),
    (r'social engineering',                 'Social engineering attack'),
    (r'dns hijack|domain hijack|front.?end.{0,30}(compro|attack|hack)',
                                            'DNS hijacking / front-end compromise'),
    (r'address poisoning',                  'Address poisoning attack'),
    (r'governance attack|malicious proposal','Governance attack / malicious on-chain proposal'),
    (r'infinite mint',                      'Infinite mint exploit'),
    (r'bridge exploit|bridge hack|bridge.{0,30}drain',
                                            'Cross-chain bridge exploit'),
    (r'rug.?pull|exit scam|absconded',      'Exit scam / rug pull'),
    (r'ponzi|pyramid scheme',               'Ponzi / pyramid scheme'),
    (r'insider.{0,30}(theft|steal|fraud)',  'Insider theft or fraud'),
    (r'51.{0,5}attack',                     '51% attack / network takeover'),
    (r'sandwich attack|mev bot',            'MEV / sandwich attack'),
    (r'smart contract.{0,40}(bug|vuln|exploit|flaw)',
                                            'Smart contract vulnerability exploit'),
    (r'malicious (code|update|package)',    'Malicious code injection / supply chain'),
]

THEME_VECTORS = {
    'hack':    'Smart contract exploit / hack',
    'scam':    'Cryptocurrency scam / fraud',
    'bug':     'Software bug / unintentional loss',
    'collapse':'Protocol collapse / insolvency',
    'law':     'Regulatory / legal action',
}

def derive_attack_vector(entry):
    collection = entry.get('collection', [])
    filters    = entry.get('filters', {})
    themes     = filters.get('theme', [])
    body       = clean_html(entry.get('body', '')).lower()

    # 1. Specific collection tags win
    for tag, vec in COLLECTION_VECTORS.items():
        if tag in collection:
            return vec

    # 2. Body text patterns
    for pat, vec in BODY_PATTERNS:
        if re.search(pat, body):
            return vec

    # 3. Filter themes as fallback
    for theme in themes:
        if theme in THEME_VECTORS:
            return THEME_VECTORS[theme]

    return ''

# ─── affected count extraction ───────────────────────────────────────────────

COUNT_PATTERNS = [
    r'(\d[\d,\.]+)\s*(million|billion|thousand)?\s*(users|victims|customers|people|wallets|accounts|individuals)',
    r'(\d[\d,]+)\s+(?:users|victims|customers|wallets|accounts)',
]

def extract_affected_count(body):
    for pat in COUNT_PATTERNS:
        m = re.search(pat, body, re.IGNORECASE)
        if m:
            num_str = m.group(1).replace(',', '')
            try:
                num = float(num_str)
                multiplier = m.group(2) or ''
                if multiplier.lower() == 'million':
                    num *= 1_000_000
                elif multiplier.lower() == 'billion':
                    num *= 1_000_000_000
                elif multiplier.lower() == 'thousand':
                    num *= 1_000
                return int(num)
            except ValueError:
                pass
    return None

# ─── vendor product extraction ───────────────────────────────────────────────

def derive_vendor(entry):
    """Use shortTitle or title; strip trailing incident keywords."""
    title = entry.get('shortTitle') or entry.get('title', '')
    title = clean_html(title)
    # Strip trailing generic suffixes like "hacked", "exploit", "hack", "scam"
    title = re.sub(
        r'\s+(hack(?:ed)?|exploit(?:ed)?|scam|rug[\s-]pull|collapses?|shuts?\s+down|loses?\s+.+|suffers?.+|breach).*$',
        '', title, flags=re.IGNORECASE
    ).strip()
    return title[:120] if title else ''

# ─── file matching ────────────────────────────────────────────────────────────

def entry_candidate_paths(entry):
    """Return list of (dir, filename) candidates this entry might live in."""
    date_str = entry.get('date', '')
    if not date_str:
        return []
    month_prefix = date_str[:7]   # YYYY-MM
    short = entry.get('shortTitle') or entry.get('title', '')
    slug  = slugify(short)

    dirs = {
        'supply-chain': 'supply-chain',
        'hack':         'data-leak',
        'scam':         'other',
        'rug-pull':     'other',
        'bug':          'other',
        'collapse':     'other',
    }
    themes = entry.get('filters', {}).get('theme', [])
    collections = entry.get('collection', [])

    cat_dirs = set()
    if 'supply-chain-attack' in collections:
        cat_dirs.add('supply-chain')
    for t in themes:
        if t in dirs:
            cat_dirs.add(dirs[t])
    if not cat_dirs:
        cat_dirs.add('other')

    candidates = []
    for d in cat_dirs:
        candidates.append((d, f"{month_prefix}_{slug}.yaml"))
    # Also check 'data-leak' and 'other' regardless
    for d in ('data-leak', 'other', 'supply-chain'):
        candidates.append((d, f"{month_prefix}_{slug}.yaml"))
    return candidates

# ─── URL-based index for fast lookup ─────────────────────────────────────────

def build_url_index(category_dirs):
    """Index all existing YAML files by source_url for fast matching."""
    idx = {}   # url -> filepath
    for d in category_dirs:
        for fn in os.listdir(d):
            if not fn.endswith('.yaml'):
                continue
            fp = os.path.join(d, fn)
            try:
                with open(fp) as f:
                    data = yaml.safe_load(f)
                url = data.get('source_url', '')
                if url:
                    idx[url.strip()] = fp
            except Exception:
                pass
    return idx

# ─── YAML load/save ──────────────────────────────────────────────────────────

def load_yaml(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f) or {}

def save_yaml(path, data):
    # Preserve field order sensibly
    FIELD_ORDER = [
        'source_name', 'source_url', 'date_of_breach', 'date_of_disclosure',
        'date_of_customer_notification', 'category', 'initial_attack_vector',
        'cve', 'vendor_product', 'software_package', 'malware',
        'supply_chain_claimed', 'blockchain', 'financial_loss_usd',
        'financial_recovered_usd', 'affected_count', 'notes',
    ]
    ordered = {}
    for k in FIELD_ORDER:
        if k in data:
            ordered[k] = data[k]
    for k, v in data.items():
        if k not in ordered:
            ordered[k] = v
    with open(path, 'w') as f:
        yaml.dump(ordered, f, sort_keys=False, allow_unicode=True,
                  default_flow_style=False, width=120)

# ─── enrichment logic ─────────────────────────────────────────────────────────

CATEGORY_DIRS = ['data-leak', 'other', 'supply-chain', 'ransomware', 'credential-theft']

def enrich_entry(entry, url_idx):
    """Find the YAML file for this entry and enrich it. Returns True if updated."""
    date_str = entry.get('date', '')
    links    = entry.get('links', [])
    scam     = entry.get('scamAmountDetails', {})

    # --- Find the file ---
    filepath = None

    # 1. Try URL match via first link href
    for lnk in links:
        href = lnk.get('href', '').strip()
        if href and href in url_idx:
            filepath = url_idx[href]
            break

    # 2. Try slug-based filename match
    if not filepath:
        for d, fn in entry_candidate_paths(entry):
            p = os.path.join(d, fn)
            if os.path.exists(p):
                filepath = p
                break

    if not filepath:
        return False, 'not_found'

    # --- Load existing data ---
    try:
        existing = load_yaml(filepath)
    except Exception as e:
        return False, f'yaml_error: {e}'

    changed = False
    body = clean_html(entry.get('body', ''))

    # financial_loss_usd
    total = scam.get('total', 0)
    if total and total > 0 and not existing.get('financial_loss_usd'):
        existing['financial_loss_usd'] = int(total)
        changed = True

    # financial_recovered_usd
    recovered = scam.get('recovered', 0)
    try:
        recovered = int(recovered or 0)
    except (TypeError, ValueError):
        recovered = 0
    if recovered > 0 and not existing.get('financial_recovered_usd'):
        existing['financial_recovered_usd'] = int(recovered)
        changed = True

    # initial_attack_vector
    if not existing.get('initial_attack_vector'):
        vec = derive_attack_vector(entry)
        if vec:
            existing['initial_attack_vector'] = vec
            changed = True

    # vendor_product
    if not existing.get('vendor_product'):
        vp = derive_vendor(entry)
        if vp:
            existing['vendor_product'] = vp
            changed = True

    # blockchain
    blockchains = entry.get('filters', {}).get('blockchain', [])
    if blockchains and not existing.get('blockchain'):
        existing['blockchain'] = ', '.join(blockchains)
        changed = True

    # supply_chain_claimed
    cat = existing.get('category', '')
    if cat == 'supply-chain' and 'supply_chain_claimed' not in existing:
        existing['supply_chain_claimed'] = True
        changed = True

    # affected_count
    if not existing.get('affected_count') and body:
        count = extract_affected_count(body)
        if count and count >= 10:
            existing['affected_count'] = count
            changed = True

    if changed:
        save_yaml(filepath, existing)
        return True, filepath
    return False, filepath

# ─── main ─────────────────────────────────────────────────────────────────────

def main():
    print("Building URL index from existing YAML files…")
    url_idx = build_url_index(CATEGORY_DIRS)
    print(f"  Indexed {len(url_idx)} files by source_url")

    print("\nFetching all entries from web3isgoinggreat.com…")
    all_entries = fetch_all_entries()
    print(f"  Total entries: {len(all_entries)}")

    updated   = 0
    not_found = 0
    errors    = 0

    print(f"\nEnriching {len(all_entries)} entries…")
    for i, entry in enumerate(all_entries):
        ok, info = enrich_entry(entry, url_idx)
        if ok:
            updated += 1
            if updated <= 20 or updated % 200 == 0:
                print(f"  [{updated}] Updated {info}")
        elif info == 'not_found':
            not_found += 1
        elif info.startswith('yaml_error'):
            errors += 1
            print(f"  ERROR {info}")

    print(f"\nDone.")
    print(f"  Updated:   {updated}")
    print(f"  Not found: {not_found}")
    print(f"  Errors:    {errors}")

if __name__ == '__main__':
    main()
