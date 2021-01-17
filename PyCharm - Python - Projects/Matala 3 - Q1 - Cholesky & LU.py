import numpy
from scipy.linalg import lu
from scipy.linalg import cholesky


# Matrix definition
A = numpy.array([[5, 2, 3],
                 [2, 6, 4],
                 [3, 4, 7]])

# LU factorization - PA=LU
P, L, U = lu(A)
print('P:\n', P)
print('L:\n', L)
print('U:\n', U)

R = cholesky(A)
print('R:')
print(R)
