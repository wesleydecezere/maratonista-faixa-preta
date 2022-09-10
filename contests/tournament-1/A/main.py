nome=input().split()
H=int(nome[0])
Z=int(nome[1])
L=int(nome[2])

if(Z<H<L or L<H<Z):
  print("huguinho")
elif(H<Z<L or L<Z<H):
  print("zezinho")
else:
  print("luisinho")