import math

n = int(input())

for _ in range(n):
    m, n = [int(x) for x in input().split()]
    largura = m - 2
    altura = n - 2

    sonaresPorLargura = largura / 3
    sonaresPorAltura = altura / 3

    print(math.ceil(sonaresPorLargura) * math.ceil(sonaresPorAltura))
