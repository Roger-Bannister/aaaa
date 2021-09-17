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
filepath = './房型数据分析p-AC.csv'
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

#不同城区的建筑面积集中情况  点状分布图
df0 = df[df['建筑面积']<400]
plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="建筑面积",data=df0)
plt.title('建设年代-建筑面积')
plt.show()

plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="有无电梯",data=df)
plt.title('建设年代-有无电梯')
plt.show()

df4 = df[df['户型建筑总开间']<60000]
plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="户型建筑总开间",data=df4)
plt.title('建设年代-户型建筑总开间')
plt.show()

df5 = df[df['户型建筑总进深']<80000]
plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="户型建筑总进深",data=df5)
plt.title('建设年代-户型建筑总进深')
plt.show()

df3 = df[df['总价']<3000]
plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="总价",data=df3)
plt.title('建设年代-总价')
plt.show()


df2 = df[df['建筑总楼']<500]
plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="建筑总楼",data=df2)
plt.title('建设年代-建筑总楼')
plt.show()

plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="所在区域",data=df)
plt.title('建设年代-所在区域')
plt.show()

plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="入户大门朝向",data=df)
plt.title('建设年代-入户大门朝向')
plt.show()

plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="客厅面积",data=df)
plt.title('建设年代-客厅面积')
plt.show()

plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="客厅朝向",data=df)
plt.title('建设年代-客厅朝向')
plt.show()

plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="客厅开间",data=df)
plt.title('建设年代-客厅开间')
plt.show()

plt.figure(figsize=(15,10))
sns.swarmplot(x="建设年代",y="客厅进深",data=df)
plt.title('建设年代-客厅进深')
plt.show()






