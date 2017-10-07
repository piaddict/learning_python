from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getLinks(articleUrl):
    url = "http://ko.wikipedia.org" + articleUrl
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks(parse.quote("/wiki/케빈_베이컨", ":/"))
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
