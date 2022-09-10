N=int(input())
c=0
Cv=Ca=Cam=0

while(c<N):
  A=int(input())
  c+=1
  R=(A/12.56)**0.5
  if(R<12):
   Cv=A*0.09
   print("vermelho = R$ %.2f"%Cv)
  elif(12<=R<=15):
    Ca=A*0.07
    print("azul = R$ %.2f"%Ca)
  else:
    Cam=A*0.05
    print("amarelo = R$ %.2f"%Cam)


  





