# 商品销售与购买

'''
 集合：
 （1）用户集合：hash散列，记录用户信息；
 （2）用户包裹：set集合，记录各用户拥有的商品名；（每一个用户包裹对应一个set）
 （3）市场集合：zset有序集合，记录商场上销售的商品及其价格。
'''

'''
 WATCH命令可以监控一个或多个键，一旦其中有一个键被任意连接修改（或删除），本连接之后的紧接着的一个事务就完全不会执行。
 WATCH的监控有效持续到本连接的下一个EXEC命令。

 UNWATCH命令可以在WATCH命令执行之后、MULTI命令执行之前对连接进行重置（reset）。

 如果其它客户端修改了本客户端WATCH的key，Redis会通知执行了WATCH的客户端，这种做法称为乐观锁，传统关系数据库中的锁是悲观锁。
'''

import time
import redis

# 将卖家sellerid的商品itemid放到市场上以price的价格出售。
# 卖之前需要保证该商品在卖家的包裹里，因此需要监听卖家的包裹是否发生变化。
def list_item(conn, sellerid, itemid, price):
    inventory = 'inventory:%s' % sellerid    # inventory:17
    item = '%s.%s' % (itemid, sellerid)      # ItemA.3
    end = time.time() + 5
    pipe = redis.pipeline()

    while time.time() < end:                 # 如果发生异常，这进行重试，最大重试时间是5s
        try:
            pipe.watch(inventory)            # 监视用户包裹发生的变化
            if not pipe.sismember(inventory, itemid):
                pipe.unwatch()               # UNWATCH命令可以在WATCH命令执行之后，MULTI命令执行之前
                return None
            pipe.multi()
            pipe.zadd('market:', item, price)
            pipe.srem(inventory, itemid)
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            pass
    return False

# 购买商品
def purchase_item(conn, buyerid, itemid, sellerid, lprice):
    buyer = 'users:%s' % buyerid
    seller = 'users:%s' % sellerid
    item = '%s.%s' % (itemid, sellerid)
    inventory = 'inventory:%s' % buyerid
    end = time.time() + 10
    pipe = conn.pipeline()

    while time.time() < end:
        try:
            pipe.watch('market:', buyer)             # 同时监视市场和买家信息
            price = pipe.zscore('market:', item)
            funds = int(pipe.hget(buyer, 'funds'))
            if price != lprice or price > buyer:     # 买家钱不够
                pipe.unwatch
                return None

            pipe.multi()
            pipe.hincrby(seller, 'funds', int(price))
            pipe.hincrby(seller, 'funds', int(-price))
            pipe.sadd(inventory, itemid)             # 买家包裹中增加商品
            pipe.zrem('market:', item)               # 删除市场上的该商品
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            pass
    return False

