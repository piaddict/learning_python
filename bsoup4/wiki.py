import datetime
import random
import re
from urllib import parse
from urllib.request import urlopen

from bs4 import BeautifulSoup

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    url = "http://ko.wikipedia.org" + articleUrl
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


# 최초 페이지에서 출발해서 위키피디아의 링크를 무작위로 선택해 계속 돌아다닌다
links = getLinks(parse.quote("/wiki/케빈_베이컨", ":/"))
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
