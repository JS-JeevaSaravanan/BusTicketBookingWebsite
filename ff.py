import sqlite3
from tkinter import *



def fser(f2w):
        f2w.destroy()
        fserw=Tk()        
        fserw.mainloop()



def freg(f2w):
        f2w.destroy()
        freg=Tk()
        
        Label(freg,text="name").pack()
        Entry().pack()

        Label(freg,text="contact no").pack()
        Entry().pack()
        
        
        Label(freg,text="").pack()
        Listbox().pack()
        Entry().pack()
        
        Label(freg,text="age").pack()
        Scale().pack()

        Entry().pack()
        
        Label(freg,text="").pack()
        Entry().pack()
        

        fregw.mainloop()


def f2(f1w):
        f1w.destroy()
        f2w=Tk()        
        Button(f2w,text="search",command=lambda : fser(f2w)).pack()
        Button(f2w,text="register",command=lambda : freg(f2w)).pack()
        f2w.mainloop()


def f1():
        f1w=Tk()

        Label(f1w,text="pass").pack()
        Button(f1w,text="i agree",command=lambda :f2(f1w) ).pack()

        f1w.mainloop()


if __name__=="__main__":

        f1()