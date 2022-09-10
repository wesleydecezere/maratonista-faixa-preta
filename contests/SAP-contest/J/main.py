while True:
  case = int(input())
  if case == 0:
    break
  planetas = dict()
  for i in range(case):
    name, a, t = input().split()
    planetas[name] = int(a)-int(t)
  planeta = sorted(planetas.items(), key=lambda x: x[1])[0][0]
  print(planeta)