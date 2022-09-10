import math

d = int(input())
n = d - 1

for i in range (2, d):
  n += d - i
  
  multiplo = i
  fator = 2
  
  while multiplo*fator <= d:
    n -= 1
    print(i, multiplo*fator, n)
    fator += 1
  
  # for j in range (i+1, d+1):
  #   if math.gcd(j,i) == 1:
  #     n += 1
  #     # print(i, j)

print(n)