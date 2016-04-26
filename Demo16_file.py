# 文件操作

'''
阿Q2：阿Q来了
阿Q1：还没下班？
阿Q2：没，阿Q还没下班呢。
阿Q1：呵呵
阿Q2：你不是阿Q吧？
阿Q1：现在人人是
阿Q2：我必须承人，我是阿Q，每两个在一起，都是QQ QQ QQ QQ
阿Q1：哈哈
阿Q2：而且还每个都有一个QQ号，看来阿Q之多，都有编号了。
阿Q1：是啊
======================================================
阿Q2：物以类聚，人以群分。你看，QQ们也是臭味相投的，都建起了一个一个的群，叫做QQ群。真有意思。好像找到了组织似的，呵呵。
阿Q1：是啊！不过有时也有用，我加的是技术群
阿Q2：呵呵呵，我加的也是技术群，技术群也是QQ群，里面也是阿Q。 QQ们可以偷菜，乐此不疲。
阿Q1：我现在不怎么玩了
阿Q2：幸亏鲁迅早死了，要不也会被QQ们气死的
阿Q1：哈哈哈
阿Q2：QQ们还会斗地主
阿Q1：我现在还斗
阿Q2：QQ们的精神乐园就在这里，唉，可以还是有很大一部分阿Q没有加入到组织中来呀，他们要么很小，要么很老，没上过学的也有，实在是没法加入这个QQ组织呀。他们是阿Q中的弱势群体，没有人帮助他们入QQ组织。群内的Q对群外的Q说，你也配Q，也不洒泡尿照照自己，配吗！这是阿Q在当今世界的真实写照，愿阿Q精神永放光茫。
'''

# 将上述文件内容分类保存
source = open('D:/output.txt', mode='r+', encoding='utf-8')
Q11 = open('D:/Q11.txt', mode='r+', encoding='utf-8')
Q12 = open('D:/Q12.txt', mode='w+', encoding='utf-8')
Q21 = open('D:/Q21.txt', mode='w+', encoding='utf-8')
Q22 = open('D:/Q22.txt', mode='w+', encoding='utf-8')

Q1List = [Q11, Q12]
Q2List = [Q21, Q22]
count=0
for each_line in source:
    if each_line[:6] != '======':
        if each_line.startswith('阿Q1：'):
            Q1List[count].write(each_line[4:])
        else:
            Q2List[count].write(each_line[4:])
    else:
        count +=1

source.close();Q11.close();Q12.close();Q21.close();Q22.close()
