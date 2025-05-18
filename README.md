# Resolução de Sistemas Lineares

<div align="center">

[![IDE](https://img.shields.io/badge/IDE-Visual%20Studio%20Code-informational)](https://code.visualstudio.com/docs/?dv=linux64_deb)
![Linguagem](https://img.shields.io/badge/Linguagem-Python-orange)

</div>

Este projeto tem como finalidade resolver sistemas lineares provenientes de problemas de **Programação Linear (PL)** para casos de **minimização**, utilizando o método de **enumeração de soluções básicas**.

---

### 🖥️ Requisitos do Ambiente

- **Python:** Versão 3.12 ou superior instalada ([instale aqui](https://www.python.org/downloads/))
- **Bibliotecas**
  - [NumPy](https://numpy.org/doc/stable/) – para manipulação de matrizes e resolução de sistemas lineares
  - [itertools](https://docs.python.org/3/library/itertools.html) – para geração de combinações de variáveis básicas
  - [sys](https://docs.python.org/3/library/sys.html) – para captura de argumentos passados via linha de comando


### 🧪 Execução do Programa

1. Certifique-se de estar dentro da pasta `src`

1. No terminal, execute:

   ```bash
   python3 main.py caminho_do_arquivo.txt
   ```

   Substitua `caminho_do_arquivo.txt` pelo caminho real do seu arquivo de entrada (ex: `input/LP_00.txt`).


   Exemplo do comando completo:
   ```bash
   python3 main.py input/LP_00.txt 
   ```

2. Acompanhe a saída do terminal.

---

## 📂 Estrutura dos Arquivos

- `file.py` : Responsável pela leitura e estruturação dos dados de entrada.
- `matrix.py` : Geração de combinações básicas, resolução dos sistemas e avaliação das soluções.
- Arquivos de entrada (ex: `input/LP_00.txt`) devem seguir o seguinte formato:

  ```
  <número de variáveis> <número de restrições>
  <coeficientes da função objetivo>
  <coeficientes da 1ª restrição>
  <coeficientes da 2ª restrição>
  ...
  ```

---

## 📚 Resolução de Sistemas com NumPy

A resolução dos sistemas lineares é realizada por meio da biblioteca [**NumPy**](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html). O método utilizado é:

```python
sol = np.linalg.solve(A, b)  
```

Caso o sistema não admita solução, o programa captura a exceção:

```python
except np.linalg.LinAlgError:
```




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
---

## 📞 Contato
> **Anna Laura Moura**  
> [LinkedIn](https://www.linkedin.com/in/anna-laura-614384205)  
> [nalauramoura@gmail.com](mailto:nalauramoura@gmail.com)
