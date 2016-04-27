# 图形用户界面GUI

# EasyGUI 官网：http://easygui.sourceforge.net
# 官方教学文档： - easygui-docs-0.96\tutorial\index.html
# 小甲鱼翻译改变的教学文档(1749426502登录查看)：http://bbs.fishc.com/thread-46069-1-1.html

# 导包的三种方式：
# import mypackage          # 最普通的方式
# from mypackage import *   # 导入包中的所有函数，应用时不需要写较长的包名，但是可能会和其他包或者本地方法重名
# import mypackage as m     # 推荐导包方式，导入时将包名重命名

import easygui as g

g.msgbox('message')
