import numpy as np
from scipy.integrate import quad
import sympy as sp

t = sp.Symbol('t')
I = sp.integrate(sp.exp(-t**2), (t, 1, 3))
print('I = ', float(I))

def f1(x):
    return np.exp(-x**2)

def f2(x):
    return np.sqrt(1 + x ** 3)

def f3(x):
    return np.sqrt(1 + x ** 2)

def trapez (f, a, b, n):
    # 1. define the coeffs
    w = 2 * np.ones((n + 1, 1))
    w[0] = 1
    w[n] = 1

    # 2. define samples
    x = np.linspace(a, b, n+1)
    y = f(x)

    # 3. final calculation
    h = (b - a) / n
    T = h / 2 * np.dot(y, w)
    return T

def simpson (f, a, b, n):
    # 1. define the coeffs
    w = 2 * np.ones((n + 1, 1))
    for i in range(1, n+1, 2):
        w[i] = 4
    w[0] = 1
    w[n] = 1

    # 2. define samples
    x = np.linspace(a, b, n+1)
    y = f(x)

    # 3. final calculation
    h = (b - a) / n
    S = h / 3 * np.dot(y, w)
    return S

T10 = trapez(f1, 1, 3, 10)
print('T10 = ', T10)

T20 = trapez(f1, 1, 3, 20)
print('T20 = ', T20)

T40 = trapez(f1, 1, 3, 40)
print('T40 = ', T40)

T80 = trapez(f1, 1, 3, 80)
print('T80 = ', T80)

S10 = simpson(f1, 1, 3, 10)
print('S10 = ', S10)

S20 = simpson(f1, 1, 3, 20)
print('S20 = ', S20)

S40 = simpson(f1, 1, 3, 40)
print('S40 = ', S40)

S80 = simpson(f1, 1, 3, 80)
print('S80 = ', S80)

ET10 = np.abs(I - T10)
print('ET10  = ', float(ET10))
ET20 = np.abs(I - T20)
print('ET20  = ', float(ET20))
ET40 = np.abs(I - T40)
print('ET40  = ', float(ET40))
ET80 = np.abs(I - T80)
print('ET80  = ', float(ET80))

ES10 = np.abs(I - S10)
print('ES10  = ', float(ES10))
ES20 = np.abs(I - S20)
print('ES20  = ', float(ES20))
ES40 = np.abs(I - S40)
print('ES40  = ', float(ES40))
ES80 = np.abs(I - S80)
print('ES80  = ', float(ES80))

print('ET10 / ET20 = ', float(ET10/ET20))
print('ET20 / ET40 = ', float(ET20/ET40))
print('ET40 / ET80 = ', float(ET40/ET80))

print('ES10 / ES20 = ', float(ES10/ES20))
print('ES20 / ES40 = ', float(ES20/ES40))
print('ES40 / ES80 = ', float(ES40/ES80))

# Next Exercise:
# f2 = sqrt(1 + x ** 3), a = 1, b = 4
# f3 = sqrt(1 + x ** 2), a = 1, b = 5



