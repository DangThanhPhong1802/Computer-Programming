#Nhập vào 1 năm bất kỳ, kiểm tra năm đó có phải năm nhuần?
#Biết : năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia hết cho 400
Y=int(input("Nhập năm bất kỳ bạn muốn Year:"))
if (Y%4==0 and Y%100!=0) or Y%400==0 :
    print('Năm nhuần')
else :
    print('Không là năm nhuần')