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


data=pd.read_excel('房价数据整理后.xlsx')
a=data.corr()

plt.subplots(figsize=(9, 9))
sns.heatmap(a, annot=True, vmax=1, square=True, cmap="Blues")
plt.show()
