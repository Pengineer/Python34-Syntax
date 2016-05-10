# 魔法方法：算术运算


# 将一个字符串转成整数：int('123')，实际上它是创建了一个int对象，然后赋值为123，并将对象返回
# 如下，创建了两个对象a和b，发现这两个对象可以相加，这底层其实是Python调用了算术运算的魔法方法。
a = int('123')
b = int('456')
print(a+b)

'''
常见的与算术运算相关的魔法方法：
__add__(self, other)：定义加法行为
__sub__(self, other)：定义减法行为
__mul__(self, other)：定义乘法行为
__truediv__(self, other)：定义真除法行为
__floordiv__(self, other)：定义整数除法行为
__mod__(self, other)：定义取摸算法的行为
__divmod__(self, other)：定义当被divmod()调用时的行为
__pow__(self, other[, modulo])：定义当被power()调用或**运算时的行为
__lshift__(self, other)：定义按位左移位的行为：<<
__rshift__(self, other)：定义按位右移位的行为：>>
__and__(self, other)：定义按位与操作的行为：&
__xor__(self, other)：定义按位异或的行为：^
__or__(self, other)：定义按位或操作的行为：|
'''
