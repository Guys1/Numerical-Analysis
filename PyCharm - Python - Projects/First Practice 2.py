# import sympy as sp
# from sympy import cos

import numpy as np
from numpy import cos
from numpy import matrix
from scipy.linalg import hilbert


def f1(x):
    return cos(x)


y = f1(30)


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))

# ---------------------------------------------
A = matrix([[1, 2, 3], [2, 3, 3], [10, 7, 5]])
print(A)
xx = matrix([[1, 2, 3]])
print(xx)
print(A * xx.T)


# -Define Pascal matrix
def PascalMat(n):
    P = np.zeros((n, n), dtype=int)
    for i in range(0, n):
        for j in range(0, n):
            P[i, j] = factorial(i + j) / factorial(i) / factorial(j)
    print(P)


PascalMat(5)

H = hilbert(5)
print(H)

