from tkinter import *
from tkinter import messagebox

w= Tk()
w.title('BẢNG ĐIỂM')
w.geometry('800x500+400+200')
w.resizable(False, False)

name = Label(w, text='Đặng Thanh Phong', font=('times new roman', 15, 'bold'), bg='crimson', fg='White')
name.pack(side=BOTTOM, fill=X)

def add() :
    try :
        if B1.get() == '' or B2.get() == '' :
            C1.insert(0, None)
            C2.insert(0, None)
        elif float(B2.get())<0 or float(B2.get())>10 :
            messagebox.showerror('Lỗi', 'Mời nhập lại giá trị !')
        else :
            C1.insert(END, B1.get())
            B1.delete(0, END)
            C2.insert(END, B2.get())
            B2.delete(0,END)
    except :
        messagebox.showerror('Lỗi', 'Mời nhập lại giá trị !')

def delete() :
    for a in C1.curselection() :
        C1.delete(a)
        C2.delete(a)

A1 = Label(w, text='HỌ VÀ TÊN:', font=('times new roman', 15, 'bold'), fg='blue')
A1.place(x=5, y=10)
A2 = Label(w, text='ĐIỂM SỐ:', font=('times new roman', 15, 'bold'), fg='blue')
A2.place(x=300, y=10)

B1 = Entry(w, width=25, font=('times new roman', 14))
B1.place(x=5, y=50)
B2 = Entry(w, width=25, font=('times new roman', 14))
B2.place(x=300, y=50)

C1 = Listbox(w, font=('times new roman', 14), width=25, height=15)
C1.place(x=5, y=100)
C2 = Listbox(w, font=('times new roman', 14), width=25, height=15)
C2.place(x=300, y=100)

D1 = Button(w, text='ADD', font=('timew new roman', 15, 'bold'), fg='black', bg='white', width=10, command=add)
D1.place(x=600, y=150)
D2 = Button(w, text='DELETE', font=('timew new roman', 15, 'bold'), fg='black', bg='white', width=10, command=delete)
D2.place(x=600, y=210)


w.mainloop()