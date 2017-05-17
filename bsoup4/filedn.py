import os
import traceback
from urllib.request import urlopen, urlretrieve

from bs4 import BeautifulSoup


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
    # if baseUrl not in url:
    #     return None
    print("absURL은 : " + url)
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDir):
    try:
        path = absoluteUrl
        path = path.replace(baseUrl.replace("www.", ""), "")
        path = path.replace("http:", "")
        path = path[:path.find("?")]
        path = downloadDir + "/" + path
        print("경로는 : " + path)
    except:
        traceback.print_exc()
        return downloadDir + "/" + "except"
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


if __name__ == "__main__":
    downloadDir = "downloaded"
    baseUrl = "http://www.pythonscraping.com"
    html = urlopen(baseUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    downloadList = bsObj.findAll(src=True)

    for download in downloadList:
        print(download["src"])
        fileUrl = getAbsURL(baseUrl, download["src"])
        downPath = getDownloadPath(baseUrl, fileUrl, downloadDir)
        urlretrieve(fileUrl, downPath)
