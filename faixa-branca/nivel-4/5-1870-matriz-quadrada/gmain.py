while True:
  num = int(input())
  matriz=[]
  linha=[]
  if num == 0:
    break
  else:
    if num%2==0:
      center = num/2
    else:
      center = num//2+1
    repeticao = num
    for k in range(num):
      valor = 1
      for lin in range(num):
        inv = False
        if valor == lin+1:
          linha.append(lin+1)
          inv = True
        else: 
          if inv:
            valor -= 1
            linha.append(valor)
          else:
            linha.append(valor)
            valor += 1
        print(linha)
        matriz.append(linha)
        linha = [] 
        print("\n")
      print("\n")    