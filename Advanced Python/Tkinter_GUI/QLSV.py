from tkinter import *
from tkinter import ttk
import pymysql


w = Tk()
w.title('Hệ Thống Quản Lý Sinh Viên - PDT University')
w.geometry('1350x700+0+0')
img = PhotoImage(file='D:/Ảnh/Education.png')
w.iconphoto(False, img)
#-------------------------------------------- Tiêu đề cho Tkinter --------------------------------------------------
title = Label(w, text="HỆ THỐNG QUẢN LÝ SINH VIÊN", bd=10, relief=GROOVE, font=('times new roman',40, 'bold'), bg='blue', fg='yellow')
title.pack(side=TOP,fill=X)

#---------------------------------------------Giá Trị Nhập Vào--------------------------------------------
mssv_var = StringVar()
name_var = StringVar()
birth_var = StringVar()
gender_var = StringVar()
email_var = StringVar()
address_var = StringVar()


Manage_Frame = Frame(w, bd=4, relief=RIDGE, bg='orange')
Manage_Frame.place(x=20, y=100, width=450, height=580)

#------------------------------------------Khung Nhập Thông Tin-----------------------------------------------------

m_title = Label(Manage_Frame, text="Quản Lý Sinh Viên", bg='orange', fg='white', font=('times new roman',30,'bold'))
m_title.grid(row=0, columnspan=2, pady=20)

lbl_mssv = Label(Manage_Frame, text="MSSV", bg='orange', fg='white', font=('times new roman', 20,'bold'))
lbl_mssv.grid(row=1, column=0, pady=10, padx=20, sticky='w')
txt_mssv = Entry(Manage_Frame, textvariable=mssv_var, bd=5, relief=GROOVE, font=('times new roman',15,'bold'))
txt_mssv.grid(row=1, column=1, pady=10, padx=20, sticky='w')

lbl_name = Label(Manage_Frame, text='Họ và Tên', bg='orange', fg='white', font=('times new roman', 20,'bold'))
lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky='w')
txt_name = Entry(Manage_Frame, textvariable=name_var, bd=5, relief=GROOVE, font=('times new roman',15,'bold'))
txt_name.grid(row=2, column=1, pady=10, padx=20, sticky='w')

lbl_birth = Label(Manage_Frame, text='Năm Sinh', bg='orange', fg='white', font=('times new roman', 20,'bold'))
lbl_birth.grid(row=3, column=0, pady=10, padx=20, sticky='w')
txt_birth = Entry(Manage_Frame, textvariable=birth_var, bd=5, relief=GROOVE, font=('times new roman',15,'bold'))
txt_birth.grid(row=3, column=1, pady=10, padx=20, sticky='w')

lbl_gender = Label(Manage_Frame, text='Giới Tính', bg='orange', fg='white', font=('times new roman', 20,'bold'))
lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky='w')
txt_gender = Entry(Manage_Frame, textvariable=gender_var, bd=5, relief=GROOVE, font=('times new roman',15,'bold'))
txt_gender.grid(row=4, column=1, pady=10, padx=20, sticky='w')
combo_gender = ttk.Combobox(Manage_Frame, state='readonly', font=('times new roman',13,'bold'))
combo_gender['values'] = ('Nam', 'Nữ', 'Khác')
combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky='w')

lbl_email = Label(Manage_Frame, text='Email', bg='orange', fg='white', font=('times new roman', 20,'bold'))
lbl_email.grid(row=5, column=0, pady=10, padx=20, sticky='w')
txt_email = Entry(Manage_Frame, textvariable=email_var, bd=5, relief=GROOVE, font=('times new roman',15,'bold'))
txt_email.grid(row=5, column=1, pady=10, padx=20, sticky='w')

lbl_address = Label(Manage_Frame, text='Địa Chỉ', bg='orange', fg='white', font=('times new roman', 20,'bold'))
lbl_address.grid(row=6, column=0, pady=10, padx=20, sticky='w')
txt_address = Text(Manage_Frame, width=30, height=4, font=('times new roman',10,'bold'))
txt_address.grid(row=6, column=1, pady=10, padx=20, sticky='w')

#------------------------------------------------Tạo các nút chỉnh sửa---------------------------------------------
btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg='orange')
btn_Frame.place(x=15, y=500, width=420)

Addbtn = Button(btn_Frame, text='Thêm Mới', width=10).grid(row=0, column=0, padx=10, pady=10)
Updatebtn = Button(btn_Frame, text='Chỉnh Sửa', width=10).grid(row=0, column=1, padx=10, pady=10)
Deletebtn = Button(btn_Frame, text='Xóa Toàn Bộ', width=10).grid(row=0, column=2, padx=10, pady=10)
Clearbtn = Button(btn_Frame, text='Xóa', width=10).grid(row=0, column=3, padx=10, pady=10)


#-------------------------------------------------Tạo Khung Nhận Dữ Liệu-----------------------------------------------
Detail_Frame = Frame(w, bd=4, relief=RIDGE, bg='cyan')
Detail_Frame.place(x=500, y=100, width=800, height=580)

lbl_search = Label(Detail_Frame, text='Tìm Kiếm', bg='cyan', fg='red', font=('times new roman', 20,'bold'))
lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky='w')
combo_search = ttk.Combobox(Detail_Frame, width=10, state='readonly', font=('times new roman',13,'bold'))
combo_search['values'] = ('MSSV', 'Họ và Tên', 'Email')
combo_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')
txt_search = Entry(Detail_Frame, width=15, bd=5, relief=GROOVE, font=('times new roman',14,'bold'))
txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')
searchbtn = Button(Detail_Frame, text='Tìm Kiếm', width=10, pady=5).grid(row=0, column=3, padx=10, pady=10)
showallbtn = Button(Detail_Frame, text='Hiển Thị Tất Cả', width=14, pady=5).grid(row=0, column=4, padx=10, pady=10)

               #------------------------Bảng Dữ Liệu----------------------

Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg='cyan')
Table_Frame.place(x=10, y=70, width=760, height=500)
scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
Student_table = ttk.Treeview(Table_Frame, columns=('mssv', 'name', 'birth', 'gender', 'email', 'address'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_x.config(command=Student_table.xview)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.config(command=Student_table.yview)
Student_table.heading("mssv", text="MSSV")
Student_table.heading("name", text="Họ và Tên")
Student_table.heading("birth", text="Năm Sinh")
Student_table.heading("gender", text="Giới Tính")
Student_table.heading("email", text="Email")
Student_table.heading("address", text="Đ/C")
Student_table['show'] = 'headings'
Student_table.pack(fill=BOTH, expand=1)








w.mainloop()