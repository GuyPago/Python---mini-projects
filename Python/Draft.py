import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-math.pi/2, 11*math.pi + math.pi/2, 0.001)
y = np.sin(x)
z = x + y

plt.plot(x, y)
plt.show()


x = 4
y = 2

try:
    print(x/y)
except:
    print('Cant divide by zero, mr athenes.')

if x/y == 2:
    raise ValueError

print((16*70)/3)
