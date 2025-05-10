# Resolução de Sistemas Lineares

<div align = "center" >

[![requirement](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-informational)](https://code.visualstudio.com/docs/?dv=linux64_deb)
![Linguagem](https://img.shields.io/badge/Linguagem-Python-orange)
</div>

Este projeto tem como objetivo resolver sistemas lineares originados de problemas de Programação Linear (PL) para problemas de Minimização, utilizando o método da enumeração de soluções básicas.

## 📚 Método de Eliminação de Gauss

Este projeto utiliza o **método de eliminação de Gauss**, também conhecido como escalonamento. O objetivo é transformar a matriz do sistema em uma forma triangular superior e, em seguida, aplicar substituição regressiva para encontrar os valores das variáveis.


   Para entender melhor o método de Gauss, recomendo a leitura dos materiais disponíveis em:
> [https://www.ime.unicamp.br/~valle/Teaching/MS211/Aula03.pdf](https://www.ime.unicamp.br/~valle/Teaching/MS211/Aula03.pdf)
> [https://www.geeksforgeeks.org/gaussian-elimination/](https://www.geeksforgeeks.org/gaussian-elimination/)


## 📂 Estrutura dos Arquivos

- `file.py` : Responsável pela leitura dos dados do arquivo de entrada.
- `matrix.py` : Contém a lógica de geração de combinações de variáveis básicas, resolução dos sistemas lineares e análise das soluções.
- Arquivo de entrada (por exemplo: `input/LP_00.txt`) com o seguinte formato:
  
  ```
  <número de variáveis> <número de restrições>
  <coeficientes da função objetivo>
  <coeficientes da 1ª restrição>
  <coeficientes da 2ª restrição>
  ...
  ```


## 💻 Como Executar


1. Execute o programa passando o caminho do arquivo como argumento:
   ```bash
   python3 main.py caminho_do_arquivo.txt
   ```

2. Acompanhe a saída no terminal.
   

## 📄 Exemplo

<p align="center"><strong>Entrada</strong></p>


```

5 3
-1 -2 0 0 0
1 1 0 0 4
1 0 1 0 2
0 1 0 1 3
```

<p align="center"><strong>Saída</strong></p>

```

x = [1, 3, 0, 1, 0]
z = -7.0 (viável)

x = [2, 2, 0, 0, 1]
z = -6.0 (viável)

x = [2, 0, 2, 0, 3]
z = -2.0 (viável)

x = [4, 0, 0, -2, 3]
z = -4.0 (inviável)

x = [0, 3, 1, 2, 0]
z = -6.0 (viável)

x = [0, 4, 0, 2, -1]
z = -8.0 (inviável)

x = [0, 0, 4, 2, 3]
z = 0.0 (viável)

Número total de soluções básicas: 8
Número de soluções básicas viáveis: 5
Número de soluções básicas inviáveis: 3

Solução ótima encontrada!
Função objetivo: -7.0
x = [1, 3, 0, 1, 0]
```



## 📞 Contato
> **Anna Laura Moura**  
> [LinkedIn](https://www.linkedin.com/in/anna-laura-614384205)  
> [nalauramoura@gmail.com](mailto:nalauramoura@gmail.com)