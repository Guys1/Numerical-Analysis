import numpy as np
from numpy.linalg import qr, svd, norm
import sympy as sp
from sympy import *

x = sp.Symbol('x')


def innerProd(v1, v2, a, b):
    return integrate(v1*v2, (x, a, b))

def normInnerProd(v1, a, b):
    return sp.sqrt(innerProd(v1, v1, a, b))

# for given set {x^0, x^1, x^2} find orthonormal basis, where the inner
# product is given in range [0, 1]
a = 0
b = 1
v1 = 1
v2 = x
v3 = x**2

u1 = v1
w1 = u1/normInnerProd(u1, a, b)
print('u1=', u1)
print('w1=', w1)

u2 = v2 - innerProd(x, w1, a, b)*w1
w2 = u2/normInnerProd(u2, a, b)
print('u2=', u2)
print('w2=', w2)

u3 = v3 - innerProd(v3, w1, a, b)*w1 - innerProd(v3, w2, a, b)*w2
w3 = u3/normInnerProd(u3, a, b)
print('u3=', u3)
print('w3=', w3)

u4 = v4 - innerProd(v4, w1, a, b)*w1 - innerProd(v3, w2, a, b)*w2
w3 = u3/normInnerProd(u3, a, b)
print('u3=', u3)
print('w3=', w3)
