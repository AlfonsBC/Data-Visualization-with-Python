import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Create the dataframe using the json file...
df = pd.read_json(r'./rain.json')


#----plot temperature

#Manage to organize better the labels
plt.figure(figsize=(20,5))
plt.plot(df['Month'], df['Temperature'], label='Temperature')
#plt.show()

#----plot rainfall
plt.figure(figsize=(20,5))
plt.plot(df['Month'], df['Rainfall'], label='Rainfall')
#plt.show()

plt.plot(df['Month'],df['Rainfall'], label='Rainfall')
plt.plot(df['Month'],df['Temperature'],label='Temperature')
plt.legend()
plt.show()



