N = int(input())

for n in range(N):
  G = int(input())
  l=1
  g=1
  while(g<G):
    l+=1
    g+=l
  print(l)
  if (G-g+l<l):
    print(l-1)
  else:
    print(l)