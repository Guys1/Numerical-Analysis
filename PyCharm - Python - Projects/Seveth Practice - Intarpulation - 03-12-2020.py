import numpy as np
from numpy import polyfit
from numpy import polyval
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

x = [2, 2.75, 4]
y = [1/2, 4/11, 1/4] # sampling of f(x) = 1/x

p = polyfit(x, y, 2)
print('p=', p)

# create graph of both functions
xx = np.linspace(0, 4.1, 100)
yy = 1/xx

yy_apprx = polyval(p, xx)

figure()
plot(xx, yy, '-r', xx, yy_apprx, '-b')
show()

x1 = [2, 3, 4, 7, 13]
y1 = [10, -1, 2, 3, -3]
