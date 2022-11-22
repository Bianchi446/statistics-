import mistat 
import matplotlib.pyplot as plt

X = mistat.load_data('YARNSTRG')
X.plot.density()

plt.show()

