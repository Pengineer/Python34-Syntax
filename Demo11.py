# map

'''
 格式：map(func, *iterables)
 filter只对序列中的元素进行过滤，并不会修改元素。map指对序列中的元素进行修改或映射，map函数的第二个参数是收集参数
'''

# 单一序列
print(list(map(lambda x : x * 2, range(5))))

# 多个序列做运算，各序列中相同脚标的元素做运算，func的参数个数与序列个数必须相同
# 如果各序列的长度不相等，则以最小长度的序列为基准
print(list(map(lambda x,y : x+y, range(5), range(20,30))))

# 多序列做映射
print(list(map(lambda x,y : (x,y), range(5), range(10,15))))
