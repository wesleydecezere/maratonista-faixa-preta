c = int(input())
cn = 0

while(cn != c):
  cn += 1
  m, n, y, x = input().split()
  m = int(m)
  n = int(n)
  x = int(x) - 1
  y = int(y) - 1

  mtx = []
  out = ''

  for _ in range(m):
    mtx.append(list(map(int, input().split())))

  for i in range(m):
    for j in range(n):
      # calcula a destruicao de acordo com a distancia à coordenada
      dx = abs(j - x)
      dy = abs(i - y)
      d = max(dx, dy)

      power = 1 if d > 9 else 10 - d

      # refaz a matriz, somando a destruicao ao valor atual
      mtx[i][j] = str(power + mtx[i][j])
    
    out += ' '.join(mtx[i]) + ('\n' if i < m - 1 else '' )

  print("Parade {}:".format(cn))
  print(out)

print()  