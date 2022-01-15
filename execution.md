# Como executar os arquivos
Na estrutura definida neste REPL, não será mais possível executar qualquer script pelo botão **Run**. 

Ao invés disso, será necessário utilizar o Shell prompt do ambiente. Ele está disponível na janela mais à direita da interface e pode ser acessado clicando na aba *Shell*, ao lado da aba previamente selecianda, *Console*.

## Navegando até a pasta correta
Antes de executar seu arquivo, é necessário navegar até o diretório em que ele se encontra.

Incialmente, o diretório de trabalho do Shell será o diretório raiz deste REPL. Por isso, você verá na primeira linha do prompt algo como `~/maratonista-faixa-preta$ ` imediatamente antes do cursor.

Para navegar até a pasta desejada, utilize o comando `cd [directory-name]`.

### Exemplo
Digamos que o caminho para o seu arquivo seja `faixa-exemplo/nivel-0/0-0000-exemplo-nome-execicio/main.cpp`.

Então, você deve executar os seguintes comandos no Shell:
```bash
cd faixa-exemplo
cd nivel-0
cd 0-0000-exemplo-nome-execicio
```
Ou então, simplemente:
```bash
cd faixa-exemplo/nivel-0/0-0000-exemplo-nome-execicio
```

Pronto, você já deve estar no mesmo diretório em que seu script se econtra. Agora, basta executá-lo. Se ficou com alguma dúvida, consulte este [artigo](https://www.geeksforgeeks.org/cd-command-in-linux-with-examples/) para saber mais sobre o comando utilizado.

## Executando o arquivo
Apesar do REPL ter uma linguagem definida, por meio do Shell prompt é possível compilar e executar arquivos de qualquer uma das linguagens suportadas.

### Python
Uma vez no diretório correto, basta chamar o interpretador `python` e passar como parâmetro o nome do script a ser executado, acompanhado da extensão (`python [script-name.py]`). 

Em nosso exemplo, basta executar:
```bash
python main.py
```
Você deve ver a frase *Hello World, I'm a pythonist!* na linha seguinte.

### C++
Em C++ há um passo a mais: você deve compliar o programa antes de executá-lo.

Por isso, primeiro é necessário gerar o arquivo executável, chamando o compilador `clang++` e passando como parâmetro a flag `-o`, o nome do executável e o nome do programa (`clang++-7 -o [executable-name] [file-name]`). Por fim, basta chamar o executável gerado.

Novamente em nosso exemplo, devemos rodar os comandos:
```bash
clang++-7 -o main.exe main.cpp
./main.exe
```
Você deve ver a frase *Hello World, I'm a C++ lover <3* na linha seguinte.

# Referências
1. [Manual do compilador clang](https://clang.llvm.org/docs/UsersManual.html)
2. [Diferença entre GCC e clang](https://pt.stackoverflow.com/questions/142573/diferen%C3%A7a-entre-gcc-clang)