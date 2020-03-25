import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import  font_manager
import statsmodels.api as sm
import tensorflow as tf
my_font =font_manager.FontProperties(fname="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc")
All1=pd.read_excel('/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/库存信息_20191224202755.xls')
All2=pd.read_excel("/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/采购入库信息_20191224202718.xls")

#=================================================不同活动耗费金额数量==========================================================

# money_amount=All2[['进货金额(元)']].groupby(All2['单据名称']).sum()[All2[['进货金额(元)']].groupby(All2['单据名称']).sum()['进货金额(元)']>=10000   ]#由于数据过多不好在窗口显示，剔除其中意义不明显的数据，只收集金额大于10000的活动
# plt.style.use('seaborn')
# #图像绘制
# fig,ax=plt.subplots()
# b=ax.barh(range(len(money_amount.index)), money_amount.values.astype('int').reshape(len(money_amount)),color='#6699CC')
# #添加数据标签
# for rect in b:
#     w=rect.get_width()
#     ax.text(w,rect.get_y()+rect.get_height()/2,'%d'%int(w),ha='left',va='center')
# fig.subplots_adjust(left=0.3)#调整子图距离底部的位置，显现子图底部
# #设置Y轴刻度线标签6699CC
# ax.set_yticks(range(len(money_amount.index)))
# ax.set_yticklabels(money_amount.index,FontProperties=my_font,size=8,color='black')
# plt.savefig('../../../图片/采购入库信息分析图片/不同活动耗费金额数量条形图.png')
# plt.show()
# plt.close('all')


#==========================================活动需要进哪些物品=需要进货的物品-库存已经存在的物品==============================
# for n in money_amount.index:
#     goods_have=All1[['物品名称','库存数量']].groupby('物品名称').sum()
#     goods_need=All2[All2['单据名称']==n][['物品名称','入库数量']].groupby('物品名称').sum()#good_need和good_have都是一维数组，表现为二维数组
#     remain_need_name=np.zeros(len(goods_need.index))#存放需要进货的货物名称
#     remain_need_number=np.zeros(len(goods_need.index))#存放剩余需要进货量
#     for i in range(len(goods_need)):
#         try:
#             if (goods_need.iloc[i][0] > (goods_have.loc[goods_need.index[i]][0])):
#                 remain_need_number[i] =(goods_need.iloc[i][0] - (goods_have.loc[goods_need.index[i]][0])) # 还需要进货的量=需要进货量-库存量
#             else:
#                 remain_need_number[i] = goods_need.iloc[i][0]
#         except KeyError:
#             remain_need_number[i] = goods_need.iloc[i][0]
#     plt.figure(figsize=(288, 88), dpi=200)
#     plt.style.use('seaborn')
#     plt.bar(goods_need.index,remain_need_number,width=0.2)
#     plt.xticks(range(len(goods_need.index)),goods_need.index,FontProperties=my_font,rotation=90,size=5)#(barh就用yticks轴，bar就用xticks轴)
#     plt.title(n+'还需购买量',FontProperties=my_font)
#     #plt.savefig('../../../图片/采购入库信息分析图片/还需要采购量统计图/'+n+'还需购买量.png')
#     #plt.show()
#     plt.close('all')



#===========================================按照制表时间统计不同活动的进货金额，预测明年的进货金额============================================
plt.rcParams['font.family'] = ['AR PL UKai CN']
for i in range(len(All2)):
    All2['制单时间'][i]=All2['制单时间'][i][5:7]



x=(np.array(All2.groupby('制单时间')['进货金额(元)'].sum().index))
y=(np.array(All2.groupby('制单时间')['进货金额(元)'].sum()))
plt.scatter(x.astype('int'),y)
plt.xticks(x.astype('int'),['{}月'.format(i) for i in x.astype('int')])
#
#
# dataframe={
#     '月份':x,
#     '总金额':y
# }
# #==============函数拟合线===============
# ok=pd.DataFrame(data=dataframe,columns=['月份','总金额'])
# fit=sm.formula.ols('总金额~月份',data=ok).fit()
#
#
#
#
#
# #=============================最小二乘法求拟合线==========================
# ok2=pd.DataFrame(data=dataframe,columns=['月份','总金额'])
# x=np.array(ok2['月份']).astype('int')
# x_mean=x.mean()
# y=np.array(ok2['总金额']).astype('int')
# y_mean=y.mean()
# x_y=np.multiply(np.array(ok2['月份'].astype('int')),np.array(ok2['总金额']).astype('float'))#x乘Y
# x_sum=x.sum()
# y_sum=y.sum()
# x_x =np.multiply(np.array(ok2['月份']).astype('int'),np.array(ok2['月份']).astype('int'))
# P1=x_y.sum()
# P2=x_sum*y_sum/len(ok2)
# P3=x_x.sum()
# P4=(x_sum*x_sum/len(ok2))
# b=(P1-P2)/(P3-P4)
# a=y_mean-b*x_mean
#
#
# x2=[0,12]
# y2=[a,a+b*12]
# plt.rcParams['font.family'] = ['AR PL UKai CN']
# plt.plot(x2,y2,'--',label='最小二乘法')#1-2的线
#
#
#
# #y=fp[0]+fp[1]*x
#
#
# print('该函数方程为y={}*x+{}'.format(b,a))
# print('*'*100)
# #====================机器学习法求拟合线============================
# x_data=np.array([1,2,3,4,5,6,7,9,10,11,12])
# model=tf.keras.Sequential()#定义一个模型
# model.add(tf.keras.layers.Dense(input_dim=1, units=1))#给模型添加一层，是y=ax+b，y是输出只有一个，所以定义为1，元祖
# model.compile(loss='mse', optimizer='sgd')#内置优化方法，计算梯度,loss是损失值，用均方差表示
# history=model.fit(x_data,y,epochs=5000)#对x和y训练5000次，求最小的误差值
# print(model.predict(x_data))
# plt.plot(x,model.predict(x_data),'*',color='r',label='机器学习法',)
# plt.legend()
# #plt.savefig('/home/haoge/桌面/500GB/备份/文档/数据分析/图片/采购入库信息分析图片/预测曲线.png')
# plt.show()
# def plot_learning_curves(history):
#     pd.DataFrame(history.history).plot(figsize=(8,5))
#     plt.grid()
#
plt.show()
# plot_learning_curves(history)
# plt.close()








#===================================knn算法=========================================================
#思想，由于活动随着时间的增加，进货金额在增加，所以物品的单价*进货量一定在增加，那么横坐标是单价，纵坐标是进货量的散点图一定有什么规律，试试。
# All3=pd.read_excel('/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/codes/py文件/线性回归方程信息图.xls')
# All_data=All3[['单据名称','入库数量','进货单价(元)']]
# All_data2=All3[['入库数量','进货单价(元)']]
# All_data_name=All_data['单据名称'].unique()
# #筛选属性：
# plt.rcParams['font.family'] = ['AR PL UKai CN']
#
# y_data_name=[]
# x_data_name=[]
# for one_data_name in All_data_name:
#     one_data=All_data[All_data['单据名称']==one_data_name]
#     if one_data['单据名称'].count()>100:#当数据超过100才比较具备特征
#         for i in range(one_data['单据名称'].count()):
#             x_data_name.append(one_data_name)#数据对应的标签
# #=========================标签搞定====================================
#             one_data_2=one_data[['入库数量','进货单价(元)']].iloc[i].values
#             y_data_name.append(one_data_2)
#
#
#         x_plt=one_data['入库数量']
#         y_plt=one_data['进货单价(元)']
#         plt.scatter(x_plt,y_plt,label=one_data_name)
# x_data_name=np.array(x_data_name)
# y_data_name=np.array(y_data_name)
# d=int(input('输入预测点的横坐标（入库数量）：'))
# e=int(input('输入预测点的纵坐标（进货单价）：'))
# print('入库数量：{},进货单价：{}'.format(d,e))
# plt.scatter(d,e,label='测试点',s=100,marker='*',c='black')
# predict=np.array([d,e])
# X_predict = predict.reshape(1, -1)
# kNN_classifier = KNeighborsClassifier(n_neighbors=6)
# kNN_classifier.fit(y_data_name,x_data_name)
# print('检测出该点应该属于'+kNN_classifier.predict(X_predict)[0])
# plt.legend()
# plt.show()
#===================================================================================
















