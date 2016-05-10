# Demo1.py

import random

print('------------python34-------------')
num=random.randint(1,10)
temp = input("猜一下xxx现在心里想的是哪个数字：")
guess = int(temp)
if guess == num:
    print("猜对了！")
else:
    print("猜错啦！答案是：" + str(num))
print("游戏结束，88！")
