import datetime
import random
import re
from urllib import parse
from urllib.request import urlopen

from bs4 import BeautifulSoup

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    url = "http://ko.wikipedia.org" + articleUrl
    print(parse.quote(url, ":/"))
    html = urlopen(parse.quote(url, ":/"))
    bsObj = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/케빈_베이컨")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
