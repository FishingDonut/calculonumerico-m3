import pandas as pd


def criterion_linha(m: list[list[float]]) -> bool:
    elementos = []  # elementos nao principais da linha A12, A13 .. An!=n.
    for ik, iv in enumerate(m):
        iv: list[float]

        principal = abs(m[ik][ik])  # pega valor de lina A11, A22, A33 ... Ann.
        for jk, jv in enumerate(iv[:-1]):
            jv: float

            if ik == jk:
                continue
            elementos.append(abs(jv))

        if principal >= sum(
                elementos):  # verifica se passa no criterio de linha A11 >= A12 + A13. Elementos sempre positivos "abs()".
            elementos = []
            continue
        else:
            return False

    return True


def permutacao(m: list[list[float]]) -> list[list[float]]:
    for i in range(len(m)):
        p = abs(m[i][i])
        for j in range(len(m)):
            if i == j:
                continue

            if p > abs(m[j][i]):
                continue

            if p < abs(m[j][i]):
                m[j], m[i] = m[i], m[j]
    return m


def equacao_interativa(m: list[list[float]], k: int = 0,
                       aproximacao_interacao: list[float] | None = None, condicao_parada: float = 0.01) -> float:
    if not aproximacao_interacao:
        return 0.0

    aproximacao_interacao_antiga = [i for i in aproximacao_interacao]

    sun_line = 0
    for ik, iv in enumerate(m):
        for jk, jv in enumerate(iv[:-1]):
            if ik == jk:
                continue

            sun_line += (jv * aproximacao_interacao[jk]) * -1

        sun_line += iv[-1]
        aproximacao_interacao[ik] = sun_line / iv[ik]
        sun_line = 0

    print(f"K {k}\n")
    df = pd.DataFrame([aproximacao_interacao], columns=["X" + str(n + 1) for n in range(len(aproximacao_interacao))])
    print(df.to_string(index=False, justify='left'), "\n")

    k += 1

    erros = [abs(aproximacao_interacao[n] - aproximacao_interacao_antiga[n]) for n in range(len(aproximacao_interacao))]
    error_max = max([n for n in erros])

    for n, erro in enumerate(erros):
        status = ">" if erro > condicao_parada else "<"
        print("X{} {:1.4f} {} {}".format(n + 1, erro, status, condicao_parada))

    if error_max <= condicao_parada:
        return error_max

    print('=' * 24)
    return equacao_interativa(m, k, aproximacao_interacao, condicao_parada)


matriz: list[list[float]] = [
    [1.0, -15.0, 1.0, -4.0],
    [1.0, 2.0, 25.0, 14.0],
    [15.0, -2.0, 1.0, 6.0]
]

print('=' * 24)
print('MATRIZ')
df = pd.DataFrame(data=matriz, columns=["X" + str(n + 1) for n in range(min([len(n) for n in matriz]))])
print(df.to_string(index=False, justify='left'))
print('=' * 24)

if not criterion_linha(matriz):
    matriz = permutacao(matriz)
    print('=' * 24)
    print('MATRIZ PERMUTADA')
    df = pd.DataFrame(data=matriz, columns=["X" + str(n + 1) for n in range(min([len(n) for n in matriz]))])
    print(df.to_string(index=False, justify='left'))
    print('=' * 24)

equacao_interativa(matriz, k=0, aproximacao_interacao=[0 for n in range(len(matriz))], condicao_parada=0.01)
