import file
from itertools import combinations
import numpy as np

def generate_combinations():
    k = file.n - file.m
    for j in combinations(range(1, file.n + 1), k):
        variables = []
        for i in j:
            var_name = f"x{i}"
            variables.append(var_name)
        # apenas gera combinações, não imprime

def exibir_melhor_solucao(valid_solutions):
    if valid_solutions:
        best_zero, best_assign, best_obj = valid_solutions[0]
        print("\n===== Solução ótima =====")
        print("Variáveis zeradas:", [f"x{i}" for i in best_zero])
        print("Valores:", best_assign)
        print("Valor da Função Objetivo:", best_obj, "\n")
    else:
        print("\nNenhuma solução viável encontrada.\n")

def resolver_sistemas():
    valid_solutions = []
    k = file.n - file.m

    for j in combinations(range(1, file.n + 1), k):
        variables = j

        # monta lista de variáveis que não foram zeradas
        remaining = []
        for i in range(1, file.n + 1):
            if i not in variables:
                var_name = f"x{i}"
                remaining.append(var_name)

        # monta matriz A
        A_list = []
        for constraint in file.constraint:
            row = []
            for var in remaining:
                value = constraint[var]
                row.append(value)
            A_list.append(row)
        A = np.array(A_list, int)

        # monta vetor b
        b_list = []
        for constraint in file.constraint:
            result_value = constraint['result']
            b_list.append(result_value)
        b = np.array(b_list, int)

        # imprime combinação atual
        lista_zeradas = []
        for i in variables:
            var_name = f"x{i}"
            lista_zeradas.append(var_name)

        print("\n=== Testando combinação ===")
        print("Variáveis zeradas:", lista_zeradas)
        print("\nMatriz A:")
        print(A)
        print("\nVetor b:")
        print(b)

        try:
            sol = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            print("⚠️ Sistema inválido: matriz A não é inversível.\n")
            continue

        # monta atribuições
        assignment = {}

        for i in variables:
            var_name = f"x{i}"
            assignment[var_name] = 0.0

        for var, val in zip(remaining, sol):
            assignment[var] = val

        # imprime todos os valores encontrados
        print("\nAtribuições encontradas:")
        for var_name in sorted(assignment.keys()):
            print(f"  {var_name} = {assignment[var_name]}")

        # verifica se há variáveis negativas
        if any(val < 0 for val in assignment.values()):
            print("⚠️ Solução inválida: variável negativa encontrada.\n")
            continue

        # calcula função objetivo
        obj = 0
        for idx, coef in enumerate(file.objective_function, start=1):
            var_name = f"x{idx}"
            value = assignment[var_name]
            produto = coef * value
            obj += produto

        if obj == 0:
            print("⚠️ Solução inválida: valor da função objetivo é 0.\n")
            continue

        # solução válida
        print("\n✅ Solução válida encontrada!")
        print(f"Valor da função objetivo: {obj}\n")

        # armazena solução
        if not valid_solutions or obj > valid_solutions[0][2]:
            valid_solutions.insert(0, (variables, assignment, obj))
        else:
            valid_solutions.append((variables, assignment, obj))

    exibir_melhor_solucao(valid_solutions)

if __name__ == "__main__":
    file.readFile()
    generate_combinations()
    resolver_sistemas()
