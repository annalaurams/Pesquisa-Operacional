import sys

restricoes = []
funcao_objetivo = []
n = 0
m = 0

def readFile(file_path):
    global restricoes, funcao_objetivo, n, m

    with open(file_path, 'r') as file:
        line = file.readline().strip().split()
        n = int(line[0])
        m = int(line[1])

        line = file.readline().strip().split()
        for valor in line:
            valor_float = float(valor) 
            funcao_objetivo.append(valor_float)

        for _ in range(m):
            line = file.readline().strip().split()
            restricao_temp = {}
            for indice in range(n):
                variavel = "x" + str(indice + 1)
                restricao_temp[variavel] = float(line[indice])
            restricao_temp['result'] = float(line[-1])
            restricoes.append(restricao_temp)

def print_():
    print("\nVariáveis:", n, "\nRestrições:", m)
    print("\nFunção objetivo:", funcao_objetivo, "\n")
    for r in restricoes:
        print(r)
    print("______________________________________________________________________________________________\n")
