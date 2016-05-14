# 发布与订阅

import threading
import unittest
import time

def publisher(conn, n):
    time.sleep(1)
    for i in range(n):
        conn.publish('c1', i)
        time.sleep(1)

def run_pubsub(conn):
    t = threading.Thread(target=publisher, args=(conn,3,))
    t.start()

    pubsub = conn.pubsub()
    pubsub.subscribe(['c1']) # 刚开始订阅一个频道的时候，客户端会接收到一条关于被订阅频道的反馈信息
    count = 0
    for item in pubsub.listen():
        print(item)
        count += 1
        if count == 4:
            pubsub.unsubscribe() # 在退订频道时，客户端会接收到一条反馈消息，告知被退订的是哪个频道，以及客户端目前仍在订阅的频道数量
        if count == 5:
            break

class test(unittest.TestCase):
    def setUp(self):
        import redis
        self.conn = redis.Redis(host='192.168.88.176', port=6379, db=15)
    def tearDown(self):
        del self.conn

    def test_run_pubsub(self):
        run_pubsub(self.conn)

if __name__ == '__main__':
    unittest.main()
