# 字符串操作

# 将字符串切割成3元组
str1 = 'aabbccbbdd'
print(str1.partition('bb'))  # 注意结果

# 将字符串切割成列表,split第二个参数表示切割次数，默认全部切割
str2 = 'aabbccbbdd'
print(str2.split('bb'))

# 将字符串中的某一部分替换成等长的子串
str3 = 'aabbccdd'
print(str3.translate(str.maketrans('bb', 'kk')))

# 删除字符串前后指定字符，默认是删除空格
str4 = '  abc d  '
print(str4.strip())

# 替换字符串中指定子串(可以指定替换次数)
str5 = 'zabcdabef'
print(str5.replace('ab',''))

# 返回子串出现的次数
print(str5.count('ab'))

# 从左边开始查找字符串中的子串，如找不到，返回-1
# index()方法与find方法的功能一样，但是如果没找到，index()会抛出异常
print(str5.find('cab'))

# 字符串格式化
# format支持两种参数的传递：未知参数和关键字参数
# 注意：如果同时使用这两种参数，那么未知参数必须出现在关键字参数前面
#       如果不想将字符串中某个大括号作为参数，可以使用双重大括号转义{{0}}
# Python3中格式化符号的含义与Python2有所差异
#
str6_1 = '{0} love {1} language.'
print('str6_1: ' + str6_1.format('I', 'python'))     # 未知参数

str6_2 = '{a} love {b} language.'
print('str6_2: ' + str6_2.format(a='I',b='python'))  # 关键字参数

str6_3 = '{0:.1f}{1}'                                # 在替换域中，冒号表示格式化符号的开始
print(str6_3.format(27.658, 'GB'))



