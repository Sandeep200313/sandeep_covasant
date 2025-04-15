'''
Question-9:
Given a URL, download that and parse 
and download all links inside that page 
    in asyncio 
    BeautifulSoup for parsing html, requests for downloading
'''
import asyncio
from bs4 import BeautifulSoup
import requests

async def simulate_download(link):
    print(f"Downloading {link}...")
    await asyncio.sleep(3)  
    print(f"Completed {link}")

async def main(url):

    print(f"Fetching {url}")
    await asyncio.sleep(2) 
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        print(f"Found {len(links)} ")
        await asyncio.gather(*(simulate_download(link) for link in links))

if __name__ == "__main__":
    asyncio.run(main("https://www.python.org"))