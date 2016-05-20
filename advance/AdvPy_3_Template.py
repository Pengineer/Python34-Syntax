import time
import os.path
from string import Template

'''
 string模块提供了一个通用Template类，可以使用占位符进行字符串格式化
'''

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BathRename(Template):
    delimiter = '%'                                    # Template默认使用 $ 占位符，如果要换一个delimiter的话，可以继承一个Template的子类，然后覆盖它的类属性delimiter

fmt = 'Pic_%{num}_%{date}%{ext}'                       # 新文件名格式
date = time.strftime('%Y%m%d')

t = BathRename(fmt)
for i, filename in enumerate(photofiles):              # enumerate在遍历的时候会自动创建一个从0开始的编号
    base, ext = os.path.splitext(filename)             # 获取文件名和文件扩展名
    newname = t.substitute(date = date, num=i, ext=ext)# 将文件名使用格式化字符串进行格式化，获取新文件名
    print('{0}-->{1}'.format(filename, newname))
