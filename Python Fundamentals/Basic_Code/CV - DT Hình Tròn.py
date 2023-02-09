#Nhập r . Tính và xuất ra màn CV - DT đường tròn
#Biết CV=2*pi*r ; DT=pi*r*r
import math

r=float(input("Mời bạn nhập r:"))
CV=2*math.pi*r
DT=(r**2)*math.pi
print("C=", CV)
print("S=", DT)

try:
    r = float(input("Mời bạn nhập r:"))
    CV = 2 * math.pi * r
    DT = (r ** 2) * math.pi
    print("C=", CV)
    print("S=", DT)
except:
    print("Bị lỗi!")

r=float(input("Mời bạn nhập r:"))
CV=2*math.pi*r
DT=(pow(r,2))*math.pi
print("C=", CV)
print("S=", DT)
