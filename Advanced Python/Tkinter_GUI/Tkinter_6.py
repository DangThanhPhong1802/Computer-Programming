from tkinter import *
from tkinter import filedialog

w = Tk()
w.title('CHƯƠNG TRÌNH TEXT - SCALE')
w.geometry('800x600+400+200')

t1 = Text(w, font=('Times New Roman', 13))
t1.place(x=0, y=0, width=600, height=600)

def b1_click() :
    x1 = filedialog.askopenfile(mode='r')
    with open(file=x1.name, mode='r', encoding='utf-8') as f : #'r' = read
        A= f.read()
        t1.delete('1.0', END)  #line=1, column=0 xóa đến cuối End
        t1.insert('1.0', A)
        f.close()

def b2_click() :
    x2 = filedialog.asksaveasfile(mode='w')
    with open(file=x2.name, mode='w', encoding='utf-8') as f : #'w' = write
        A= t1.get('1.0', END)
        f.write(A)
        f.close()

b1 = Button(w, text='OPEN', font=('arial', 15), width=12, bg='crimson', command=b1_click)
b1.place(x=630, y=50)
b2 = Button(w, text='SAVE', font=('arial', 15), width=12, bg='green', command=b2_click)
b2.place(x=630, y=100)

def scale_change(a) :
    t1.configure(font=('Times New Roman', a))
s1 = Scale(w, orient='vertical', from_=8, to=20, length=300, command=scale_change)
s1.place(x=670, y=200)
s1.set(13)


w.mainloop()

