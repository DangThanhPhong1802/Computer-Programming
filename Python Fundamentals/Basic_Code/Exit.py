while True :
    print("Nhập số: n=")
    n=int(input())
    Đếm=0
    for i in range(1,n+1)
        if n%i==0 :
            Đếm+=1
        if Đếm==2 :
            print(n, "là số nguyên tố")
        else :
            print(n, "không là số nguyên tố")
        print("Bạn có muốn tiếp tục không?(c/k):")
        if input()== 'k' :
            exit()
# Thay bằng Break thì nó thoát nhưng tiếp tục chạy
#Còn exit thì thoát và dừng luôn, không xuất "See you again!"
print("See you again!")