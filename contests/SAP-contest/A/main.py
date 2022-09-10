C=input().split()
A=int(C[0])
B=int(C[1])
C=int(C[2])

Delta=(B**2-4*A*C)**0.5

if (Delta == round(Delta)):
  print("Y")
else:
  print("N")



