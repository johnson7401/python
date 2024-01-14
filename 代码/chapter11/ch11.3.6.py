# coding=utf-8
# 代码文件：chapter11/ch11.3.6.py


class Animal(object):
    """定义动物类"""

    def __init__(self, age, sex=1, weight=0.0):
        self.age = age  # 定义年龄实例变量
        self.sex = sex  # 定义性别实例变量
        self.weight = weight  # 定义体重实例变量

    def eat(self,eat_add = 0.1):
        self.weight += eat_add
        print('eat...')

    def run(self,run_deg = 0.05):
        self.weight -= run_deg
        print('run...')

a1 = Animal(2, 0, 10.0)
print('a1体重：{0:0.2f}'.format(a1.weight))
a1.eat(2)
print('a1体重：{0:0.2f}'.format(a1.weight))
a1.run(6)
print('a1体重：{0:0.2f}'.format(a1.weight))
