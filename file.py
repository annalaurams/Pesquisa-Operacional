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
    
def print_():
    print()
    print("\nVariáveis:", n, "\nRestrições:", m)
    print("\nFunção objetivo:", objective_function, "\n")
    for r in constraint:
        print(r)
    print("______________________________________________________________\n")
    