from tkinter import  *

root = Tk()

myLabel1 = Label(root, text="Hello DiDi !!")
myLabel2 = Label(root, text="It's Okay don't worry")

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=3)

root.mainloop() 