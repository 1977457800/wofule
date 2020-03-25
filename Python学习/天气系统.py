#数据类型：数字（整数，小数，复数）字符串 列表 元组 字典
#流程结构：顺序，选择，循环
#函数与oop：继承和封装
#txt的读取和操作
#对excel操作，xlrd,xlutils
#对mysql操作：pymsql


#两个小时交出代码
#txt文档，excel表格，mysql表数据，2019-12月，2020年1月，2020年2月份
import  pymysql
db=pymysql.connect('127.0.0.1','this','123456','haoge')
cursor=db.cursor()
cursor.execute("select * from hg")
# hg='''
#   CREATE TABLE `hg`(
#  `FIRST_NAME` INT(11) DEFAULT NULL,
#  `LAST_NAME` VARCHAR(10) DEFAULT NULL,
#  `AGE` INT (5),
#  `SEX` CHAR (10),
#  `INCOME` CHAR (10)
#  )ENGINE=MyISAM DEFAULT CHARSET=utf8
#  '''
#
#
# sql = "INSERT INTO `hg`(FIRST_NAME, \
#        LAST_NAME, AGE, SEX, INCOME) \
#        VALUES (%s,%s,%s,%s,%s)"
#
# var=((10,20,3,'男','安徽'),(11,60,9,'www','ppp'))
# cursor.executemany(sql,var)
#
# row_3 = cursor.fetchall()
# print(row_3[0])
import pymysql
import requests
from bs4 import BeautifulSoup


url='http://www.tianqihoubao.com/weather/top/wuhan.html'
# 获取网页信息

html = requests.get(url)
html.encoding = 'gb2312'
soup = BeautifulSoup(html.text, 'html.parser')


year = ['2017', '2018']

month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

time = [y + x for y in year for x in month]
for date in time:
    url = 'http://www.tianqihoubao.com/lishi/jinan/month/' + date + '.html'
    soup = get_html(url)
    sup = soup.find('table', attrs={'class': 'b'})
    tr = sup.find_all('tr')
    for trl in tr[1:]:
        td = trl.find_all('td')
        href = td[0].find('a')['href']  # 获取链接信息
        title = td[0].find('a')['title']  # 获取名称
        wether = td[1].get_text().replace('\r\n', '').replace(' ', '')  # 获取天气状况
        wendu = td[2].get_text().strip().replace(' ', '').replace('\r\n', '')  # 获取温度
        fengli = td[3].get_text().strip().replace(' ', '').replace('\r\n', '')  # 获取风力大小

        sql = """insert into wether_test(time_local, link, wether_type, temperature, wind_power) \
                values(%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (title, href, wether, wendu, fengli))
        db.commit()
    print("  已经爬取" + date + "数据")
db.close
print('结束')