# 映射类型之字典

# 字典的创建一：直接创建
# 通过键获取值
dict1 = {'1':'赵', '2':'钱', '3':'孙', '4':'李'}
print(dict1['1'])

# 字典的创建二：通过BIF创建
# 由于dict只能接受一个参数，因此需要使用()将序列包装起来
dict2 = dict((['a',65],['b',66],['c',67]))
print(dict2['a'])

# 字典值的修改
dict1['4'] = '彭'
print(dict1['4'])

# 如果所修改的键不在字典中，则会自动增加
dict1['5'] = '周'
print(dict1)

# 给字典的键设置值，如果键不存在，则添加，如果键存在，则不变
dict3 = {'a':None,'b':'B'}
print(dict3)
dict3.setdefault('c', 'C')
print(dict3)
dict3.setdefault('a', 'AA')
print(dict3)

# 获取字典的所有键：keys()
for eachKey in dict2.keys():
    print(eachKey)

# 获取字典的所有值：values()
for eachValue in dict2.values():
    print(eachValue)

# 获取字典的所有键值对：items()
for eachItem in dict2.items():
    print(eachItem)

# 获取字典中一个未知的键，若存在，则输出其值，否则，输出给定值（默认输出None）
print(dict2.get('d', '不存在！'))

# 判断一个键是否在字典中，直接使用成员操作符in
print('d' in dict2)

# 清空一个字典
# dict2.clear()

# 深拷贝一个字典：dict3 = dict2.copy()

# 弹出/删除字典中的一个Item：pop(key) 或则 popitem()
# 前者是根据key值弹出指定Item，后者是随机弹出一个
print(dict1)
print(dict1, dict1.pop('5'), dict1)
print(dict1.popitem())
