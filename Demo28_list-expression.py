#  列表表达式

'''
1.列表推导式书写形式：　　

[表达式 for 变量 in 列表]    或者  [表达式 for 变量 in 列表 if 条件]
'''
li = [1,2,3,4,5,6,7,8,9]

print([x**2 for x in li])

print([x**2 for x in li if x>5])

print (dict([(x,x*10) for x in li]))

print ([(x,x*10) for x in li])

print([x*y for x in [1,2,3] for y in  [1,2,3]])

print([ (x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8 ])
