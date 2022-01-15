l, c = list(map(int, input().split()))
x, y = list(map(int, input().split()))

mtx = []

for _ in range(l):
  mtx.append(input().split())
 
  # define nro de direcoes

  # enquanto houver direcao
    # se houver 1 nessa direcao E se nao for contratia a direcao inicial
      # movimenta na direcao
      # (re)define direcao inicial
      # redefine nro de direcoes
    # se nao
      # muda de direcao
      # diminui nro de direcoes

print(mtx)
