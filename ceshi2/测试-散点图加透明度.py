# 导入常用包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
from jedi.api.refactoring import inline
from matplotlib.pyplot import savefig




plt.rcParams['font.sans-serif']=['SimHei'] #显示中文标签
plt.rcParams['axes.unicode_minus']=False   #这两行需要手动设置

# 导入数据
filepath = './房型数据最终-完整版.csv'
rawdata = pd.read_csv(filepath, header=0)


# 查看数据

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



#df0 = df[df['建筑面积']<400]

elements = ['建筑面积',	'有无电梯',	'户型建筑总开间',	'户型建筑总进深',	'总价',	'建筑总楼',	'梯户比例',	'建设年代',	'所在区域',	'入户大门朝向',	'客厅面积',	'客厅朝向',	'客厅开间',	'客厅进深',	'客餐厅建筑面积',	'客餐厅面宽',	'客餐厅进深',	'客餐厅窗户朝向',	'客餐厅有无走廊',	'客餐厅走廊面积（无走廊则填0）','客餐厅是否外出阳台',	'客厅阳台面积',	'卧室A建筑面积',	'卧室A面宽',	'卧室A进深',	'卧室A窗户朝向',	'卧室A窗户数量',	'卧室A有无走廊',	'卧室A走廊面积',	'卧室A是否外出阳台',	'卧室B建筑面积',	'卧室B面宽',	'卧室B进深',	'卧室B窗户朝向',	'卧室C建筑面积',	'卧室C面宽',	'卧室C进深',	'卧室C窗户朝向',	'卫生间窗户朝向',	'卫生间建筑面积',	'卫生间面宽',	'卫生间進深',	'卫生间开门对应位置',	'卫生间有无走廊',		'是否有次卫生间',		'厨房建筑面积',			'厨房窗户朝向',	'厨房有无走廊',	'厨房走廊面积',
            '阳台一建筑面积',	'阳台一面宽',	'阳台一进深','阳台一朝向',	'阳台二建筑面积',	'阳台二面宽',	'阳台二进深',	'阳台二朝向',	'餐厅建筑面积',	'餐厅面宽',	'餐厅进深',	'餐厅窗户朝向',	'是否有卧室套内卫生间',	'卧室套内卫生间建筑面积',	'卧室套内卫生间面宽',	'卧室套内卫生间进深',	'卧室套内卫生间窗户朝向',	'单位面积价格']

for element in elements:

    plt.figure(figsize=(15,10))

    sns.regplot(data = df, x = '建设年代', y = element, fit_reg = False,
           x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 1/3})
    plt.title('建设年代-'+element)
    plt.show()





'''
df1 = df[df['建筑面积']<400]
plt.figure(figsize=(15,10))
sns.regplot(data = df1, x = '建设年代', y = '建筑面积', fit_reg = False,
           x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 1/3})
plt.title('建设年代-建筑面积')
plt.show()


df1 = df[df['有无电梯']<400]
plt.figure(figsize=(15,10))
sns.regplot(data = df1, x = '建设年代', y = '有无电梯', fit_reg = False,
           x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 1/3})
plt.title('建设年代-有无电梯')
plt.show()

savefig("F:/anaconda/a.jpg")


df1 = df[df['有无电梯']<400]
plt.figure(figsize=(15,10))
sns.regplot(data = df1, x = '建设年代', y = '有无电梯', fit_reg = False,
           x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 1/3})
plt.title('建设年代-有无电梯')
plt.show()
'''





