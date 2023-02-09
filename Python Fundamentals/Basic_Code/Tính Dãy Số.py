#S(x,n)= x + x^2/2! + x^3/3! + ... + x^n/n1
#Dùng hàm for
x=float(input("Nhập : x="))
n=int(input("Nhập : n="))    #nếu mẫu =0 hay mẫu ko phải số nguyên thì ko giải được
s=0
for i in range(1,n+1) :
    Tử=x**i
    Mẫu=1
    for j in range(1,i+1) :
        Mẫu=Mẫu*j
    s=s+(Tử/Mẫu)
print("s=({0},{1})={2}".format(x,n,s))

