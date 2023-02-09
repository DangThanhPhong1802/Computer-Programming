from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

w = Tk()
w.title('CHƯƠNG TRÌNH TEXT - MENU - MESSAGEBOX - TOPLEVEL')
w.geometry('800x600+400+200')

t1 = Text(w, font=('Times New Roman', 13))
t1.pack(expand=True, fill='both')

def b1_click() :
    x1 = filedialog.askopenfile(mode='r')
    with open(file=x1.name, mode='r', encoding='utf-8') as f : #'r'=read
        A= f.read()
        t1.delete('1.0', END)  #line=1, column=0 xóa đến cuối End
        t1.insert('1.0', A)
        f.close()

def b2_click() :
    x2 = filedialog.asksaveasfile(mode='w')
    with open(file=x2.name, mode='w', encoding='utf-8') as f : #'w'=write
        A= t1.get('1.0', END)
        f.write(A)
        f.close()

s = IntVar(value=13)
def Phong_To() :
    s.set(s.get()+1)  #(+1) có nghĩa là tăng cỡ chữ lên 1đv
    t1.configure(font=('times new roman', s.get()))
def Thu_Nho() :
    s.set(s.get()-1)  #(-1) có nghĩa là giảm cỡ chữ lên 1đv
    t1.configure(font=('times new roman', s.get()))
def zoom() :
    t1.configure(font=('times new roman', s.get()))
def new() :
    messagebox.showinfo(title='Thông Báo', message='Tạo mới một tập tin')
def exit() :
    M = messagebox.askquestion(title='Thông Báo', message='Bạn có chắc muốn thoát khỏi chương trình không ?')
    if M=='yes' : #nếu bấm Yes thì thoát, bấm No thì ở lại
        w.destroy()
def Zoom_default() :
    # ---------------------Thêm cửa sổ khác vào giao diện----------------------#
    w1 = Toplevel()
    w1.geometry('300x250+600+300')
    w1.title('ZOOM')
    w1.grab_set()   #chỉ làm cửa sổ mới, ko cho làm ở cửa sổ cũ
    def n1_click() :
        x = int(e1.get())
        s.set(x)
        t1.configure(font=('times new roman', s.get()))
        w1.destroy()

    r1 = Radiobutton(w1, text='50%', font=('arial',15), value=10, variable=s)
    r1.place(x=20, y=20)
    r2 = Radiobutton(w1, text='100%', font=('arial', 15), value=15, variable=s)
    r2.place(x=20, y=60)
    r3 = Radiobutton(w1, text='150%', font=('arial', 15), value=20, variable=s)
    r3.place(x=20, y=100)
    l1 = Label(w1, text='Percent', font=('arial', 15))
    l1.place(x=150, y=30)
    e1 = Entry(w1, font=('arial', 15), width=10)
    e1.place(x=150, y=80)
    n1 = Button(w1, text='OK', font=('arial', 15), width=9, command=n1_click)
    n1.place(x=20, y=160)
    n2 = Button(w1, text='CANCEL', font=('arial', 15), width=9)
    n2.place(x=160, y=160)

#----------------Tạo Thanh Menu------------------------#
menu_bar = Menu(w)
w.configure(menu=menu_bar)
#----------------Tạo Menu Thành Phần và Các Menu Con Bên Trong---------------------------#
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=new)
file_menu.add_command(label='Open', command=b1_click)
file_menu.add_command(label='Save', command=b2_click)
file_menu.add_command(label='Exit', command=exit)

view_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='View', menu=view_menu)
view_menu.add_command(label='Zoom', command=Zoom_default)
view_menu.add_command(label='Phóng To', command=Phong_To)
view_menu.add_command(label='Thu Nhỏ', command=Thu_Nho)
view_menu.add_separator()
view_menu.add_radiobutton(label='100%', value=13, variable=s, command=zoom)
view_menu.add_radiobutton(label='200%', value=26, variable=s, command=zoom)
view_menu.add_radiobutton(label='300%', value=52, variable=s, command=zoom)
view_menu.add_radiobutton(label='400%', value=104, variable=s, command=zoom)
view_menu.add_radiobutton(label='500%', value=208, variable=s, command=zoom)




w.mainloop()

