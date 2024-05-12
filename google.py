import requests
from bs4 import BeautifulSoup


result = requests.get('http://github.com/')
google = requests.get('https://www.google.com/')
jumia = requests.get('https://www.jumia.co.ke/')

# print(result.status_code)
# print(google.status_code)

src = google.content
#print(src)
soup = BeautifulSoup(src, 'lxml')
links = soup.find_all('a')
# print(links)
for link in links:
    url = link.get('href')
    if 'google' in url:
        # link_text = link.text
        print(f'URL: {url}')
