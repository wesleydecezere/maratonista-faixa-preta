#0 dobras=4=2²(2*1-0) 
#1 dobra=9=3²(2*2-1)
#2 dobras=25=5²(1*3+2)
#3 dobras=81=9²()
#4 dobras=289=17²(4*4+1)
#5 dobras=1039=33²(2*17-1)
#1/4 do papel gera 1 pedaço(17:22-17:40, 14:38-)
n=0
while True:
  N=int(input())
  n+=1
  if(N==-1):
    print()
    break
  else:
    if(n==1):
      print("Teste 1")
      print((2**N+1)**2)
    else:
      print()
      print("Teste",n)
      print((2**N+1)**2)
  


   
   

