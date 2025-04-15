'''Question-8:
Given a URL, download that and parse 
and download all links inside that page 
    Use ThreadPoolExecutor or ProcessPoolExecutor 
    BeautifulSoup for parsing html, requests for downloading 
'''

import requests
import time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

def download(link):
    print(f"Downloading: {link}")
    time.sleep(3)
    print(f"Done: {link}")

def get_links(url):
    print(f"Fetching page: {url}")
    time.sleep(2)
    response = requests.get(url)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        print(f"Found {len(links)} ")
        return links
    else:
        print("Failed to fetch.")
        return []

if __name__ == "__main__":
    url = "https://www.python.org"
    links = get_links(url)

    with ThreadPoolExecutor() as executor:
        executor.map(download, links)

