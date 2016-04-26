# Python序列类型之元组

'''
元组的操作与列表类似，但是元组的元素不可修改
元组的关键不是小括号，而是逗号
'''

tuple1 = (1,2,3,4,5)
print(tuple1[1])

tuple2 = (1)
print(type(tuple2))     # int

tuple3 = 1,2,3
print(type(tuple3))     # tuple

# 创建只有一个元素的元组: 元素后面加个逗号
tuple4 = (1,)
print(type(tuple4))

# 可以使用拼接的方式间接修改一个元组的内容，得到的是一个新元组
