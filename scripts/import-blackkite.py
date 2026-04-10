import urllib.request
import re
import yaml
import os
import json

os.chdir('/home/chris/GitHub/breach-notes')

def to_slug(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

url = "https://blackkite.com/data-breaches-caused-by-third-parties/"
print(f"Fetching {url}")

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

# The breaches seem to be in self.__next_f.push. We can use a regex to look for typical breach patterns.
# Let's find dates and titles. Often they are next to each other.
# A simpler approach: there's probably a JSON or list of dictionaries somewhere.
# Since we know BlackKite mentions third party breaches, let's search the HTML for some known ones to find the structure.
pass
