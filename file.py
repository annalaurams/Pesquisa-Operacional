import sys

constraint = []
objective_function = []
n = 0
m = 0

def readFile(file_path):
    global constraint, objective_function, n, m

    with open(file_path, 'r') as file:
        line = file.readline().strip().split()
        n = int(line[0])
        m = int(line[1])

        line = file.readline().strip().split()
        objective_function = [float(valor) for valor in line]

        for _ in range(m):
            line = file.readline().strip().split()
            restricao_temp = {}
            for indice in range(n):
                variavel = "x" + str(indice + 1)
                restricao_temp[variavel] = float(line[indice])
            restricao_temp['result'] = float(line[-1])
            constraint.append(restricao_temp)

def print_():
    print("\nVariáveis:", n, "\nRestrições:", m)
    print("\nFunção objetivo:", objective_function, "\n")
    for r in constraint:
        print(r)
    print("______________________________________________________________________________________________\n")
