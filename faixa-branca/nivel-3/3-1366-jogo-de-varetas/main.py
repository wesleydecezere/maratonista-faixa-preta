while True:
  N = int(input())
  if N == 0:
    break
  retangulos = 0
  n_par = 0
  for i in range(N):
    comprimento, quantidade = input().split()
    if int(quantidade)>=4:
      resto = int(quantidade)%4
      retangulos += int(quantidade)//4
      if resto>=2:
        n_par += 1
    elif int(quantidade)==2 or int(quantidade)==3:
      n_par+=1
  retangulos += n_par//2
  print(retangulos)