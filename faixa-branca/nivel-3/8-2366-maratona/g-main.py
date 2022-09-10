n, m = input().split()
postos = [int(x) for x in input().split()]
postos.append(42195)
resposta = 'S'
for i in range(len(postos)-1):
  if postos[i+1] - postos[i] > int(m):
    resposta = 'N'
    break
print(resposta)