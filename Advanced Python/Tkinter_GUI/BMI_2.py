from tkinter import *
W=Tk()
W.geometry('300x400+400+200')
W.title('BMI Calculator')


L1 = Label(master=W, text="Height : Centimeters", font=('arial',15))
L1.place(x=60,y=40)

E1 = Entry(master=W, width=12 , font=('arial',15))
E1.place(x=60,y=80)

L2 = Label(master=W, text="Weight : Kilograms", font=('arial',15))
L2.place(x=60,y=140)

E2 = Entry(master=W, width=12 , font=('arial',15))
E2.place(x=60,y=180)

def B1_click():
    h=float(E1.get())/100
    m=float(E2.get())
    bmi = round(m/(h*h), 1)
    L3.configure(text='BMI :' + str(bmi))
B1 = Button(master=W, text="Calculate", fg='white', bg='blue', font=('arial',15), command=B1_click)
B1.place(x=60,y=240)

L3 = Label(w, text='BMI :', fg='green')
L3.place(x=60,y=300)

w.mainloop()