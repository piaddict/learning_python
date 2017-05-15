import os
from urllib.request import urlopen, urlretrieve

from bs4 import BeautifulSoup

downloadDir = "downloaded"
baseUrl = "http://www.pythonscraping.com"


def getAbsURL(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        source = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source

    if baseUrl not in url:
        return None

    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDir):
    try:
        path = absoluteUrl.replace("www", "")
        path = path.replace(baseUrl, "")
        path = downloadDir + path
    except:
        return downloadDir + "except"

    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


# -*- main -*-

html = urlopen(baseUrl)
bsObj = BeautifulSoup(html, "html.parser")
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsURL(baseUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)

urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDir))
