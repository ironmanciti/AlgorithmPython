from tkinter import *
root = Tk()
root.title("Radio Button")

#tkinter 변수 선언. tkinter 가 change tracking
# r = IntVar()
# r.set("1")

MENU = ["치킨", "너겟", "피자", "파파로니"]

r = StringVar()
r.set("치킨")

def clicked():
    global myLabel
    myLabel.destroy()

    myLabel = Label(root, text=r.get())
    myLabel.pack()
    return

for item in MENU:
    Radiobutton(root, text=item, variable=r, value=item).pack()

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(1)).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(2)).pack()

my_button = Button(root, text="Click Me", command=clicked)
my_button.pack()

myLabel = Label(root, text=r.get())
myLabel.pack()

mainloop()
