from tkinter import *
from tkinter import messagebox


class Tkin_1:
    def __init__(self, w1):
        self.master = w1

        self.name = Label(w1, text='Đặng Thanh Phong', font=('times new roman', 15, 'bold'), bg='crimson', fg='White')
        self.name.pack(side=BOTTOM, fill=X)

        self.A1 = Label(w1, text='HỌ VÀ TÊN:', font=('times new roman', 15, 'bold'), fg='blue')
        self.A1.place(x=5, y=10)
        self.A2 = Label(w1, text='ĐIỂM SỐ:', font=('times new roman', 15, 'bold'), fg='blue')
        self.A2.place(x=300, y=10)

        self.B1 = Entry(w1, width=25, font=('times new roman', 14))
        self.B1.place(x=5, y=50)
        self.B2 = Entry(w1, width=25, font=('times new roman', 14))
        self.B2.place(x=300, y=50)

        self.C1 = Listbox(w1, font=('times new roman', 14), width=25, height=15)
        self.C1.place(x=5, y=100)
        self.C2 = Listbox(w1, font=('times new roman', 14), width=25, height=15)
        self.C2.place(x=300, y=100)

        self.D1 = Button(w1, text='ADD', font=('times new roman', 15, 'bold'), fg='black', bg='white', width=10, command=self.add)
        self.D1.place(x=600, y=150)
        self.D2 = Button(w1, text='DELETE', font=('times new roman', 15, 'bold'), fg='black', bg='white', width=10, command=self.delete)
        self.D2.place(x=600, y=210)

        self.menu_bar = Menu(self.master)
        self.master.configure(menu=self.menu_bar)
        self.help_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label='HELP', menu=self.help_menu)
        self.help_menu.add_command(label='About', command=self.about)



    def add(self):
        try:
            if self.B1.get() == '' or self.B2.get() == '':
                self.C1.insert(0, None)
                self.C2.insert(0, None)
            elif float(self.B2.get()) < 0 or float(self.B2.get()) > 10:
                messagebox.showerror('Lỗi', 'Mời nhập lại giá trị !')
            else:
                self.C1.insert(END, self.B1.get())
                self.B1.delete(0, END)
                self.C2.insert(END, self.B2.get())
                self.B2.delete(0, END)
        except:
            messagebox.showerror('Lỗi', 'Mời nhập lại giá trị !')

    def delete(self):
        for a in self.C1.curselection():
            self.C1.delete(a)
            self.C2.delete(a)

    def about(self):
        x = []
        for i in range(self.C2.size()):
            x.append(float(self.C2.get(i)))
        Tkin_1.average = round(sum(x)/len(x), 2)
        Tkin_1.mark = max(x)
        Tkin_1.fullname = self.C1.get(x.index(max(x)))
        W = Toplevel()
        W.geometry('600x200+600+200')
        W.resizable(False, False)
        W.grab_set()
        app_2 = Tkin_2(W)



class Tkin_2:
    def __init__(self, w2):
        self.master = w2

        self.L1 = Label(w2, text='THÔNG BÁO', font=('times new roman', 15, 'bold'), fg='white', bg='crimson')
        self.L1.pack(side=TOP, fill=X)
        self.L2 = Label(w2, text='SV có điểm cao nhất : {}'.format(Tkin_1.fullname), font=('times new roman', 15))
        self.L2.place(x=80, y=50)
        self.L2 = Label(w2, text='(Điểm : {})'.format(Tkin_1.mark), font=('times new roman', 15))
        self.L2.place(x=450, y=50)
        self.L4 = Label(w2, text='Điểm Trung Bình Của Lớp : {}'.format(Tkin_1.average), font=('times new roman', 15))
        self.L4.place(x=80, y=100)

        self.P1 = Button(w2, text='OK', font=('times new roman', 15, 'bold'), fg='white', bg='blue', width=15, command=self.P1_click)
        self.P1.place(x=200, y=150)


    def P1_click(self):
        self.master.destroy()


def main():
    w= Tk()
    w.title('BẢNG ĐIỂM')
    w.geometry('800x500+400+200')
    w.resizable(False, False)
    app_1 = Tkin_1(w)

    w.mainloop()

if __name__=='__main__' :
    main()