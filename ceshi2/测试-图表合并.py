# 导入常用包


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from jedi.api.refactoring import inline
from snownlp.seg import train

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



#出现频率图
sns.set_style({'font.sans-serif':['simhei','Arial']})
f, [ax1,ax2,ax3,ax4,ax5,ax6] = plt.subplots(6,1, figsize=(15, 15))
sns.distplot(df['1990-1995年住宅面积分布'], bins=50, ax=ax1, color='r')
sns.kdeplot(df['1990-1995年住宅面积分布'], shade=True, ax=ax1)
ax1.set_xlim(1,31)
ax1.set_xticks(range(0,202,10))

sns.distplot(df['1996-2000年住宅面积分布'], bins=100, ax=ax2, color='r')
sns.kdeplot(df['1996-2000年住宅面积分布'], shade=True, ax=ax2)
ax2.set_xlim(1,31)
ax2.set_xticks(range(0,202,10))

sns.distplot(df['2001-2005年住宅面积分布'], bins=150, ax=ax3, color='r')
sns.kdeplot(df['2001-2005年住宅面积分布'], shade=True, ax=ax3)
ax3.set_xlim(1,31)
ax3.set_xticks(range(0,202,10))
plt.show()

sns.distplot(df['2006-2010年住宅面积分布'], bins=50, ax=ax4, color='r')
sns.kdeplot(df['2006-2010年住宅面积分布'], shade=True, ax=ax4)
ax4.set_xlim(1,31)
ax4.set_xticks(range(0,202,10))
plt.show()



sns.distplot(df['2011-2015年住宅面积分布'], bins=50, ax=ax5, color='r')
sns.kdeplot(df['2011-2015年住宅面积分布'], shade=True, ax=ax5)
ax5.set_xlim(1,31)
ax5.set_xticks(range(0,202,10))
plt.show()

sns.distplot(df['2016-2020年住宅面积分布'], bins=50, ax=ax6, color='r')
sns.kdeplot(df['2016-2020年住宅面积分布'], shade=True, ax=ax6)
ax6.set_xlim(1,31)
ax6.set_xticks(range(0,202,10))
plt.show()