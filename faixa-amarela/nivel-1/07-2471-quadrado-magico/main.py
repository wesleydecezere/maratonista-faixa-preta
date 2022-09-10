n = int(input())

mtx = []
somaLinha = []
somaColuna = [0] * n
idx = []

for i in range(n):
  linha = [int(c) for c in input().split()]
  mtx.append(linha)  
  somaLinha.append(sum(linha))

  for j in range(n):
    somaColuna[j] += linha[j]

soma = [somaLinha, somaColuna]

for i in range(2):
  a, b = set(soma[i])
  
  nA = soma[i].count(a)
  nB = soma[i].count(b)
  
  idx.append(soma[i].index(a if nA < nB else b))

substituto = mtx[idx[0]][idx[1]]
somaCorreta, somaErrada = (a,b) if nA > nB else (b,a)

substituido = substituto + (somaCorreta - somaErrada)

print(substituido, substituto)