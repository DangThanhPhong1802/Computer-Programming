from tkinter import *
from tkinter import messagebox

w= Tk()
w.title('BINARY CONVERSION')
w.geometry('500x400+400+200')
w.resizable(False, False)

name = Label(w, text='Đặng Thanh Phong', font=('times new roman', 15, 'bold'), bg='crimson', fg='White')
name.pack(side=TOP, fill=X)
#-----------------------------------function Convert()------------------------------------------#
def convert() :
    if A2.get() != '':
        try:
            u = int(A2.get())
            B2.delete(0, END)
            B2.insert(0, '{:b}'.format(u))
        except:
            messagebox.showerror(title='Lỗi', message='Nhập sai định dạng giá trị !')
    else:
        B2.delete(0, END)
        B2.insert(0, '0')
#---------------------------------------------------------------------------------#

A1 = Label(w, text='DECIMAL : ', font=('timew new roman', 15, 'bold'))
A1.place(x=80, y=100)
A2 = Entry(w, width=15, font=('timew new roman', 15))
A2.place(x=200, y=100)

B1 = Label(w, text='BINARY : ', font=('timew new roman', 15, 'bold'))
B1.place(x=80, y=150)
B2 = Entry(w, width=15, font=('timew new roman', 15))
B2.place(x=200, y=150)

C1 = Button(w, text='CONVERT', font=('timew new roman', 15, 'bold'), fg='white', bg='blue', width=15, command=convert)
C1.place(x=200, y=200)


w.mainloop()