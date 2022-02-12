### programam principal
- le valor n
- se n == 0, termina
- inicializa um dicionario vazio (string -> string)  
- enquanto n > 0
  - recebe um par de valores
  - armazena val1 -> val2
- le valor m
- inicializa um int = 0 
- enquanto m > 0
  - recebe um par de valores
  - resgata dict[val1]
  - conta as diferencas entre dict[val1] e val2
  - se diferencas >= 2, int += 1
- repete

### contar diferencas entre strings
- recebe duas strings e um valor para o máxima de diferencas(2)
- le tamanho str1
- le tamanho str2
- armazena menor tamanho
- inicializa int dif = 0
- de 0 até o tamanho-1:
  - se (str1[n] != str2[n]) dif += 1
  - se (dif == 2) retorna verdadeiro
- retorna falso
