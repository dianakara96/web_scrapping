import requests
from bs4 import BeautifulSoup
import csv

zindua = requests.get('https://zinduaschool.com/')
src = zindua.content


soup = BeautifulSoup(src, 'lxml')
links = soup.find_all('a')

zindua_urls = [] 
for link in links:
    url = link.get('href')
    if 'zindua' in url:
        zindua_urls.append(url)

csv_file_path = 'urls/zindua.csv'

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    csv_writer.writerow(['Zindua links'])
    for url in zindua_urls:
        csv_writer.writerow([url])

print(f"zindua links saved to '{csv_file_path}'")