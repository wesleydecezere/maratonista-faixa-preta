while True:
  n = int(input())
  if n == 0:
    break
  else:
    bacias = input().split()
    n_partidas = 0
    for i in range(len(bacias)):
      n_partidas += 2**(i)*int(bacias[i])
    print(n_partidas)