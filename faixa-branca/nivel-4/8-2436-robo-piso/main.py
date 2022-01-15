l, c = list(map(int, input().split()))
y, x = list(map(int, input().split()))
x -= 1
y -= 1


mtx = []

for _ in range(l):
  mtx.append(input().split())
 
dList = [
  (1, 0),   # direita
  (0, 1),   # para baixo
  (-1, 0),  # esquerda
  (0, -1)   # para cima
] 

# define a direcao incial
dInit = (0, 0)

# define nro de direcoes
dLen = len(dList)
d = 0

# enquanto houver direcao
while (d < dLen):
  dx = dList[d][0]
  dy = dList[d][1]
  
  nx = x + dx
  ny = y + dy

  # (se nao atingir as bordas) E 
  # (se houver 1 nessa direcao) E 
  # (se ela nao for contratia a direcao inicial)
  if (nx < len(mtx[0]) and ny < len(mtx)):
    if (mtx[ny][nx] == '1'):
      if ((dInit[0] != -dx or dx == 0) and (dInit[1] != -dy or dy == 0)):
        # movimenta na direcao
        x = nx
        y = ny
        
        # (re)define direcao inicial
        dInit = dList[d]

        # redefine nro de direcoes
        d = 0
      else:
        d += 1
    else: 
      d += 1
  # se nao
  else:
    # muda de direcao
    # diminui nro de direcoes
    d += 1

print(y + 1, x + 1)
