import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = './年代面积2.csv'

rawdata = pd.read_csv(filepath, header=0)

rows=rawdata.iloc[3:50]

df0 = rows['建设年代']
df = rows
print(df0)




sns.set_style({'font.sans-serif':['simhei','Arial']})
f, ax1 = plt.subplots(figsize=(15, 15))
sns.distplot(rows['建设年代'], bins=50, ax=ax1, color='r')
sns.kdeplot(rows['建设年代'], shade=True, ax=ax1)
ax1.set_xlim(1,31)
ax1.set_xticks(range(0,202,10))