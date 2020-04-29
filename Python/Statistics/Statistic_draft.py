import numpy as np
import matplotlib.pyplot as plt

mean = 89; std = 6; variance = np.square(std)
x = np.arange((mean-2*std),(mean+2*std),0.1)
f = np.exp(-np.square(x-mean)/2*variance)/(np.sqrt(2*np.pi*variance))
plt.plot(x,f)
plt.ylabel('gaussian distribution')
plt.show()
