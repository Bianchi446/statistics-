import mistat
import matplotlib.pyplot as plt

X = mistat.load_data('YARNSTRG')
ax = X.plot.box(color='red')
ax.set_ylabel('Log yarn strenght')
plt.show()
