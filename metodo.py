import file
from itertools import combinations
import numpy as np

def gerar_combinacoes():
    k = file.n - file.m
    for _ in combinations(range(1, file.n + 1), k):
        pass 

def exibir_melhor_solucao(solucao_valida):
    if solucao_valida:
        best_zero, result, objetivo = solucao_valida[0]
        print("\nSolução ótima encontrada!")
        print(f"Função objetivo: {objetivo}")
        print("x =", [result[f"x{i}"] for i in range(1, file.n + 1)])
    else:
        print("\nNenhuma solução viável encontrada.")

def testar_combinacao(variaveis):
    restante = []
    for i in range(1, file.n + 1):
        if i not in variaveis:
            var_name = f"x{i}"
            restante.append(var_name)

    A_list = []
    for constraint in file.constraint:
        row = []
        for var in restante:
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
        sol = np.linalg.solve(A, b) # resolve o sistema Ax = b
    except np.linalg.LinAlgError: # sistema sem solução
        return None  # sem solução

    resposta = {}
    for i in variaveis:
        var_name = f"x{i}"
        resposta[var_name] = 0.0

    for var, val in zip(restante, sol):
        resposta[var] = val

    x_list = []
    for i in range(1, file.n + 1):
        var_name = f"x{i}"
        x_list.append(resposta[var_name])

    z = 0
    for i in range(file.n):
        coeficiente = file.objective_function[i]
        valor_variavel = x_list[i]
        produto = coeficiente * valor_variavel
        z += produto

    if any(val < -1e-6 for val in resposta.values()):
        return x_list, z, False, resposta

    return x_list, z, True, resposta

def resolver_sistemas():
    solucao_valida = []
    viaveis = 0
    inviaveis = 0
    k = file.n - file.m
    todas_combinacoes = list(combinations(range(1, file.n + 1), k))

    for variaveis in todas_combinacoes:
        resultado = testar_combinacao(variaveis)

        if resultado is None:
            continue  # sistema sem solução

        x_list, z, eh_viavel, resposta = resultado

        print(f"\nx = {x_list}")
        if eh_viavel:
            print(f"z = {z} (viável)")
            viaveis += 1

            if z == 0:
                continue

            if not solucao_valida or z < solucao_valida[0][2]:
                solucao_valida.insert(0, (variaveis, resposta, z))
            else:
                solucao_valida.append((variaveis, resposta, z))
        else:
            print(f"z = {z} (inviável)")
            inviaveis += 1

    print(f"\nNúmero total de soluções básicas: {viaveis + inviaveis}")
    print(f"Número de soluções básicas viáveis: {viaveis}")
    print(f"Número de soluções básicas inviáveis: {inviaveis}")

    exibir_melhor_solucao(solucao_valida)
