import numpy as np
import sympy as sp
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

x = sp.Symbol('x')

def fourierSeries(x, n):
    g = -0.5
    for i in range(1, n):
        g = g + 6/((2*i - 1)*pi)*sp.sin((2*i-1)*x)
    return g

t  = np.linspace(-pi, pi, 300)
t2  = np.linspace(-3*pi, 3*pi, 1500)

f = np.piecewise(t, [t < 0, t >= 0], [-2, 1])
fourier = fourierSeries(x, 20)
fourier_t = [fourier.subs(x, x0) for x0 in t2]
figure()
plot(t, f, 'r', t2, fourier_t, 'b')
show()
