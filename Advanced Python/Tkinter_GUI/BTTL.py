#Tính biểu thức
import math
print((2+3**2)/((5/2)+2**5))
print(math.log(27,3))
print(math.sin(3*math.pi/6))
print(math.exp((2*math.pi)/math.log(4)))
print(math.sqrt(5**6+math.factorial(3)))

print(80*'-')

#Tính DT tam giác
c=10
h=6
DT = 1/2 * h*c
print("Diện tích của tam giác là : ", DT, "cm2")

print(80*'-')

#Tính DT hình tròn
d=8
DT = math.pi*((d/2)**2)
print("DT hình tròn là: ", DT, "cm2")

print(80*'-')

#KT biểu thức Đ/S
A = (math.sin(math.pi))**2 + (math.cos(math.pi))**2
B = (math.sin(math.pi/2))**2 + (math.cos(math.pi/2))**2
C = (math.sin(4*math.pi/3))**2 + (math.cos(4*math.pi/3))**2
if A==1 :
    print('A:TRUE')
else :
    print('A:FALSE')
if B==1 :
    print('B:TRUE')
else :
    print('B:FALSE')
if C==1 :
    print('C:TRUE')
else :
    print('C:FALSE')

print(80*'-')

#Tìm nghiệm PT B2
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

print(80*'-')

#Tìm số có trị tuyệt đối nhỏ hơn 10
x=float(input('Nhập : x='))
y=float(input('Nhập : y='))
z=float(input('Nhập : z='))
if abs(x)<10 :
    print('Số x có |...|<10 là:', x)
else :
    print('Không có số x')
if abs(y)<10 :
    print('Số y có |...|<10 là:', y)
else :
    print('Không có số y')
if abs(z)<10 :
    print('Số z có |...|<10 là:', z)
else :
    print('Không có số z')

print(80*'-')

#Tìm Min/Max từ 5 số đã nhập
a = float(input("- So thu 1: "))
b = float(input("- So thu 2: "))
c = float(input("- So thu 3: "))
d = float(input("- So thu 4: "))
e = float(input("- So thu 5: "))
list = [a,b,c,d,e]
print('Số lớn nhất trong 5 số là : ', max(list))
print('Số nhỏ nhất trong 5 số là : ' ,min(list))
