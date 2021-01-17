import numpy as np
from numpy.linalg import qr, svd, norm

A = np.matrix([[1, 0, 1],
               [0, 1, 0],
               [0, 1, 1],
               [0, 1, 0],
               [1, 1, 0]])

# QR factorization
Q, R = qr(A)

print('A=', A)
print('Q=', Q)
print('R=', R)

print('norm of q1', norm(Q[:, 0]))
print('q1*q2=', np.dot(Q[:, 0].T, Q[:, 1]))

# SVD factorization

U, S, V = svd(A)
print('U=', U)
print('S=', S)
print('V=', V)

