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

        constraint.append(restricao_temp)

        counter += 1

    file.close()

def gerar_combinacoes_para_zero():

    k = n - m
    for combo in combinations(range(1, n+1), k):
        vars_zero = [f"x{i}" for i in combo]
        print(vars_zero)


def resolver_sistemas():
    """
    Para cada conjunto de (n-m) variáveis a zero:
     - monta A·x = b
     - resolve via numpy.linalg.solve
     - descarta se alguma variável < 0 ou se valor objetivo == 0
     - armazena soluções válidas, mantendo a de maior objetivo em valid_solutions[0]
    Ao final imprime todas as soluções válidas e destaca a ótima.
    """
    valid_solutions = []
    k = n - m

    for combo in combinations(range(1, n+1), k):
        vars_zero = combo
        remaining = [f"x{i}" for i in range(1, n+1) if i not in vars_zero]

        A = np.array([[constr[var] for var in remaining] for constr in constraint], dtype=float)
        b = np.array([constr['result'] for constr in constraint], dtype=float)

        try:
            sol = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            continue

        assignment = {f"x{i}": 0.0 for i in vars_zero}
        assignment.update({var: val for var, val in zip(remaining, sol)})

        if any(val < 0 for val in assignment.values()):
            continue

        obj = sum(coef * assignment[f"x{idx}"] for idx, coef in enumerate(objective_function, start=1))
        if obj == 0:
            continue

        # imprime cada solução válida
        print(f"Solução válida - Variáveis zeradas: {[f'x{i}' for i in vars_zero]}")
        print("  Atribuições:", assignment)
        print("  Valor objetivo:", obj)
        print()

        # armazena solução
        if not valid_solutions or obj > valid_solutions[0][2]:
            valid_solutions.insert(0, (vars_zero, assignment, obj))
        else:
            valid_solutions.append((vars_zero, assignment, obj))

    # imprime solução ótima
    if valid_solutions:
        best_zero, best_assign, best_obj = valid_solutions[0]
        print("=== Solução ótima encontrada ===")
        print("Variáveis zeradas:", [f"x{i}" for i in best_zero])
        print("Atribuições:", best_assign)
        print("Valor objetivo:", best_obj)
    else:
        print("Nenhuma solução viável encontrada.")


if __name__ == "__main__":
    readFile()
    print("Combinações de variáveis a zerar:")
    gerar_combinacoes_para_zero()
    print("\nResolvendo sistemas e listando soluções válidas:\n")
    resolver_sistemas()
