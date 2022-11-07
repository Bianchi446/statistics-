from scipy.stats import binom
import numpy as np

x = binom.rvs(1, 0.5, size=60)

print(x)
