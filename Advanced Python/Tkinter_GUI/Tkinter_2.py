from tkinter import *
from PIL import Image, ImageTk
W = Tk()

W.title('CHƯƠNG TRÌNH GUI')

L1 = Label(W, text = 'Welcome', fg='Red', bg='blue', font = ("arial", 16, 'bold'))
L1.pack()
B= Image.open('D:/Ảnh/HCMUTE.jpg')
A = ImageTk.PhotoImage(B)
L2 = Label(master = W, image = A, heigh=300, width=1000)
L2.pack()

def B1_click():
    L2.configure(bg='red')
B1 = Button(master = W, text ='Fore Ground',width=12, font=('arial', 16), bg='red', fg='black', command = B1_click )

W.mainloop()