# @property 为类定义属性
#
# _name 表示希望你视这个变量为私有的，不要直接调用它，但是没有强制作用，即instance._name 是合法的。
# __name 表示这个变量是私有的，无法直接调用。即 instance__name 是非法的。但是这是因为解释器将该变量解析成了_ClassName__name的形式，因此instance._ClassName__name是合法的。（当然具体解析出的形式如何取决于解释器，因此最佳实践是不要直接调用这种变量）
# __name__表示这是具有特殊功能的变量

class Student():

#    score = 0                # 通过赋初值的方式定义一个类属性对所有实例生效。通过__init__声明属性使得实例化对象不够灵活

    @property                 # get属性
    def score(self):
        return self._score

    @score.setter             # set属性
    def score(self, value):
        if not isinstance(value, int):   # 可以对属性值的合法性进行校验
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

stu1 = Student()
stu1.score=100
print(stu1.score)

stu2 = Student()
stu2.score=10
print(stu2.score)
