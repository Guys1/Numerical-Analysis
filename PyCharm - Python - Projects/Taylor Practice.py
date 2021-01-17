import numpy as np
import sympy as sy
from sympy.functions import sin
import matplotlib.pyplot as plt

x = sy.Symbol('x')
f = sin(x)
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


t7 = taylor(f, 0, 7)
t5 = taylor(f, 0, 5)
t3 = taylor(f, 0, 3)

xx = np.linspace(-5, 5, 100)

yy7 = []
yy5 = []
yy3 = []

for ii in xx:
    yy7.append(t7.subs(x, ii))
    yy5.append(t5.subs(x, ii))
    yy3.append(t3.subs(x, ii))

# plt.plot(xx,yy3,label='3 terms',xx,yy5,label='5 terms',xx,yy7,label='7 terms')
plt.plot(xx, yy3, xx, yy5, xx, yy7)
plt.show()
