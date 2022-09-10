n = int(input())
bispos_pos = []
ajuste = 0
#dominantes = [0 for i in range(n)]
dom = n
for i in range(n):
  bispos_pos.append([int(x) for x in input().split()])
for i in range(n):
  temp = 0
  for pos in bispos_pos:
    if pos == bispos_pos[i-ajuste]:
      pass
    if abs(bispos_pos[i-ajuste][0] - pos[0])==abs(bispos_pos[i-ajuste][1] - pos[1]):
      bispos_pos.remove(pos)
      ajuste +=1
      temp = 1
  if temp:
    bispos_pos.pop(i)
    ajuste +=1
print(len(bispos_pos))