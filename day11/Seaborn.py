import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
sns.set_style(style='darkgrid')
# sns.set_palette('colorblind')
# sns.set_palette(sns.color_palette('deep'))
# datas=pd.read_csv(r'D:\workplace\人工智能\day11\data\adult.txt')
datas= pd.read_csv(r'D:\workplace\人工智能\day4\dating.txt',sep='\t',names=['salary','taobao','tv','result'])
datas=MinMaxScaler().fit_transform(X=datas)
datas=pd.DataFrame(datas,columns=['salary','taobao','tv','result'])
# datas = pd.DataFrame([{'姓名':'马洪顺','年龄':37},{'姓名':'宋琦','年龄':58}])
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# datas = pd.DataFrame([{'姓名':'1','年龄':37},{'姓名':'2','年龄':58},{'姓名':'3','年龄':45}])
# sns.violinplot(x='result', y='salary', data=datas) #小提琴图
# sns.barplot(x='result', y='salary', data=datas)#柱形图
# sns.pointplot(x='姓名',y='年龄',data=datas)#折线图
# sns.pointplot(x='result', y='salary', data=datas)
# sns.stripplot(x='result',y='salary',data=datas) #树状图 不展开 （如果存在相同数据，自动重合）
sns.swarmplot(x='result',y='salary',data=datas)#树状图 展开
# sns.boxplot(x='result',y='salary',data=datas) #箱线图
# sns.scatterplot(x='tv',y='salary',data=datas) #散点图
# sns.kdeplot(data=datas,data2=datas1) 等高线图
# sns.distplot(datas)#可以自动拟合一条曲线，并且展示数据可能在的范围
# sns.countplot(x='result',data=datas) #数量统计图
# sns.heatmap(data=datas) #可以直接看出数据的分布和断档情况
# sns.pairplot(datas) #两两特征对比图
plt.show()