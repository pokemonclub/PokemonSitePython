import urllib.request
from urllib.request import Request, urlopen

import time
from bs4 import BeautifulSoup

link = "https://pokemondb.net/pokedex/bulbasaur"
request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(request).read().decode("utf-8")
soup = BeautifulSoup(page)
while "Rowlett" not in soup.find_all("title")[0].text:
    name = soup.find_all("title")[0].text.partition(' ')[0].lower()
    save_link = "html/" + name + ".html"
    file = open(save_link, "w")
    file.write(page)
    file.close()
    name = soup.find(rel="next").get("href")
    link = "https://pokemondb.net" + name
    request = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(request).read().decode("utf-8")
    soup = BeautifulSoup(page)