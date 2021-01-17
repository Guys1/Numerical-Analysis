import numpy as np
import numpy
#from numpy import np


A = numpy.array([[4, -2, -2],
                 [3, -5, -1],
                 [2, -4, -7]])
b = ([[1],
      [1],
      [1]])

x0 = ([[0],
       [0],
       [-0.5]])

def DLU(A):
    D = np.zeros(A.shape)
    L = np.tril(A)
    U = np.triu(A)

    for i in range (A.shape[0]):
        D[i, i] = A[i, i]
        L[i, i] = 0
        U[i, i] = 0

    return D, L, U

def Jaacobi(A, x0, b, n):
    D, L, U = DLU(A)

    for i in range (n):
        x0 = np.dot(np.linalg.inv(D), (np.dot(-U-L, x0) + b))

    return x0

def GaussZaidel(A, x0, b, n):
    D, L, U = DLU(A)

    for i in range(n):
        x0 = np.dot(np.linalg.inv(D+L), (np.dot(-U, x0) + b))

    return x0
x1, y1, z1 = Jaacobi(A, x0, b, 2)
print('Jaacobi:\n x = {}\n y = {}\n z = {}'.format(x1, y1, z1))
x2, y2, z2 = GaussZaidel(A, x0, b, 2)
print('Gauss Zidel:\n x = {}\n y = {}\n z = {}'.format(x2, y2, z2))

