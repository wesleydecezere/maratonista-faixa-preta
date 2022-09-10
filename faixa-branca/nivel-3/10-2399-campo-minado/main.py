campo = int(input())
minas = [int(input()) for i in range(campo)] #usar isso com mais frequência
resposta = [0 for i in range(campo)]
for i in range(campo):
  if minas[i] == 1:
    resposta[i] += 1
  if ((i+1)<campo) and (minas[i+1]==1):
    resposta[i] += 1
  if (i-1>=0) and (minas[i-1]==1):
    resposta[i] += 1
  print(resposta[i])