#思想，由于活动随着时间的增加，进货金额在增加，所以物品的单价*进货量一定在增加，那么横坐标是单价，纵坐标是进货量的散点图一定有什么规律，试试。
import pandas as pd
import numpy as np
from matplotlib import  font_manager
from matplotlib import pyplot as plt
fig, ax = plt.subplots()
my_font =font_manager.FontProperties(fname="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc")

from sklearn.neighbors import KNeighborsClassifier#导入写好的knn的库
All=pd.read_excel('/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/采购入库信息_20191224202718.xls')
#==============================处理数据==================
All['入库仓库']=All['入库仓库'].apply(lambda a:a[:2])#仓库名称切片
All['制单时间']=All['制单时间'].apply(lambda b:b[5:10])#制单时间切片
Allname=All['单据名称'].unique()
name_ck=All['入库仓库']
time_zd=All['制单时间']
All['制单时间'] = All['制单时间'] .map(lambda y: y[:2]).astype('int') + 0.01 * All['制单时间'] .map(lambda y: y[-2:]).astype('int')  # 1.1:1月1号
make_time=All['制单时间']
into_cage=All['入库仓库']
j=0
into_cage_index=np.array(['YW', 'SX', 'HH', 'TY', 'DZ', 'JX', 'QC', 'YS', 'XX', 'JS'])
for i in into_cage.unique():
    into_cage[into_cage==i]=j
    j=j+1
#========================================预处理，把时间变数字，把仓库名称变数字
x_dataname=[]   #标签名
y_data=[]        #标签名对应数据
for i in Allname:
    if  All[All['单据名称']==i].count()[0]>10:
        Into_cage_one=All[All['单据名称']==i]['入库仓库']
        into_Time=All[All['单据名称']==i]['制单时间']
        plt.scatter(Into_cage_one,into_Time,label=i)
        #==================现在要把标签和数据存下来
        for j in range(len(Into_cage_one)):
            x_dataname.append(i)
            y_data.append(All[All['单据名称']==i][['入库仓库','制单时间']].iloc[j].values)

plt.rcParams['font.family'] = ['AR PL UKai CN']
plt.xlabel('warehouse')
plt.xticks(np.arange(10),into_cage_index)
plt.ylabel('time')
#========================================大量的活动重叠了=====================
into_cage_index2={'YW':0, 'SX':1, 'HH':2, 'TY':3, 'DZ':4, 'JX':5, 'QC':6, 'YS':7, 'XX':8, 'JS':9}

d=into_cage_index2[input('输入仓库名：')]
e=float(input('输入时间（1月5日输入1.5）：'))
plt.scatter(d,e,marker='*')
predict=np.array([d,e])
X_predict = predict.reshape(1, -1)
kNN_classifier = KNeighborsClassifier(n_neighbors=6)
kNN_classifier.fit(y_data,x_dataname)
plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0)
fig.subplots_adjust(right=0.8)

plt.show()
print('检测出该点应该属于'+kNN_classifier.predict(X_predict)[0])