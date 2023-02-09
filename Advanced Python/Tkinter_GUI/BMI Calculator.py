from tkinter import *
from functools import partial
import tkinter as tk


window=tk.Tk()
window.title("BMI Calculator")
window.geometry("400x300+10+10")
#-----------------------------------------------Tính toán ---------------------------------------------
def bmi(label_result, ht, wt):
    ht = float((ht.get()))
    wt = float((wt.get()))
    ht=ht/100
    bmi=float(wt / (ht*ht))
    bmi=round(bmi,1)

    conclusion=""

    if bmi<18.5:
      conclusion="Under Weight"
    elif bmi>18.4 and bmi<=24.9:
      conclusion="Normal"
    elif bmi>24.9 and bmi<=29.9:
      conclusion="Over Weight"
    else:
      conclusion="Obesity"

    output= "BMI = "+str(bmi)+"\n" +conclusion

    label_result.config(text=output)
    return
#------------------------------------------Giao Diện-----------------------------------------------------------
ht = tk.StringVar()
wt = tk.StringVar()

A=Label(window, text="Adult BMI Calculator", foreground='white', background='blue', font=('arial',18,'bold')).grid(row=0, padx=10, pady=10)

heightText=Label(window,text="Height : Centimeters", font=('arial',14)).grid(row=1, column=0, padx=10, pady=10)
height=Entry(window, textvariable = ht ).grid(row=1, column=1, padx=10,pady=10)

weightText=Label(window,text="Weight : Kilograms", font=('arial',14)).grid(row=2, column=0, padx=10, pady=10)
weight=Entry(window, textvariable = wt ).grid(row=2, column=1, padx=10, pady=10)

labelResult = tk.Label(window)
labelResult.grid(row=4, column=0)

bmi = partial(bmi, labelResult, ht, wt)
bmi =Button(window,text="Calculate", foreground='white', background='blue', font=('arial',14,'bold'),command = bmi).grid(row=3, column=0, padx=10, pady=10)



window.mainloop()
