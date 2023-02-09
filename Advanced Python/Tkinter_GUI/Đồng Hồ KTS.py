from tkinter import *
from tkinter.ttk import *
from time import strftime

r = Tk()
r.title('Đồng Hồ Kỹ Thuật Số')

def clock():
    string = strftime('%I:%M:%S:%p')
    A.config(text=string)
    A.after(1000,clock)

A = Label(master=r, font=('digital-7.ttf',100), background='black', foreground='green')
A.pack(anchor='center')
clock()

r.mainloop()