q=int(input())
c=0
while(c<q):
  n=int(input())
  c+=1
  p=int(n**0.5)
  if n<9:
    p=3
  for i in range (2,p+1):
    if n%i==0 and n!=2 and n!=3:
      print ("Not Prime", n)
      break
  if i==(p):
     print ("Prime", n)