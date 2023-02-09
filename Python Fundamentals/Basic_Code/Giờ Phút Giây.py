#Nhập vào số giây t bất kỳ. Tính và xuất ra dạng Giờ:Phút:Giây
#VD: Nhập 3750 thì xuất 1:2:30 AM
#Công thức : H=(t//3600)%24 ; M=(t%3600)//60 ; S=(t%3600)%60
try:
    t=int(input("Mời bạn nhập số giây t:"))
    H=(t//3600)%24
    M=(t%3600)//60
    S=(t%3600)%60
    print("Giờ:Phút:Giây=", H, ":", M, ":", S)
except:
    print("Bị lỗi!")