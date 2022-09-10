cases = int(input())
for i in range(cases):
  muro = {"l1":[],"l2": [],"l3": [],"l4": [],"l5": [], "l6": [], "l7": [], "l8": [], "l9": []}
  completo = {"l1":[0],"l2": [0,0],"l3": [0,0,0],"l4": [0,0,0,0],"l5": [0,0,0,0,0], "l6": [0,0,0,0,0,0], "l7": [0,0,0,0,0,0,0], "l8": [0,0,0,0,0,0,0,0], "l9": [0,0,0,0,0,0,0,0,0]}
  for i in range(0,10,2):
    valores = input().split()
    muro["l{}".format(i+1)] = valores
  num_t = 9
  for i in range(9):
    for j in range(num_t):
      if num_t == 9:
        if j%2 == 0:
          completo["l9"][j] = int(muro["l9"][j//2])
        else:
          completo["l9"][j] = (int(muro["l7"][j//2]) - (int(muro["l9"][(j-1)//2])+int(muro["l9"][(j+1)//2])))//2
      else:
        completo["l{}".format(num_t)][j] = completo["l{}".format(num_t+1)][j] + completo["l{}".format(num_t+1)][j+1] 
    num_t -= 1
  for i in range(9):
    str = ""
    for v in completo["l{}".format(i+1)]:
      str += "{} ".format(v)
    print(str)    