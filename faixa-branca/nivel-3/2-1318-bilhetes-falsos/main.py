from collections import Counter
while True:
  N, M = input().split(" ")
  if int(N) == 0 and int(M) == 0:
    break
  tickets = input().split(" ")
  valores_duplicados = 0
  contagem = dict(Counter(tickets))
  for i in contagem.keys():
    if contagem[i]>1:
      valores_duplicados+=1
  print(valores_duplicados)