from tkinter import *

root = Tk()

# 이름 입력
e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "insert your name")

# click 하면 Hello : + 이름 display
def buttonClick():
    txtLabel = Label(root, text="Hello : " + e.get())
    txtLabel.pack()

# button 생성    
btton = Button(root, text="click me", command=buttonClick)
btton.pack()

root.mainloop()
