d1=1.11 - 1.10
d2=2.11 - 2.10
print('d1=', d1, 'd2=', d2)
if d1==d2 :
  print('d1=d2')
else :
  print('d1!=d2')

print("-"*20)

d1=1.11 - 1.10
d2=2.11 - 2.10
print('d1=', d1, 'd2=', d2)
diff=d1 - d2  #Computer difference
if diff<0 :  #Computer absolute value
   diff = - diff
if diff<0.001 :  #Are the values close enough?
   print('d1=d2')
else :
   print('d1!=d2')