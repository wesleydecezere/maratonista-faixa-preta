teste = 1
while True:
  a, v = input().split()
  if a == "0" and v == "0":
    break
  n_voos_aeroporto = {str(i+1): 0 for i in range(int(a))}
  for i in range(int(v)):
    departure, arrival = input().split()
    n_voos_aeroporto[departure] += 1
    n_voos_aeroporto[arrival] += 1
  a_max_trafegos = [i for i in n_voos_aeroporto.keys() if n_voos_aeroporto[i]==max(n_voos_aeroporto.values())]
  resposta = ""
  for i in a_max_trafegos:
    resposta += "{} ".format(i)
  print("Teste {}\n{}\n".format(teste, resposta))
  teste +=1