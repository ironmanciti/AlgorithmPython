from tkinter import *

root = Tk()

# click 하면 text display
def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()

#creating a Label Widget
myLabel1 = Label(root, text="Hello World")
myLabel2 = Label(root, text="My Name is John Elder")
myLabel1.pack()
myLabel2.pack()

myButton = Button(root, text="click me", command=myClick)

# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=1)

myButton.pack()

root.mainloop()

