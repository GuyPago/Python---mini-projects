import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import random


font = {'family':'arial','color':'brown','weight':'normal','size':'22'}

mu = 77.02
sigma = 15.23
variance = sigma**2
x = np.linspace(mu - 3*sigma, 100, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.yticks([])
plt.title(label='Macro economics B grades',fontdict=font)
plt.xlabel('Grade', fontsize=15)

plt.show()



int(random.gauss(77.02,12.23))
