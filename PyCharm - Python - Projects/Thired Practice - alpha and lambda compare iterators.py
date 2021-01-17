import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
from sympy.functions import sin, exp

# f - nonlinear equation
# n - number of iterations
# x0 - initial guess

x = sy.Symbol('x')
f = x**2 - 2
g = x - 2 * sy.sin(x)
'''
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
'''
p = 1/np.sqrt(2) # nekudat shevet
g2 = (2*x**2+1)/(8*x)+x/(2*x**2+1) # our new function g
dg2_1 = g2.diff(x, 1) # first nigzeret
print('dg2_1 = ', dg2_1)
a1 = dg2_1.subs(x, p) # hatzava shel nekudat shevet
print('a1 = ', a1)

dg2_2 = g2.diff(x, 2) # seconed nigzeret
print('dg2_2 = ', dg2_2)
a2 = dg2_2.subs(x, p)
print('a2 = ', a2)

dg2_3 = g2.diff(x, 3) # thired nigzeret
print('dg2_3 = ', dg2_3)
a3 = dg2_3.subs(x, p)
print('a3 = ', a3)

dg2_4 = g2.diff(x, 4) #forth nigzeret
print('dg2_4 = ', dg2_4)
a4 = dg2_4.subs(x, p)
print('a4 = ', a4)