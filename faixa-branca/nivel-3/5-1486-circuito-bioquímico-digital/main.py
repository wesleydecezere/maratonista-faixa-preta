while True:
  P,N,comparacao = input().split()
  if P=="0" and N=="0" and comparacao=="0":
    break
  experimento = []
  comprimento = []
  resposta = 0
  for i in range(int(N)):
    experimento.append(input().split())
  for j in range(int(P)):
    valor = 0
    for i in range(int(N)):
      if experimento[i][j] == "1":
        valor+=1
      else:
        comprimento.append(valor)
        valor = 0
    comprimento.append(valor)
  for i in comprimento:
    if i>=int(comparacao):
      resposta+=1
  print(resposta)