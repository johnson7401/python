# coding=utf-8
# 代码文件：chapter11/ch11.3.4.py


class Account:
    """定义银行账户类"""

    interest_rate = 0.0668  # 类变量利率

    def __init__(self, owner, amount):
        self.owner = owner  # 定义实例变量账户名
        self.amount = amount  # 定义实例变量账户金额


account = Account('Tony', 1_800_000.0)

print('账户名：{0}'.format(account.owner))
print('账户金额：{0}'.format(account.amount))
print('利率：{0}'.format(Account.interest_rate))

print('Account利率：{0}'.format(Account.interest_rate))
print('ac1利率：{0}'.format(account.interest_rate))

print('修改前ac1实例所有变量：{0}'.format(account.__dict__))
account.interest_rate = 0.01        #这里通过类对象account来给类变量interest_rate赋值，实际上
                                    #是创建了account.interest_rate一个实例，并没有修改类变量
account.interest_rateg = 0.01       #这下面三行，都是动态的给类对象account添加了interest_rateg,
account.interest_rate5 = 0.05       #interest_rate5,interest_rate_dd三个实例变量
account.i1nterest_rate_dd = 0.08    #第一行虽然似乎修改了interest_rate，但是实际上只是修改了示例变量
print('修改后ac1实例所有变量：{0}'.format(account.__dict__))
print('Account类的interest_rate：{0}'.format(Account.interest_rate))  #这里可以看到类Account的类变量没有被修改