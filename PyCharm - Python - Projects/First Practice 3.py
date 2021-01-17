import numpy as np
import matplotlib.pyplot as plt

x= np.linspace(1, 10, 100) #linspace creates array from 1 to 10 , 100 points
y= np.exp(-x)*np.sin(x)

plt.plot(x, y, 'or')
plt.grid(True)
plt.show()

c = lambda x, y: x**2 + y**2
print(c(3, 4))
