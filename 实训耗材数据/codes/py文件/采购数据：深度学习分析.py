import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from tensorflow import keras
All1=pd.read_excel('/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/库存信息_20191224202755.xls')
All2=pd.read_excel("/home/haoge/桌面/500GB/备份/文档/数据分析/实训耗材数据/数据分析excel表/采购入库信息_20191224202718.xls")
y_data=All1['物品类别'].values
name=All1['物品类别'].unique()
array=np.full(2091,np.NAN)#array存的就是标签
for i in range(len(name)):
    for j in range(len(y_data)):
        if name[i] == y_data[j]:
            array[j]=i



new_All1=All1[['物品代码','库存数量','进货单价']].values[:2000]
new_test=All1[['物品代码','库存数量','进货单价']].values[2000:]
index_All1=array[:2000]
index_test=array[2000:]











model=keras.models.Sequential()
model.add(keras.layers.Dense(input_shape=(3,),units=1))
model.add(keras.layers.Dense(300,activation='selu'))#输入

model.add(keras.layers.Dense(100,activation='selu'))#selu自带归一化功能，缓解梯度消失
# model.add(keras.layers.AlphaDropout(rate=0.5))#对上一层自动进行droupout，防止某个数据过多，均值和方差不变，归一化性质不变计算机记住样本
model.add(keras.layers.Dense(8,activation='softmax'))#输出


#===================重写callback函数=====================
dirname='./callback'
if not os.path.exists(dirname):
    os.mkdir(dirname)
output_html=os.path.join(dirname,'fashion_mnist_model.h5')




callbacks=[
    keras.callbacks.TensorBoard(dirname),
    keras.callbacks.ModelCheckpoint(output_html,save_best_only=True),]






#========================================================
model.compile(loss='sparse_categorical_crossentropy',optimizer ='adam',metrics=['accuracy'])
history=model.fit(new_All1,index_All1,epochs=100,validation_data=(new_test,index_test),callbacks=callbacks)

def plot_learning_curves(history):
    pd.DataFrame(history.history)[['accuracy','val_accuracy']].plot(figsize=(8,5))
    plt.grid()
    plt.xlabel('训练次数')
    plt.ylabel('训练准确度')
    plt.savefig('深度学习采购入库信息表.png')
    plt.show()
plot_learning_curves(history)
for i in new_test:
    a = model.predict([(tuple(i))])
    sort = np.argsort(-a)
    print('测试集的数据为：{},经分析得出该特征最可能为是{},其次是{}'.format(i, name[sort[0][0]], name[sort[0][1]]))
