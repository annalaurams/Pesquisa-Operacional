import math
from itertools import combinations
import numpy as np

constraint = []
objective_function = []
n = 0
m = 0

def readFile():
    global constraint, objective_function, n, m

    file = open('arquivo.txt', 'r')

    line = file.readline().strip().split()
    n = int(line[0])
    m = int(line[1])

    line = file.readline().strip().split()
    for valor in line:
        objective_function.append(int(valor))

    counter = 0
    while counter < m:
        line = file.readline().strip().split()

        restricao_temp = {}
        for indice in range(n):
            variavel = "x" + str(indice + 1)
            restricao_temp[variavel] = int(line[indice])

        restricao_temp['result'] = int(line[-1])

        constraint.append(restricao_temp)  # agora está certo!

        counter += 1

    file.close()

def print_():

    print()
    print("Número de variáveis:", n)
    print("Número de restrições:", m)
    print("Função objetivo:", objective_function)
    for r in constraint:
        print(r)

    print()
    
def gerar_combinacoes_para_zero():
    """
    Gera e imprime na tela todas as combinações de variáveis
    que serão zeradas, de tamanho n - m.
    """
    k = n - m
    # gera combinações de índices [1..n] tomados k a k
    for combo in combinations(range(1, n+1), k):
        vars_zero = [f"x{i}" for i in combo]
        print(vars_zero)

def print_():
    print()
    print("Número de variáveis:", n)
    print("Número de restrições:", m)
    print("Função objetivo:", objective_function)
    for r in constraint:
        print(r)
    print()

def resolver_sistemas():
    """
    Para cada conjunto de (n-m) variáveis a zero, monta A·x = b
    (A: coeficientes das variáveis restantes; b: termos independentes)
    e resolve via numpy.linalg.solve. Imprime solução completa.
    """
    k = n - m
    for combo in combinations(range(1, n+1), k):
    
        vars_zero = combo
        print("Combo", combo)

        remaining = [f"x{i}" for i in range(1, n+1) if i not in vars_zero]
        
        print("Remaining", remaining)

        # monta A e b
        A = np.array([[constr[var] for var in remaining] for constr in constraint], dtype=float)
        b = np.array([constr['result'] for constr in constraint], dtype=float)
        
        print("A", A)
        print("b", b)

        # tenta resolver
        try:
            sol = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            print(f"Combinação {[f'x{i}' for i in vars_zero]}: matriz singular, sem solução única\n")
            continue

        # monta dicionário com todas as variáveis
        assignment = {f"x{i}": 0.0 for i in vars_zero}
        assignment.update({var: val for var, val in zip(remaining, sol)})

        # imprime
        print(f"Variáveis zeradas: {[f'x{i}' for i in vars_zero]}")
        print("Solução encontrada:", assignment)
        print()


if __name__ == "__main__":
    readFile()
    # print_()
    # print("Total de combinações:", math.comb(n, n-m))
    # print("Combinações de variáveis a zerar:")
    gerar_combinacoes_para_zero()
    # print("Resolvendo todos os sistemas básicos:\n")
    resolver_sistemas()