while True:
    n, m = [int(x) for x in input().split()]
    
    if n == m == 0:
        break
    
    original = []
    
    for _ in range(n):
        original.append(input())
        
    a, b = [int(x) for x in input().split()]
    
    fatorLinha = int(a / n)
    fatorColuna = int(b / m)
    
    novo = []
    
    for i in range(n):
        linhaNova = ''
        
        for c in original[i]:
            linhaNova += c * fatorColuna
            
      # novo.append([linhaNova] * fatorLinha)  
        for _ in range(fatorLinha):
            print(linhaNova)

    print()