import file
from itertools import combinations
import numpy as np

def generate_combinations():
    k = file.n - file.m
    for j in combinations(range(1, file.n+1), k):
        variables = []
        for i in j:
            var_name = f"x{i}"
            variables.append(var_name)

        #print(variables)
        
def exibir_melhor_solucao(valid_solutions):
    if valid_solutions:
        best_zero, best_assign, best_obj = valid_solutions[0]
        print("\n===== Solução ótima =====")
        print("Variáveis = 0:", [f"x{i}" for i in best_zero])
        print("Valores:", best_assign)
        print("Valor Função Objetivo:", best_obj, "\n")
    else:
        print("Nenhuma solução viável encontrada.\n")

def resolver_sistemas():
    valid_solutions = []
    k = file.n - file.m

    for j in combinations(range(1, file.n+1), k):
        variables = j
        # remaining = [f"x{i}" for i in range(1, file.n+1) if i not in variables]
        
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

        A = np.array(A_list, int)
        
        
        b_list = []
        for constraint in file.constraint:
            result_value = constraint['result']
            b_list.append(result_value)

        b = np.array(b_list, int)

        lista_zeradas = []
        for i in variables:
            var_name = f"x{i}"
            lista_zeradas.append(var_name)

        print("\nCombinação:", lista_zeradas)

        print("\nEntrada\n")
        print(A)
        print("\nSaída\n")
        print(b)

        try:
            sol = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            print("Sistema inválido: matriz A não é inversível.\n")
            continue


        assignment = {}

        # Parte 1: atribui 0.0 para as variáveis que foram zeradas
        for i in variables:
            var_name = f"x{i}"
            assignment[var_name] = 0.0

        # Parte 2: atribui os valores calculados para as variáveis restantes
        for var, val in zip(remaining, sol):
            assignment[var] = val

        if any(val < 0 for val in assignment.values()):
            continue

        obj = 0  # valor objetivo inicial

        for idx, coef in enumerate(file.objective_function, start=1):
            var_name = f"x{idx}"          # nome da variável correspondente, como "x1", "x2", ...
            value = assignment[var_name]  # valor da variável na solução atual
            produto = coef * value        # contribuição para a função objetivo
            obj += produto                # soma ao valor objetivo total

        if obj == 0:
            continue

        # print(f"Solução válida – zeradas: {[f'x{i}' for i in variables]}")
   
        print("\nSolução válida\n  Atribuições:", assignment)
        print("  Resultado:", obj, "\n")

        if not valid_solutions or obj > valid_solutions[0][2]:
            valid_solutions.insert(0, (variables, assignment, obj))
        else:
            valid_solutions.append((variables, assignment, obj))

    exibir_melhor_solucao(valid_solutions)

if __name__ == "__main__":
    file.readFile()
    generate_combinations()
    resolver_sistemas()
