import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filepath = './房型数据分析p-AC.csv'

rawdata = pd.read_csv(filepath, header=0)

rows1=rawdata.iloc[2:228]
rows2=rawdata.iloc[228:629]
rows3=rawdata.iloc[629:983]


rows4=rawdata.iloc[983:1164]
rows5=rawdata.iloc[1164:1404]
rows6=rawdata.iloc[1404:1479]
elements = ["建筑面积","客厅面积"]
for element in elements:
    df1 = rows1[element]
    df2 = rows2[element]
    df3 = rows3[element]
    df4 = rows4[element]
    df5 = rows5[element]
    df6 = rows6[element]
    #dfi = rowsi[element]



    sns.set_style({'font.sans-serif': ['simhei', 'Arial']})
    plt.figure(figsize=(10, 13), dpi=80)
    plt.figure(1)
    xs = [1,2,3,4,5,6]
    ys = ['df1','df2','df3','df4','df5','df6']
    for x,y in zip(xs,ys):
        n = 'ax'+str(x)

        p = plt.subplot(661)
        sns.distplot(y, bins=50, ax=p, color='r')
        sns.kdeplot(y, shade=True, ax=p)
        p.set_xlim(1, 31)
        p.set_xticks(range(0, 202, 10))
        plt.title(element+str(x))
    plt.show()
'''
sns.set_style({'font.sans-serif':['simhei','Arial']})

plt.figure(figsize=(10,13), dpi=80)
plt.figure(1)

ax1 = plt.subplot(611)
sns.distplot(df1, bins=50, ax=ax1, color='r')
sns.kdeplot(df1, shade=True, ax=ax1)
ax1.set_xlim(1,31)
ax1.set_xticks(range(0,202,10))
plt.title('1990-1995年住宅面积变化')



ax2 = plt.subplot(612)
sns.distplot(df2, bins=50, ax=ax2, color='r')
sns.kdeplot(df2, shade=True, ax=ax2)
ax2.set_xlim(1,31)
ax2.set_xticks(range(0,202,10))
plt.title('1996-2000年住宅面积变化')



ax3 = plt.subplot(613)
sns.distplot(df3, bins=100, ax=ax3, color='r')
sns.kdeplot(df3, shade=True, ax=ax3)
ax3.set_xlim(1,31)
ax3.set_xticks(range(0,202,10))
plt.title('2001-2005年住宅面积变化')



ax4 = plt.subplot(614)
sns.distplot(df4, bins=150, ax=ax4, color='r')
sns.kdeplot(df4, shade=True, ax=ax4)
ax4.set_xlim(1,31)
ax4.set_xticks(range(0,202,10))
plt.title('2005-2010年住宅面积变化')



ax5 = plt.subplot(615)
sns.distplot(df5, bins=100, ax=ax5, color='r')
sns.kdeplot(df5, shade=True, ax=ax5)
ax5.set_xlim(1,31)
ax5.set_xticks(range(0,202,10))
plt.title('2011-2015年住宅面积变化')


ax6 = plt.subplot(616)
sns.distplot(df6, bins=50, ax=ax6, color='r')
sns.kdeplot(df6, shade=True, ax=ax6)
ax6.set_xlim(1,31)
ax6.set_xticks(range(0,202,10))
plt.title('2015-2020年住宅面积变化')
plt.show()








sns.set_style({'font.sans-serif':['simhei','Arial']})

plt.figure(figsize=(10,13), dpi=80)
plt.figure(1)

ax1 = plt.subplot(611)
sns.distplot(df12, bins=50, ax=ax1, color='r')
sns.kdeplot(df12, shade=True, ax=ax1)
ax1.set_xlim(1,31)
ax1.set_xticks(range(0,102,10))
plt.title('1990-1995年住宅面积变化')



ax2 = plt.subplot(612)
sns.distplot(df22, bins=50, ax=ax2, color='r')
sns.kdeplot(df22, shade=True, ax=ax2)
ax2.set_xlim(1,31)
ax2.set_xticks(range(0,102,10))
plt.title('1996-2000年住宅面积变化')



ax3 = plt.subplot(613)
sns.distplot(df32, bins=50, ax=ax3, color='r')
sns.kdeplot(df32, shade=True, ax=ax3)
ax3.set_xlim(1,31)
ax3.set_xticks(range(0,102,10))
plt.title('2001-2005年住宅面积变化')



ax4 = plt.subplot(614)
sns.distplot(df42, bins=50, ax=ax4, color='r')
sns.kdeplot(df42, shade=True, ax=ax4)
ax4.set_xlim(1,31)
ax4.set_xticks(range(0,102,10))
plt.title('2005-2010年住宅面积变化')



ax5 = plt.subplot(615)
sns.distplot(df52, bins=50, ax=ax5, color='r')
sns.kdeplot(df52, shade=True, ax=ax5)
ax5.set_xlim(1,31)
ax5.set_xticks(range(0,102,10))
plt.title('2011-2015年住宅面积变化')


ax6 = plt.subplot(616)
sns.distplot(df62, bins=50, ax=ax6, color='r')
sns.kdeplot(df62, shade=True, ax=ax6)
ax6.set_xlim(1,31)
ax6.set_xticks(range(0,102,10))
plt.title('2015-2020年住宅面积变化')
plt.show()
'''


