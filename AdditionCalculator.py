

from tkinter import *
import re

root = Tk()

root.title('Calculator')


#Functions

def clicked(n):
    p = str(e.get())
    e.delete(0,END)
    e.insert(0,p+str(n))




def clear():
    return e.delete(0,END)

def add():
    global first_value,sign
    sign = '+'
    first_value = e.get()
    e.delete(0,END)

def equal():
    second_value = e.get()
    if sign == '+':
       if re.search('[\.]+?',first_value) or re.search('[\.]+?',second_value):
           e.delete(0,END)
           return e.insert(0,float(first_value) + float(second_value))
       else:
           e.delete(0,END)
           return e.insert(0,int(first_value) + int(second_value))

#Def


e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=8, pady=8)



button_1 = Button(root, text="1", padx=40, pady=20,command=lambda : clicked(1))
button_2 = Button(root, text="2", padx=40, pady=20,command=lambda : clicked(2))
button_3 = Button(root, text="3", padx=40, pady=20,command=lambda : clicked(3))

button_4 = Button(root, text="4", padx=40, pady=20,command=lambda : clicked(4))
button_5 = Button(root, text="5", padx=40, pady=20,command=lambda : clicked(5))
button_6 = Button(root, text="6", padx=40, pady=20,command=lambda : clicked(6))

button_7 = Button(root, text="7", padx=40, pady=20,command=lambda : clicked(7))
button_8 = Button(root, text="8", padx=40, pady=20,command=lambda : clicked(8))
button_9 = Button(root, text="9", padx=40, pady=20,command=lambda : clicked(9))

button_0 = Button(root, text="0", padx=40, pady=20,command=lambda : clicked(0))

button_plus = Button(root, text="C", padx=40, pady=20,command=clear)
button_clear = Button(root, text="+", padx=90, pady=20,command=add)
button_equal = Button(root, text="=", padx=90, pady=20,command=equal)


#Use

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_plus.grid(row=5, column=0)
button_clear.grid(row=4, column=1,columnspan=2)
button_equal.grid(row=5, column=1,columnspan=2)
#mainLoop
root.mainloop()