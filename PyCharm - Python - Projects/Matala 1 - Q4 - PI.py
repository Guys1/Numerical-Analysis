import numpy as np
import sympy as sy

x = sy.Symbol('x')  # x is symbol varible so in f varible we can change the function and it will work because f is also symbol
print('π = ', np.pi) # pi check

def PI(n):
    i = 1
    sum = 0
    while i <= n:
        sum = sum + ((-1)**(i-1)*1/(2*i-1))
        i = i + 1
    sum = sum * 4
    return sum

n10 = PI(10)
print('π with n = 10 is: ', n10)
print('Absolute Error between π and n = 10 is: ', abs(np.pi - n10))
print('Relative Error between π and n = 10 is: ', abs(np.pi - n10)/abs(np.pi))

n20 = PI(20)
print('π with n = 20 is: ', n20)
print('Absolute Error between π and n = 20 is: ', abs(np.pi - n20))
print('Relative Error between π and n = 20 is: ', abs(np.pi - n20)/abs(np.pi))

n40 = PI(40)
print('π with n = 40 is: ', n40)
print('Absolute Error between π and n = 40 is: ', abs(np.pi - n40))
print('Relative Error between π and n = 40 is: ', abs(np.pi - n40)/abs(np.pi))
