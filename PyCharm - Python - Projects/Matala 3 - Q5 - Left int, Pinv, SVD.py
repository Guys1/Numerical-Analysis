import numpy
import numpy as np
from numpy.linalg import svd

# A1
A1 = numpy.array([[2, 1],
                 [3, 5],
                 [2.2, -1.1],
                 [4, 3.1]])

# B1
B1 = numpy.array([[-1.1],
                 [2.3],
                 [-4.2],
                 [5.1]])

# A2
A2 = numpy.array([[2, 1],
                 [3, 5]])

# B2
B2 = numpy.array([[-1.1],
                   [5]])

# A3
A3 = numpy.array([[3, 2, -2, -1],
                 [1, 0.3, 1, 5]])

# B3
B3 = numpy.array([[-1.3],
                  [2.7]])


def LeftInverse(A, B):
    x1 = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(A), A)), np.transpose(A)), B)
    return x1

def SVD(A, B):
    U, S, V = svd(A)
    Vt = np.transpose(V)
    S = np.diag(S)
    a = np.dot(np.dot(U, S), Vt)
    a_inv = np.linalg.inv(a)
    x2 = np.dot(a_inv, B)
    return x2

def Pinv(A, B):
    check3 = np.dot(np.linalg.pinv(A), B)
    return check3

def CheckSolution(A, B):
    try:
        check1 = LeftInverse(A, B)
        if check1.any() != None:
            print('Solution of matrix is:\n {}'.format(check1))
        else:
            print('Left Inverse is not working\n')
    except:
        print('\nMatrix has no solution\n')
    try:
        check2 = SVD(A, B)
        if check2.any() != None:
            print('Solution of matrix is:\n {}'.format(check2))
        else:
            print('SVD is not working\n')
    except:
        print('\nMatrix has no solution\n')
    try:
        check3 = Pinv(A, B)
        if check3.any() != None:
            print('Solution of matrix is:\n {}'.format(check3))
        else:
            print('Pinv is not working\n')
    except:
        print('\nMatrix has no solution\n')

print("First Matrix:\n")
CheckSolution(A1, B1)
print("Seconed Matrix:\n")
CheckSolution(A2, B2)
print("Third Matrix:\n")
CheckSolution(A3, B3)
