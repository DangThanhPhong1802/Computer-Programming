a=int(input("Nhập : a="))
s=0
for n in range(5,10) :
    if 4%a==1 :
        print("Ngừng for")
        break
    s=s+n
else :
    print("Sum=", s)