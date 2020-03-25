
import  numpy as np
import ra

class Dog:
    def __init__(self, name, healhy, honey, kind, food):
        self.name = name
        self.healthy = healhy
        self.honey = honey
        self.kind = kind
        self.food = food

    @property
    def play(self):
        self.healthy = self.healthy - 10
        self.honey = self.honey + 5
        print(self.name + '玩盘子后，健康值为：' + str(self.healthy) + '好感度为：' + str(self.honey))

    @property
    def eat(self):
        if self.kind == 1:
            self.food = self.food - 1
            self.healthy = self.healthy + 5
            self.honey = self.honey + 5
            print('喂' + self.name + '一口茶叶蛋,中国狗喜欢吃这个：健康值为' + str(self.healthy) + '好感度为' + str(self.honey))
        if  self.kind==2:
            self.food=self.food-10
            self.healthy=self.healthy+0.01
            self.honey=self.honey+0.01
            print('喂' + self.name + '一口寿司,日本狗喜欢吃这个：健康值为' + str(self.healthy) + '好感度为' + str(self.honey))


class  QQ:
    def __init__(self, name, healthy, honey, gender, food):
        self.name = name
        self.healthy = healthy
        self.honey = honey
        self.gender = gender
        self.food = food

    @property
    def play(self):
        self.healthy = self.healthy - 10
        self.honey = self.honey + 5
        print(self.name + '游泳后，健康值为：' + str(self.healthy) + '好感度为：' + str(self.honey))

    @property
    def eat(self):
        if self.gender == 1:
            self.food = self.food - 1
            self.healthy = self.healthy + 5
            self.honey = self.honey + 5
            print('喂' + self.name + '企鹅腿一个,公企鹅喜欢吃这个：健康值为' + str(self.healthy) + '好感度为' + str(self.honey))
        if self.gender == 2:
            self.food = self.food - 10
            self.healthy = self.healthy + 0.01
            self.honey = self.honey + 0.01
            print('喂' + self.name + '猪大肠一根,母企鹅喜欢吃这个：健康值为' + str(self.healthy) + '好感度为' + str(self.honey))


class Pandas(QQ):
    def __init__(self,name, healthy, honey, gender, food,weight):
        self.weight=weight
        super().__init__(name, healthy, honey, gender, food)
    @property
    def play(self):
        self.healthy = self.healthy - 10
        self.honey = self.honey + 5
        print(self.name + '陪你爬树后，健康值为：' + str(self.healthy) + '好感度为：' + str(self.honey))
    @property
    def eat(self):
        if self.gender == 1:
            self.food = self.food - 1
            self.healthy = self.healthy + 5
            self.honey = self.honey + 5
            self.weight=self.weight+10
            print('喂' + self.name + '臭鸡蛋一个,公熊猫喜欢吃这个：健康值为' + str(self.healthy) + '好感度为' + str(self.honey)+'体重为'+str(self.weight))
        if self.gender == 2:
            self.food = self.food - 10
            self.healthy = self.healthy + 0.01
            self.honey = self.honey + 0.01
            self.weight = self.weight + 10
            print('喂' + self.name + '臭鸭蛋一个,母熊猫喜欢吃这个：健康值为' + str(self.healthy) + '好感度为' + str(self.honey)+'体重为'+str(self.weight))


if __name__ == '__main__':
    p = True
    while (p):
        dog =list('ABCDEFGH')
        animal = input('养狗还是企鹅还是熊猫')
        j = 0;
        if animal == '狗':
            i = True

            while (i):#养狗系统
                choice = int(input('领狗：1,\n玩狗：2,\n喂狗：3,\n离开此页面:4\n输入你的选择，刘浩超级喂养系统竭诚为您服务:'))
                if choice == 1:
                    if j < 10:
                        name = input('狗名：')
                        healthy = int(input(('健康值：')))
                        honey = int(input('忠诚度：'))
                        kind = int(input('种类：1：中国狗，2：小日本狗'))
                        food = int(input('有多少食物（1～100）：'))
                        dog[j] = Dog(name, healthy, honey, kind, food)
                        j = j + 1
                    else:
                        print('养那么多找死阿')
                if choice == 2:
                    num = int(input('玩第几只狗')) - 1
                    if (num) < j:
                        if dog[num ].food < 0:
                            print('没有食物还想遛狗！！！！！')
                        else:
                            dog[num ].play

                    else:
                        print('你猜你养了这只狗没？')

                if choice == 3:
                    num = int(input('喂第几只狗'))
                    if j >= num > -1:
                        dog[num - 1].eat

                    else:
                        print('别挑战我的智商')

                if choice == 4:
                    i = False






        if animal=='企鹅':
            qq=list('ABCDEFGHJK')
            i = True

            while (i):  # 养🐧企鹅系统
                choice = int(input('领企鹅：1,\n玩企鹅：2,\n喂企鹅：3,\n离开此页面:4\n输入你的选择，刘浩超级喂养系统竭诚为您服务:'))
                if choice == 1:
                    if j < 10:
                        name = input('企鹅名：')
                        healthy = int(input(('健康值：')))
                        honey = int(input('忠诚度：'))
                        gender = int(input('性别：1：公企鹅，2：母企鹅'))
                        food = int(input('有多少食物（1～100）：'))
                        qq[j] = QQ(name, healthy, honey, gender, food)
                        j = j + 1
                    else:
                        print('养那么多找死阿')
                if choice == 2:
                    num = int(input('玩第几只企鹅')) - 1
                    if (num) < j:
                        if qq[num ].food < 0:
                            print('没有食物还想遛企鹅！！！！！')
                        else:
                            qq[num ].play

                    else:
                        print('你猜你养了这只企鹅没？')

                if choice == 3:
                    num = int(input('喂第几只企鹅'))
                    if j >= num > -1:
                        qq[num - 1].eat

                    else:
                        print('别挑战我的智商')

                if choice == 4:
                    i = False








        if animal=='熊猫':
            print('牢底坐穿兽，小伙子胆子真肥')
            pd=list('ABCDEFGHIJ')
            i = True

            while (i):  # 养🐧企鹅系统
                choice = int(input('领熊猫：1,\n玩熊猫：2,\n喂熊猫：3,\n离开此页面:4\n输入你的选择，刘浩超级喂养系统竭诚为您服务:'))
                if choice == 1:
                    if j < 10:
                        name = input('熊猫名：')
                        healthy = int(input('健康值：'))
                        honey = int(input('忠诚度：'))
                        gender = int(input('性别：1：公熊猫，2：母熊猫'))
                        food = int(input('有多少食物（1～100）：'))
                        weight=50

                        pd[j] = Pandas(name, healthy, honey, gender, food,weight)

                        j = j + 1
                    else:
                        print('养那么多找死阿')
                if choice == 2:
                    num = int(input('玩第几只熊猫,虽然你玩第二只你就应该死了，但是刘浩超级喂养系统竭诚为您服务')) - 1
                    if (num) < j:
                        if pd[num - 1].food < 0:
                            print('没有食物还想遛熊猫！！！！！')
                        else:
                            pd[num - 1].play

                    else:
                        print('你猜你养了这只熊猫没？')

                if choice == 3:
                    num = int(input('喂第几只熊猫'))
                    if j >= num > -1:
                        pd[num - 1].eat

                    else:
                        print('别挑战我的智商')

                if choice == 4:
                    i = False