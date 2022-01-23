# Detalhes para execução de scripts Python

## Passar inputs como parâmetro, ao invés de digitá-las

### O comando
Salve os casos de teste em um arquivo de texto e coloque-o no mesmo diretório em que seu programa se encontra. Então, passe-o como parâmetro, após chamar o arquivo executável `./[executalbe-file] [input-file]`.

#### Exemplo
Digamos que o executável que você gerou após a compilação chama-se `main.exe` e seus casos de teste estejam armazenados no arquivo `inputs.txt`. Então, execute o seguinte comando no terminal:
```bash
./main.exe inputs.txt
```

### Recebendo os parâmetros de execução
Em C++, devemos fazer alguns passos a mais para receber os valores de entrada do problema pelo terminal.

O primeiro deles é obter o nome do arquivo a ser aberto. Como passamos ele como parâmetro do comando, podemos resgatálos pelos argumentos da função *main*

```c++
int main(int argc, char** argv) {
  // ...
}
```

O argumento `argc` receberá o número de parâmetros passados na linha de comando. Já o argumento `argv` é um ponteiro para as posições de memória em que eles foram armazenado.

#### Exemplo
No nosso caso, como o comando foi `./main.exe inputs.txt`, teremos que `argc = 2`, `argv[0]` = `"./main.exe"` e `argv[1] = inputs.txt`.

### Lendo o conteúdo do arquivo
Na sequência, devemos abrir o arquivo cujo nome foi passado como parâmetro do comando, com o auxílio de uma biblioteca externa, para então ler seu conteúdo.

A biblioteca utilizada é a `fstream`, que conta com métodos para criar, ler e escrever arquivos.

```c++
#include <fstream>
```

Utilizaremos uma variável do tipo `ifstream` para armazenar o conteúdo do arquivo e a função `getline()` para transferir, linha por linha, o conteúdo do arquivo para uma variável específica. 

#### Exemplo
No exemplo abaixo, ao executar o comando `./main.exe inputs.txt`, primeiramente o conteúdo do arquivo `inputs.txt` é armazenado na variável `input`, do tipo `ifstrem`. 

Então, linha por linha, o conteúdo da variável `ìnput` é passado à variável `inputLine`, do tipo `string`, que é exibida na tela.

Por fim, o arquivo é fechado.

```c++
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv) {
  string inputLine;

  ifstream input(argv[1]);

  while (getline (input, inputLine)) {
    cout << inputLine;
  }

  input.close(); 
}
```

# Referências
1. [Passar o nome de um arquivo a um executável] (https://stackoverflow.com/questions/33527418/how-to-pass-a-file-to-an-exe-in-console)
2. [Manipular arquivos em C++](https://stackoverflow.com/questions/33527418/how-to-pass-a-file-to-an-exe-in-console)