# Demo2.py

print('------------python34-------------')
temp = input("猜一下xxx现在心里想的是哪个数字：")
guess = int(temp)
if guess == 8:
    print("猜对了！")
elif guess > 8:
    print("大了")
else:
    print("小了！")
print("游戏结束，88！")
