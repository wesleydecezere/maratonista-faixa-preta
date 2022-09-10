import math

T=int(input())

for i in range(T):
  N=float(input())
  Ne=(50.16-N*6)/4 * 10
  Ne = math.trunc(Ne)
  print(Ne/10)