while(1):
  try:
    n, m = list(map(int, input().split()))

    mtx = []

    x = [0, 0, 1, -1]
    y = [1, -1, 0, 0]

    for _ in range(n):
      mtx.append(input().replace('1', '9').split())

    for i in range(n):
      for j in range(m):
        if mtx[i][j] != '9':
          cnt = 0

          for direction in range(len(x)):
            i_adj = i + y[direction]
            j_adj = j + x[direction]
          
            if i_adj < 0 or i_adj >= n or j_adj < 0 or j_adj >= m:
              continue
            
            cnt += 1 if mtx[i_adj][j_adj] == '9' else 0
            
          mtx[i][j] = '{}'.format(cnt)
        
      print(''.join(mtx[i]))
  
  except EOFError:
    break