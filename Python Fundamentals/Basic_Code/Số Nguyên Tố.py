#Số nguyên tố là số chỉ chia hết cho 1 và chính nó
#Nếu còn chia hết cho số khác thì KHÔNG là SNT
#Số 0 và 1 không là SNT

#Dùng vòng While để kiểm tra SNT
while True :
    n=int(input("Nhập số nguyên dương : n="))
    Đếm=0
    for i in range(1,n+1) :
        if n%i==0 :
            Đếm+=1
    if Đếm==2 :  #Chỉ có 2 ước số là chia hết cho 1 và chính nó
        print(n, "là số nguyên tố")
    else :
        print(n, "không là số nguyên tố")
    Hỏi=input("Bạn có muốn tiếp tục không?(c/k):")
    if Hỏi=="k" :
        break  #Thoát phần mềm
print("Bạn đã dừng lại phép tính ! Cảm ơn bạn! Hẹn Gặp Lại!")

