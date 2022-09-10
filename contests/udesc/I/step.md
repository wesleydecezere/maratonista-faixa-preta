# le string

# clausulas = string split by '&'
# literais = clausulas split by '|'

# qtd_clausulas = multiplica(para cada clausula, len(clausula))
# max_tam = maior literal + segunda maior literal
# min_tam = menor literal + menor literal

se max == min:
  se max == 1: SAT1
  se nao: SAT3
se nao: SAT2