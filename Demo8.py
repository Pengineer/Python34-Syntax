# python函数

# 一般函数定义
def function():
    print('定义函数')

# 带参数和返回值的函数定义
def function2(num1, num2) :
    return num1 + num2

# 关键字参数：python中函数调用传入的参数顺序可以与函数定义时不一致，只需要在传递时指定参数名即可
def function3(arg1, arg2):
    print(arg1 + '->' + arg2)

function3('前', '后')
function3(arg2='后', arg1='前')

# 默认参数：当调用函数没有传递对应的参数时，Python自动获取默认参数值
def function4(num1=0, num2=0) :
    return num1 + num2

print(function4())
print(function4(1))
print(function4(1, 1))

# 收集参数：等同于java中的可变参数，在参数前加*即可
# python会将传递进函数的参数用元组打包
# 如果函数参数同时含有收集参数和非收集参数，则非收集参数最好设置为默认参数，同时在调用函数时需要加关键字
def function5_1(*args):
    print(args)
    print('参数长度：', len(args))
    print('第二个参数：', args[1])

function5_1(1, '张三', 'CN')

def function5_2(*args, exp=0):
    print(args, exp)

function5_2(1, '张三', 'CN', exp=3)

# 局部变量和全局变量：
# 局部变量的作用域是函数内，全局变量的作用域是整个py文件。
# 不建议在函数内修改全局变量的值（可以访问），因为这样的修改是无效的，在函数内修改全局变量的值时，
# Python会采用shading屏蔽的方式在函数内自动创建一个和全局变量同名的局部变量，因此函数内修改的其实是新建的局部变量
def function6():
    price = 50
    print('函数内值：', price)

price = 100
print('函数调用前全局值：', price)
function6()
print('函数调用后全局值：', price)

# 在函数内修改全局变量的方式
def function7():
    global price        # 指明price为全局变量
    price = 50
    print('函数内值：', price)

price = 100
print('函数调用前全局值：', price)
function7()
print('函数调用后全局值：', price)

# 内嵌函数
def function8():
    print("外层函数执行。。。")
    def function8_1():
        print("内层函数执行。。。")
    function8_1()

function8()

# 闭包：它是面向函数式编程的核心，是一种编程范式（面向对象，面向过程都是一种变成范式）
# 简单点说闭包就是一个被返回的函数对象
def function9(x):
    def fun9_1(y):          # fun9_1就是一个闭包
        return x * y
    return fun9_1
f = function9(8)
print(f)
print(type(f))       # f是一个function类型的变量
print(function9(8)(9))

# 关于闭包中变量的使用：需要遵循类似局部变量和全局变量的规则
'''
下面是错误的使用：它的本意是内层函数将外层函数的x平方并返回，但是内层函数并不能直接修改外层函数的变量，当内层函数修改x的值时，Python会通过屏蔽手段
在内层函数的栈中新建一个与外层函数同名的变量x，而这个变量在内层函数有没有初始化，因此会报错。
这里不能使用global关键字来解决，因为外层函数的变量并不是全局变量。
def function10():
    x = 5
    def function10_1():
        x = x * x
        return x
    return function10_1()
function10()

错误信息：
Traceback (most recent call last):
  File "Demo8.py", line 95, in <module>
    function10()
  File "Demo8.py", line 94, in function10
    return function10_1()
  File "Demo8.py", line 92, in function10_1
    x = x * x
UnboundLocalError: local variable 'x' referenced before assignment          # x在被赋初值之前被引用了
'''

# 方案一的解决方式：因为函数变量是存储在各自的栈空间，因此不同的函数不能直接共享变量。但是由于容器类型并不存储在栈中，而Python在函数中屏蔽变量时只会
# 屏蔽栈中的变量，因此可以采用容器的方式来解决。
def function11():
    x = [5]
    def function11_1():
        x[0] = x[0] * x[0]
        return x[0]
    return function11_1()
print(function11())

# 方案二的解决方式：方案一是在Python3之前的有点投机取巧的解决方式，python引入了nonlocal关键字，它可以指明一个被调用变量是非局部变量
def function12():
    x = 5
    def function12_1():
        nonlocal x
        x = x * x
        return x
    return function12_1()
print(function12())

# 显然这里就会涉及到global和nonlocal关键字的比较：
# python引用变量的顺序：当前作用域局部变量->外层作用域变量->当前模块中的全局变量->python内置变量
# global关键字用来在函数或其他局部作用域中使用全局变量。但是如果不修改全局变量也可以不使用global关键字。
# nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
