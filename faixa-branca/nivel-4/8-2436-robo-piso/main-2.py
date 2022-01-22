l, c = [int(n) for n in input().split()]
a, b = [int(n)-1 for n in input().split()]

mtx = []

for _ in range(l):
  mtx.append(list(map(int, input().split())))

x = [0, 0, 1, -1]
y = [1, -1, 0, 0]

for i in range(l):
  for j in range(c):
    if (i == a and j == b) or mtx[i][j] != 1:
      continue

    black_tile_adj = 0

    for direction in range(len(x)):
      i_adj = i + y[direction]
      j_adj = j + x[direction]

      if i_adj in range(0, l) and j_adj in range(0, c):
        black_tile_adj += mtx[i_adj][j_adj]
    
    if black_tile_adj == 1:
      print(i + 1, j + 1)





