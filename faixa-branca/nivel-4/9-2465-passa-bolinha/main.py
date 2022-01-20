n = int(input())
init = tuple([int(x) - 1 for x in input().split()])

m = []
m_aux = []

for _ in range(n):
  m.append(list(map(int, input().split())))
  m_aux.append([0 for _ in range(n)])

# cria um set com a coordenada inicial
coords = set([init])

# enquanto houver coordenada a ser verificada
while len(coords) != 0:
  # seleciona uma coordenada e remove-a da coleção  
  coord = coords.pop()
  i = coord[0]
  j = coord[1]

  y = [0, 0, 1, -1]
  x = [1, -1, 0, 0]

  # para todas as direções (N, S, E, W)
  for direction in range(len(y)):
    i_neighbor = i + y[direction]
    j_neighbor = j + x[direction]
    coord_neighbor = (i_neighbor, j_neighbor)

    if(i_neighbor < 0 or j_neighbor < 0):
      continue

    try:
      # se vizinho tiver camisa igual ou maior E vizinho tiver bandeira abaixada
      if m[i_neighbor][j_neighbor] >= m[i][j] and m_aux[i_neighbor][j_neighbor] == 0:
        # adiciona coordenada do vizinho para ser verificada
        coords.add(coord_neighbor)
    except:
      # ignora indices fora da lista
      pass

    # levanta a bandeira 
    m_aux[i][j] = 1


m_aux_str = ''

for idx in range(n):
  m_aux_str += '%d'*n % tuple(m_aux[idx])

print(m_aux_str.count('1'))