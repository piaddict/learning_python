# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', db='db0331', charset='utf8')

curs = conn.cursor()

sql = "select * from member"
curs.execute(sql)

rows = curs.fetchall()
print (rows)

conn.close()