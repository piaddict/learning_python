# -*- coding: utf-8 -*-

from tkinter import *
 
class MyFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
 
        self.master = master
        self.master.title("로그인")
        self.pack(fill=BOTH, expand=True)
 
        # 성명
        frame1 = Frame(self)
        frame1.pack(fill=X)
 
        lblName = Label(frame1, text="성명", width=10)
        lblName.pack(side=LEFT, padx=10, pady=10)
 
        entryName = Entry(frame1)
        entryName.pack(fill=X, padx=10, expand=True)
 
        # 회사
        frame2 = Frame(self)
        frame2.pack(fill=X)
 
        lblComp = Label(frame2, text="회사명", width=10)
        lblComp.pack(side=LEFT, padx=10, pady=10)
 
        entryComp = Entry(frame2)
        entryComp.pack(fill=X, padx=10, expand=True)
 
        # 저장
        frame3 = Frame(self)
        frame3.pack(fill=X)
        btnSave = Button(frame3, text="로그인")
        btnSave.pack(side=LEFT, padx=10, pady=10)
 
 
def main():
    root = Tk()
    root.geometry("600x250+100+100")
    app = MyFrame(root)
    root.mainloop()

 
if __name__ == '__main__':
    main()