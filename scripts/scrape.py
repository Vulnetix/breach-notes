import requests
from bs4 import BeautifulSoup
import json
import yaml
import os
import re
from datetime import datetime

os.chdir('/home/chris/GitHub/breach-notes')

def to_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def create_yaml(data):
    cat = data.get('category', 'other')
    if cat not in ['ransomware', 'data-leak', 'supply-chain', 'credential-theft', 'other']:
        cat = 'other'
    
    date_str = data.get('date_of_breach', '')
    if not date_str:
        return
        
    try:
        dt = datetime.strptime(date_str, '%Y-%M-%d') if len(date_str) == 10 else datetime.strptime(date_str[:7], '%Y-%m')
        prefix = dt.strftime('%Y-%m')
    except:
        prefix = date_str[:7]
        
    slug = to_slug(data.get('source_name', 'unknown'))
    filename = f"data/{cat}/{prefix}_{slug}.yaml"
    
    if os.path.exists(filename):
        return
        
    with open(filename, 'w') as f:
        yaml.dump(data, f, sort_keys=False, default_flow_style=False)
        print(f"Created {filename}")

def scrape_breaches_cloud():
    print("Scraping breaches.cloud...")
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        r = requests.get('https://www.breaches.cloud/incidents/', headers=headers)
        if r.status_code != 200:
            print("Failed to fetch breaches.cloud")
            return
            
        soup = BeautifulSoup(r.text, 'html.parser')
        # This is a guess on structure, will need to refine based on actual output
        for article in soup.find_all('article'):
            title = article.find('h2') or article.find('h3')
            title_text = title.text.strip() if title else ''
            
            date_el = article.find('time')
            date_str = date_el['datetime'] if date_el and date_el.has_attr('datetime') else ''
            
            link = article.find('a')
            url = 'https://www.breaches.cloud' + link['href'] if link and link.has_attr('href') else ''
            
            if not title_text: continue
            
            create_yaml({
                'source_name': title_text,
                'source_url': url,
                'date_of_breach': date_str,
                'date_of_disclosure': date_str,
                'category': 'credential-theft', # defaults for cloud
                'initial_attack_vector': 'Cloud misconfiguration or credential leak',
                'cve': [],
                'vendor_product': 'Cloud Provider',
                'malware': '',
                'supply_chain_claimed': False,
                'notes': title_text + ' (Sourced from breaches.cloud)'
            })
    except Exception as e:
        print(f"Error breaches.cloud: {e}")

scrape_breaches_cloud()
