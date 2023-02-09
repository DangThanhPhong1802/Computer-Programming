#Kt tính hợp lệ của tam giác
#Tính DT tam giác theo CT Herong
from math import sqrt

a=float(input("Nhập cạnh: a="))
b=float(input("Nhập cạnh: b="))
c=float(input("Nhập cạnh: c="))
cv=a+b+c
p=cv/2
S=sqrt(p*(p-a)*(p-b)*(p-c))
if (a<=0 or b<=0 or c<=0) or (a+b)<=c or (a+c)<=b or (b+c)<=a :
    print("Giá trị cạnh không hợp lệ!Mời nhập lại")
else :
    print("Diện tích tam giác là : S=", S)