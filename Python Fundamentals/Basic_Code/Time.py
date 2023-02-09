
# Alt + Enter
from time import clock, sleep

start=clock()
print("Nhập 1 số :")
x=input()
print("Nhập : x=", x)
end=clock()
duration=end-start
print("duration=", duration)

start=clock()
for x in range(100000) :
    print(x, end= ' ')
end=clock()
duration=end-start
print("duration của for", duration)

for x in range(10) :
    print(x)
    sleep(1)



