N=int(input())
c=0
while(c<N):
  c+=1
  l1=int(input())
  l2=input().split(' ')
  l3=int(input())
  e0=int(l2[0])
  e1=int(l2[1])
  e2=int(l2[2])
  e3=int(l2[3])

  if((l1+l3)==7 and (e0+e2)==7 and (e1+e3)==7):
    r=1

  l2.append(l1)
  l2.append(l3)
  
  for i in range (1,len(l2)):
    for i in range(1,len(l2)):
      if int(l2[i-1])>int(l2[i]):
        l2[i-1],l2[i]=l2[i],l2[i-1]
  for i in range (1,7):
    if i!=int(l2[i-1]):
      r=0
      break
  
  if r==1:
    print("SIM")
  else:
    print("NAO")