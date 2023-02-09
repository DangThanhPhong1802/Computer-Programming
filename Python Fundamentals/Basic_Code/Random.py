from random import randrange

while True :
    x=randrange(-100,100)
    print(x, end=' , ')
    if x==50 :
        break
print("STOP!")

print("-"*50)

count=0
while True :
    y=randrange(-50,50)
    count+=1
    print(y, end='---')
    if y==18 :
        break
print("\nSố 18 ngẫu nhiên thứ", count)
print("STOP!")