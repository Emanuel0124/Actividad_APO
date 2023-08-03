from random import randint
def matriz_aleatoria():
    N = 5
    M = 10

    m = [[randint(1,10) for j in range(M)] for i in range(N)]

    for h in m:
        print("la matriz es: ", h)