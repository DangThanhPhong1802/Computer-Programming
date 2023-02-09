print("Mời bạn nhập giá trị:")
s=input()
print(s)

print("Mời bạn nhập giá trị:")
s=input()
print("Bạn đã nhập:", s)

print("Mời bạn nhập giá trị:")
s=input()
print("Bạn đã nhập:", s)
print("Kiểu DL:", type(s))

print("Mời bạn nhập giá trị:")
s=int(input())
print("Bạn đã nhập:", s)
print("Kiểu DL:", type(s))

s=float(input("Mời bạn nhập giá trị:"))
print("Bạn đã nhập:", s)
print("Kiểu DL:", type(s))

def StrToBool(s):
    return s.lower () in ("true", "t", "1", "yes")
x=input("Mời bạn nhập True/False:")
x=StrToBool(x)
print(x)

