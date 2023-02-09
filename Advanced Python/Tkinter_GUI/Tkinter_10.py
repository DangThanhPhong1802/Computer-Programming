from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

w = Tk()
w.title('CHƯƠNG TRÌNH TEXT - MENU - MESSAGEBOX')
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
view_menu.add_command(label='Phóng To', command=Phong_To)
view_menu.add_command(label='Thu Nhỏ', command=Thu_Nho)
view_menu.add_separator()
view_menu.add_radiobutton(label='100%', value=13, variable=s, command=zoom)
view_menu.add_radiobutton(label='200%', value=26, variable=s, command=zoom)
view_menu.add_radiobutton(label='300%', value=52, variable=s, command=zoom)
view_menu.add_radiobutton(label='400%', value=104, variable=s, command=zoom)
view_menu.add_radiobutton(label='500%', value=208, variable=s, command=zoom)



w.mainloop()

