step_by_prev_step = {
"01": {
    "10": "R",
    "-10": "L"
},
"0-1": {
    "10": "L",
    "-10": "R"
},
"10": {
    "01": "L",
    "0-1": "R"
},
"-10": {
    "01": "R",
    "0-1": "L"
},
}

def get_direction(prev_step: list, step: list):
if prev_step == step:
    return "F" 

prev_step_str = ''.join(str(x) for x in prev_step)
step_str = ''.join(str(x) for x in step)

#    print(prev_step_str, step_str)

return step_by_prev_step[prev_step_str][step_str]

def get_move(current_position: list, linhas: list[list], prev_step: list): 
current_linha, current_coluna = current_position
steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]
hasNext = None

for step in steps:
    step_linha, step_coluna = step    
    try:
        next_linha = current_linha + step_linha
        next_coluna = current_coluna + step_coluna

        adjacente = linhas[next_linha][next_coluna]            
        if adjacente == '0':
            hasNext = True
            break            
    except:
        pass

if hasNext == None:
    return None

#    print(linhas, current_position, step)

if prev_step == [0, 0] or prev_step == step:
    linhas[next_linha][next_coluna] = 'X'
    new_position = [next_linha, next_coluna]
    return ['F', new_position, step]

return [get_direction(prev_step, step), current_position, step]


while True:

try:
    numero_linhas, numero_colunas = [int(i) for i in input().split()]
except EOFError:
    break

linhas = []
start_position = []

for numero_linha in range(numero_linhas):
    linha = input().split()
    linhas.append(linha)

    try:
        start_position = [numero_linha, linha.index('X')]
    except ValueError:
        pass

directions = []
position = start_position 
prev_step = [0, 0]

while(True):
#        print(linhas)

    move = get_move(position, linhas, prev_step)

    if move == None:
        directions.append('E')
        break

    [direction, new_position, step] = move
    directions.append(direction)
    position = new_position
    prev_step = step

print(' '.join(directions))





