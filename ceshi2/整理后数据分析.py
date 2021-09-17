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
filepath = './房型数据整理后-完整版.csv'
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



#建设年代/建设面积  出现频率图
sns.set_style({'font.sans-serif':['simhei','Arial']})
f, [ax1,ax2] = plt.subplots(2,1, figsize=(15, 5))
sns.distplot(df['建设年代'], bins=30, ax=ax1, color='r')
sns.kdeplot(df['建设年代'], shade=True, ax=ax1)
sns.distplot(df['建筑面积'], bins=30, ax=ax2, color='r')
sns.kdeplot(df['建筑面积'], shade=True, ax=ax2)

plt.show()


#年代-电梯比例分布   矩形和针管图
df_price_mean=df.groupby("建设年代")["有无电梯"].mean().sort_values(ascending=False).to_frame().reset_index()
f,[ax1,ax2]=plt.subplots(2,1,figsize=(20,15))
sns.barplot(x="建设年代",y="有无电梯",palette="Blues_d",data=df_price_mean,ax=ax1)
ax1.set_title("电梯比例-年代变化图")
ax1.set_xlabel('年代')
ax1.set_ylabel('电梯')

sns.boxplot(x="建设年代",y="有无电梯",data=df,ax=ax2)
ax2.set_title("电梯-年代变化图")
ax2.set_xlabel('年代')
ax2.set_ylabel('电梯')
plt.xticks(fontsize=9)
plt.show()


#年代-总价分布   矩形和针管图
df_price_mean=df.groupby("建设年代")["总价"].mean().sort_values(ascending=False).to_frame().reset_index()
f,[ax1,ax2]=plt.subplots(2,1,figsize=(20,15))
sns.barplot(x="建设年代",y="总价",palette="Blues_d",data=df_price_mean,ax=ax1)
ax1.set_title("年代-总价变化图")
ax1.set_xlabel('年代')
ax1.set_ylabel('总价')

sns.boxplot(x="建设年代",y="总价",data=df,ax=ax2)
ax2.set_title("年代-总价变化图")
ax2.set_xlabel('年代')
ax2.set_ylabel('总价')
plt.xticks(fontsize=9)
plt.show()


#年代-建筑总楼分布   矩形和针管图
df_price_mean=df.groupby("建设年代")["建筑总楼"].mean().sort_values(ascending=False).to_frame().reset_index()
f,[ax1,ax2]=plt.subplots(2,1,figsize=(20,15))
sns.barplot(x="建设年代",y="建筑总楼",palette="Blues_d",data=df_price_mean,ax=ax1)
ax1.set_title("年代-建筑总楼变化图")
ax1.set_xlabel('年代')
ax1.set_ylabel('建筑总楼')

sns.boxplot(x="建设年代",y="建筑总楼",data=df,ax=ax2)
ax2.set_title("年代-建筑总楼变化图")
ax2.set_xlabel('年代')
ax2.set_ylabel('建筑总楼')
plt.xticks(fontsize=9)
plt.show()


#年代-客厅面积分布   矩形和针管图
df_price_mean=df.groupby("建设年代")["客厅面积"].mean().sort_values(ascending=False).to_frame().reset_index()
f,[ax1,ax2]=plt.subplots(2,1,figsize=(20,15))
sns.barplot(x="建设年代",y="客厅面积",palette="Blues_d",data=df_price_mean,ax=ax1)
ax1.set_title("年代-客厅面积变化图")
ax1.set_xlabel('年代')
ax1.set_ylabel('客厅面积')

sns.boxplot(x="建设年代",y="客厅面积",data=df,ax=ax2)
ax2.set_title("年代-客厅面积变化图")
ax2.set_xlabel('年代')
ax2.set_ylabel('客厅面积')
plt.xticks(fontsize=9)
plt.show()