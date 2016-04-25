# 递归

# 非递归实现阶乘
def recur1(i):
    result = 1
    while(i>0):
        result *= i
        i -=1
    return result

def recur2(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

# 递归实现阶乘
def recur3(i):
    if(i == 1):
        return 1
    return recur3(i-1) * i

# 递归实现斐波拉契数列
def recur4(n):
    if n == 1 or n == 2:
        return 1
    else:
        return recur4(n-1) + recur4(n-2)

# 递归实现汉诺塔问题
# 参数意义：将x上n个盘子借助y移动到z上
def hanoi(n ,x ,y ,z):
    if n == 1:
        print(x, '->', z)
    else:
       hanoi(n-1, x, z, y)  # 将x上前n-1个盘子从x借助z移动到y上
       print(x, '->', z)    # 将最底下的最后一个盘子从x移动到z上
       hanoi(n-1, y, x , z) # 将y上的n-1个盘子借助x移动到z上


print(recur1(5))
print(recur2(5))
print(recur3(5))
print(recur4(6))
hanoi(3, 'X', 'Y', 'Z')
