# python事务

'''
 Redis有5个命令可以让用户在不被打断的情况下对多个键执行操作，他们分别是WATCH, MULTI, EXEC, UNWACTCH, DISCARD。
 Redis的基本事务（basic transaction）需要用到MUTIL和EXEC命令，Redis的事务和传统关系型数据库的事务概念不一样，
 Redis的事务是指保证在事务内的所有命令在执行过程中不被其它线程所打断，没有回滚的概念。

 Redis执行MUTIL命令后，会创建一个队列，将其后的指令都放入队列中，当碰到EXEC命令时，就开始一个接一个的执行队列
 里面的指令。

 Redis事务在Python中是通过流水线（pipeline）来实现的。这种方式可以减少客户端与Redis服务器之间的网络通信次数来
 提升Redis在执行多个命令时的性能。
'''
import redis
import time
import threading

def trans(conn):
    pl = conn.pipeline()
    pl.incr('var:')
    time.sleep(.1)
    pl.incr('var:', -4)
    list = pl.execute()  # execute()返回的是管道中每一个命令执行后的返回结果的列表
    print(list)
    print(conn.get('var:'))

if __name__ == '__main__':
    print('start...')
    conn = redis.Redis(host='192.168.88.176', port=6379, db=15)
    for i in range(3):
        threading.Thread(target=trans, args=(conn,)).start()
    time.sleep(.5)
    print('over...')
