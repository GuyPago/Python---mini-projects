import matplotlib.pyplot as plt
import numpy as np
from math import pi
import math


x = np.arange(-pi/2, 11*pi + pi/2, 0.001)
y = np.sin(x)
z = x + y

plt.plot(x, y)
plt.show()



print('Hey Betanir,\v what\'s up ?')

x = [2,4,2,32,34,32,432,4,324,324,32,4,3,4,2,23,4,4,3,4,2,5,62,62,6,3,6]
set(x)

for i in range(1,6,2):
    print(i)
help(math.factorial)
math.factorial(0)

x = 0
for i in range(-4,4):
    if i:
        x+=i
        print(x)
