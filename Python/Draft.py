import matplotlib.pyplot as plt
import numpy as np
import math


x = np.arange(-math.pi/2, 11*math.pi + math.pi/2, 0.001)
y = np.sin(x)
z = x + y

plt.plot(x, y)
plt.show()



print('Hey Betanir,\v what\'s up ?')

x = [2,4,2,32,34,32,432,4,324,324,32,4,3,4,2,23,4,4,3,4,2,5,62,62,6,3,6]
set(x)
