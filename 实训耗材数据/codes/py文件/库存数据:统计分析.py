import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import  font_manager
fig, ax = plt.subplots()
my_font =font_manager.FontProperties(fname="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc")
import  numpy as np
import  seaborn as sns
#t1:库存信息exel表格
All=pd.read_excel("/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/库存信息_20191224202755.xls")




#
# #=======================================按照物品类别分类的条形图============================================================
# # # item_kind=['教学使用类','办公用品类','工具类','其他类','劳保类','低值仪器仪表','材料类耗材']
item_kind=All['物品类别'].unique()#不重复物品种类名称
b=np.zeros(len(item_kind))#创建0数组,b存放不同种类物品的种数
#
for i in range(len(item_kind)):
    b[i]=(All[All["物品类别"] == item_kind[i]]).shape[0]#统计不同物品的种类


#====================================画图=================================================================================
plt.style.use('seaborn')#高级绘图工具
plt.bar(item_kind, b)
print(item_kind,b)
#item_kind=['教学使用类' '办公用品类' '其它类' '工具类' '低值仪器仪表' '劳保类' '材料类耗材']
# b=[941.  76. 61. 285. 654, 41.  32.   1.]
plt.xticks(range(len(item_kind)), item_kind, FontProperties=my_font, rotation=45)#画图
plt.xlabel('不同种类',FontProperties=my_font)
plt.ylabel('种类数量',FontProperties=my_font)
plt.title('不同种类数量统计图', FontProperties=my_font)
plt.style.use('seaborn')
fig.subplots_adjust(bottom=0.2)#调整子图距离底部的位置，显现子图底部

plt.savefig('../图片/不同类别包含物品总类数量/不同类别包含物品总类数量.png')
plt.show()
plt.close()





#
# #====================================按照不同类别分类================================================================================
#
#
#
ALL_groupdy=All['物品名称'].groupby(by=[All['物品类别'],All['仓库']]).count()
#定义7个数组存放7个不同种类的物品
for kind in item_kind:
    store_kind=ALL_groupdy[kind].index#存放不同类中放到哪个仓库的名字
    store_kind_data=np.zeros(len(ALL_groupdy[kind]))#该类别放在仓库的数量
    j=0;
    for i in ALL_groupdy[kind]:
        store_kind_data[j]=i;
        j=j+1;
#==============================画图=============================================================================================
    plt.style.use('seaborn')
    plt.bar(store_kind, store_kind_data)
    plt.xticks(range(len(store_kind)), store_kind, FontProperties=my_font, rotation=-90)#画图
    plt.title(kind, FontProperties=my_font)
    plt.xlabel('仓库名称',FontProperties=my_font)
    plt.ylabel('种类（种）',FontProperties=my_font)
    fig.subplots_adjust(bottom=0.4)  # 调整子图距离底部的位置，显现子图底部
    plt.savefig('../图片/同一类别存放不同仓库的物品种类数量'+kind+'存放在不同仓库的物品种类数量.png')
    plt.show()
    plt.close()






#===============================================仓库容纳量=========================================================
plt.style.use('seaborn')
pie_store_kind_data=np.zeros(len(All.groupby('仓库').count()['物品类别']))
store_sum_name=All.groupby('仓库').count().index
pie_store_kind_name=All.groupby('仓库').count().index
k=0;
for pie_data in All.groupby('仓库').count()['物品类别']:
    pie_store_kind_data[k]=pie_data
    k=k+1;

plt.rcParams['font.family'] = ['AR PL UKai CN']

plt.pie(x=(pie_store_kind_data/All.groupby('仓库').count()['物品类别'].sum()),labels=pie_store_kind_name,autopct='%.1f%%')
plt.title('仓库存货量饼状图')
plt.savefig('../图片/不同仓库存放物品总类饼状图/不同仓库存放物品总类饼状图.png')
plt.show()
plt.close()












#==========================================相同类别相同名称库存数量统计=======================================================================

store_number_sum=All[['库存数量']].groupby(by=[All['物品类别'],All['物品名称']]).sum()#统计相同类别相同名称的库存数量



for item_kind_name in item_kind:#array(['教学使用类', '办公用品类', '其它类', '工具类', '其他类', '低值仪器仪表', '劳保类', '材料类耗材'],
    store_number_one=store_number_sum.loc[item_kind_name]
    plt.style.use('seaborn')
    plt.figure(figsize=(28, 88), dpi=200)  # 图片大小，线宽
    plt.plot(range(len(store_number_one)),store_number_one.values.reshape(len(store_number_one.values)),label=item_kind_name)#教学使用类不同物品的仓库存量总和,label='first')
    plt.title(item_kind_name+'仓库存量统计折线图',FontProperties=my_font)
    _xtick_lables = ["{}".format(i) for i in store_number_one.index]
    # 标记最大值和最小值位置
    max_index=store_number_one.values.reshape(len(store_number_one.values)).argmax()#求最大值所在的一维数组索引
    min_index = store_number_one.values.reshape(len(store_number_one.values)).argmin()
    plt.plot(max_index, store_number_one.max(), 'r-o')#画出最大值和最小值
    plt.plot(min_index, store_number_one.min(), 'r-o')
    show_max = '[' +store_number_one.index[max_index]  + ' ' + str(store_number_one.max()[0]) + ']'
    show_min='[' +store_number_one.index[min_index]  + ' ' + str(store_number_one.min()[0]) + ']'
    plt.annotate(show_max, xytext=(max_index,store_number_one.max()), xy=(max_index, store_number_one.max()),FontProperties=my_font)
    plt.annotate(show_min, xytext=(min_index,store_number_one.min()), xy=(min_index, store_number_one.min()),FontProperties=my_font)
    if(len(store_number_one)>=28):
        plt.xticks(list(range(len(store_number_one)))[::int((len(store_number_one)/28))],_xtick_lables[::int((len(store_number_one)/28))],rotation=90,FontProperties=my_font,size='6')
    else:
        plt.xticks(list(range(len(store_number_one))),_xtick_lables, rotation=90, FontProperties=my_font, size='6')
    plt.xlabel('物品种类', FontProperties=my_font)
    plt.ylabel('数量（个）', FontProperties=my_font)
    #plt.savefig('../图片/同一类别存放物品数量折线图/'+item_kind_name+'物品数量折线图.jpg')
    plt.show()







