import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import  font_manager
my_font =font_manager.FontProperties(fname="/usr/share/fonts/truetype/wqy/wqy-microhei.ttc")
All2=pd.read_excel("/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/采购入库信息_20191224202718.xls")

申请状态 = input('申请状态')
单据名称 = input('单据名称')
单据编号 = input('单据编号')
供应商 = input('供应商')
入库仓库 = input('入库仓库')
经费来源 = input('经费来源')
物品名称 =input('物品名称')
物品代码=input('物品代码')
规格型号=input('规格型号')
入库数量=input('入库数量')
进货单价=input('进货单价')
进货金额=input('进货金额')



if (申请状态 == ''):
    申请状态 = All2['申请状态'];
if (单据名称 == ''):
    单据名称 = All2['单据名称'];
if (单据编号 == ''):
    单据编号 = All2['单据编号'];
if (供应商 == ''):
    供应商 = All2['供应商'];
if (入库仓库 == ''):
    入库仓库 = All2['入库仓库'];
if (经费来源 == ''):
    经费来源 = All2['经费来源'];

if (物品名称 == ''):
    物品名称 = All2['物品名称'];
if (物品代码 == ''):
    物品代码 = All2['物品代码'];
if (规格型号 == ''):
    规格型号 = All2['规格型号'];
if (入库数量 == ''):
    入库数量 = All2['入库数量'];
if (进货单价 == ''):
    进货单价 = All2['进货单价(元)'];
if (进货金额 == ''):
    进货金额 = All2['进货金额(元)'];

data = All2[(All2['申请状态'] == 申请状态) & (All2['单据名称'] == 单据名称) & (All2['单据编号'] == 单据编号) & (All2['供应商'] == 供应商) & (
                All2['入库仓库'] == 入库仓库) & (All2['经费来源'] == 经费来源) \
                 & (All2['物品名称'] == 物品名称)\
            & (All2['物品代码'] == 物品代码) & (All2['规格型号'] == 规格型号)\
            & (All2['入库数量'] == 入库数量) & (All2['进货单价(元)'] == 进货单价)\
            & (All2['进货金额(元)'] == 进货金额)]
print(data)
data.to_html('/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材前端/采购excel表.html')
