while True:
  try:
    n = int(input())
    monte = input().split()
    topo = []
    resultado = 0
    for i in range(len(monte)):
      while True:
        if len(topo) == 0:
          topo.append(int(monte[i]))
          break
        elif int(monte[i]) > topo[-1]:
          topo.append(int(monte[i]))
          break
        else:
          resultado += topo.pop(-1)
    print(resultado)
  except EOFError:
    break