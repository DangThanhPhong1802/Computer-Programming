from random import randrange
while True :
    somay=randrange(1,101) #Chạy từ 1-100
    solandoan=0
    Thắng = False
    while solandoan < 7 :
        solandoan+=1
        print("Lần đoán thứ:", solandoan)
        songuoi = int(input("Máy đoán [1...100], mời bạn đoán số :"))
        if somay == songuoi :
            print("Congratulation!, số máy là:", somay)
            Thắng = True
            break
        if somay > songuoi :
            print("Bạn đã đoán sai, số máy > số bạn đoán")
        elif somay < songuoi :
            print("Bạn đã đoán sai, số máy < số bạn đoán")
    if Thắng == False :
        print("GAME OVER!Thank you very much!See you again!, số máy=", somay)
    hoi=input("Bạn có muốn tiếp tục không?(c/k)")
    if hoi=="k" :
        break
print("Cảm ơm bạn đã chơi cùng tôi!")