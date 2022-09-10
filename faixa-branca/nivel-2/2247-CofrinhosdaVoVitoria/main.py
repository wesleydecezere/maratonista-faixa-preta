n=0
while True:
  soma=0
  N=int(input())
  n+=1
  if(N==0):
    print()
    break
  else:
    if(n==1):
      print("Teste 1")
    else:
      print()
      print("Teste",n)

  for d in range(0,N):
    j_z=input().split(' ')
    j=int(j_z[0])
    z=int(j_z[1])
    soma+=j-z
    print(soma)
    
  

    
    
  
  