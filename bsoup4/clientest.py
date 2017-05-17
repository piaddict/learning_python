from urllib.request import urlopen

import pymysql
from bs4 import BeautifulSoup


def getData(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    titles = bsObj.find("div", {"class": "card-grid"}
                        ).findAll("div", {"class": "list-row"})

    data = list()
    for title in titles:
        clien = [
            title.find("a", {"class": "list-subject"}).get_text().strip(),
            title.find("a", {"class": "dropdown-toggle nick"}
                       ).get_text().strip()
        ]
        data.append(clien)

    return data


def setData(data):
    try:
        conn = pymysql.connect(
            host="localhost", user="crawl", password="crawl", db="crawl", charset="utf8")
        curs = conn.cursor()
        sql = "insert into clien(title, author) values(%s, %s)"
        # execute만 반복가능
        for item in data:
            curs.execute(sql, (item[0], item[1]))
    except:
        print("db 입력실패")
    finally:
        conn.commit()
        conn.close()


if __name__ == "__main__":
    try:
        for num in range(5):
            url = "https://www.clien.net/service/board/park?&od=T31&po=" + \
                str(num)
            setData(getData(url))
    except (KeyboardInterrupt, SystemExit):
        pass
