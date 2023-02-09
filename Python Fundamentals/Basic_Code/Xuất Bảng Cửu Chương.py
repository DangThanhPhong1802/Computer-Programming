#Xuất từ cửu chương 2 đến 9
#Có : 8 cột ; 10 dòng
#Căn đều giữa 2 ký tự chữ số cho đẹp : VD :  2* 4 = 8
#                                            2* 5 =10
#Căn đều bên phải giữa số 8 và 10, bạn để ý
#Dữ liệu xuất ra max là 2 ký tự, do bảng cửu chương KQ không có max là 3 chữ số

#Dùng 2 vòng lặp for lồng nhau
for i in range(1,11) :  #Chạy từ 1 đến 10 => 10 cột
    for j in range(2,10) : #Chạy từ 2 đến 9 => Cửu chương 2 đến 9
        line = "{0}*{1:>2} = {2:>2}".format(j,i,i*j)
        #{0}: ký tự đầu ko cần căn phải, vì chỉ có 1 ký tự
        #{1:>2}: 2 ký tự, căn lề phải 2 ký tự
        print(line, end='\t')
    print()