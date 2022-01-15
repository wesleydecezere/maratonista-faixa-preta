# Detalhes para execução de scripts Python

## Passar inputs como parâmetro, ao invés de digitá-las
Salve os casos de teste em um arquivo de texto e coloque-o no mesmo diretório em que seu script se encontra. Então, passe-o como parâmetro ao intepretador `python [script-name] < [input-file]`.

### Exemplo
Digamos que o nome de seu script seja `main.py` e seus casos de teste estejam armazenados no arquivo `inputs.txt`. Então, execute o seguinte comando no terminal:
```bash
python main.py < inputs.txt
```
Você deverá ver a saída de seu programa na impressa na linha seguinte.

# Referências
1. [Passar o conteúdo de um arquivo a um script python](https://stackoverflow.com/questions/17648482/how-to-pass-file-contents-to-a-python-script-on-windows)