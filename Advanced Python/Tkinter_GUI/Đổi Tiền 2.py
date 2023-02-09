from tkinter import *

w = Tk()
w.title('MONEY EXCHANGE')
w.geometry('600x400+400+200')

A=['USD: 22.000', 'EUR: 26.000', 'JYP: 200']
B= StringVar(value=A)

C1 = Listbox(w, font=('arial', 15), width=15, height=6, listvariable=B)
C1.grid(row=0, column=0, padx=20, pady=20, sticky='w')

def D2_click() :
    m = 0
    t = 0
    if D1.get() != '' :
        m=float(D1.get())
    if C1.get(ACTIVE) == 'USD: 22.000' :
        t= m*22000
    if C1.get(ACTIVE) == 'EUR: 26.000' :
        t= m*26000
    if C1.get(ACTIVE) == 'JYP: 200' :
        t= m*200
    L1.configure(text='GIÁ TRỊ QUY ĐỔI: {:,} vnd'.format(t))


D1 =Entry(w, width=20)
D1.grid(row=0, column=1, padx=20, pady=20)

D2 = Button(w, text='EXCHANGE', bg='white', font=('arial',15), width=10, command=D2_click)
D2.grid(row=1, column=1, padx=20, pady=20)
L1 = Label(w, text='GIÁ TRỊ QUY ĐỔI:', fg='blue', font=('arial',15, 'bold'), width=30)
L1.grid(row=4, column=1, padx=20, pady=20)

w.mainloop()