N=float(input())
#22:45
l_divisores=[100.00,50.00,20.00,10.00,5.00,2.00,1.00,0.50,0.25,0.10,0.05,0.01]

c=0
d=6
print("NOTAS:")
D=N//l_divisores[c]
R=round(N - D*l_divisores[c],2)
print("%d"%D, "nota(s) de R$","%.2f"%l_divisores[c])
while(c<5):
  c+=1
  D=R//l_divisores[c]
  R=round(R - D*l_divisores[c],2)
  print("%d"%D, "nota(s) de R$","%.2f"%l_divisores[c])
  
print("MOEDAS:")
D1=R//l_divisores[d]
R1=round(R - D1*l_divisores[d],2)
print("%d"%D1, "moeda(s) de R$", "%.2f"%l_divisores[d])
#print(D1)
#print (R1)
while(d<11):
  d+=1
  D1=R1//l_divisores[d]
  R1=round(R1 - D1*l_divisores[d],2)
  if d!=11:
    print("%d"%D1, "moeda(s) de R$","%.2f"%l_divisores[d])
#    print(D1)
#    print(R1)

if R1 == 0.01:
  D1 += 1

print("%d"%D1, "moeda(s) de R$","%.2f"%l_divisores[d])
#print(D1)
#print(R1)


  #5 n