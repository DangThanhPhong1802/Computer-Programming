count=sum=0
print("Nhập 5 số >=0 để tính TB:")
while count<5 :
    val=int(input("Nhập giá trị:"))
    if val<0 :
        print("Bạn đã nhập sai quy tắc")
        break
    count+=1  #count=count+1
    sum+=val  #sum=sum+val
else :
    print("Trung Bình=", sum/count)
