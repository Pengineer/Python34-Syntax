# 集合

# 区分集合和字典，均是由{}封装元素，如果元素呈映射关系，则是字典，否则为集合，空{}表示字典
# type({})       ---<class 'dict'>
# type({1,2})    ---<class 'set'>

# 集合中的元素具有唯一性，它会自动清除重复元素
# 集合中的元素是无序(输入输出顺序是不一致的)的，不能根据index获取集合中的元素

# 集合的创建一：直接创建
set1 = {1,2,3,4,5,5,5}
print(set1)

# 集合的创建二：通过BIF创建，set(iterable)
set2 = set([4,2,1,3])
print(set2)

# 集合中的元素具有唯一性
# 例：去掉列表[1,3,2,4,3]中重复的元素
list1 = [1,3,2,4,3]
list1 = list(set(list1))
print(list1)

set2.add(5); print(set2)         # {1, 2, 3, 4, 5}
set2.remove(4); print(set2)      # {1, 2, 3, 5}
set2.pop(); print(set2)          # {2, 3, 5}

# 不可变集合：frozenset
set3 = frozenset([3,4,5,6,5])
print(set3)
