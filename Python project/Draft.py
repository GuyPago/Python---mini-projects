import matplotlib.pyplot as plt
import numpy as np
import math

x = np.arange(-math.pi/2, 11*math.pi + math.pi/2, 0.001)
y = np.sin(x)
z = x + y

plt.plot(x, y)
plt.show()

ages = [25,32,16,56]
type(ages)

ages[-1]
newAges = ages + [12,42,11]
newAges
ages.append(120)
ages


def say_my_name():
    print("My name is Guy")
