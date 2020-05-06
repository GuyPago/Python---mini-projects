import matplotlib.pyplot as plt
import numpy as np
from math import pi
import math


x = np.arange(-pi/2, 11*pi + pi/2, 0.001)
y = np.sin(x)
z = x + y

plt.plot(x, y)
plt.show()
