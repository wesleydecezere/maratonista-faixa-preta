while True:
  pos = [-1,-1]
  caminho = []
  direcoes = [[0, 1], [0, -1], [1, 0], [1, -1]]
  dir = [0, 0]
  steps = ""
  
  try:
    m, n = [int(a) for a in input().split()]
    
    for i in range(m):
      linha = input()
    
      # encontra a posicao do x na linha            
      j = linha.find('X')
      if (j >= 0):
        pos = [i, j]

      # encontra a posicao dos 0s na linha, removendo-os
      for _ in range(linha.count('0')):
        j = linha.find('0')
        caminho.append([i, j])
        linha = linha.replace('0', '1', 1)

    while(len(caminho) > 1):
      for d in direcoes:
        
        try:
          print(d)
          # procura
          npos = [x + y for x, y in zip(pos, d)]
          print(npos)
          caminho.index(npos)

          if (dir == (0, 0)):
            steps += 'F'
          else:
            if (dir != d):
              k1 = sum(d)
              k2 = dir[0]*(-dir[1])
              steps += 'L' if k1 == k2 else 'R'
            steps += 'F'
              
          pos = npos
          dir = d
          caminho.pop(npos)
          print(caminho)
          break           
        except:
          pass  
  
  except EOFError:
    break