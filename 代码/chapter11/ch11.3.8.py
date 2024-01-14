# coding=utf-8
# 代码文件：chapter11/ch11.3.8.py


class Account:
    """定义银行账户类"""

    interest_rate = 0.0668  # 类变量利率

    def __init__(self, owner, amount):
        self.owner = owner  # 定义实例变量账户名
        self.amount = amount  # 定义实例变量账户金额

    # 类方法
    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt

    # 静态方法
    @staticmethod
    def interest_with(amt):
        return Account.interest_by(amt)


act1 = Account(1,1000)

interest1 = act1.interest_by(12_000.0)
print('类实例调用类方法，计算利息：{0:.4f}'.format(interest1))    #用类实例act1调用了类方法

interest1 = act1.interest_with(12_000.0)
print('类实例调用静态方法，计算利息：{0:.4f}'.format(interest1))    #用类实例act1调用了静态方法

interest2 = Account.interest_by(12_000.0)
print('类对象调用类方法，计算利息：{0:.4f}'.format(interest2))    #用类对象调用了类方法

interest3 = Account.interest_with(12_000.0)
print('类对象调用静态方法，计算利息：{0:.4f}'.format(interest3))    #用类对象调用了静态方法
                                                #从上面4中调用来看，从语法上都是可行的，但从python规范用法上不推荐

