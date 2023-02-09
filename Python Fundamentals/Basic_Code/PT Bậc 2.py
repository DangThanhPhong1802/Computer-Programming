#Giải phương trình : ax^2 + bx + c = 0 (a#0)
import math

a=float(input("Nhập hệ số: a="))
b=float(input("Nhập hệ số: b="))
c=float(input("Nhập hệ số: c="))
if a==0 :  #bx+c=0
    if b==0 and c==0 :
        print("VSN")
    elif b==0 and c!=0 :
        print("VN")
    else :
        x= -b/a
        print("x=", x)
else :  #ax^2+bx+c=0
    D= b**2 - 4*a*c
    print("D=", D)
    if D>0 :
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        print("PT có 2 no pb:","x1=", x1, "x2=", x2)
    elif D==0 :
        x= -b/(2*a)
        print("PT có no kép:", "x1=x2=", x)
    else :
        print("PT VN")
