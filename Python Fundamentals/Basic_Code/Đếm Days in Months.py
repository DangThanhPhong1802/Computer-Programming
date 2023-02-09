#Nhập vào 1 tháng, xuất tháng đó có bao nhiêu ngày
#Nếu là tháng 2 thì nhập thêm năm. Nhuần thì 29 ngày, không thì 28 ngày
#Biết tháng (1-3-5-7-8-10-12) có 31 ngày, (4-6-9-11) có 30 ngày
M=int(input("Nhập vào tháng bất kỳ:"))
if M in (1,3,5,7,8,10,12) :
    print("Tháng", M, "có 31 ngày")
elif M in (4,6,9,11) :
    print("Tháng", M, "có 30 ngày")
elif M==2 :
    Y=int(input("Năm bất kỳ:"))
    if (Y%4==0 and Y%100!=0) or Y%400==0 :
        print('Năm Nhuần - Có 29 ngày')
    else :
        print('Không là năm nhuần - Có 28 ngày')
else :
    print("Rất tiếc! Tháng bạn vừa nhập không hợp lệ")