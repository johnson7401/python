class CLanguage :

    name = "xxx" #类变量
    add = "http://" #类变量

    def __init__(self):
        self.name = "我爱python" #实例变量
        self.add = "网络地址" #实例变量

    # 下面定义了一个say实例方法
    def say(self):
        self.catalog = 13 #实例变量

clang = CLanguage()
print("clang.name",clang.name)
print("clang.add",clang.add)

clang2 = CLanguage()
#修改 clang2 对象的实例变量
clang2.name = "python教程"
clang2.add = "网络地址/python"
print("clang2.name",clang2.name)
print("clang2.add",clang2.add)

#输出类变量的值
print("Clanguage.name",CLanguage.name)
print("Clanguage.add",CLanguage.add)