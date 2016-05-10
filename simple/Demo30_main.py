# 关于属性__name__

import Demo29_main

# 这个时候29中的__name__属性的值为Demo29_main，因此29中的if不满足

if __name__ == '__main__':
    print('执行30')


# 补充：
# Python模块导入顺序：当前路径 --> lib目录  --> site-package目录
