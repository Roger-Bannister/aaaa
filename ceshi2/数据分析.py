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
filepath = './lianjia.csv'
rawdata = pd.read_csv(filepath, header=0)

# 查看数据
rawdata.head()
rawdata.info()

check_dup = rawdata.loc[rawdata.duplicated() == True, :]
check_dup.head()

if (rawdata.duplicated().any()):
    print("存在重复行")
df1 = rawdata.drop_duplicates(subset=None, keep='last')
print("去除重复行前，数据集维度：{}".format(rawdata.shape))
print("去除重复行后，数据集维度：{}".format(df1.shape))

df1['Elevator'].isnull().sum()
df = df1.copy()
df.loc[(df['Elevator'].isnull()) & (df['Floor'] > 6), 'Elevator'] = '有电梯'
df.loc[(df['Elevator'].isnull()) & (df['Floor'] <= 6), 'Elevator'] = '无电梯'

df.groupby('Elevator')['Elevator'].count()

del_row = df[(df['Elevator'] == '毛坯') | (df['Elevator'] == '简装') | (df['Elevator'] == '精装')].index.tolist()
len(del_row)
df = df.drop(del_row).reset_index(drop=True)
df.info()

df.describe()

#查看区域面积分布
f, ax1=plt.subplots(1,figsize=(15,10))
sns.boxplot(x="Region",y="Size",data=df,ax=ax1)
ax1.set_title("北京各大区二手房面积分布")
ax1.set_xlabel('区域')
ax1.set_ylabel('二手房面积')
plt.xticks(fontsize=9)
plt.show()



#户型面积分布
f, ax1=plt.subplots(1,figsize=(10,10))
sns.boxplot(y="Layout",x="Size",data=df,ax=ax1)
ax1.set_title("北京二手房户型面积分布")
ax1.set_xlabel('户型')
ax1.set_ylabel('二手房面积')
plt.xticks(fontsize=9)
plt.show()


#找到需要删除的行
del_list=df.loc[(df['Layout']=='5房间0卫')|(df['Layout']=='3房间0卫')|(df['Layout']=='2房间0卫')|(df['Layout']=='1房间0卫')].index.tolist()
del_list
df=df.drop(del_list) #删除x房间0卫

#选取子集
df=df.drop(['Id'],axis=1).reset_index(drop=True)
# 添加新特征房屋均价
df['PerPrice'] =df['Price']/df['Size']
# 重新摆放列位置
columns = ['Region', 'District', 'Garden', 'Layout', 'Floor', 'Year', 'Size', 'Elevator', 'Direction', 'Renovation', 'PerPrice', 'Price']
df = pd.DataFrame(df, columns = columns)
df.head()

df.describe()


# 对二手房区域分组对比二手房数量
df_house_count = df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()

#正确显示中文以及负号
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
sns.set_style({'font.sans-serif':['SimHei','Arial']})

f,ax=plt.subplots(1,1,figsize=(20,10))
sns.barplot(x='Region', y='Price',palette="Greens_d", data=df_house_count)
ax.set_title('北京各大区二手房数量对比')
ax.set_xlabel('区域')
ax.set_ylabel('数量')
plt.xticks(fontsize=9)#减小字体以免变成方框
plt.show()




#各城区房平均总价分布
df_price_mean=df.groupby("Region")["Price"].mean().sort_values(ascending=False).to_frame().reset_index()
f,[ax1,ax2]=plt.subplots(2,1,figsize=(20,15))
sns.barplot(x="Region",y="Price",palette="Blues_d",data=df_price_mean,ax=ax1)
ax1.set_title("北京各大区二手房总价对比")
ax1.set_xlabel('区域')
ax1.set_ylabel('总价（区域均值）')

sns.boxplot(x="Region",y="Price",data=df,ax=ax2)
ax2.set_title("北京各大区二手房总价分布")
ax2.set_xlabel('区域')
ax2.set_ylabel('总价')
plt.xticks(fontsize=9)
plt.show()



#各城区房每平米单价分布
df_perprice_mean=df.groupby("Region")["PerPrice"].mean().sort_values(ascending=False).to_frame().reset_index()
f,[ax1,ax2]=plt.subplots(2,1,figsize=(20,15))
sns.barplot(x="Region",y="PerPrice",palette="Blues_d",data=df_perprice_mean,ax=ax1)
ax1.set_title("北京各大区二手房每平米单价对比")
ax1.set_xlabel('区域')
ax1.set_ylabel('每平米单价')

sns.boxplot(x="Region",y="PerPrice",palette="Blues_d",data=df,ax=ax2)
ax2.set_title("北京各大区二手房每平米单价分布")
ax2.set_xlabel('区域')
ax2.set_ylabel('每平米单价')
plt.xticks(fontsize=9)
plt.show()

df.loc[(df['Size']>=0)&(df['Size']<50),'Size_level']="Mini Small"
df.loc[(df['Size']>=50)&(df['Size']<100),'Size_level']="Small"
df.loc[(df['Size']>=100)&(df['Size']<150),'Size_level']="Mediumn"
df.loc[(df['Size']>=150)&(df['Size']<200),'Size_level']="Big"
df.loc[(df['Size']>=200),'Size_level']="Huge"
df_sizelevel_count=df.groupby('Size_level')['Price'].count().sort_values(ascending=False).to_frame().reset_index()

# 对二手房面积分类后对比二手房数量，总价和每平米房价
df_house_count1 = df.groupby('Size_level')['Price'].count().sort_values(ascending=False).to_frame().reset_index()
df_house_mean1 = df.groupby('Size_level')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

f, [ax1,ax2,ax3] = plt.subplots(1,3,figsize=(15,5))

sns.barplot(x='Size_level', y='Price', palette="Greens_d", data=df_house_count1, ax=ax1)
ax1.set_title('北京各类别二手房数量对比')
ax1.set_xlabel('类别')
ax1.set_ylabel('数量')
sns.boxplot(x='Size_level', y='Price', data=df, ax=ax2)
ax2.set_title('北京类别二手房房屋总价')
ax2.set_xlabel('类别')
ax2.set_ylabel('房屋总价')
sns.barplot(x='Size_level', y='PerPrice', palette="Blues_d", data=df_house_mean1, ax=ax3)
ax3.set_title('北京各类别二手房每平米单价对比')
ax3.set_xlabel('类别')
ax3.set_ylabel('每平米单价')
plt.show()


#房每平米均价/数量和户型
df_layout_count1=df.groupby('Layout')['PerPrice'].count().sort_values(ascending=False).to_frame().reset_index().head(26)
sel_layout=df_layout_count1['Layout'].tolist()
df2=df.loc[df['Layout'].isin(sel_layout)]
df_layout_perprice1=df2.groupby('Layout')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index().head(26)
plt.figure(figsize=(15,5))
x=np.arange(df_layout_perprice1.shape[0])
plt.bar(x*3+1, df_layout_perprice1['PerPrice'])
plt.title('房屋户型均价')
plt.xticks(x*3+1.5,df_layout_perprice1['Layout'],fontsize=8)
plt.xlabel('房屋户型')
plt.ylabel('均价')
plt.show()


#房均价/数量和朝向
sel_direct=df['Direction'].value_counts().to_frame()
sel_direct_list=sel_direct.loc[sel_direct['Direction']>100].index.tolist()
df_direct=df.loc[df['Direction'].isin(sel_direct_list)]
df_direct['Direction'].value_counts()

# 对二手房朝向
df_house_count2 = df_direct.groupby('Direction')['Price'].count().sort_values(ascending=False).to_frame().reset_index()
df_house_mean2 = df_direct.groupby('Direction')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

f, [ax1,ax2,ax3] = plt.subplots(3,1,figsize=(10,15))

sns.barplot(x='Direction', y='Price', palette="Greens_d", data=df_house_count2, ax=ax1)
ax1.set_title('北京各朝向二手房数量对比')
ax1.set_xlabel('朝向')
ax1.set_ylabel('数量')
sns.boxplot(x='Direction', y='Price', data=df_direct, ax=ax2)
ax2.set_title('北京各朝向二手房房屋总价')
ax2.set_xlabel('朝向')
ax2.set_ylabel('房屋总价')
sns.barplot(x='Direction', y='PerPrice', palette="Blues_d", data=df_house_mean2, ax=ax3)
ax3.set_title('北京各朝向二手房每平米单价对比')
ax3.set_xlabel('朝向')
ax3.set_ylabel('每平米单价')
plt.show()


#房均价/数量和装修
df['Renovation'].value_counts()
# 画幅设置
f, [ax1,ax2,ax3] = plt.subplots(1, 3, figsize=(15, 5))
sns.countplot(df['Renovation'], ax=ax1)
sns.barplot(x='Renovation', y='Price', data=df, ax=ax2)
sns.boxplot(x='Renovation', y='Price', data=df, ax=ax3)
plt.show()


#房均价/数量和楼层
df['Floor'].value_counts()

f, [ax1,ax2,ax3] = plt.subplots(3, 1, figsize=(20, 10))
sns.countplot(df['Floor'], ax=ax1)
sns.barplot(x='Floor', y='PerPrice', data=df, ax=ax2)
sns.boxplot(x='Floor', y='Price', data=df, ax=ax3)
plt.show()

#房均价/数量和有无电梯
f, [ax1,ax2] = plt.subplots(1, 2, figsize=(20, 10))
sns.countplot(df['Elevator'], ax=ax1)
ax1.set_title('有无电梯数量对比',fontsize=15)
ax1.set_xlabel('是否有电梯')
ax1.set_ylabel('数量')
sns.barplot(x='Elevator', y='Price', data=df, ax=ax2)
ax2.set_title('有无电梯房价对比',fontsize=15)
ax2.set_xlabel('是否有电梯')
ax2.set_ylabel('总价')
plt.show()


y1=df.groupby('Year').Price.mean().reset_index()
y2=df.groupby('Year').PerPrice.count().reset_index()
x=y1.Year
plt.plot(x,y1.Price,label='Total Price')
plt.plot(x,y2.PerPrice,'r--',label='Total Number')
plt.legend(loc='best')
plt.show()

plt.figure(figsize=(15,5))
df.groupby('Year').PerPrice.mean().plot()
plt.title('建筑时间-每平米单价')


#不同城区的建筑情况
plt.figure(figsize=(15,10))
sns.swarmplot(x="Year",y="Region",data=df)
plt.title('建筑时间-数量')
plt.show()



sns.set_style({'font.sans-serif':['simhei','Arial']})
f, [ax1,ax2,ax3] = plt.subplots(3,1, figsize=(15, 5))
sns.distplot(df['Size'], bins=30, ax=ax1, color='r')
sns.kdeplot(df['Size'], shade=True, ax=ax1)
sns.distplot(df['Price'], bins=30, ax=ax2, color='r')
sns.kdeplot(df['Price'], shade=True, ax=ax2)
sns.distplot(df['PerPrice'], bins=30, ax=ax3, color='r')
sns.kdeplot(df['PerPrice'], shade=True, ax=ax3)
plt.show()
