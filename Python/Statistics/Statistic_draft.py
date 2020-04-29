import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 89, 6
s = np.random.normal(mu, sigma,size=10000)

# Create the bins and histogram
count, bins, ignored = plt.hist(s,100, stacked=True, range=(70,100), cumulative=True)

# Plot the distribution curve
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    np.exp( - (bins - mu)**2 / (2 * sigma**2) ),       linewidth=3, color='y')
plt.show()
