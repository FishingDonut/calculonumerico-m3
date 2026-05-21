import math


def f(x: float) -> float:
    return (2 * (math.sin(x) ** 2)) / (x + 1)


x = math.pi / 16
n = 5

xi = [0.0, math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2]
yi = [math.sin(v) for v in xi]
y0, y1, x0, x1 = 0.0, 0.0, 0.0, 0.0

for v in range(len(xi) - 1):
    if xi[v] <= x <= xi[v + 1]:
        y0 = yi[v]
        y1 = yi[v + 1]
        x0 = xi[v]
        x1 = xi[v + 1]
        break


def interpolacao_linear() -> float:
    return y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)

def draw_table() -> None:
    print('_'*28)
    print("| {:<6} | {:<6} | {:<6} |".format('I', 'Xi', 'Sen(x)'))
    print('-'*28)
    for v in range(len(xi)):
        print("| {:^6} | {:^5.4f} | {:^5.4f} |".format(v, xi[v], yi[v]))
    print('_'*28)
    print('\n')
    pass

def draw_amount_calculo():
    print('_'*28)
    print('\n')
    print("y0 + ((y1 - y0) / (x1 - x0)) * (x - x0)")
    print(f"{y0} + (({y1} - {y0}) / ({x1} - {x0})) * ({x} - {x0})")
    print('\n')
    print('_'*28)
    pass

draw_table()
draw_amount_calculo()

print('interpolacao_linear')
print(interpolacao_linear())
