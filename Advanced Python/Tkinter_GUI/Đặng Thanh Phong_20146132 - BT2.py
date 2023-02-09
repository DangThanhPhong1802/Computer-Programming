from tkinter import *
w = Tk()
w.geometry('700x400+400+200')
w.title('BMI CALCULATOR')

x1=IntVar()

L1 = Label(w, text="CHIỀU CAO :", font=('arial',15))
L1.grid(row=0, column=0, padx=10, pady=10)
E1 = Entry(w, width=12 , font=('arial',15))
E1.grid(row=1, column=0, padx=10, pady=10)

L2 = Label(w, text="CÂN NẶNG :", font=('arial',15))
L2.grid(row=2, column=0, padx=10, pady=10)
E2 = Entry(w, width=12 , font=('arial',15))
E2.grid(row=3, column=0, padx=10, pady=10)


def view():
    if (x1.get()) == 1 :
        L1.configure(text='CHIỀU CAO (cm)')
        L2.configure(text='CÂN NẶNG (kg)')
    if (x1.get()) == 2 :
        L1.configure(text='CHIỀU CAO (inches)')
        L2.configure(text='CÂN NẶNG (pounds)')
E3 = Radiobutton(w, text='Metric', font=('arial, 15'), value=1, variable=x1, command=view)
E3.grid(row=1, column=1, padx=10, pady=10)
E4 = Radiobutton(w, text='English', font=('arial, 15'), value=2, variable=x1, command=view)
E4.grid(row=2, column=1, padx=10, pady=10)


def B1_click():
    h=float(E1.get())
    m=float(E2.get())
    if (x1.get()) == 1 :
        cao = h/100
        nang = m
        bmi_1 = round(nang/(cao*cao), 2)
        ##-----------------Thang phân loại theo IDI & WPRO (châu Á)--------------------##
        if bmi_1 >= 18.5 and bmi_1 <= 22.9:
            conclusion = "Bình thường"
        elif bmi_1 >= 23 and bmi_1 <= 24.9:
            conclusion = "Tiền béo phì"
        elif bmi_1 >= 25 and bmi_1 <= 29.9:
            conclusion = "Béo phì độ I"
        else:
            conclusion = "Béo phì độ II"
        output_1 = "BMI = " + str(bmi_1) + " => " + conclusion
        L3.config(text=output_1)
        return

    if (x1.get()) == 2 :
        bmi_2 = round((m/(h*h))*703, 2)
        ##-----------------Thang phân loại theo WHO (châu Âu)--------------------##
        if bmi_2 < 18.5:
            conclusion = "Cân nặng thấp (gầy)"
        elif bmi_2 >= 18.4 and bmi_2 <= 24.9:
            conclusion = "Bình thường"
        elif bmi_2 >= 25 and bmi_2 <= 29.9:
            conclusion = "Tiền béo phì"
        elif bmi_2 >= 30 and bmi_2 <= 34.9:
            conclusion = "Béo phì độ I"
        elif bmi_2 >= 35 and bmi_2 <= 39.9:
            conclusion = "Béo phì độ II"
        else:
            conclusion = "Béo phì độ III"
        output_2 = "BMI = " + str(bmi_2) + " => " + conclusion
        L3.config(text=output_2)
        return

B1 = Button(w, text="CALCULATE", fg='white', bg='blue', font=('arial',15), command=B1_click)
B1.grid(row=4, column=1, padx=10, pady=20)


L3 = Label(w, text='BMI =', fg='green', font=('arial',15))
L3.grid(row=5, column=1, padx=10, pady=10)

L4 = Label(w, text='ĐẶNG THANH PHONG', font=('arial',15, 'bold'), bg='crimson', fg='yellow')
L4.grid(row=6, column=1, padx=10, pady=20)

w.mainloop()

