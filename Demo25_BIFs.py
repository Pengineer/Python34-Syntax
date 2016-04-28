# Python3中的一些BIF

# issubclass(class, classinfo)：如果class是classinfo的子类，则返回true
# 需要注意的是：
# 1，一个类是自身的子类；
# 2，classinfo可以是类对象组成的元组，只要class是其中任何一个候选类的子类，则返回true

# isinstance(object, classinfo)；如果object是classinfo的实例对象，则返回true

# hasattr(object, name)：如果对象object中有属性name，则返回true

# getattr(object, name[, default])：获取对象的属性值，如果属性不存在，返回default值

# setattr(object, name, value)：为对象的属性设置值，如果属性不存在，则新建。

# delattr(object, name)：删除对象中指定的属性，若不存在则抛出异常。
