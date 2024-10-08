# Importing Libraries
import numpy as np
import pandas as pd

# data = np.array['-122.23','37.88','41.0','880.0','129.0','322.0','126.0','8.3252','452600.0','NEAR BAY']



# If all of your columns are the same type:

x = pd.read_csv('data/housing.csv', header=0).values
print(x)