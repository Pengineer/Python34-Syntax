# 异常处理之with

# with主要用于自动完成事后清理工作，比如文件句柄的关闭。
# http://blog.csdn.net/suwei19870312/article/details/23258495
#
# 上述对Python中with的理解较为深入，基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
# 首先会执行with所求值对象的__enter__()方法，然后执行with里面的具体业务，最后执行对象的__exit__()方法。
#
'''
对原先的文件打开，为了执行关闭，通常会加上finally：
file = open("aa.txt")
try:
    data = file.read()
finally:
    file.close()

用with替换后的结果就相当简洁了：
with open("aa.txt") as file:
    data = file.read()

如果想加入对异常的处理，还可以使用try-except进行封装：
try:
    with open("aa.txt") as file:
    data = file.read()
except OSError as reason:
    print('出错了' + str(reason))
'''

try:
    with open("aa.txt") as file1:
        data = file1.read()
except OSError as reason:
    print('出错了' + str(reason))
