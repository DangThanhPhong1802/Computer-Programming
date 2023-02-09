#Viết chương trình nhập vào điểm 3 môn T-L-H của 1 HS
#In ra ĐTB với 2 số lẻ thập phân
try:
    T=float(input("Điểm Toán:"))
    L=float(input("Điểm Lý:"))
    H=float(input("Điểm Hóa:"))
    ĐTB=round((T+L+H)/3 , 2)
    print("Điểm TB = ", ĐTB)
except:
    print("Bị lỗi!")

print("-"*20)

T=float(input("Điểm Toán:"))
L=float(input("Điểm Lý:"))
H=float(input("Điểm Hóa:"))
ĐTB=(T+L+H)/3
print("Điểm TB = ", round(ĐTB,2))