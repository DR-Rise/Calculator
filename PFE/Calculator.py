from tkinter import  *

root = Tk()
root.title ("Calculator")
root.iconbitmap("Calc.ico")

e= Entry(root, width=60 ,borderwidth=5,)

e.grid(row=0, column=0, columnspan=5, padx=10,pady=10)
global f_num
global operation

def button_click(number):
    num = e.get()
    e.delete(0,END)
    e.insert(0,str(num) + str(number))
    return

def button_Clear():
    e.delete(0,END)



def button_add():
    global f_num
    global operation
    f_num = float(e.get())
    operation = "+"
    e.delete(0, END)


def button_sub():
    global f_num
    global operation
    f_num = float(e.get())
    operation = "-"
    e.delete(0, END)


def button_multi():
    global f_num
    global operation
    f_num = float(e.get())
    operation = "*"
    e.delete(0, END)


def button_div():
    global f_num
    global operation
    f_num = float(e.get())
    operation = "/"
    e.delete(0, END)


def button_eq():
    global f_num
    global operation
    s_num = float(e.get())
    global result
    if (operation == "+"):
        result = f_num + s_num
    elif(operation == "-"):
        result = f_num - s_num
    elif(operation == "*"):
        result = f_num * s_num
    elif (operation == "/"):
        if(s_num != 0.0):
            result = f_num / s_num
        else:result = f_num

    else: result = f_num

    e.delete(0, END)
    e.insert(0,result)


#Define Buttons

button_1=Button(root, text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(root, text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root, text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4=Button(root, text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5=Button(root, text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(root, text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7=Button(root, text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root, text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9=Button(root, text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0=Button(root, text="0",padx=40,pady=20,command=lambda: button_click(0))

button_addition=Button(root, text="+ ",padx=37,pady=20,command=button_add)
button_subtraction=Button(root, text="-",padx=40,pady=20,command=button_sub)
button_multiplication=Button(root, text="*",padx=40,pady=20,command=button_multi)
button_Division=Button(root, text="/",padx=40,pady=20,command=button_div)


button_clear=Button(root, text="Clear",padx=29,pady=20,command=button_Clear)
button_equal=Button(root, text="=",padx=40,pady=20,command=button_eq)

#Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_equal.grid(row=4, column=1)
button_clear.grid(row=1, column=3)

button_addition.grid(row=4, column=3)
button_subtraction.grid(row=2, column=3)
button_multiplication.grid(row=3, column=3)
button_Division.grid(row=4, column=2)




root.mainloop()