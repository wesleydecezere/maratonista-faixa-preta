P=[int(p) for p in input().split()]

min = int(min(P))
min_idx = P.index(min)
idx = [0,1,2]
idx.remove(min_idx)

passo = [0] * 3
passo[min_idx] = 1

passo[idx[0]] = int(P[idx[0]]) / min
passo[idx[1]] = int(P[idx[1]]) / min

print(min)
for i in range(0, min):
  PH = passo[0] * i
  PM = passo[1] * i
  PS = passo[2] * i
  
  print(int(PH), int(PM), int(PS))


  
  