from bs4 import BeautifulSoup

import requests

url = "http://www.medindia.net/drug-price/index.asp?alpha="
for join in range(1,1):
    r = requests.get(url+chr(join+64))

    data = r.text
    '''print(data)'''
    soup = BeautifulSoup(data,"html5lib")


    for link in soup.find_all('td'):
        for exp in link.find_all('a'):
            print(exp.get('href'))
