import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [1.03, 1.43, 1.76, 2.20, 2.78, 3.15, 3.55, 4.12]
y = [2.37, 1.53, 1.02, 0.60, 0.26, 0.17, 0.13, 0.08]

def polinomial(x, y, xi):
    n = len(x)
    fdd = [[None for x in range(n)] for x in range(n)]

    for i in range(n):
        fdd[i][0] = y[i]

    for j in range(1, n):
        for i in range(n-j):
            fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1])/(x[i + j] - x[i])

    xterm = 1
    yint = fdd[0][0]

    for o in range(1, n):
        xterm = xterm * (xi - x[o - 1])
        yint = yint + fdd[0][o] * xterm
    
    return yint

xp = np.interp(2, x, y)
y_interpolado = polinomial(x, y, xp)
t = np.arange(0.7, 4.2, 0.1) # CONSIDERANDO O SEGUINTE INTERVALO DE TEMPO

yt = []

for i in t:
    yt.append(polinomial(x, y, i))

print(xp)