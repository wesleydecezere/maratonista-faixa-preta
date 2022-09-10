while(1):
  try:
    n = int(input())
  except EOFError:
    print()
    break

  init = int(n / 3)

  m = [[]]
  for i in range(n):
    m.append([])
    for j in range(n):
      m[i].append('0')
    
      if i == j:
        m[i][j] = '2'
      if i + j == n-1:
        m[i][j] = '3'
      if (i >= init and i <= n-1-init) and (j >= init and j <= n-1-init):
        m[i][j] = '1'
      if i == j and i == int(n/2):
        m[i][j] = '4'

    print(''.join(m[i]))
  print()