c=input().split(' ')
p=input().split(' ')
A=int(c[0])
B=int(c[1])
C=int(c[2])
H=int(p[0])
L=int(p[1])
if(A>L or B>H):
  print("N")
else:
  print("S")
