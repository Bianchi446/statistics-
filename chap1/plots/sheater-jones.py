import mistat
import matplotlib.pyplot as plt

from KDEpy.bw_selection import improved_sheather_jones

X = mistat.load_data('YARNSTRG')

h = improved_sheather_jones(X.values.reshape(-1, 1))
ax = X.plot.density(color='grey')
X.plot.density(bw_method=h, color='black', ax=ax)
ax.set_xlabel('Log yarn stregth')
ax.set_ylabel(f'Density (h={h:.2f})')
plt.show()
