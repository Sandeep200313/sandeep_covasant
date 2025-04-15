import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import os

url = "https://example.com"  

os.makedirs("downloads", exist_ok=True)

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
links = []

for tag in soup.find_all("a", href=True):
    full_url = urljoin(url, tag["href"])
    if full_url.startswith("http"):
        links.append(full_url)

def download(link):
    try:
        r = requests.get(link, timeout=10)
        name = urlparse(link).netloc.replace(".", "_") + ".html"
        with open(os.path.join("downloads", name), "w", encoding="utf-8") as f:
            f.write(r.text)
        print("Downloaded:", link)
    except:
        print("Failed:", link)

with ThreadPoolExecutor(max_workers=5) as pool:
    pool.map(download, links)
