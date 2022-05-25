from tkinter import  *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look ! I clicked a Button !",fg="Red")
    myLabel.pack()

myButton1 = Button(root, text="Button1 !" , stat = DISABLED , padx = 50 , pady = 20 )
myButton1.pack()

myButton2 = Button(root, text="Click Me !" , command= myClick , fg="Blue", bg="#ffffff" )
myButton2.pack()

root.mainloop()