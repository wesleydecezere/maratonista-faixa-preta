from math import factorial

n = int(input())
for _ in range(n):
    a, b = [int(x) for x in input().split()]

    if b == 0:
        grau = 1
    elif a == 0:
        grau = 2
    else:
        grau = 4

    valor = 0

    for i in range(0, grau + 1):
        if i % 2 == 0:
            coeficiente = factorial(grau) / (factorial(i) * factorial(grau - i))
            parcela = coeficiente * a**(grau - i) * (b)**i
            valor += -parcela if i == 2 else parcela
            print(coeficiente)

    if valor >= 2**30:
        print(valor, "TOO COMPLICATED")
    else:
        print(valor, grau)
