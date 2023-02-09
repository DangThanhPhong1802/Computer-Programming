from tkinter import *


class GUI_1:
    def __init__(self, w1):
        self.master = w1

        self.name = Label(w1, text='Đặng Thanh Phong', font=('times new roman', 15, 'bold'), bg='crimson', fg='White')
        self.name.pack(side=TOP, fill=X)

        self.A1 = Label(w1, text='DECIMAL : ', font=('times new roman', 15, 'bold'))
        self.A1.place(x=80, y=100)
        self.A2 = Entry(w1, width=15, font=('times new roman', 15))
        self.A2.place(x=200, y=100)

        self.B1 = Label(w1, text='BINARY : ', font=('times new roman', 15, 'bold'))
        self.B1.place(x=80, y=150)
        self.B2 = Entry(w1, width=15, font=('times new roman', 15))
        self.B2.place(x=200, y=150)

        self.C1 = Button(w1, text='CONVERT', font=('times new roman', 15, 'bold'), fg='white', bg='blue', width=15, command=self.convert)
        self.C1.place(x=200, y=200)

        self.menu_bar = Menu(self.master)
        self.master.configure(menu=self.menu_bar)
        self.help_menu = Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label='HELP', menu=self.help_menu)
        self.help_menu.add_command(label='About', command=self.about)

    def convert(self):
        x1 = int(self.A2.get())
        x2 = '{:b}'.format(x1)
        self.B2.delete(0, END)
        self.B2.insert(0, x2)

    def about(self):
        W1 = Toplevel()
        W1.geometry('600x300+600+200')
        W1.grab_set()
        application_2 = GUI_2(W1)

class GUI_2 :
    def __init__(self, w2):
        self.master = w2
        self.L1 = Label(w2, text='Tên Chương Trình : Binary Convertion', font=('times new roman', 15))
        self.L1.place(x=80, y=100)
        self.L2 = Label(w2, text='Ngày tạo : 01/12/2021', font=('times new roman', 15))
        self.L2.place(x=80, y=150)
        self.C1 = Button(w2, text='OK', font=('times new roman', 15, 'bold'), fg='white', bg='blue', width=15, command=self.convert)
        self.C1.place(x=200, y=200)

    def convert(self):
        self.master.destroy()

def main() :
    w = Tk()
    w.title('BINARY CONVERSION - Class')
    w.geometry('500x400+400+200')
    w.resizable(False, False)
    appication_1 = GUI_1(w)

    w.mainloop()

if __name__=='__main__' :  #câu lệnh cố định
    main()