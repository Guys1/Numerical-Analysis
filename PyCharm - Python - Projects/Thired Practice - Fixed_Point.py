import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.Symbol('x')


# script for x=g(x) iteration implementation


def f1(xx):
    return np.cos(xx)


def f2(xx):
    return np.arccos(xx)


def f3(xx):
    return xx - np.sin(xx) + np.exp(-xx)


def f4(xx):
    return xx - 2 * np.sin(xx) + 2 * np.exp(-xx)


def fixedpoint_plot(g, p0, xmin, xmax):
    xx = np.linspace(xmin, xmax, 100)
    yy = g(xx)
    plt.ion()
    plt.plot(xx, xx, xx, yy)
    plt.show()
    plt.title("fixed point iteration")

    for i in range(10):
        p = g(p0)
        plt.plot([p0, p0], [p0, p], 'r')
        plt.pause(1)
        plt.plot([p0, p], [p, p], 'r')
        plt.show()
        plt.pause(1)
        p0 = p
        print(i, p)


print('Example 1')
fixedpoint_plot(f1, 1, 0, 1.3)

# print('Example 2')
# fixedpoint_plot(f2, 0.75, 0, 1)
#
# print('Example 3')
# fixedpoint_plot(f3,1,0,1.3)

# print('Example 4')
# fixedpoint_plot(f4,0.55,0.5,0.6)
