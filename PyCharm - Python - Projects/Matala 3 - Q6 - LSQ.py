import numpy
import numpy as np

X = numpy.array([[0, 1],
                 [0.5, 1],
                 [1, 1],
                 [1.5, 1],
                 [2, 1],
                 [2.5, 1],
                 [3, 1],
                 [3.5, 1],
                 [4, 1],
                 [4.5, 1],
                 [5, 1]])

Y = numpy.array([[6],
                 [4.83],
                 [3.7],
                 [3.15],
                 [2.41],
                 [1.83],
                 [1.49],
                 [1.21],
                 [0.96],
                 [0.73],
                 [0.64]])

m, B = np.dot(np.linalg.pinv(X), Y)
b = np.exp(B)

print('m is: {}\nB is: {}\nb is: {}\n'.format(m, B, b))