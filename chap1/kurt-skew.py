import mistat
import pandas as pd

X = mistat.load_data('YARNSTRG')
print(f'Skewness {X.skew():.4f}')
print(f'kurtosis {X.kurtosis():.4f}')

from scipy.stats import skew, kurtosis

print(f'Skewness {skew(X):.4f}')
print(f'kurtosis {kurtosis(X):.4f}')
