#from sympy import sin
from numpy import sin
def bisect(f,a,b,Nmax):
    n = 1
    while n <= Nmax:
        c = (a+b)/2.0
        print("a=%s\tc=%s \t b=%s \t f(c)=%s" % (a, c, b, f(c)))
        if f(c) == 0 or n == Nmax:
            return c
        else:
            n = n+1
            if f(c)*f(a) < 0:
                b = c
            else:
                a = c

def regulaFalsi(f,a,b,Nmax):
    n = 1
    while n <= Nmax:
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        print("a=%s\tc=%s \t b=%s \t f(c)=%s" % (a, c, b, f(c)))
        if f(c) == 0 or n == Nmax:
            return c
        else:
            n = n+1
            if f(c)*f(a) < 0:
                b = c
            else:
                a = c


def func1(x):
    return x*sin(x)-1

def func2(x):
    return 4*x**3-2

#alpha = bisect(func2,-2,2,20)
#alpha = bisect(func1, 0, 2, 30)
#alpha = bisect(func2, -2, 2, 30)
alpha = regulaFalsi(func1, 0, 2, 5)
print(alpha)

"""
when we use regula falsi the sin is not calculate numeric
so we will use -> from numpy import sin
"""