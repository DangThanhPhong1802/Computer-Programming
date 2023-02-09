x=5
y=x**3
print(x,y)

year=2018
t= year % 2 == 0 and year % 3 > 1
print(t)
t= year % 2 == 0 and year % 3 > 6
print(t)
t= year % 2 == 0 or year % 3 > 6
print(t)
t= year % 2 == 0 or year % 3 > 1
print(t)

print("@"*10)

print(5 is not 5)
print(5 is 5)
print((5*2) is 10)

print(9/4)
print(18//8)
print(36%16)