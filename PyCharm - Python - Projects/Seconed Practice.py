"""
matrixes and conditions example - Michael
"""

import numpy as np
import scipy as sp
from scipy.linalg import hilbert

# matrix definition
A = np.matrix(([2, 3, 4], [1, 1, 1], [3, 4, 4]))
AA = np.array(([2, 3, 4], [1, 1, 1], [3, 4, 4]))

print('A=', A)
print('AA=', AA)
print('A*AA=', A*AA) # multiplaction matrix
invA = np.linalg.inv(A)
print('inv(A)=', invA) # opposite matrix
print('A*inv(A)=', A*invA)

# get matrix component
print(A[0, 0])

B = np.zeros((3, 4), dtype=int)  # matrix of zeros
print('B=', B)

C=np.ones((3, 4), dtype=int)  # matrix of ones
print('C=', C)

# define hilbert matrix H(i,j)=1/(i+j+1)

H = hilbert(4)
print('H=', H)
print('condition of H:', np.linalg.cond(H))   # cond of Hilbert matrix size 4

# implement solution of H*x=b with small error in initinal conditions
b = np.matrix(([1], [1], [1], [1]))
print('b', b)

#solve x1=inv(H)*b

x1 = np.linalg.inv(H)*b
print('x1=', x1)

# let's increase H[4,4] by 1%, H[4,4]=H[4,4]*1.01
H[3,3] = H[3, 3]*1.01
print('H=', H)

x2 = np.linalg.inv(H)*b
print('x1=', x2)




