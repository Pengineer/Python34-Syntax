# else 语句

# if - else

# while - else
# 当while顺利执行完成时，执行else；如果while被break阻断，这不执行else
n = 5
while n > 0:
    if n == 0:
        break
    print(n)
    n -= 1
else:
    print('顺利执行。。。')


# for - else
# 同while

# 与异常语句搭配：无异常，则执行else
try:
    int('12')
except ValueError as reason:
    print('出错：' + str(reason))
else:
    print('无异常。')
