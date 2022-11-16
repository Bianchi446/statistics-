import mistat
import pandas as pd

blemishes = mistat.load_data('BLEMISHES')

#Blemishes is a called a data frame, because its matrix-like structure 

blemishes.head(3)

print(blemishes.iloc[1,0])
print(blemishes.iloc[2,1])


