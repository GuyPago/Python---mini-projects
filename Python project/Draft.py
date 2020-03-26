import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-math.pi/2, 11*math.pi + math.pi/2, 0.001)
y = np.sin(x)
z = x + y

plt.plot(x, y)
plt.show()
