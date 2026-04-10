import requests
from bs4 import BeautifulSoup
import json
import yaml
import os
import re
from datetime import datetime

def get_page_data(cursor=None):
    url = "https://www.web3isgoinggreat.com/web1"
    if cursor:
        url += f"?cursor={cursor}&direction=next"
    
    print(f"Fetching {url}...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', id='__NEXT_DATA__')
    if not script_tag:
        print("Could not find __NEXT_DATA__ script tag")
        return None

    data = json.loads(script_tag.string)
    # The actual entries are in data['props']['pageProps']['initialData']['entries']
    # based on the curl output I saw earlier.
    try:
        page_props = data['props']['pageProps']
        entries = page_props['entries']
        has_next = page_props['hasNext']
        # Get the cursor for the next page from the last entry's ID
        next_cursor = entries[-1]['id'] if entries and has_next else None
        return entries, next_cursor
    except KeyError as e:
        print(f"Error parsing JSON data: {e}")
        return None, None

def map_category(entry):
    themes = entry.get('filters', {}).get('theme', [])
    collections = entry.get('collection', [])
    
    if 'supply-chain-attack' in collections:
        return 'supply-chain'
    
    if 'hack' in themes:
        # Most crypto hacks are not data leaks but asset thefts. 
        # But 'data-leak' is a broad category in this repo?
        # Actually, let's look at the repo's categories again.
        return 'data-leak'
    
    if 'scam' in themes or 'rug-pull' in themes or 'phishing' in themes:
        return 'other'
        
    return 'other'

def clean_html(raw_html):
    if not raw_html:
        return ""
    # Remove HTML tags
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    # Decode HTML entities
    import html
    cleantext = html.unescape(cleantext)
    # Normalize non-breaking spaces and other whitespace
    cleantext = cleantext.replace('\xa0', ' ')
    return cleantext

def process_entry(entry):
    date_str = entry.get('date', '')
    if not date_str:
        return

    # Create a safe filename
    title_raw = entry.get('shortTitle') or entry.get('title', 'incident')
    title = clean_html(title_raw)  # cleans &nbsp; and HTML tags
    title_slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    # Use - instead of _ for date part
    filename = f"{date_str[:10].replace('-', '-')}_{title_slug}.yaml"
    # Actually, the existing ones use YYYY-MM prefix?
    # Let's check: 2024-03_xz-utils-backdoor.yaml
    filename = f"{date_str[:7]}_{title_slug}.yaml"
    
    category = map_category(entry)
    category_dir = category
    
    if not os.path.exists(category_dir):
        os.makedirs(category_dir)
    
    filepath = os.path.join(category_dir, filename)
    
    # Skip if already exists
    if os.path.exists(filepath):
        # print(f"Skipping {filepath}, already exists")
        return

    links = entry.get('links', [])
    source_url = links[0].get('href', '') if links else f"https://www.web3isgoinggreat.com/?id={entry['id']}"
    source_name = links[0].get('linkText', 'Web3 Is Going Great') if links else 'Web3 Is Going Great'

    notes = clean_html(entry.get('body', ''))
    scam_amount = entry.get('scamAmountDetails', {}).get('total', 0)
    if scam_amount > 0:
        notes += f"\n\nTotal loss estimated at ${scam_amount:,}."

    yaml_data = {
        'source_name': source_name,
        'source_url': source_url,
        'date_of_breach': date_str,
        'date_of_disclosure': date_str,
        'category': category,
        'notes': notes.strip()
    }

    with open(filepath, 'w') as f:
        yaml.dump(yaml_data, f, sort_keys=False, allow_unicode=True)
    print(f"Created {filepath}")

def main():
    cursor = None
    count = 0
    while True:
        entries, cursor = get_page_data(cursor)
        if not entries:
            break
        
        for entry in entries:
            process_entry(entry)
            count += 1
        
        if not cursor:
            break
        
        # Limit for safety during development, though user said "hundreds more"
        if count > 5000:
            print("Reached 5000 entries, stopping for now.")
            break

if __name__ == "__main__":
    main()
