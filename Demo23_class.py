# 类

# Python不仅具有面向函数编程的思想，它还是一门面向对象的编程语言，拥有面向对象的三大基本特性：封装、继承、多态

'''
 self:
 1，self等同于Java中的this关键字，首先明确的是self只有在类的方法中才会有，独立的函数或方法是不必带有self的。
    self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
 2，self名称不是必须的，在python中self不是关键词，你可以定义成a或b或其它名字都可以,但是约定成俗，不要搞另类，大家会不明白的。
 3，类的所有方法必须只要有一个参数，类的所有方法的第一个参数一定表示类实例化对象本身。
 4，通过self创建的属性在实例化对象之间具有隔离性，且不需要事先声明；直接在类里面定义的变量被所有的实例化对象所共享。
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
    __propertyB = '属性B'

    def function1(self):
        print('方法B1')

    def functionB2(self):
        print('方法B2')

# 类的多重继承
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
# 在Python中定义私有变量只需要在变量名或函数名前加上"__"两个下划线，那么这个函数或变量就会为是有的了
# 与Java不同的是，Python类的某个属性一旦被私有化，通过这个类实例化的对象也是不能访问这个属性的，一般会提供对应的get/set方法
# （Java的私有化主要是子类的实例化对象访问）。
# Python类的私有其实是伪私有的（Python没有成员的权限控制功能）它是将具有双下划线的变量进行了重命名：_类名__属性名，前面加了一个单下划线+类名。
class person:
    def __init__(self, name):
        self.name = name

    def func(self):
        print(self.name)



