# 类、类对象、实例对象

'''
 通过class定义的是类；
 类被加载后就会产生一个类对象，对象名就是类名；
 通过类实例化出来的对象就叫实例对象。
'''

class Clazz:
    count =0;

a=Clazz()
b=Clazz()
c=Clazz()

a.count+=10
print(a.count)
print(b.count)
print(c.count)

Clazz.count=100    # 类对象调用属性
print(a.count)     # 10
print(b.count)     # 100
print(c.count)     # 100

'''
 测试结果表明，a.count+=10，当实例对象a修改了类的属性时，该操作会在a的栈空间创建一个新的属性，该属性才归a独享，否则将共享类对象的属性。
'''

# 类属性、实例属性
# 在Python中建议多使用实例属性，少用类属性。
# 如下面x和y就是实例属性，在对象被创建而且属性被赋值后，即使删除类对象，也不会影响实例对象的使用，这就是Python的绑定机制。
# 实例对象及其属性和方法类似于C语言中static关键字，其生命周期与程序相同。
class classA:
    def func(self, x, y):
        self.x = x
        self.y = y

a = classA()
print(a.__dict__)       # 返回{}。__dict__属性记录了一个对象的所有属性
print(classA.__dict__)  # {'__weakref__': <attribute '__weakref__' of 'classA' objects>, '__dict__': <attribute '__dict__' of 'classA' objects>, '__doc__': None, '__module__': '__main__', 'func': <function classA.func at 0x01730420>}

a.func(4,5)
print(a.__dict__)       # {'x': 4, 'y': 5}。一旦调用func方法，就会为实例对象a创建两个属性（Python中属性的创建不需要声明）
