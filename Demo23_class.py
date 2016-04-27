# 类

# Python不仅具有面向函数编程的思想，它还是一门面向对象的编程语言，拥有面向对象的三大基本特性：封装、继承、多态

'''
 self:
 1，self等同于Java中的this关键字，首先明确的是self只有在类的方法中才会有，独立的函数或方法是不必带有self的。
    self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
 2，self名称不是必须的，在python中self不是关键词，你可以定义成a或b或其它名字都可以,但是约定成俗，不要搞另类，大家会不明白的。
 3，类的所有方法必须只要有一个参数，类的所有方法的第一个参数一定表示类实例化对象本身。
 4，通过self创建的属性在实例化对象之间具有隔离性，且不需要事先声明；直接在类里面定义的变量被所有的实例化对象所共享。
 5，self只能在__init__()方法中创建属性。
'''

# 类定义
class classA:
    __propertyA = '属性A'

    def function1(self):
        print('方法A1')

    def functionA2(self):
        print('方法A2')

# 类继承
class classB(classA):
    propertyB = '属性B'

    def function1(self):
        print('方法B1')

    def functionB2(self):
        print('方法B2')

# 类的多重继承（实际中尽量少用）
class classC:
    propertyC = '属性C'

    def functionC(self):
        print('方法C')

class classD(classA, classC):
    propertyD = '属性D'

    def functionD(self):
        print('方法D')

# 类的魔法方法：__init__(self,para1,para2...)
# 等价于Java语言中的构造函数，在类实例化对象时创建。
# 在Python中定义私有变量只需要在变量名或函数名前加上"__"两个下划线，那么这个函数或变量就是私有的了（后面再加两下划线就不是私有了）
# 与Java不同的是，Python类的某个属性一旦被私有化，通过这个类实例化的对象也是不能访问这个属性的，一般会提供对应的get/set方法
# （Java的私有化主要是子类的实例化对象访问）。
# Python类的私有其实是伪私有的（Python没有成员的权限控制功能）它是将具有双下划线的变量进行了重命名：_类名__属性名，前面加了一个单下划线+类名。
class person:
    def __init__(self, name):
        self.name = name

    def func(self):
        print(self.name)

# 再说继承
# 在Python3中，子类继承父类，如果想调用父类的同名方法，有两种方式，父类.父类方法、super().父类方法（如果父类名称修改了也没关系）
# 但是，使用super()时，只会执行一个父类的构造函数
class BaseClass1:
    def __init__(self):
        print('BaseCalss1: Constructor called')

class BaseClass2:
    def __init__(self):
        print('BaseClass2: Constructor called')

class DerivedClass2(BaseClass1, BaseClass2):
    def __init__(self):
#        BaseClass1.__init__(self)
#        BaseClass2.__init__(self)
        super().__init__()
        print('DerivedClass: Constructor called')

if __name__ == '__main__':
    class3 = DerivedClass2()

# 多重继承中出现的几个概念：新式类、旧式类、MRO、深度优先算法、广度优先算法、C3算法
# 1，在Python2中存在新式类和经典类，Python3中只有新式类；新式类是在Python2.2开始引入的，统一了type和__class__的输出。如果
#    一个class继承于object，或其bases class里面任意一个继承于object，这个class都是new-style class。
# 2，将一个旧式类编程新式类有两种方式：继承object或者在类模块代码的最前面加一句__metaclass__ = type。
# 3，在Python的方法或属性搜寻中，符合MRO原则，即method resolution order，2.3之前的旧式类的MRO基于深度优先算法，2.3之前的旧式类的MRO基于
#    C3p0算法，所有版本的新式类的MRO均基于广度优先算法。
# 测试如下：让D继承object和不继承object将会得到不同的输出结果。
class D(object):
    def foo(self):
        print("class D")

class B(D):
    pass

class C(D):
    def foo(self):
        print("class C")

class A(B, C):
    pass

f = A()
f.foo()
