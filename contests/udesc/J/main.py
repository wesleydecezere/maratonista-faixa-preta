n =int(input())
trinca = {}
mao_atual = []
baralho = []
rodada = 0

def verifica_trinca(mao):
  pass

for i in range(n):
  carta = input()
  valor,naipe = list(carta)
  baralho.append(carta)
  if valor not in trinca:
    trinca[valor] = 1
  else:
    trinca[valor] +=1
if trinca.values().count(3) >= 1:
  if n>9: 
    while True:
      if len(mao_atual) == 9:
        out = mao_atual.pop(0)
        mao_atual.append(baralho[rodada%n])
        if verifica_trinca(mao_atual):
          print(rodada+1)
          break
      else:
        mao_atual.append(baralho[rodada%n])
        if verifica_trinca(mao_atual):
          print(rodada+1)
          break
      rodada += 1
  else:
    pass
else:
  print(-1)