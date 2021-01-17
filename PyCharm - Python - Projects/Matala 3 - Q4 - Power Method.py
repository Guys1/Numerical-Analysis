import numpy
import numpy as np

# A
A = numpy.array([[0, 11, -5],
                 [-2, 17, -7],
                 [-4, 26, -10]])

# B
B = numpy.array([[4, 3, -3],
                 [2, 3, -2],
                 [4, 4, -3]])

#x0
x0 = numpy.array([[1],
                 [1],
                 [1]])

def PowerMethod(matrix, x0, n):
    for i in range(n):
        x0 = np.dot(matrix, x0)
        print('x{}:\n'.format(i), x0)
    AX = np.dot(matrix, x0)
    AXX = np.dot(np.transpose(AX), x0)
    XTX = np.dot(np.transpose(x0), x0)
    lamda = AXX / XTX
    print('The dominant self-value is:\n', lamda)

PowerMethod(A, x0, 5)
PowerMethod(B, x0, 5)
