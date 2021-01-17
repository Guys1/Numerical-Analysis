import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

# f - nonlinear equation
# n - number of iterations
# x0 - initial guess

x = sy.Symbol('x')
f = x**2 - 2
g = x - 2 * sy.sin(x)

def NR(f,n,x0):
    i = 0
    while (i <= n): # x_k+1 = x_k - f(x_k)/f'(x_k)
        x1 = x0 - f.subs(x,x0)/f.diff(x,1).subs(x,x0) #diff is nigzeret if you want seconed nigzert instaed of 1 put 2
        i = i+1
        x0 = x1
        print('xn=', '{:2.6f}'.format(float(x0))) #we want to print it as float and not shever

NR(g, 4, 1)

xx = np.linspace(0, 2, 100)
yy = xx**2-2

zz = xx*0
plt.plot(xx,yy,xx,zz)
plt.show()