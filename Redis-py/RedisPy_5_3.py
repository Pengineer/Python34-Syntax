# 非事务型流水线

'''
 在非事务型处理过程中，流水线的执行速度往往是不使用流水线的4-6倍。因为流水线执行通过一次发送所有命令减少了通信
 次数并降低了延迟值。

 给pipeline()方法传入False参数时，客户端同样会像执行事务那样收集起用户要执行的所有命令，只是不再使用MULTI和EXEC
 包裹这些命令。

 使用流水线的前提：流水线中的一个命令的执行结果不会影响另一个命令，因为流水线中每个命令的结果是一起返回的。
'''

import redis
import time

# 将RedisPy_3中的update_token进行修改，使之成为流水线
def update_token_pipeline(conn, token, user, item=None):
    pipe = conn.pipeline(False)
    timestamp = time.time()
    pipe.hset('login:', token, user)
    pipe.zadd('recent:', token, timestamp)
    if item:
        pipe.zadd('viewd:' + token, item, timestamp)
        pipe.zremrangebyrank('viewd:' + token, 0, -26)
        pipe.zincrby('viewed:', item, -1)
    pipe.execute()

'''
 个人总结：不能直接通过pipe.get(key)的方法获取想要的值，它返回的仍然是一个pipe对象。这也印证了管道中的命令直接应该
           互不影响。

           再次说明，互不影响指的是不能通过一个命令的返回值来操作另一个命令，如下面的命令2的返回值操作了命令3，显然
           这是不会得到正确结果的；而不是说上一个命令的操作对其他命令的返回结果没有影响，如下面的命令2的返回是1，
           显然是受到命令1的影响。

           管道中的命令不执行完，内存中的键值是不会变化的，如下面的命令5得到的k1值还是0
'''
conn = redis.Redis(host='192.168.88.176', port=6379, db=0)
conn.set('k1', 0)

pipe = conn.pipeline(False)
pipe.set('k1', 1)      # 命令1
# time.sleep(10)
res = pipe.get('k1')   # 命令2，没有什么意义，res仍然是个pipe对象
print(type(res))       # 非管道命令，因此execute不会记录这个命令的值
pipe.set('k2', res)    # 命令3，本意是想将k1的值复制给k2
pipe.get('k2')         # 命令4
# 正确复制方法
pipe.set('k3', conn.get('k1')) # 命令5，不使用pipe获取k1的值，但是这里的k1的值是0，而不是1
pipe.get('k3')         # 命令6
list = pipe.execute()

print(list)            # list中依次存放了上述6个命令的返回结果
