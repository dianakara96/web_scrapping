import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.freecodecamp.org/'
response = requests.get(url)

if response.status_code == 200:
    soup =  BeautifulSoup(response.content, 'lxml')

    links = soupy.find_all('a', href=True)

    filtered_urls = []

    for link in links:
        url = link.get('href')

        if url and 'camp' in url:
            filtered_urls.append(url)

    if filtered_urls:
        print("Filtered urls containing 'camp' ")   