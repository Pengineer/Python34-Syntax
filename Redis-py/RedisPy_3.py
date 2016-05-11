import json
import threading
import time
import unittest
import urllib.parse as parse
import uuid

# 获取令牌对应的用户
def check_token(conn, token):
    return conn.hget('login:', token)

# 更新token，每次浏览页面则更新token，如果浏览的是商品则更新浏览记录
def update_token(conn, token, user, item=None):
    timestamp = time.time()
    conn.hset('login:', token, user)
    conn.zadd('recent:', token, timestamp)
    if item:
        conn.zadd('viewd:' + token, item, timestamp)
        conn.zremrangebyrank('viewd:' + token, 0, -26)
        conn.zincrby('viewed:', item, -1) # viewed有序集合用来存储被浏览商品的浏览次数，浏览的次数越多分值越小排位越靠前

# 清除旧的会话，包括：login，recent，viewd三个键中的记录
QUIT= False
LIMIT = 1000000
def clean_token(conn):
    while not QUIT:
        size = conn.zcard('recent:')
        if size <= LIMIT:
            time.sleep(1)
            continue
        end_index = min(size - LIMIT, 100)
        tokens = conn.zrange('recent:', 0, end_index -1)
        token_keys = []
        for token in tokens:
            token_keys.append('viewd:' + token)
            token_keys.append('cart:' + token)
        conn.delete(*token_keys)  # 这里用到了Python中关于任意参数列表和参数列表的分拆语法
        conn.hdel('login:', *tokens)
        conn.zrem('recent:', *tokens)

# 商品购物车管理
def add_to_cart(conn, token, item, count):
    if count <= 0:
        conn.hrem('cart:' + token, item)
    else:
        conn.hset('cart:' + token, item, count)

# 缓存页面
def cache_request(conn, request, callback):
    if not can_cache(conn, request):
        return callback(request)

    page_key = 'cache:' + hash_request(request)
    content = conn.get(page_key)
    if not content:
        content = callback(request)
        conn.setex(page_key, content, 300)
    return content

# 调度缓存和终止缓存：设置缓存计划
def schedule_row_cache(conn, row_id, delay):
    conn.zadd('delay:', row_id, delay)
    conn.zadd('schedule:', row_id, time.time())

# 守护进程：缓存数据
def cache_rows(conn):
    while not QUIT:
        next = conn.zrange('schedule:', 0, 0, withscores=True)
        now = time.time()
        if not next or next[0][1] > now:
            time.sleep(.05)
            continue
        row_id = next[0][0]

        delay = conn.zscore('delay:', row_id)
        if delay <= 0: # 不必再缓存该行数据，移除之
            conn.zrem('delay:', row_id)
            conn.zrem('schedule:', row_id)
            conn.delete('inv:' + row_id)

        row = Inventory.get(row_id)
        conn.zadd('schedule:', row_id, now + delay)
        conn.set('inv:' + row_id, json.dumps(row.to_dict())) # 缓存

# 守护进程：调整商品浏览次数排行榜
def rescale_viewed(conn):
    while not QUIT:
        conn.zremrangebyrank('viewed:', 0, -20001)
        conn.zinterstore('viewed:', {'viewed':.5})
        time.sleep(300)

# 判断页面是否需要缓存
def can_cache(conn, request):
    item_id = extract_item_id(request)
    if not item_id or is_dynamic(request):
        return False
    rank = conn.zrank('viewed:', item_id)
    return rank is not None and rank < 10000

#--------------- Below this line are helpers to test the code ----------------

def extract_item_id(request):
    parsed = parse.urlparse(request)
    query = parse.parse_qs(parsed.query)
    return (query.get('item') or [None])[0]

def is_dynamic(request):
    parsed = parse.urlparse(request)
    query = parse.parse_qs(parsed.query)
    return '_' in query

def hash_request(request):
    return str(hash(request))

class Inventory():
    def __init__(self, id):
        self.id = id

    @classmethod
    def get(cls, id):
        return Inventory(id)

    def to_dict(self):
        return {'id':self.id, 'data':'to cache...', 'cached':time.time()}

class TestCh02(unittest.TestCase):
    def setUp(self):
        import redis
        self.conn = redis.Redis(host='192.168.88.176', port=6379, db=15)

    def tearDown(self):
        conn = self.conn
        to_del = (conn.keys('login:*') + conn.keys('recent:*') + conn.keys('viewed:*') +
            conn.keys('cart:*') + conn.keys('cache:*') + conn.keys('delay:*') +
            conn.keys('schedule:*') + conn.keys('inv:*'))
        if to_del:
            self.conn.delete(*to_del)
        del self.conn
        global QUIT, LIMIT
        QUIT = False
        LIMIT = 1000000
        print()

    def test_login_cookie(self):
        conn = self.conn
        global LIMIT, QUIT
        token = str(uuid.uuid4())

        update_token(conn,token,'username','itemx')
        print('We just logged-in/updated token:', token)
        print('For user:', 'username')

        print('What username do we get when we look-up that token?')
        r = check_token(conn,token)
        print(r)
        self.assertTrue(r)

        print("Let's drop the maximum number of cookies to 0 to clean them out")
        print("We will start a thread to do the cleaning, while we stop it later")

        LIMIT = 0
        t = threading.Thread(target=clean_token, args=(conn))
        t.setDaemon(1)
        t.start()
        time.sleep(1)
        QUIT = True
        time.sleep(2)
        if t.isAlive():
            raise Exception("The clean sessions thread is still alive.")

        s = conn.hlen('login:')
        print("The current number of sessions still available is:", s)
        self.assertTrue(s)

    def test_shopping_cart_cookie(self):
        conn = self.conn
        global LIMIT, QUIT
        token = str(uuid.uuid4())

        print("We'll refresh our session...")
        update_token(conn, token, 'username', 'itemX')
        print("And add an item to the shopping cart")
        add_to_cart(conn, token, "itemY", 3)
        r = conn.hgetall('cart:' + token)
        print("Our shopping cart currently has:", r)
        print()

        self.assertTrue(len(r) >= 1)

        print("Let's clean out our sessions and carts")
        LIMIT = 0
        t = threading.Thread(target=clean_token, args=(conn))
        t.setDaemon(1) # to make sure it dies if we ctrl+C quit
        t.start()
        time.sleep(1)
        QUIT = True
        time.sleep(2)
        if t.isAlive():
            raise Exception("The clean sessions thread is still alive?!?")

        r = conn.hgetall('cart:' + token)
        print("Our shopping cart now contains:", r)

        self.assertFalse(r)

    def test_cache_request(self):
        conn = self.conn
        token = str(uuid.uuid4())

        def callback(request):
            return "content for " + request

        update_token(conn, token, 'username', 'itemX')
        url = 'http://test.com/?item=itemX'
        print("We are going to cache a simple request against", url)
        result = cache_request(conn, url, callback)
        print("We got initial content:", repr(result))
        print()

        self.assertTrue(result)

        print("To test that we've cached the request, we'll pass a bad callback")
        result2 = cache_request(conn, url, None)
        print("We ended up getting the same response!", repr(result2))

        self.assertEquals(result, result2)

        self.assertFalse(can_cache(conn, 'http://test.com/'))
        self.assertFalse(can_cache(conn, 'http://test.com/?item=itemX&_=1234536'))

    def test_cache_rows(self):
        import pprint
        conn = self.conn
        global QUIT

        print("First, let's schedule caching of itemX every 5 seconds")
        schedule_row_cache(conn, 'itemX', 5)
        print("Our schedule looks like:")
        s = conn.zrange('schedule:', 0, -1, withscores=True)
        pprint.pprint(s)
        self.assertTrue(s)

        print("We'll start a caching thread that will cache the data...")
        t = threading.Thread(target=cache_rows, args=(conn,))
        t.setDaemon(1)
        t.start()

        time.sleep(1)
        print("Our cached data looks like:")
        r = conn.get('inv:itemX')
        print(repr(r))
        self.assertTrue(r)
        print()
        print("We'll check again in 5 seconds...")
        time.sleep(5)
        print("Notice that the data has changed...")
        r2 = conn.get('inv:itemX')
        print(repr(r2))
        print()
        self.assertTrue(r2)
        self.assertTrue(r != r2)

        print("Let's force un-caching")
        schedule_row_cache(conn, 'itemX', -1)
        time.sleep(1)
        r = conn.get('inv:itemX')
        print("The cache was cleared?", not r)
        print()
        self.assertFalse(r)

        QUIT = True
        time.sleep(2)
        if t.isAlive():
            raise Exception("The database caching thread is still alive?!?")

    # We aren't going to bother with the top 10k requests are cached, as
    # we already tested it as part of the cached requests test.

if __name__ == '__main__':
    unittest.main()
