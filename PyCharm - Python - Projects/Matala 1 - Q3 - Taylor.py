import numpy as np
import sympy as sy
from sympy.functions import sin, exp
import matplotlib.pyplot as plt

x = sy.Symbol('x')  # x is symbol varible so in f varible we can change the function and it will work because f is also symbol
# f = 2*exp(x)
# x = x * (-1)
f = (1 - exp(-x)) / x
f1 = exp(-x)
# f = exp(2*x+3)
# f = np.e**x #this is scalar from numpy(np)
# f.subs(x, 0)

f.subs(x, 1)

df = f.diff(x, 2)
print(df)

print(df.diff(x, 1))

print(sy.factorial(3))


def taylor(fun, x0, n):
    i = 0
    s = 0
    while i <= n:
        s = s + (fun.diff(x, i).subs(x, x0)) * (x - x0) ** i / sy.factorial(i)
        i = i + 1
    return s


t2 = taylor(f1, 0, 2)
t4 = taylor(f1, 0, 4)
t6 = taylor(f1, 0, 6)

s2 = (1 - t2) / x
s4 = (1 - t4) / x
s6 = (1 - t6) / x
xx = np.linspace(-1, 1, 100)

yy2 = []
yy4 = []
yy6 = []

for ii in xx:
    yy2.append(s2.subs(x, ii))
    yy4.append(s4.subs(x, ii))
    yy6.append(s6.subs(x, ii))

# plt.plot(xx,yy2,label='2 terms',xx,yy4,label='4 terms',xx,yy6,label='6 terms')
plt.plot(xx, yy2, xx, yy4, xx, yy6)
plt.show()
