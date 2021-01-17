import numpy as np
from numpy.linalg import qr, svd, norm

A = np.matrix([[-0.808, 0.914, -1.38],
               [-1.828, -0.405, -0.513],
               [-0.06, 0.056, 0.912]])

b = np.matrix([[1],
               [0],
               [0]])

# QR factorization
Q, R = qr(A)

print('A=', A)
print('b=', b)
print('Q=', Q)
print('R=', R)
x = np.dot(np.linalg.inv(R), np.dot(np.transpose(Q), b))

print('X=', x)

