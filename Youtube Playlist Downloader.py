from bs4 import BeautifulSoup
from pytube import YouTube
import re

import requests

url = "Your Playlist URl example = https://www.youtube.com/playlist?list=PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj"
r = requests.get(url)
final_url_list = []
data = r.text
soup = BeautifulSoup(data, "lxml")
for link in soup.find_all('a'):
    list_url = link.get('href')
    list_url = re.split("\n", list_url)
    for one_url in list_url:
        if "/watch?v" in one_url:
            final_url_list.append(one_url)

seen = set()
result = []
for item in final_url_list:
    if item not in seen:
        seen.add(item)
        result.append(item)

for item in result[1:]:
    print(item)
    YouTube("https://www.youtube.com"+item).streams.first().download('Download folder location')