import numpy as np
from numpy import linalg

x = [1.03, 1.43, 1.76, 2.20, 2.78, 3.15, 3.55, 4.12]
y = [2.37, 1.53, 1.02, 0.60, 0.26, 0.17, 0.13, 0.08]

def minimosQuadrados():
    pontos = 8
    grau = 1

    # vetor h
    H = np.zeros((grau+1, pontos))
    for i in range(len(H)):
        for j in range(len(H[0])):
            H[i][j] = pow(x[j], i)

    A  = np.zeros((grau+1, grau+1))
    b = np.zeros(grau+1)
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] = H[i].dot(H[j])
        b[i] = (-1) * H[i].dot(y)

    print("A = ", A)
    print("b = ", b)

    X = np.linalg.solve(A, b)
    for i in range(len(X)):
        print("a" + str(i+1) + "= ", X[i])

    print("y(x) para x = 2: ", X[1] * np.exp(X[0] * 2))
minimosQuadrados()