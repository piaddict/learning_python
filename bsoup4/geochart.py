import random

import datetime
import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki)((?!:).)*$"))


def getHistoryIps(pageUrl):
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is :" + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, "html.parser")

    ipAddresses = bsObj.findAll("a", {"class": "mw-anonuserlink"})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


# __main__

links = getLinks("/wiki/Python_(programming_language)")

while (len(links) > 0):
    for link in links:
        print("-")
        historyIPs = getHistoryIps(link.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP)

# newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
# links = getLinks(newLink)
