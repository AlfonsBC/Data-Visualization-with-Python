import pandas as pd
import matplotlib.pyplot as plt

#Create the dataframe using the json file...
df = pd.read_json(r'./rain.json')
print(df)

#Print som statistics
print("df statistics: ", df.describe())

df.plot(x='Month', y='Temperature')
df.plot(x='Month', y='Rainfall')
plt.show()