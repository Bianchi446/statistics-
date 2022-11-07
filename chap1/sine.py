import math
import mistat
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt

# Create a list of 50 values representing the sine curve

x = [math.sin(x * 2 * math.pi / 50) for x in range(1, 51)]

# Add a random normal with mean 0 and standard deviation 0.05

x = [xi + norm.rvs(loc=0, scale=0.05) for xi in x]
ax = pd.Series(x).plot(style='', color='black')
ax.set_ylabel('Values')
ax.axhline(y=0, linestyle='--', color='darkgrey')
plt.show()
