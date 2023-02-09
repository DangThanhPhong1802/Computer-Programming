n=int(input("Nhập N:"))
s=0
for x in range(1,n+1):
    s=s+x
    if s>=15:
        break
print("s=", s)

#VD : N=8 => range(1,9) => si={1;2;3;4;5;6;7;8}
#Thay vì cộng đến 8 thì s=36, nhưng vì s>=15 nên dừng ở si=5 (s=15)
#Nếu đk s>15 thì dừng lại ở si=6 (s=21)
