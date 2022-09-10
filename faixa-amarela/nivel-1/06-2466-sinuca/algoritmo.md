# enquanto n > 1
    # n = N - 1
    # para i de 0 a n
        # se linha[n] == linha[n+1] 
            # prox_linha[i] = 1
        # se nao
            # prox_linha[i] = -1
            
    # linha = prox_linha
    
# se linha[0] == 1
    # imprime 'preto'
# se linha[0] == -1
    # imprime 'branco'