while True:
  try:
    N,R = input().split()
    retornaram = input().split()
    resposta = ""
    #print(retornaram)
    if N == R:
      resposta = "*"
    else:
      for i in range(int(N)+1):
        if str(i) not in retornaram:
          if i == 0:
            pass
          else:
            resposta = resposta + "{} ".format(i)
    print(resposta)
  except EOFError:
    break