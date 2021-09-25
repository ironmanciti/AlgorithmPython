from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.title("Tkinter Frame")

frame = LabelFrame(root, text="This is my frame", padx=50, pady=50) #pad inside frame
frame.pack(padx=100, pady=100)   #pad outside frame

b1 = Button(frame, text="누르지 마시요 !")
b2 = Button(frame, text="누르지 마시요 !")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
