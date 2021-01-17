import numpy
import numpy as np

# A
A = numpy.array([[10, -1, 2, 0],
                 [-1, 11, -1, 3],
                 [2, -1, 10, -1],
                 [0, 3, -1, 8]])
# b
b = numpy.array([[6],
                 [25],
                 [-11],
                 [15]])
# zero vector
x0 = numpy.array([[0],
                  [0],
                  [0],
                  [0]])

def DLU(A):
    D = np.zeros(A.shape)
    L = np.tril(A)
    U = np.triu(A)

    return D, L, U

def GaussZaidel(A, x0, b, n):
    D, L, U = DLU(A)

    for i in range(n):
        x0 = np.dot(np.linalg.inv(D+L), (np.dot(-U, x0) + b))

    return x0

x1, x2, x3, x4 = GaussZaidel(A, x0, b, 2)
print('Gauss Zidel:\n x1 = {}\n x2 = {}\n x3 = {}\n x4 = {}'.format(x1, x2, x3, x4))