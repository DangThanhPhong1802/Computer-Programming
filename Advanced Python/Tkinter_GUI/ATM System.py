from tkinter import *
from tkinter import ttk
import tkinter.messagebox

w = Tk()
blank_space = " "
w.title(110*blank_space + "Hệ Thống ATM - PDTBank")
w.geometry("800x760+280+0")
w.configure(background='gainsboro')
#-----------------------------------------------------------------------

def Pin() :
    pinNo = txtReceipt.get("1.0", "end-1c")
    if (pinNo==str("654321")) or (pinNo==str("123456")) :
        txtReceipt.delete("1.0", END)

        txtReceipt.insert(END, '\t\t      ATM' + "\n\n")
        txtReceipt.insert(END, 'Rút Tiền Mặt\t\t\t Vay Tiền' + "\n\n\n\n")
        txtReceipt.insert(END, 'Nhận Tiền Mặt\t\t\t Tiền Gửi' + "\n\n\n\n")
        txtReceipt.insert(END, 'Số Dư\t\t\t Yêu Cầu Mã PIN mới' + "\n\n\n\n")
        txtReceipt.insert(END, 'Bản Sao Kê Rút Gọn\t\t\t In Bản Sao Kê' + "\n\n\n\n")

        btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=vaytien, image=imag_arrow_Right).grid(row=0, column=0, padx=2, pady=2)
        btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=tiengui, image=imag_arrow_Right).grid(row=1, column=0, padx=2, pady=2)
        btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=yeucaumaPINmoi, image=imag_arrow_Right).grid(row=2, column=0, padx=2, pady=2)
        btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=NORMAL, command=bansaoke, image=imag_arrow_Right).grid(row=3, column=0, padx=2, pady=2)

        btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=withdrawcash, image=imag_arrow_Left).grid(row=0, column=0, padx=2, pady=2)
        btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=withdrawcash, image=imag_arrow_Left).grid(row=1, column=0, padx=2, pady=2)
        btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=sodu, image=imag_arrow_Left).grid(row=2, column=0, padx=2, pady=2)
        btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=NORMAL, command=bansaoke, image=imag_arrow_Left).grid(row=3, column=0, padx=2, pady=2)
    else :
        txtReceipt.delete("1.0", END)
        txtReceipt.insert(END, 'Invalid Pin Number' + "\n\n")

def clear() :
    txtReceipt.delete("1.0", END)
    btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, image=imag_arrow_Left).grid(row=0, column=0, padx=2, pady=2)
    btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, image=imag_arrow_Left).grid(row=1, column=0, padx=2, pady=2)
    btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, image=imag_arrow_Left).grid(row=2, column=0, padx=2, pady=2)
    btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, image=imag_arrow_Left).grid(row=3, column=0, padx=2, pady=2)

    btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=imag_arrow_Right).grid(row=0, column=0, padx=2, pady=2)
    btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=imag_arrow_Right).grid(row=1, column=0, padx=2, pady=2)
    btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=imag_arrow_Right).grid(row=2, column=0, padx=2, pady=2)
    btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, image=imag_arrow_Right).grid(row=3, column=0, padx=2, pady=2)

def insert0() :
    value0 = 0
    txtReceipt.insert(END,value0)
def insert1() :
    value1 = 1
    txtReceipt.insert(END, value1)
def insert2() :
    value2 = 2
    txtReceipt.insert(END, value2)
def insert3() :
    value3 = 3
    txtReceipt.insert(END,value3)
def insert4() :
    value4 = 4
    txtReceipt.insert(END, value4)
def insert5() :
    value5 = 5
    txtReceipt.insert(END, value5)
def insert6() :
    value6 = 6
    txtReceipt.insert(END,value6)
def insert7() :
    value7 = 7
    txtReceipt.insert(END, value7)
def insert8() :
    value8 = 8
    txtReceipt.insert(END, value8)
def insert9() :
    value9 = 9
    txtReceipt.insert(END, value9)

def cancel() :
    cancel = tkinter.messagebox.askyesno("ATM", "Confirm if you want to cancel")
    if cancel>0 :
        w.destroy()
        return()

def withdrawcash() :
    Pin()
    txtReceipt.delete("1.0", END)
    txtReceipt.focus_set()

def vaytien() :
    Pin()
    txtReceipt.delete("1.0", END)
    txtReceipt.insert(END, "Vay Tiền VNĐ")
    txtReceipt.focus_set()

def tiengui() :
    Pin()
    txtReceipt.delete("1.0", END)
    txtReceipt.focus_set()

def yeucaumaPINmoi() :
    Pin()
    txtReceipt.delete("1.0", END)
    txtReceipt.insert(END, '\tChào Mừng Bạn Đến Với PDTBank\n')
    txtReceipt.insert(END, 'Mã PIN mới sẽ được gửi qua hệ thống SMS của bạn!\n')
    txtReceipt.insert(END, 'Rút Tiền Mặt\t\t\t Vay Tiền' + "\n\n\n\n")
    txtReceipt.insert(END, 'Nhận Tiền Mặt\t\t\t Tiền Gửi' + "\n\n\n\n")
    txtReceipt.insert(END, 'Số Dư\t\t\t Yêu Cầu Mã PIN mới' + "\n\n\n\n")
    txtReceipt.insert(END, 'Bản Sao Kê Rút Gọn\t\t\t In Bản Sao Kê' + "\n\n\n\n")
    txtReceipt.insert(END, '\t\tCảm Ơn Bạn Đã Sử Dụng PDTBank\n')
def sodu() :
    txtReceipt.delete("1.0", END)
    txtReceipt.insert(END, '\tChào Mừng Bạn Đến Với PDTBank\n')
    txtReceipt.insert(END, '50,000,000 VNĐ' + "\n")
    txtReceipt.insert(END, 'Rút Tiền Mặt\t\t\t Vay Tiền' + "\n\n\n\n")
    txtReceipt.insert(END, 'Nhận Tiền Mặt\t\t\t Tiền Gửi' + "\n\n\n\n")
    txtReceipt.insert(END, 'Số Dư\t\t\t Yêu Cầu Mã PIN mới' + "\n\n\n\n")
    txtReceipt.insert(END, 'Bản Sao Kê Rút Gọn\t\t\t In Bản Sao Kê' + "\n\n\n\n")
    txtReceipt.insert(END, '\t\tCảm Ơn Bạn Đã Sử Dụng PDTBank\n')

def bansaoke() :
    pinNo1 = str(txtReceipt.get("1.0", "end-1c"))
    pinNo2 = str(pinNo1)
    pinNo3 = float(pinNo2)
    pinNo4 = float(50,000,000 - (pinNo3))
    txtReceipt.delete("1.0", END)
    txtReceipt.insert(END, '\n\t'   + str(pinNo4) + '\t\t')
    txtReceipt.insert(END, '\t\t\t\n\n  Số Dư Tài Khoản (VNĐ)' + str(pinNo4) + "\t\t\n\n")
    txtReceipt.insert(END, 'Cho Thuê \t\t\t\t 10,000,000 VNĐ' + "\n\n")
    txtReceipt.insert(END, 'Tèo \t\t\t\t 6,000,000 VNĐ' + "\n\n")
    txtReceipt.insert(END, 'Cho Thuê \t\t\t\t 10,000,000 VNĐ' + "\n\n")
    txtReceipt.insert(END, 'Tú \t\t\t 15,000,000 VNĐ' + "\n\n")
    txtReceipt.insert(END, 'Trinh \t\t\t\t 250,000 VNĐ' + "\n\n")
    txtReceipt.insert(END, 'Đạt \t\t\t\t 1,000,000 VNĐ' + "\n\n")


#-----------------------------------------------------------------------

MainFrame = Frame(w, bd=20, width=784, height=700, relief=RIDGE)
MainFrame.grid()

TopFrame1 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
TopFrame1.grid(row=1, column=0, padx=12)

TopFrame2 = Frame(MainFrame, bd=7, width=734, height=300, relief=RIDGE)
TopFrame2.grid(row=0, column=0, padx=8)

TopFrame2Left = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
TopFrame2Left.grid(row=0, column=0, padx=8)

TopFrame2Mid = Frame(TopFrame2, bd=5, width=200, height=300, relief=RIDGE)
TopFrame2Mid.grid(row=0, column=1, padx=8)

TopFrame2Right = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
TopFrame2Right.grid(row=0, column=2, padx=8)


txtReceipt = Text(TopFrame2Mid, height=17, width=42, bd=12, font=('arial',9,'bold'))
txtReceipt.grid(row=0, column=0)

imag_arrow_Left = PhotoImage(file= 'D:/Ảnh/ATM_Icon/leftArrow.png')
btnArrowL1 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=withdrawcash, image=imag_arrow_Left).grid(row=0, column=0, padx=2, pady=2)
btnArrowL2 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=withdrawcash, image=imag_arrow_Left).grid(row=1, column=0, padx=2, pady=2)
btnArrowL3 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=sodu, image=imag_arrow_Left).grid(row=2, column=0, padx=2, pady=2)
btnArrowL4 = Button(TopFrame2Left, width=160, height=60, state=DISABLED, command=bansaoke, image=imag_arrow_Left).grid(row=3, column=0, padx=2, pady=2)

imag_arrow_Right = PhotoImage(file= 'D:/Ảnh/ATM_Icon/rightArrow.png')
btnArrowR1 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=vaytien, image=imag_arrow_Right).grid(row=0, column=0, padx=2, pady=2)
btnArrowR2 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=tiengui, image=imag_arrow_Right).grid(row=1, column=0, padx=2, pady=2)
btnArrowR3 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=yeucaumaPINmoi, image=imag_arrow_Right).grid(row=2, column=0, padx=2, pady=2)
btnArrowR4 = Button(TopFrame2Right, width=160, height=60, state=DISABLED, command=bansaoke, image=imag_arrow_Right).grid(row=3, column=0, padx=2, pady=2)

imag_1 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/1.png')
btn1 = Button(TopFrame1, width=160, height=60, command=insert1, image=imag_1).grid(row=2, column=0, padx=6, pady=4)
imag_2 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/2.png')
btn2 = Button(TopFrame1, width=160, height=60, command=insert2, image=imag_2).grid(row=2, column=1, padx=6, pady=4)
imag_3 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/3.png')
btn3 = Button(TopFrame1, width=160, height=60, command=insert3, image=imag_3).grid(row=2, column=2, padx=6, pady=4)
imag_clear = PhotoImage(file= 'D:/Ảnh/ATM_Icon/clear.png')
btnclear = Button(TopFrame1, width=160, height=60, command=clear, image=imag_clear).grid(row=2, column=3, padx=6, pady=4)

imag_4 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/4.png')
btn4 = Button(TopFrame1, width=160, height=60, command=insert4, image=imag_4).grid(row=3, column=0, padx=6, pady=4)
imag_5 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/5.png')
btn5 = Button(TopFrame1, width=160, height=60, command=insert5, image=imag_5).grid(row=3, column=1, padx=6, pady=4)
imag_6 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/6.png')
btn6 = Button(TopFrame1, width=160, height=60, command=insert6, image=imag_6).grid(row=3, column=2, padx=6, pady=4)
imag_cancel = PhotoImage(file= 'D:/Ảnh/ATM_Icon/cancel.png')
btncancel = Button(TopFrame1, width=160, height=60, command=cancel, image=imag_cancel).grid(row=3, column=3, padx=6, pady=4)

imag_7 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/7.png')
btn7 = Button(TopFrame1, width=160, height=60, command=insert7, image=imag_7).grid(row=4, column=0, padx=6, pady=4)
imag_8 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/8.png')
btn8 = Button(TopFrame1, width=160, height=60, command=insert8, image=imag_8).grid(row=4, column=1, padx=6, pady=4)
imag_9 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/9.png')
btn9 = Button(TopFrame1, width=160, height=60, command=insert9, image=imag_9).grid(row=4, column=2, padx=6, pady=4)
imag_enter = PhotoImage(file= 'D:/Ảnh/ATM_Icon/enter.png')
btnenter = Button(TopFrame1, width=160, height=60, command=Pin, image=imag_enter).grid(row=4, column=3, padx=6, pady=4)


imag_empty1 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/empty.png')
btnempty1 = Button(TopFrame1, width=160, height=60, image=imag_empty1).grid(row=5, column=0, padx=6, pady=4)
imag_0 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/0.png')
btn0 = Button(TopFrame1, width=160, height=60, command=insert0, image=imag_0).grid(row=5, column=1, padx=6, pady=4)
imag_empty2 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/empty.png')
btnempty2 = Button(TopFrame1, width=160, height=60, image=imag_empty2).grid(row=5, column=2, padx=6, pady=4)
imag_empty3 = PhotoImage(file= 'D:/Ảnh/ATM_Icon/empty.png')
btnempty3 = Button(TopFrame1, width=160, height=60, image=imag_empty3).grid(row=5, column=3, padx=6, pady=4)


#-------------------------------------------------
w.mainloop()

