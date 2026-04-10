import xml.etree.ElementTree as ET
import urllib.request
import re
import yaml
import os
from datetime import datetime

os.chdir('/home/chris/GitHub/breach-notes')

def to_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

url = "https://www.breaches.cloud/incidents/index.xml"
print(f"Fetching {url}")

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    xml_data = response.read()

root = ET.fromstring(xml_data)

new_count = 0
for item in root.findall('./channel/item'):
    title = item.find('title').text if item.find('title') is not None else ''
    link = item.find('link').text if item.find('link') is not None else ''
    pubDate = item.find('pubDate').text if item.find('pubDate') is not None else ''
    desc = item.find('description').text if item.find('description') is not None else ''
    
    if not title: continue
    
    # Parse date
    # Format: Sun, 30 Jun 2024 11:08:05 -0400
    try:
        dt = datetime.strptime(pubDate[5:16], "%d %b %Y")
        date_str = dt.strftime("%Y-%m-%d")
        prefix = dt.strftime("%Y-%m")
    except Exception as e:
        date_str = pubDate
        prefix = "YYYY-MM"
    
    # Clean desc
    desc_clean = re.sub(r'<[^>]+>', '', desc).strip()
    
    slug = to_slug(title)
    filename = f"data/other/{prefix}_{slug}.yaml"
    
    # Cloud breaches typically fall under data-leak or credential-theft or other.
    # Let's check existing ones. We will put them in `data-leak` by default unless we see keywords.
    cat = 'data-leak'
    if 'credential' in desc_clean.lower() or 'access key' in desc_clean.lower() or 'password' in desc_clean.lower():
        cat = 'credential-theft'
        
    filename = f"data/{cat}/{prefix}_{slug}.yaml"
    
    if os.path.exists(filename):
        continue
        
    data = {
        'source_name': title + " (Cloud Breach)",
        'source_url': link,
        'date_of_breach': date_str,
        'date_of_disclosure': date_str,
        'category': cat,
        'initial_attack_vector': 'Cloud misconfiguration or credential leak',
        'cve': [],
        'vendor_product': 'Cloud Provider',
        'malware': '',
        'supply_chain_claimed': False,
        'notes': desc_clean + "\n\nSourced from breaches.cloud"
    }
    
    with open(filename, 'w') as f:
        yaml.dump(data, f, sort_keys=False, default_flow_style=False)
        print(f"Created {filename}")
        new_count += 1

print(f"Added {new_count} new incidents from breaches.cloud")
