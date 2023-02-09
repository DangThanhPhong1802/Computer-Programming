from tkinter import *

w = Tk()
w.title('VẼ - CANVAS')
w.geometry('800x600+400+200')

c1 = Canvas(w, bg='white', width=600, height=600)
c1.place(x=0, y=0)

def b1_click() :
    c1.create_line(100,100,100,300, width=4, fill='orange')
def b2_click() :
    c1.create_arc(100,100,400,400, start=0, extent=180, width=4, fill='green',outline='crimson', style=PIESLICE)
def b3_click() :
    c1.create_rectangle(100,100,100,300, width=4, fill='blue', tags='H1')
def b4_click(event) :
    x1 = event.x
    y1 = event.y
    c1.create_oval(x1,y1,x1+400,y1+400, width=4, outline='#D87BEC')
def b5_click() :
    c1.delete(ALL)
b1 = Button(w, text='Đoạn Thẳng', font=('arial', 15), width=12, bg='crimson', command=b1_click)
b1.place(x=630, y=50)
b2 = Button(w, text='Cung Tròn', font=('arial', 15), width=12, bg='green', command=b2_click)
b2.place(x=630, y=100)
b3 = Button(w, text='HCN', font=('arial', 15), width=12, bg='crimson', command=b3_click)
b3.place(x=630, y=150)
b4 = Button(w, text='Hình Tròn', font=('arial', 15), width=12, bg='green', command=b4_click)
b4.place(x=630, y=200)
b5 = Button(w, text='Delete', font=('arial', 15), width=12, bg='crimson', command=b5_click)
b5.place(x=630, y=250)

c1.bind('<Button-1>', b4_click)

w.mainloop()

