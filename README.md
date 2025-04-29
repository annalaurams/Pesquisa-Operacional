
# Resolução de Sistemas Lineares

Este projeto tem como objetivo resolver sistemas lineares originados de problemas de Programação Linear (PL)

## Estrutura dos Arquivos

- `file.py` : Responsável pela leitura dos dados do arquivo.
- `matrix.py` : Contém a lógica de geração de combinações, resolução dos sistemas e impressão dos resultados.
- `arquivo.txt` : Contém os dados de entrada no seguinte formato:
  ```
  <numero de variaveis> <m>
  <coeficientes da função objetivo>
  <restrição 1>
  <restrição 2>
  ...
  <restrição m>
  ```

## Como Executar

1. Certifique-se de que os arquivos `file.py`, `matrix.py` e `arquivo.txt` estão no mesmo diretório.
2. Execute o arquivo principal:
   ```bash
   python main.py
   ```
3. Acompanhe a saída no terminal.

## Exemplo de Saída

```
=== Testando combinação ===
Variáveis zeradas: ['x3', 'x5']

Matriz A:
[[1 1 0]
 [1 0 1]
 [0 1 0]]

Vetor b:
[4 2 3]

Atribuições encontradas:
  x1 = 1.0
  x2 = 3.0
  x3 = 0.0
  x4 = 1.0
  x5 = 0.0

✅ Solução válida encontrada!
Valor da função objetivo: 7.0
```

## Contato

> **Anna Laura Moura**  

> [LinkedIn](https://www.linkedin.com/in/anna-laura-614384205) | Email: nalauramoura@gmail.com

