while True:
  n,m = input().split()
  if n == '0' and m == '0':
    break
  else:
    desenho = []
    for i in range(int(n)):
      desenho.append(input().split())
    ratio_w = int(input())/int(m) 
    ratio_h = int(input())/int(n)
    for linha in desenho:
      pass #lógica de redimensionamento aqui