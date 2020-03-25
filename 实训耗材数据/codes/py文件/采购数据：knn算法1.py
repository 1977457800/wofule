#思想，由于活动随着时间的增加，进货金额在增加，所以物品的单价*进货量一定在增加，那么横坐标是单价，纵坐标是进货量的散点图一定有什么规律，试试。
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


from sklearn.neighbors import KNeighborsClassifier#导入写好的knn的库
All3=pd.read_excel('/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/采购入库信息_20191224202718.xls')
All_data=All3[['单据名称','入库数量','进货单价(元)']]
All_data2=All3[['入库数量','进货单价(元)']]
All_data_name=All_data['单据名称'].unique()
#筛选属性：
plt.rcParams['font.family'] = ['AR PL UKai CN']

y_data_name=[]
x_data_name=[]
for one_data_name in All_data_name:
    one_data=All_data[All_data['单据名称']==one_data_name]
    if one_data['单据名称'].count()>100:#当数据超过100才比较具备特征
        for i in range(one_data['单据名称'].count()):
            x_data_name.append(one_data_name)#数据对应的标签
#=========================标签搞定====================================
            one_data_2=one_data[['入库数量','进货单价(元)']].iloc[i].values
            y_data_name.append(one_data_2)


        x_plt=one_data['入库数量']
        y_plt=one_data['进货单价(元)']
        plt.scatter(x_plt,y_plt,label=one_data_name)
x_data_name=np.array(x_data_name)
y_data_name=np.array(y_data_name)
d=int(input('输入预测点的横坐标（入库数量）：'))
e=int(input('输入预测点的纵坐标（进货单价）：'))
print('入库数量：{},进货单价：{}'.format(d,e))
plt.scatter(d,e,label='测试点',s=100,marker='*',c='black')
predict=np.array([d,e])
X_predict = predict.reshape(1, -1)
kNN_classifier = KNeighborsClassifier(n_neighbors=6)
kNN_classifier.fit(y_data_name,x_data_name)
print('检测出该点应该属于'+kNN_classifier.predict(X_predict)[0])
plt.legend()
plt.show()