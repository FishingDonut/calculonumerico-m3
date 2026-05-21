matriz = [[10, 2, 3, 7],
          [1, 5, 1, -8],
          [2, 3, 10, 6]]

# matriz = [[1,   -15,    1,  -4],
#           [1,   2,      25, 14],
#           [15,  -2,     1,  6]]

i = len(matriz)
j = len(matriz[0])

z = [0 for _ in range(j - 1)]


def criterio_linha_verificacao(a: float, b: float) -> bool:
    return a >= b


def rotacao_matriz(matriz):
    for y in range(i):
        k = max(range(y, i), key=lambda x: abs(matriz[x][y]))
        matriz[y], matriz[k] = matriz[k], matriz[y]
    return matriz


def criterio_linha(matriz):
    for y in range(i):
        for x in range(j - 1):
            if (y == x):
                a = matriz[y][x]
                b = sum(matriz[y][n] for n in range(j) if n != x)
                if (criterio_linha_verificacao(a, b)):
                    return rotacao_matriz(matriz)
                else:
                    return matriz


def equacao_iterativas(matriz):
    for y in range(i):
        pass
        soma = sum(x ** k for key, x in enumerate(matriz[y]) if key != j for k in z if k < y)
        resultado = (matriz[y][-1] + soma) / matriz[y][y]
