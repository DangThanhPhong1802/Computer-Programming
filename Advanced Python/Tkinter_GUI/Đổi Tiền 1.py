from tkinter import *

w = Tk()
w.title('MONEY EXCHANGE')
w.geometry('600x400+400+200')

x1= IntVar()

C1 = Radiobutton(w, text='USD: 22.000 : ', font=('arial', 15), value=22000, variable=x1)
C1.grid(row=0, column=0, padx=20, pady=20, sticky='w')
C2 = Radiobutton(w, text='EUR: 26.000 ', font=('arial', 15), value=26000, variable=x1)
C2.grid(row=1, column=0, padx=20, pady=20, sticky='w')
C3 = Radiobutton(w, text='JYP: 200 ', font=('arial', 15), value=200, variable=x1)
C3.grid(row=2, column=0, padx=20, pady=20, sticky='w')

def D2_click() :
    m = 0
    t = 0
    if D1.get() != '' :
        m=float(D1.get())
    if x1.get() == 0 :
        L1.configure(text='Mời chọn loại ngoại tệ')
    else :
        t= m*x1.get()
        L1.configure(text='GIÁ TRỊ QUY ĐỔI: {:,} vnd'.format(t))

D1 =Entry(w, width=20)
D1.grid(row=0, column=1, padx=20, pady=20)

D2 = Button(w, text='EXCHANGE', bg='white', font=('arial',15), width=10, command=D2_click)
D2.grid(row=1, column=1, padx=20, pady=20)
L1 = Label(w, text='GIÁ TRỊ QUY ĐỔI:', fg='blue', font=('arial',15, 'bold'), width=30)
L1.grid(row=4, column=1, padx=20, pady=20)

w.mainloop()