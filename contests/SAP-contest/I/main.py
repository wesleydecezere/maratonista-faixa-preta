while(True):
  try:
    N=int(input())
    M=input().split()
    
    H=int(M[0])
    C=int(M[1])
    L=int(M[2])
    
    CP=N*(C**2+H**2)**0.5
    A=L*CP/10000
    print("%.4f"%A)
  except EOFError:
    break
  



