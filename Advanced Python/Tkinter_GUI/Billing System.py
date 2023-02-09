from tkinter import *
w = Tk()
w.title('PDT Shop - Welcome !')
w.geometry('1350x700+0+0')
title1 = Label(w, text='BILLING SYSTEM', bg='#074463', fg='white', bd=12, relief=GROOVE, font=('times new roman', 30, 'bold'), pady=2).pack(fill=X)

#----------------------------Customer Details Frame--------------------
F1 = LabelFrame(w, text='Customer Details', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'), fg='gold', bg='#074463')
F1.place(x=0, y=80, relwidth=1)

cname_lbl = Label(F1, text='Customer Name', bg='#074463', fg='white', font=('times new roman', 18, 'bold')).grid(row=0, column=0, padx=20, pady=5)
cname_txt = Entry(F1, width=15, bd=7, relief=SUNKEN, font=('arial', 15)).grid(row=0, column=1, pady=5, padx=10)

cphn_lbl = Label(F1, text='Phone No.', bg='#074463', fg='white', font=('times new roman', 18, 'bold')).grid(row=0, column=2, padx=20, pady=5)
cphn_txt = Entry(F1, width=15, bd=7, relief=SUNKEN, font=('arial', 15)).grid(row=0, column=3, pady=5, padx=10)

cbill_lbl = Label(F1, text='Bill Number', bg='#074463', fg='white', font=('times new roman', 18, 'bold')).grid(row=0, column=4, padx=20, pady=5)
cbill_txt = Entry(F1, width=15, bd=7, relief=SUNKEN, font=('arial', 15)).grid(row=0, column=5, pady=5, padx=10)

bill_btn = Button(F1, text='Search', width=10, bd=7, font=('arial', 12, 'bold')).grid(row=0, column=6, pady=10, padx=10)

#-----------------------Cosmetics Frame---------------------------
F2 = LabelFrame(w, text='Cosmetics', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'), fg='gold', bg='#074463')
F2.place(x=5, y=180, width=325, height=380)

bath_lbl = Label(F2, text='Bath Soap', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=0, column=0, padx=10 ,pady=10 ,sticky='w')
bath_txt = Entry(F2, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1 ,padx=10, pady=10)

FaceCream_lbl = Label(F2, text='Face Cream', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=1, column=0, padx=10 ,pady=10 ,sticky='w')
FaceCream_txt = Entry(F2, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1 ,padx=10, pady=10)

FaceW_lbl = Label(F2, text='Face Wash', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=2, column=0, padx=10 ,pady=10 ,sticky='w')
FaceW_txt = Entry(F2, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1 ,padx=10, pady=10)

HairS_lbl = Label(F2, text='Hair Spray', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=3, column=0, padx=10 ,pady=10 ,sticky='w')
HairS_txt = Entry(F2, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1 ,padx=10, pady=10)

HairG_lbl = Label(F2, text='Hair Gell', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=4, column=0, padx=10 ,pady=10 ,sticky='w')
HairG_txt = Entry(F2, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1 ,padx=10, pady=10)

Body_lbl = Label(F2, text='Body Loshan', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=5, column=0, padx=10 ,pady=10 ,sticky='w')
Body_txt = Entry(F2, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1 ,padx=10, pady=10)

#-------------------Grocery Frame---------------------
F3 = LabelFrame(w, text='Grocery', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'), fg='gold', bg='#074463')
F3.place(x=340, y=180, width=325, height=380)

Rice_lbl = Label(F3, text='Rice', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=0, column=0, padx=10 ,pady=10 ,sticky='w')
Rice_txt = Entry(F3, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1 ,padx=10, pady=10)

FO_lbl = Label(F3, text='Food Oil', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=1, column=0, padx=10 ,pady=10 ,sticky='w')
FO_txt = Entry(F3, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1 ,padx=10, pady=10)

Da_lbl = Label(F3, text='Daal', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=2, column=0, padx=10 ,pady=10 ,sticky='w')
Da_txt = Entry(F3, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1 ,padx=10, pady=10)

Wheat_lbl = Label(F3, text='Wheat', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=3, column=0, padx=10 ,pady=10 ,sticky='w')
Wheat_txt = Entry(F3, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1 ,padx=10, pady=10)

Su_lbl = Label(F3, text='Sugar', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=4, column=0, padx=10 ,pady=10 ,sticky='w')
Su_txt = Entry(F3, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1 ,padx=10, pady=10)

Tea_lbl = Label(F3, text='Tea', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=5, column=0, padx=10 ,pady=10 ,sticky='w')
Tea_txt = Entry(F3, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1 ,padx=10, pady=10)

#-------------------Cold Drink Frame---------------------
F4 = LabelFrame(w, text='Cold Drinks', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'), fg='gold', bg='#074463')
F4.place(x=675, y=180, width=325, height=380)

Ma_lbl = Label(F4, text='Maza', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=0, column=0, padx=10 ,pady=10 ,sticky='w')
Ma_txt = Entry(F4, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1 ,padx=10, pady=10)

Co_lbl = Label(F4, text='Cock', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=1, column=0, padx=10 ,pady=10 ,sticky='w')
Co_txt = Entry(F4, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1 ,padx=10, pady=10)

Fr_lbl = Label(F4, text='Frooti', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=2, column=0, padx=10 ,pady=10 ,sticky='w')
Fr_txt = Entry(F4, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1 ,padx=10, pady=10)

ThU_lbl = Label(F4, text='Thumbs Up', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=3, column=0, padx=10 ,pady=10 ,sticky='w')
ThU_txt = Entry(F4, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1 ,padx=10, pady=10)

Lim_lbl = Label(F4, text='Limca', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=4, column=0, padx=10 ,pady=10 ,sticky='w')
Lim_txt = Entry(F4, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1 ,padx=10, pady=10)

Spr_lbl = Label(F4, text='Sprite', font=('times new roman', 16, 'bold'), bg='#074463', fg='lightgreen').grid(row=5, column=0, padx=10 ,pady=10 ,sticky='w')
Spr_txt = Entry(F4, width=10, font=('times new roman', 16, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1 ,padx=10, pady=10)

#----------------Bill Area-------------------------------
F5 = Frame(w, bd=10, relief=GROOVE)
F5.place(x=1010, y=180, width=520, height=380)
bill_title = Label(F5, text='Bill Area', font=('arial', 15, 'bold'), bd=7, relief=GROOVE).pack(fill=X)
scrol_y = Scrollbar(F5, orient=VERTICAL)
txtArea = Text(F5,yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=txtArea.yview)
txtArea.pack(fill=BOTH, expand=1)

#-----------------------Button Frame-------------------------
F6 = LabelFrame(w, text='Bill Menu', bd=10, relief=GROOVE, font=('times new roman', 15, 'bold'), fg='gold', bg='#074463')
F6.place(x=0, y=560, relwidth=1 ,height=240)

m1_lbl = Label(F6, text='Total Cosmetic Price', bg='#074463', fg='white', font=('times new roman', 14, 'bold')).grid(row=0, column=0, padx=20, pady=1, sticky='w')
m1_txt = Entry(F6, width=18, font=('arial', 10, 'bold'), bd=7, relief=SUNKEN).grid(row=0, column=1, padx=10 ,pady=1)

m2_lbl = Label(F6, text='Total Grocery Price', bg='#074463', fg='white', font=('times new roman', 14, 'bold')).grid(row=1, column=0, padx=20, pady=1, sticky='w')
m2_txt = Entry(F6, width=18, font=('arial', 10, 'bold'), bd=7, relief=SUNKEN).grid(row=1, column=1, padx=10 ,pady=1)

m3_lbl = Label(F6, text='Total Cold Drinks Price', bg='#074463', fg='white', font=('times new roman', 14, 'bold')).grid(row=2, column=0, padx=20, pady=1, sticky='w')
m3_txt = Entry(F6, width=18, font=('arial', 10, 'bold'), bd=7, relief=SUNKEN).grid(row=2, column=1, padx=10 ,pady=1)

m4_lbl = Label(F6, text='Cosmetic Tax', bg='#074463', fg='white', font=('times new roman', 14, 'bold')).grid(row=0, column=2, padx=20, pady=1, sticky='w')
m4_txt = Entry(F6, width=18, font=('arial', 10, 'bold'), bd=7, relief=SUNKEN).grid(row=0, column=3, padx=10 ,pady=1)

m5_lbl = Label(F6, text='Grocery Tax', bg='#074463', fg='white', font=('times new roman', 14, 'bold')).grid(row=1, column=2, padx=20, pady=1, sticky='w')
m5_txt = Entry(F6, width=18, font=('arial', 10, 'bold'), bd=7, relief=SUNKEN).grid(row=1, column=3, padx=10 ,pady=1)

m6_lbl = Label(F6, text='Cold Drinks Tax', bg='#074463', fg='white', font=('times new roman', 14, 'bold')).grid(row=2, column=2, padx=20, pady=1, sticky='w')
m6_txt = Entry(F6, width=18, font=('arial', 10, 'bold'), bd=7, relief=SUNKEN).grid(row=2, column=3, padx=10 ,pady=1)

btn_F = Frame(F6, bd=7, relief=GROOVE)
btn_F.place(x=850, width=650, height=105)

title2 = Label(F6, text='PHONG DANG THANH', font=('Times New Roman', 20, 'bold'), bg='#074463', fg='yellow').grid(row=8, column=3, pady=10)

total_btn = Button(btn_F, text='Total', bg='cadetblue', fg='white', bd=2, pady=15, width=10, font=('arial', 15, 'bold')).grid(row=0, column=0, padx=15, pady=5)
gbill_btn = Button(btn_F, text='Genrate Bill', bg='cadetblue', fg='white', bd=2, pady=15, width=10, font=('arial', 15, 'bold')).grid(row=0, column=1, padx=15, pady=5)
clear_btn = Button(btn_F, text='Clear', bg='cadetblue', fg='white', bd=2, pady=15, width=10, font=('arial', 15, 'bold')).grid(row=0, column=2, padx=15, pady=5)
exit_btn = Button(btn_F, text='Exit', bg='cadetblue', fg='white', bd=2, pady=15, width=10, font=('arial', 15, 'bold')).grid(row=0, column=3, padx=15, pady=5)














w.mainloop()