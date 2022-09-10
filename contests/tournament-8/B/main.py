test_cases = int(input())
for i in range(test_cases):
  pisos = int(input())
  cor_atual = 0
  andares = []
  predio = []
  for n in range(pisos):
    an = int(input())
    andares.append(an)
  for i in range(pisos):
    andar = andares.pop(andares.index(max(andares, key=abs)))
    if cor_atual != 0: 
      if (andar < 0 and cor_atual == "V") or (andar > 0 and cor_atual == "A"): #mesma cor anterior 
        continue
      else: #cores diferentes
        if abs(andar) < predio[-1]:         
          predio.append(abs(andar))
          cor_atual = "V" if andar < 0 else "A"
    else:
      predio.append(abs(andar))
      cor_atual = "V" if andar < 0 else "A"
  print(len(predio))