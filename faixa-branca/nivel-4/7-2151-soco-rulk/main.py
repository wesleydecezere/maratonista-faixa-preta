c = int(input())

while(c):
  c -= 1
  m, n, x, y = input().split()

  mtx = []

  for _ in range(int(m)):
    mtx.append(input().split())

  print(mtx)
