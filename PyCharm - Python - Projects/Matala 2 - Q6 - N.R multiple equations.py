import sympy as sp
from sympy import *

# Define the variables
x = sp.Symbol('x')
y = sp.Symbol('y')
z = sp.Symbol('z')

# Define the system of equations
f1 = z**2 + 1 - (x*y)
f2 = x**2 + 1 - (x*y*z + y**2)
f3 = sp.exp(-y) + 3 - (sp.exp(x) + z)

# Define the initial guess and the column of equations
X0 = Matrix(3, 1, [1, 1, 1])
F = Matrix(3, 1, [f1, f2, f3])

# function for calculating the inverse of Jacobian
def invJ(J,X):
    jsub = J.subs([(x, X[0]), (y, X[1]), (z, X[2])])
    jsub = jsub.evalf()
    Jinv = jsub.inv()  # inverse the matrix

    return Jinv

# implement iterations
def Iteration(X, Jinv, F):
    Res = X - Jinv*F

    return Res


# function for implementing the whole iterative process
def NR_Multivar(X0, F, kk):
    J = Matrix.jacobian(F, [x, y, z]) # calculate Jacobian matrix

    for i in range(kk):
        Jinv = invJ(J, X0)
        Fi = sp.nfloat(F.subs([(x, X0[0]), (y, X0[1]), (z, X0[2])]), 7) # 7 is numbers after the point
        X0 = Iteration(X0, Jinv, Fi)
        print(sp.nfloat(X0, 7))

NR_Multivar(X0, F, 6)