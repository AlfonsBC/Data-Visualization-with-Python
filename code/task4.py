import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'./birthYearly.csv')
print(df)

#Making pivots in order to get a matrix form of data

dfP = df.pivot("month", "year", "births") 
print(dfP)

sns.heatmap(dfP, annot=True, fmt="d")
plt.show()
