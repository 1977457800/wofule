import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import  font_manager
import statsmodels.api as sm
import tensorflow as tf

from sklearn.neighbors import KNeighborsClassifier#导入写好的knn的库
my_font =font_manager.FontProperties(fname="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc")
All1=pd.read_excel('/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/库存信息_20191224202755.xls')
All2=pd.read_excel("/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/采购入库信息_20191224202718.xls")

物品类别 = input('物品类别')
物品名称 = input('物品名称')
物品代码 = input('物品代码')
规格型号 = input('规格型号')
库存数量 = input('库存数量')
进货单价 = input('进货单价')

进货金额 = input('进货金额')
仓库 = input('仓库')



if (物品类别 == ''):
    物品类别 = All1['物品类别'];
if (物品名称 == ''):
    物品名称 = All1['物品名称'];
if (物品代码 == ''):
    物品代码 = All1['物品代码'];
if (规格型号 == ''):
    规格型号 = All1['规格型号'];
if (库存数量 == ''):
    库存数量 = All1['库存数量'];
if (进货单价 == ''):
    进货单价 = All1['进货单价'];
if (进货金额 == ''):
    进货金额 = All1['进货金额'];
if (仓库 == ''):
    仓库 = All1['仓库'];

data = All1[(All1['物品类别'] == 物品类别) & (All1['物品名称'] == 物品名称) & (All1['物品代码'] == 物品代码) & (All1['规格型号'] == 规格型号) & (
                All1['库存数量'] == 库存数量) & (All1['进货单价'] == 进货单价) \
                & (All1['进货金额'] == 进货金额) & (All1['仓库'] == 仓库)]
print(data)
data.to_html('/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材前端/库存excel表.html')
