n=15
s=0
for x in range(1,n+1,2) :
    if x==3 or x==11 :
        continue
    s=s+x
print("S=", s)

#range(1,16,2) => x={1,3,5,7,9,11,13,15}
#Vì đến x=3 hoặc 11 sẽ bỏ qua nên x={1,5,7,9,13,15}
#S=50