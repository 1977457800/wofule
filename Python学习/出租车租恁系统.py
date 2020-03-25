
import time

if __name__=='__main__':
    p = True
    a = b = c = d = e = f =g=h=i= 0
    while (p):
        choice=input('租借系统：租借轿车按：1\n,租借客车按：2\n,租借货车按：3\n,结算按：4\n')
        if  choice=='1':
            a,b,c,d=map(int,input('输入4个数字，用空格隔开，分别输入租借别克商务舱GL8的数量,宝马550i的数量,别克林荫大道的数量,租借多少日：').split())
        if  choice=='2':
            e,f,g=map(int,input('输3个数字，用空格隔开，分别输入租借金杯的数量,金龙的数量,租借多少日：').split())
        if   choice=='3':
            h,i=map(int,input('输2个数字，用空格隔开，分别输入租借货车的吨位，租借多少日,：').split())
        if  choice=='4':
            money=(a*600+b*500+c*300)*d+(e*800+f*1500)*g+50*h*i
            day=d+g+i
            f=open('租恁系统图.txt','a')
            f.writelines(time.asctime( time.localtime(time.time()))+\
                  '租借别克商务舱GL8:{}辆,宝马550i:{}辆,别克林荫大道：{}辆,金杯：{}辆,金龙：{}辆,货车：{}吨,共租借{}天,租金为{}元\n'.format(
                a,b,c,e,f,h,day,money))
            f.close()
            p=False




