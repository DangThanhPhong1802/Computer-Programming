from tkinter import *

w = Tk()
w.title('LISTBOX')
w.geometry('600x400+400+200')

F1 = Frame(w)
F1.place(x=50, y=50)

A1 = ['Món 1 : 50.000đ', 'Món 2 : 100.000đ', 'Món 3 : 150.000đ']
A2 = [50000, 100000, 150000]
B = StringVar(value=A1)

LB1 = Listbox(F1, font=('arial',12), width=20, height=10, listvariable=B, selectmode=EXTENDED)
LB1.grid(row=0, column=0, padx=20, pady=10)
LB2 = Listbox(F1, font=('arial',12), width=20, height=10, listvariable=B, selectmode=EXTENDED)
LB2.grid(row=0, column=1, padx=20, pady=10)


def b1_click() :
    tong = 0
    x = LB1.curselection()
    for i in x :
        tong = tong + A2[i]
    L1.configure(text = 'TOTAL=' + str(tong) + 'VNĐ')

b1 = Button(w, text='Check', bg='sky blue', font=('arial',15), width=10, command=b1_click)
b1.grid(row=0, column=1, padx=20, pady=10)
L1 = Label(w, text='TOTAL=', fg='crimson', font=('arial',10, 'bold'), width=10)
L1.grid(row=0, column=2, padx=20, pady=10)



w.mainloop()