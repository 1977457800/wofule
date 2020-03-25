dic = {'名称': [], '电话': [], '职位': [], '公司': [], '地址': []}
n=True

while n==True:
    i = True
    print('名片系统')
    print('增加名片按a,显示所有名片按b,查询名片按c,修改名片按d,删除名片按e,退出系统按f')

    income=input('请按:')
    if income == 'f':
        break

    while i==True:
        #==========================增加名片
        if  income=='a':
            name=input('名称:')
            dic['名称'].append(name)
            tel=input('电话：')
            dic['电话'].append(tel)
            post=input('职位：')
            dic['职位'].append(post)
            company=input('公司：')
            dic['公司'].append(company)
            home=input('地址:')
            dic['地址'].append(home)
            if input('继续添加按1，不添加按0:')=='0':
                i=False
        #==================查询所有名片
        if  income=='b':
            print(dic)
            i=False



        if income=='c':
            postion=int(input('查询第几条信息'))
            print(dic['名称'][postion],dic['电话'][postion],dic['职位'][postion],dic['公司'][postion],dic['地址'][postion])
            i=False
        if   income=='d':
            postion=int(input('请选择第几个位置修改信息：1，2，3，4.....：'))
            dic['名称'][postion]=input('名称：')
            dic['电话'][postion]=input('电话：')
            dic['职位'][postion]=input('职位：')
            dic['公司'][postion]=input('公司：')
            dic['地址'][postion]=input('地址：')
            i=False
        if  income=='e':
            postion = int(input('请选择第几个位置删除信息：1，2，3，4.....：'))
            dic['名称'].pop(postion)
            dic['电话'].pop(postion)
            dic['职位'].pop(postion)
            dic['公司'].pop(postion)
            dic['地址'].pop(postion)
            i = False




