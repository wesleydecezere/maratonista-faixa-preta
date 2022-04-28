d=int(input())
l=input().split(' ')
A=int(l[0])
L=int(l[1])
P=int(l[2])
if(d<=A and d<=L and d<=P):
  print("S")
else:
  print("N")