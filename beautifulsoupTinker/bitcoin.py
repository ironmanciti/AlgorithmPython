from tkinter import *
from PIL import Image, ImageTk
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from datetime import datetime
import webbrowser

URL = "https://kr.investing.com/crypto/bitcoin/"
hdr = {'User-Agent': 'Mozilla/5.0'}

root = Tk()
root.title('Python Education - Bitcoin Price Finder')
root.geometry("500x210")  # window size
root.config(bg="black")   # 배경색 설정

# Create a Frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Define logo image
img = ImageTk.PhotoImage(Image.open('images/bitcoin.png').resize((100, 100)))
logo_label = Label(my_frame, image=img, bd=2)
logo_label.grid(row=0, column=0, rowspan=2)

# bitcoin price label
bit_label = Label(my_frame, text='TEST', font=("Helvetica", 45), bg="white")
bit_label.grid(row=0, column=1, padx=20, sticky="s")

# website url 연결
def callback():
    webbrowser.open_new(URL)

# website 를 직접 찾아가는 link button
bit_button = Button(my_frame, text="웹사이트 직접 연결", cursor="hand", command=callback)
bit_button.grid(row=0, column=2)

# 현재 시간
now = datetime.now()
current_time = now.strftime("%I:%M:%S %p")

# bitcoin price 가져오기
def update():
    global previous
    #Grab Bitcoin Price
    req = Request(URL, headers=hdr)
    page = urlopen(req)

    html = BeautifulSoup(page, "html.parser")
    found = html.find(class_="newInput inputTextBox alertValue")
    start = re.search('[0-9,.]+', str(found))
    price = start.group()
    
    bit_label.config(text=f"${price}")
    
    now = datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    status.config(text=f'Last Updated {current_time}')
    
    # timer 를 10초로 setting
    root.after(10000, update)  
    
# status  bar 생성
status = Label(root, text=f'Last Updated {current_time}', anchor=E)
status.pack(fill=X, side=BOTTOM, ipady=2)

# program start 시 update 함수 수행
update()

root.mainloop()
