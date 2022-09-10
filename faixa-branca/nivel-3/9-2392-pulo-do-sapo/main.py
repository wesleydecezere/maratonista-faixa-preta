n,m = input().split()
posicoes = [0 for i in range(int(n))]
for i in range(int(m)):
  p,d = input().split()
  posicoes[int(p)-1] += 1
  for i in range(len(posicoes)):
    if int(p)+i*int(d) <= len(posicoes):
      posicoes[int(p)+i*int(d)-1] += 1
    if int(p)-i*int(d) >= 1:
      posicoes[int(p)-i*int(d)-1] += 1
for i in posicoes:
  print(1 if i > 0 else 0)