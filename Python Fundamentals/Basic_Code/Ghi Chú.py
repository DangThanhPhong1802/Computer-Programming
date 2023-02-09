
#Ghi chú 1 dòng - Chương trình xuất ra màn hình kết quả của c khi biết a và b
a=18
b=2
c=a-b
if  c<0 :
    print(c)
else :
    print(c*2)



"""
(Ghi chú nhiều dòng - 3 nháy đôi)
Giải phương trình bậc 1 : ax+b=0
Có 3 TH để biện luận
Nếu hệ số a=0 và hệ số b=0 ==> vô số nghiệm
Nếu hệ số a=0 và hệ số b !=0 ==> vô nghiệm
Nếu hệ số a !=0 ==> có nghiệm -b/a
"""
a=0
b=113
if a==0 and b==0 :
    print("Vô số nghiệm")
elif a==0 and b !=0 :
    print("Vô nghiệm")
else :
    print("Có nghiệm X=", -b/a)



'''
(Ghi chú nhiều dòng - 3 nháy đơn)
Đây là lệnh kiểm tra năm nhuần year
Năm nhuần là năm chia hết cho 4 nhưng không chia hết cho 100 hoặc chia hết cho 400
'''
year=2016
if (year % 4==0 and year % 100 !=0) or year % 400==0 :
   print(year, "Là năm nhuần")
else :
   print(year, "Không là năm nhuần")