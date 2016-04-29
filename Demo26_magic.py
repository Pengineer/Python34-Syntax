# 魔法方法

'''
 魔法方法总是被双下划线包围，例如__init__。
 魔法方法是面向对象的Python的一切，如果你不知道魔法方法，说明你还没能意识到面向对象的Python的强大。
 魔法方法的“魔力”体现在它们总能够子啊适当的时候被自动调用。
'''

# __init__(self[,...])
# 对象实例化时被自动调用

# __new__(cls[,...])
# __init__方法并不是对象实例化时被调用的第一个方法，而是__new__(cls[,...])方法
# 第一个参数数class，后面如果有参数则原封不动的传给__init__方法。
# 这个方法执行后会返回一个类的实例化对象，我们一般不会去重写这个方法。
# 仅当我们修改一个不可变类型时会重写该方法。
#
# 如下，因为str类型是不可变类型，为了强制统一str的格式，我们可以覆写str的__new__(),在创建str对象之前将其进行相应的修改，然后在创建对象。
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)

c = CapStr('Hello Python')
print(c)

# __del__(self)
# Python的析构器，当对象要被销毁的时候，这个方法被自动的调用。
# 当一个对象的引用计数为0时，将执行该方法。