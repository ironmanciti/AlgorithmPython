from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# click 하면 입력한 숫자 display
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))
# 입력 field clear    
def clear():
    e.delete(0, END)
    global first_number
    first_number = 0
    
def plus():
    current = e.get() 
    global first_number 
    global math
    math = "add"
    first_number = int(current)
    e.delete(0, END) 
    
def sub():
    current = e.get()
    global first_number
    global math
    math = "sub"
    first_number = int(current)
    e.delete(0, END)

def mult():
    current = e.get()
    global first_number
    global math
    math = "mult"
    first_number = int(current)
    e.delete(0, END)

def div():
    current = e.get()
    global first_number
    global math
    math = "div"
    first_number = int(current)
    e.delete(0, END)

# 입력했던 math operation 에 따라 이전값과 현재 값 계산
def equal():
    global first_number
    global math

    current = e.get()
    if math == "add":
        total = first_number + int(current) 
    elif math == "sub":
        total = first_number - int(current)
    elif math == "mult":
        total = first_number * int(current)
    elif math == "div":
        total = first_number / int(current)

    e.delete(0, END)
    e.insert(0, str(total))

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

button_plus = Button(root, text="+", padx=40, pady=20, command=plus)
button_sub = Button(root, text="-", padx=40, pady=20, command=sub)
button_mult = Button(root, text="*", padx=40, pady=20, command=mult)
button_div = Button(root, text="/", padx=40, pady=20, command=div)
button_equal = Button(root, text="=", padx=100, pady=20, command=equal)
button_clear = Button(root, text="Clear", padx=90, pady=20, command=clear)

# 자판 배치
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

button_clear.grid(row=4, column=1, columnspan=2)

button_plus.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2)

button_sub.grid(row=6, column=0)
button_mult.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()
