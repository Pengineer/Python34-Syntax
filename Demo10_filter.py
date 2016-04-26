# 过滤器filter

'''
功能说明：
 filter(function or None, iterable)是Python的内建函数，如果第一个参数为None，则输出第二个参数中味True的元素；
 如果第一个参数为function，则输出iterable中那些在function作用下能返回True的元素
 '''

# None
list1 = [1, 0, False, True]
filter1 = filter(None, list1)
print(list(filter1))

# function：输出1-10内的奇数
def odd(x):
    return x % 2
filter2=filter(odd, range(10))
print(list(filter2))

# 将上面的实现使用lambda实现
print(list(filter(lambda x : x % 2, range(10))))

# 测试：None本身代表false
if not None:
    print('测试输出！')
