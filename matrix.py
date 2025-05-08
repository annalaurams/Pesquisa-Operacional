import file
from itertools import combinations
import numpy as np

def generate_combinations():
    k = file.n - file.m
    for _ in combinations(range(1, file.n + 1), k):
        pass 

def exibir_melhor_solucao(valid_solutions):
    if valid_solutions:
        best_zero, best_assign, best_obj = valid_solutions[0]
        print("\nSolução ótima encontrada!")
        print(f"Função objetivo: {best_obj}")
        print("x =", [best_assign[f"x{i}"] for i in range(1, file.n + 1)])
    else:
        print("\nNenhuma solução viável encontrada.")

def testar_combinacao(variables):
    remaining = []
    for i in range(1, file.n + 1):
        if i not in variables:
            var_name = f"x{i}"
            remaining.append(var_name)

    A_list = []
    for constraint in file.constraint:
        row = []
        for var in remaining:
            value = constraint[var]
            row.append(value)
        A_list.append(row)
    A = np.array(A_list, float)

    b_list = []
    for constraint in file.constraint:
        result_value = constraint['result']
        b_list.append(result_value)
    b = np.array(b_list, float)

    try:
        sol = np.linalg.solve(A, b)
    except np.linalg.LinAlgError:
        return None  # sem solução

    assignment = {}
    for i in variables:
        var_name = f"x{i}"
        assignment[var_name] = 0.0

    for var, val in zip(remaining, sol):
        assignment[var] = val

    x_list = []
    for i in range(1, file.n + 1):
        var_name = f"x{i}"
        x_list.append(assignment[var_name])

    z = 0
    for i in range(file.n):
        coeficiente = file.objective_function[i]
        valor_variavel = x_list[i]
        produto = coeficiente * valor_variavel
        z += produto

    if any(val < -1e-6 for val in assignment.values()):
        return x_list, z, False, assignment

    return x_list, z, True, assignment

def resolver_sistemas():
    valid_solutions = []
    viaveis = 0
    inviaveis = 0
    k = file.n - file.m
    todas_combinacoes = list(combinations(range(1, file.n + 1), k))

    for variables in todas_combinacoes:
        resultado = testar_combinacao(variables)

        if resultado is None:
            continue  # sistema sem solução

        x_list, z, eh_viavel, assignment = resultado

        print(f"\nx = {x_list}")
        if eh_viavel:
            print(f"z = {z} (viável)")
            viaveis += 1

            if z == 0:
                continue

            if not valid_solutions or z < valid_solutions[0][2]:
                valid_solutions.insert(0, (variables, assignment, z))
            else:
                valid_solutions.append((variables, assignment, z))
        else:
            print(f"z = {z} (inviável)")
            inviaveis += 1

    print(f"\nNúmero total de soluções básicas: {viaveis + inviaveis}")
    print(f"Número de soluções básicas viáveis: {viaveis}")
    print(f"Número de soluções básicas inviáveis: {inviaveis}")

    exibir_melhor_solucao(valid_solutions)
