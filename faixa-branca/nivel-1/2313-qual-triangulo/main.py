l=input().split(' ')
A=int(l[0])
B=int(l[1])
C=int(l[2])
A1=A*A
B1=B*B
C1=C*C
if(A<B+C and B<A+C and C<A+C): 
  if(A==B==C):
    print("Valido-Equilatero")
  elif(A==B or A==C or B==C):  
    print("Valido-Isoceles")
  else:
    print("Valido-Escaleno")
  if(A1==B1+C1 or B1==A1+C1 or C1==A1+B1):
    print("Retangulo: S")
  else:
    print("Retangulo: N")
else:
  print("Invalido")
    