from tkinter import  *

root = Tk()

e= Entry(root, width=50 ,borderwidth=10)
e.pack()
e.insert(0, "Enter Your Name: ")


def myClick():
    txt = "Hello  " + e.get()
    myLabel = Label(root, text=txt , fg="Blue")
    myLabel.pack()

myButton1 = Button(root, text="Button " , command=myClick  )
myButton1.pack()


root.mainloop()