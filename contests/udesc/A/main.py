from numpy import arccos

r,d,c= [int(x) for x in input().split()]
x = 1-(d**2)/(2*r**2)
ang = arccos(x)
a = ang * r
# print(a)

if (2*a) > c:
  print("impossivel")
else:
  print("possivel")