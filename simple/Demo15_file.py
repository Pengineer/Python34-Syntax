# 文件

'''
 文件打开模式与执行操作列表：
 'r'：以只读方式打开文件（默认）
 'w'：以写入的方式打开文件，会覆盖已存在的文件，如果文件不存在则自动新建
 'x'：如果文件已经存在，使用此模式打开将引发异常
 'a'：以写入模式打开，如果文件存在，则在末尾追加写入
 'b'：以二进制模式打开文件
 't'：以文本模式打开（默认）
 '+'：可读写模式（可添加到其他模式中使用）
 'U'：通用换行符支持

 文件对象方法：
 f.close()：关闭文件
 f.read(size=-1)：从文件读取size个字符，当未给定size或给定负值的时候，读取剩下的所有字符，然后作为字符串返回
 f.readline()：以写入模式打开，如果文件存在，则在末尾追加写入
 f.write(str)：将字符串str写入文件
 f.writelines(seq)：向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象
 f.seek(offset, from)：在文件中移动文件指针，从from（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节
 f.tell()：返回当前在文件中的位置
'''

# import codecs,sys

# 文件打开
# f = open("D:\\Python\\Workspace\\Demos\\Demo9.py", mode = 'r', encoding = 'utf-8')
# print(f)   # <_io.TextIOWrapper name='D:\\Python\\Workspace\\Demos\\Demo9.py' mode='r' encoding='utf-8'>

# 文件读取：在读取文件时，会有一个文件指针，每读一个字符指针后移一位
# 下面第二次read返回的结果就是空
# print(f.read())
# print(f.read())
# f.close()

# 文件指定长度的读取，同时获取指针位置
# print(f.read(5))
# print(f.tell())
# f.close()

# 设置文件指针的位置
# f = open("D:\\Python\\Workspace\\Demos\\Demo9.py", mode = 'rb')
# f.seek(-16,2)
# print(f.read(5))

# 文件的行级迭代读取
# 不要讲f转成list，然后在读取，效率太低，特别是文件很大时，尤为明显
# f = open("D:\\Python\\Workspace\\Demos\\Demo9.py", mode = 'r', encoding = 'utf-8')
# for each_line in f:
#     print(each_line)

# 文件的写入,
# w+表示以写入的方式打开可读写文件
# r+表示以只读的方式打开可读写文件
f = open("D:/output.txt", mode='w+', encoding='utf-8')
f.write("风萧萧兮易水寒，壮士一去兮不复还。\n")
f.write("三十功名尘与土，八千里路云和月。")
f.close()

# 实际中个人推荐文件的打开方式：
# with open('filepath') as f:
#     pass
