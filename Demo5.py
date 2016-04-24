# Python序列类型之列表

# 定义一个列表
member = ['张三','李四','王五']
print(member)

# 一次追加一个元素
member.append('马六子')
print(member)

# 一次追加多个元素：用一个列表来扩展另一个列表
member.extend(['陆七','赵八'])
print(member)

# 任意位置插入元素
member.insert(0, 'britar')
print(member)

# 从列表中获取元素
print('1号人物：' + member[0])

# 从列表中删除一个元素：根据元素内容删除
member.remove('britar')
print(member)

# 从列表中删除一个元素：根据元素位置
# 注意：del不是列表的方法，而是一条语句。
#       del member 将删除整个列表的元素
del member[0]
print(member)

# 删除列表中指定位置的元素并获取之：Python的列表是使用栈来存储的，因此提供了pop方法
# pop如果不带参数，默认弹出列表中最后一个元素
print(member.pop(2))
print(member)

# 列表分片
print(member[0:2])
print(member[:])

# 列表的排序,list的排序采用的是归并算法
lists = [4,6,2,8,5,9,1]
print(lists)
lists.sort()
print(lists)
lists = [4,6,2,8,5,9,1]
lists.sort(reverse=True)   # 或者lists.sort();lists.reverse()
print(lists)

# 列表的拷贝
list1 = [1,2,3]
list2 = list1     # 浅拷贝
list3 = list1[:]  # 深拷贝
print(id(list1) == id(list2))
print(id(list1) == id(list3))

# 字符串转列表
str1 = 'I love python language.'
list4 = list(str1)
print(list4)

# 元组转列表
tuple1 = (1,1,2,3,5,8)
list5 = list(tuple1)
print(list5)
