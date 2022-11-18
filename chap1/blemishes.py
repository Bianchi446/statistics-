import mistat
import pandas as pd
import matplotlib.pyplot as plt

blemishes = mistat.load_data('BLEMISHES')

#Blemishes is a called a data frame, because its matrix-like structure 

blemishes.tail(3)

print(blemishes.iloc[1,0])
print(blemishes.iloc[2,1])


# Use value counts with normalize to get relative frequencies 
X = pd.DataFrame(blemishes['count'].value_counts(normalize = True))
X.loc[4, 'count'] = 0
X = X.sort_index()   # Sort by number of blemishes 

ax = X['count'].plot.bar(color='grey', legend = False)
ax.set_xlabel('number of blemishes')
ax.set_ylabel('proportional frequency')
plt.show()


X['Number'] = X.index
X['cumulative frequency'] = X['count'].cumsum()
