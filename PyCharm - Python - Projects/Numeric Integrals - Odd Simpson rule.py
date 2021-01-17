import numpy as np
from scipy.integrate import quad
import sympy as sp
#dadadaddaa
t = sp.Symbol('t')
I = sp.integrate(sp.exp(-t**2), (t, 1, 3))
print('I = ', float(I))

def f1(x):
    return np.exp(-x**2)

def f2(x):
    return np.sqrt(1 + x ** 3)

def f3(x):
    return np.sqrt(1 + x ** 2)

def simpson (f, a, b, n):
    # 1. define the coeffs
    w = 2 * np.ones((n + 1, 2))
    start = 1
    stop = n+1
    step = 1
    for i in range(start, stop, step):
        w[i] = 3
        if i % 3 == 0:
            w[i] = 2
    w[0] = 1
    w[n] = 1

    # 2. define samples
    x = np.linspace(a, b, n+1)
    y = f(x)

    # 3. final calculation
    h = (b - a) / n
    S = ((3 * h) / (8 * np.dot(y, w))) - ((3 * h ** 5) / (80)) * np.diff(np.shape(y), n = 4)
    return S

S10 = simpson(f1, 1, 10, 12)
print('S10 = ', S10)

S20 = simpson(f1, 1, 10, 24)
print('S20 = ', S20)

S40 = simpson(f1, 1, 10, 48)
print('S40 = ', S40)

S80 = simpson(f1, 1, 10, 96)
print('S80 = ', S80)

ES10 = np.abs(I - S10)
print('ES10  = ', float(ES10))
ES20 = np.abs(I - S20)
print('ES20  = ', float(ES20))
ES40 = np.abs(I - S40)
print('ES40  = ', float(ES40))
ES80 = np.abs(I - S80)
print('ES80  = ', float(ES80))

print('ES10 / ES20 = ', float(ES10/ES20))
print('ES20 / ES40 = ', float(ES20/ES40))
print('ES40 / ES80 = ', float(ES40/ES80))


