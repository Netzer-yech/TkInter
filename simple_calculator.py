from tkinter import *

root = Tk()
# create the main window

root.title("Simple Calculator")
# create a title
root.iconbitmap("C:\\automation course\\icons\\calculator-icon_34473.ico")
app_width = 290
app_height = 431
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# create input field at the design we want



def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)

def button_add():
     first_number = e.get()
     global f_num
     global math
     math = "addition"
     f_num = float(first_number)
     e.delete(0, END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_division():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    second_number = float(e.get())
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))
    if math == "subtraction":
        e.insert(0, f_num - float(second_number))
    if math == "multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "division":
        e.insert(0, f_num / float(second_number))
#

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_equal = Button(root, text="=", padx=89, pady=20, command=button_equal)
button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply)
button_division = Button(root, text="/", padx=40, pady=20, command=button_division)
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
# define buttons

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
button_add.grid(row=5, column=0)
button_multiply.grid(row=4, column=1)
button_division.grid(row=4, column=2)
button_subtract.grid(row=6, column=0)
button_equal.grid(row=6, column=1, columnspan=2)
button_clear.grid(row=5, column=1, columnspan=2)
# using grid to put buttons and labels in order at main root (window)

root.mainloop()
# looping the root