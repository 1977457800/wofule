import math#蔡勒公式：w=y+[y/4]+[c/4]-2c+[26(m+1）/10]+d-1
import numpy as np
dict = {1: '星期一', 2: '星期二', 3: '星期三', 4: '星期四', 5: '星期五', 6: '星期六', 0: '星期天'}

y=int(input('请输入年份'))
m=int(input('请输入月份'))
day=np.arange(1,32)
if m==1 :
    m=13
    y=y-1
elif m==2:
    m=14
    y=y-1
for i in day:
    allday=math.floor((y-1)+(y-1)/4-(y-1)/100+(y-1)/400+13*(m+1)/5+(m-1)*28-7+i)
    x=allday%7
    print('{}号对应的是'.format(i)+dict.get(x))

