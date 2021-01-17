import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

x = [0.9, 1.3, 1.9, 2.1, 2.6, 3.0, 3.9, 4.4, 4.7, 5.0, 6.0, 7.0, 8.0, 9.2, 10.5, 11.3, 11.6, 12.0, 12.6, 13.0, 13.3]
y = [1.3, 1.5, 1.85, 2.1, 2.6, 2.7, 2.4, 2.15, 2.05, 2.1, 2.25, 2.3, 2.25, 1.95, 1.4, 0.9, 0.7, 0.6, 0.5, 0.4, 0.25]

p = np.polyfit(x, y, 20)
f_interp = interp1d(x,y,kind='cubic')
xnew = np.linspace(0.9, 13.3, 100)
f_fit = np.polyval(p, xnew)

R = 5
theta = np.linspace(0,2*np.pi, 10)
x_theta = R*np.cos(theta)
y_theta = R*np.sin(theta)

x_cubic_spline = interp1d(theta, x_theta, kind='cubic')
y_cubic_spline = interp1d(theta, y_theta, kind='cubic')
theta2 = np.linspace(0,2*np.pi, 100)
x_theta2 = R*np.cos(theta2)
y_theta2 = R*np.sin(theta2)

plt.plot(x, y, 'o', xnew, f_interp(xnew), 'r', xnew, f_fit, 'b')
plt.axis([0, 14, 0, 5])
plt.show()



