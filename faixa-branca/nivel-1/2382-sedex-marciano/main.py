l=input().split(' ')
L=int(l[0])
A=int(l[1])
P=int(l[2])
R=int(l[3])
d=2*R
if(d>=(A**2+P**2+L**2)**0.5):
  print("S")
else:
  print("N")