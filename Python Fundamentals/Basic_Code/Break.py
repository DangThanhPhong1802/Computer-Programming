while True :
    x=int(input("Nhập vào một số:"))
    print(x, "là số chẵn" if x%2==0 else "là số lẻ")
    hỏi=input("Tiếp tục chứ?(c/k):")
    if hỏi=="k":
        break;
print("BYE!Cảm ơn bạn")