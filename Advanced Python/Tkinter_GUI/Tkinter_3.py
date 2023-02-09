from tkinter import *


w = Tk()
w.title('CHECKBOX')
w.geometry('700x500+400+200')

#----------------------CHECKBOX-----------------------


c1 = Checkbutton(w, text='Option 1 : ', font=('arial', 15), onvalue=50000)
c1.grid(row=0, column=0, padx=20, pady=20, sticky='w')
c2 = Checkbutton(w, text='Option 2 : ', font=('arial', 15), onvalue=100000)
c2.grid(row=1, column=0, padx=20, pady=20, sticky='w')
c3 = Checkbutton(w, text='Option 3 : ', font=('arial', 15), onvalue=150000)
c3.grid(row=2, column=0, padx=20, pady=20, sticky='w')

def b1_click() :
    tong = x1.get() + x2.get() + x3.get()
    L1.configure(text = 'TOTAL = ' + str(tong))

b1 = Button(w, text='Check', bg='sky blue', font=('arial',15), width=10, command=b1_click)
b1.grid(row=0, column=2, padx=20, pady=20)
L1 = Label(w, text='TOTAL = ', fg='crimson', font=('arial',15, 'bold'), width=10)
L1.grid(row=2, column=2, padx=50, pady=20, sticky='w')

#---------------------------Radiobutton---------------------

c4 = Radiobutton(w, text='Option 1 : ', font=('arial', 15), value=50000, variable=x1)
c4.grid(row=3, column=0, padx=20, pady=20, sticky='w')
c5 = Radiobutton(w, text='Option 2 : ', font=('arial', 15), value=100000, variable=x2)
c5.grid(row=4, column=0, padx=20, pady=20, sticky='w')
c6 = Radiobutton(w, text='Option 3 : ', font=('arial', 15), value=150000, variable=x3)
c6.grid(row=5, column=0, padx=20, pady=20, sticky='w')




w.mainloop()