# 导入常用包


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from jedi.api.refactoring import inline

plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置
# 导入数据
filepath = './年代面积2.csv'
rawdata = pd.read_csv(filepath, header=0)

# 查看数据
rawdata.head()
rawdata.info()

check_dup = rawdata.loc[rawdata.duplicated() == True, :]
check_dup.head()

if (rawdata.duplicated().any()):
    print("存在重复行")
df1 = rawdata
print("去除重复行前，数据集维度：{}".format(rawdata.shape))
print("去除重复行后，数据集维度：{}".format(df1.shape))

df1['建设年代'].isnull().sum()
df = df1.copy()

df.info()

df.describe()

#查看区域面积分布  针管图
f, ax1=plt.subplots(1,figsize=(15,10))
sns.boxplot(x="建设年代",y="建筑面积",data=df,ax=ax1)
ax1.set_title("1990-2020二手房面积分布")
ax1.set_xlabel('建设年代')
ax1.set_ylabel('建筑面积')
plt.xticks(fontsize=9)
plt.show()


#各城区房平均总价分布  平均后的一个值  矩形和针管图
df_price_mean=df.groupby("建设年代")["建筑面积"].mean().sort_values(ascending=False).to_frame().reset_index()
f,[ax1,ax2]=plt.subplots(2,1,figsize=(20,15))
sns.barplot(x="建设年代",y="建筑面积",palette="Blues_d",data=df_price_mean,ax=ax1)
ax1.set_title("房价-年代变化图")
ax1.set_xlabel('建设年代')
ax1.set_ylabel('建筑面积')

sns.boxplot(x="建设年代",y="建筑面积",data=df,ax=ax2)
ax2.set_title("房价-年代变化图")
ax2.set_xlabel('建设年代')
ax2.set_ylabel('建筑面积')
plt.xticks(fontsize=9)
plt.show()










#不同城区的建筑面积集中情况  点状分布图
plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="建筑面积",data=df)
sns.barplot(x="建设年代",y="建筑面积",palette="Blues_d",data=df_price_mean,ax=ax1)

plt.title('建筑时间-面积')
plt.show()




#单个数据折线图

plt.figure(figsize=(15,5))
df.groupby('建设年代').建筑面积.mean().plot()
plt.title('建设年代-建筑面积')



#出现频率图
sns.set_style({'font.sans-serif':['simhei','Arial']})
f, [ax1,ax2] = plt.subplots(2,1, figsize=(15, 5))
sns.distplot(df['建设年代'], bins=30, ax=ax1, color='r')
sns.kdeplot(df['建设年代'], shade=True, ax=ax1)
sns.distplot(df['建筑面积'], bins=30, ax=ax2, color='r')
sns.kdeplot(df['建筑面积'], shade=True, ax=ax2)

plt.show()


y1=df.groupby('建设年代').ares.mean().reset_index()

x=y1.year
plt.plot(x,y1.建设年代,label='建设年代')

plt.legend(loc='best')
plt.show()


df.groupby('建设年代').ares.mean().plot()
plt.title('建设年代-建筑面积')



