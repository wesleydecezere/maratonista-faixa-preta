# -*- coding: utf-8 -*-

# adiciona 0 adjacentes na lista, atual recebe 1
# para cada item da lista, repete
# termina quando nao houver adjacente


# problemas
# 1. adicionar elemento da lista atual na proxima lista
# 2. caminho deve ser contínuo
# 3. mais caminhos possíveis depois de chegar no final

# solucoes
# 1a. para adicionar na lista posterior, verifica lista atual (pode ficar grande)
# 2a. começar pela posição 0,0, skipando tudo se tiver valor '1'
# 3a. parar quando encontrar fim

cases = int(input())

def get_adjacents(x, y):
    adjacents = []
    positions = [
        [x+1, y],
        [x-1, y],
        [x, y+1],
        [x, y-1]
    ]

    for position in positions:
        [i, j] = position
        if i < 5 and i >= 0 and j < 5 and j >= 0 and matrix[j][i] == '0':
            adjacents.append([i, j])
            matrix[y][x] = '1'
    
    return adjacents

def comp(prev_adjacents):
    new_adjacents = []
    for adjacent in prev_adjacents:
        [x, y] = adjacent
        new_adjacents += get_adjacents(x, y)
  
    is_new_adjacent = lambda adjacent : adjacent not in prev_adjacents and adjacent != []
    new_adjacents = [adjacent for adjacent in new_adjacents if is_new_adjacent(adjacent)]

    return new_adjacents

def get_matrix():
    matrix = []
    k = 0
    
    while k < 5:
        line = input().split()
        if len(line) == 0:
            continue
        
        matrix.append(line)
        k += 1

    return matrix

for _ in range(cases):
    matrix = get_matrix()

    if matrix[0][0] == '1':
        print('ROBBERS')
        continue

    adjacents = [[0, 0]]
    while True:
        new_adjacents = comp(adjacents)
        if len(new_adjacents) == 0 or [4, 4] in adjacents:
            break
        
        adjacents = new_adjacents

    if [4,4] in adjacents:
        print('COPS')
    else:
        print('ROBBERS')

