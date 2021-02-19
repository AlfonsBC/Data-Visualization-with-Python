import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'./tempYearly.csv')
print(data)

#kind hex hexagons like dots
#kind reg regression line
sns.jointplot("Rainfall", "Temperature", data=data, kind="reg")
plt.show()