n=int(input("Nhập n:"))
s=0
if n%2==0 :  #n chẵn
    for x in range(2,n+1,2) :
        s=s+x
elif n%2!=0 :  #n lẻ
    for x in range(1,n+1,2) :
        s=s+x
print("Tổng s=", s)

#Giải thích :
#n=8 : range(2,9,2) => x=2;4;6;8 => s=20
  # Cột x          Cột s=s+x
  #   2                0+2=2
  #   4                2+4=6
  #   6                6+6=12
  #   8                12+8=20
#n=7 : range(1,8,2) => x=1;3;5;7 => s= 16 (Tương tự)