z= -1
while z<1 or z>10 :
     z=int(input("Nhập giá trị [1..10]: z="))
print(z**2)

print("-"*20)

#S=1+2+3+...+n
print("Nhập n:")
n=int(input())
S=0
i=1
while i<=n :
    S=S+i
    i=i+1
print("Tổng = ", S)