# -*- coding: utf-8 -*-
from tkinter import *
import pymysql


class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
 
        self.master = master
        self.master.title("정보조회")
        self.pack(fill=BOTH, expand=True)
 
        frame1 = Frame(self)
        frame1.pack(fill=X)
        
        self.lblComp = Label(frame1, text="내용", width=10)
        self.lblComp.pack(side=LEFT, padx=10, pady=10)
 
        self.textComp = Text(frame1)
        self.textComp.pack(fill=X, padx=10, expand=True)
 
        frame2 = Frame(self)
        frame2.pack(fill=X)
        
        self.btnSave = Button(frame2, text="조회", command=self.getRes)
        self.btnSave.pack(side=LEFT, padx=10, pady=10)
 
    def getRes(self):
        data = self.getData()
        for x in data:
            self.textComp.insert(END, x)
            self.textComp.insert(END,"\n")


    def getData(self):
        conn = pymysql.connect(host='localhost', user='root', password='', db='member', charset='utf8')

        curs = conn.cursor()

        sql = "select * from emp"
        curs.execute(sql)

        rows = curs.fetchall()
        conn.close()

        return rows


def main():
    root = Tk()
    root.geometry("600x350+100+100")
    app = MyFrame(root)
    root.mainloop()

 
if __name__ == '__main__':
    main()
