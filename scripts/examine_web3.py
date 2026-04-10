import requests
from bs4 import BeautifulSoup
import json
import sys

def examine_data():
    url = "https://www.web3isgoinggreat.com/web1"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find('script', id='__NEXT_DATA__')
    if not script_tag:
        print("Could not find __NEXT_DATA__ script tag")
        return

    data = json.loads(script_tag.string)
    
    def print_keys(d, depth=0):
        if not isinstance(d, dict):
            return
        for k, v in d.items():
            print("  " * depth + k)
            if isinstance(v, dict):
                print_keys(v, depth + 1)
            elif isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
                print("  " * (depth + 1) + "[list of dicts]")
                # print_keys(v[0], depth + 2)
    
    # print_keys(data)
    # Based on the curl output from earlier, I saw "initialData" 
    # Let's see where it is.
    if 'props' in data and 'pageProps' in data['props']:
        pp = data['props']['pageProps']
        print("PageProps keys:", list(pp.keys()))
        if 'initialData' in pp:
            print("InitialData keys:", list(pp['initialData'].keys()))
        else:
            # Let's see if it's directly in pageProps or something else
            for k in pp:
                if isinstance(pp[k], dict):
                    print(f"Key '{k}' is a dict with keys: {list(pp[k].keys())}")

examine_data()
