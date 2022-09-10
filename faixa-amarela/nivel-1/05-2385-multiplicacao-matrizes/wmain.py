n = int(input())
p, q, r, s, x, y = [int(x) for x in input().split()]
i, j = [int(x) for x in input().split()]

linha = []
coluna = []
C = 0

for _ in range(1, n+1):
    Ai_ = (p*i + q*_) % x
    B_j = (r*_ + s*j) % y
  
    C += Ai_ * B_j

print(C)