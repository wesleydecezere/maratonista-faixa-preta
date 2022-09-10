x,y = input().split()
imagem = []
n_brancos = []
pos_branco = []
cores = 0
for i in range(int(x)):
  linha = list(input())
  imagem.append(linha)
  n_brancos.append(linha.count("."))

def preenche_abaixo(i,j):
  if x == "1":
      return False
  else:
      if imagem[i+1][j] != ".":
        return False
      else:
        imagem[i+1][j] = -1
      preenche_abaixo(i+1,j)
      preenche_direita(i,j+1)
      preenche_esquerda(i,j-1)

def preenche_acima(i,j):
  if x == "1":
      return False
  else:
      if imagem[i-1][j] != ".":
        return False
      else:
        imagem[i-1][j] = -1
      preenche_acima(i-1,j)
      preenche_direita(i,j+1)
      preenche_esquerda(i,j-1)

def preenche_direita(i,j):
  if y == "1":
      return False
  else:
      if imagem[i][j+1] != ".":
        return False
      else:
        imagem[i][j+1] = -1
      preenche_abaixo(i+1,j)
      preenche_acima(i-1,j)
      preenche_direita(i,j+1)  

def preenche_esquerda(i,j):
  if y == "1":
      return False
  else:
      if imagem[i][j-1] != ".":
        return False
      else:
        imagem[i][j-1] = -1
      preenche_abaixo(i+1,j)
      preenche_acima(i-1,j)
      preenche_esquerda(i,j-1)

for i in range(int(x)):
  if n_brancos[i] == 0:
    pass
  else:
    for j in range(int(y)):
      #print(i,j)
      #print("Cores: ",cores)
      #print(imagem)
      if imagem[i][j] == ".":
        cores += 1
        if i == 0 and j == 0:
          preenche_abaixo(i,j)
          preenche_direita(i,j)
        elif i == int(x)-1 and j == int(y)-1:
          preenche_acima(i,j)
          preenche_esquerda(i,j)
        elif i == int(x)-1:
          preenche_direita(i,j)
          preenche_acima(i,j)
          preenche_esquerda(i,j)
        elif j == int(y)-1:
          preenche_abaixo(i,j)
          preenche_acima(i,j)
          preenche_esquerda(i,j)
        elif i == 0:
          preenche_abaixo(i,j)
          preenche_direita(i,j)
          preenche_esquerda(i,j)
        elif j == 0:
          preenche_abaixo(i,j)
          preenche_direita(i,j)
          preenche_acima(i,j)
        else:
          preenche_abaixo(i,j)
          preenche_direita(i,j)
          preenche_acima(i,j)
          preenche_esquerda(i,j)
        imagem[i][j] = -1
print(cores)