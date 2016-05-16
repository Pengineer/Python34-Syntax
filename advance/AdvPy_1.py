# @ 在Python中的应用之装饰器
# 参考：http://blog.sina.com.cn/s/blog_571b19a001013h7j.html  讲的很好
#       http://wiki.python.org/moin/PythonDecoratorLibrary    底层实现
#
#

class myDecorator():
    def __init__(self, f):
        print("inside myDecorator.__init__()")
        self.f = f

    def __call__(self):
        print("inside myDecorator.__call__()")
        self.f()   # 调用方法本身

@myDecorator       # 按python自带说明，这里@操作符相当于aFunction = myDecorator(aFunction)。从输出可以看出，这个运算其实在开始import时就已经在执行了
def aFunction():
    print("inside aFunction()")

print("Finished decorating aFunction()")

aFunction()

print(type(aFunction))


'''
输出结果：

inside myDecorator.__init__()
Finished decorating aFunction()
inside myDecorator.__call__()
inside aFunction()
<class '__main__.myDecorator'>
'''

# 或者如果不想使用类，也可以使用内部函数的办法。如下的代码和上面的同样的效果。装饰器。
def entryExit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return new_f

@entryExit
def func1():
    print("inside func1()")
