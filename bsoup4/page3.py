from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

print("처음")
for child in bsObj.find("table", {"id":"giftList"}).children:
    print(child)

print("다음")
for siblings in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    print(siblings)

print("부모")
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

print("사진")
images = bsObj.find_all("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image)