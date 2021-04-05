from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.crunchyroll.com/videos/anime').text
soup = BeautifulSoup(source, 'lxml')
thumblist = []
titlelist = []
clink = []
coverimg = []
description = []

for thumbnail in soup.find_all("span", class_="img-holder"):
  thumblist.append(thumbnail.img['src'])

for title in soup.find_all("span", itemprop="name"):
  titlelist.append(title.text)

for link in soup.find_all("div", class_="wrapper hover-toggle-queue container-shadow hover-classes"):
  clink.append(f"https://www.crunchyroll.com{link.a['href']}")

for i in clink:
  source = requests.get(i).text
  soup2 = BeautifulSoup(source, 'lxml')
  k = soup2.find("div", id="sidebar")
  coverimg.append(k.img['src'])
  f = soup2.find("span", class_="more")
  if(f):
    description.append(f.text)
  else:
    description.append(soup2.find("span", class_="trunc-desc").text)

