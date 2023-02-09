#Dùng 2 vòng for lồng nhau
n=int(input("Nhập chiều cao : h="))
for  i  in  range(n) :
    for  j  in  range(n) :
        if  j==0  or  i==j  or  j==n-1 :
            print("*", end= ' ')
        else :
            print(" ", end= ' ')
    print()

print("_"*50)

n=int(input("Nhập chiều cao : h="))
for  i  in  range(n) :
    for  j  in  range(n) :
        if  j==0  or  i==j  or  i==n-1 :
            print("*", end= ' ')
        else :
            print(" ", end= ' ')
    print()

print("_"*50)

#Dùng 2 vòng while lồng nhau
i=0
while i<n :
    j=0
    while j<n :
        if j==0 or i==j or j==n-1 :
            print("#", end=' ')
        else :
            print(" ", end=' ')
        j+=1
    i+=1
    print()
