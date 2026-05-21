import pandas as pd
import math

n = 4
a = 0
b = 1.2
h = (b - a) / n

print("A:{} | B:{} | N:{} | H:{}".format(a, b, n, h))


def f(x: float):
    try:
        return (math.e**x)*math.cos(x)
    except:
        print('Erro ', x, '\nRETURN 0 default')
        return 0


def trapezios(m: list[list[float | int]]) -> float:
    return sum([(h / 2) * (m[i - 1][1] + m[i][1]) for i in range(1, len(m))])

def simpson(m: list[list[float | int]]) -> float:
    if n%2 != 0:

        print("Error, n impar")
        return -1
    return sum([(h / 3) * (m[i][1] if i == 0 or i == len(m)-1 else (m[i][1] * 4 if i%2 != 0 else m[i][1] * 2)) for i in range(len(m))])

def formula_composta() -> None:
    intervalo: list[float] = [(i * h) + a for i in range(n + 1)]

    matriz = [[intervalo[i], f(intervalo[i])] for i in range(n + 1)]
    df = pd.DataFrame(data=matriz, columns=['X', 'Y'])
    print('▮' * 24)
    print(df.round(4))
    print('▮' * 24)
    #trapezios(matriz)
    s = simpson(matriz)
    print(f"{s:.4f}")
    return None

formula_composta()
