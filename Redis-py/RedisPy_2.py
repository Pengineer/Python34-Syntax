
import time
import unittest

'''
需求：实现对文章进行投票并排序
key='article:id'的散列存储：存储文章信息                  title -> 简爱
key='time:'的有序集合：存储文章和文章发布时间的键值对。   article:10048 -> 1332065417.17
key='score:'的有序集合：存储文章和文章得分。              article:10048 -> 1332065689.36
key='voted:id'的集合：存储每篇文章的所有投票者。          user:23448
key='group:name'的集合：存储分组里面的文章，每个分组都是一个独立的key

key=id_generator 记录id最大值
'''

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432

'''
投票
article参数形式 article:id
user参数形式    user:id
'''
def article_vote(conn, user, article):
    cutoff = time.time() - ONE_WEEK_IN_SECONDS  # 当前时间回退一周
    if conn.zscore('time:', article) < cutoff:  # zscore(key, member)，从'time:'集合中取出member为article的score
        return
    article_id = article.partition(':')[-1]
    if conn.sadd('voted:' + article_id, user):      # 给voted:article集合增加一个投票者
        conn.zincrby('score:', article, VOTE_SCORE) # 将'score:'集合中的member为article的分数增加
        conn.hincrby(article, 'votes', 1)       # 将散列中article的投票数字段+1

'''
文章发布
'''
def post_article(conn, user, title, link):
    article_id = str(conn.incr('article:'))

    voted = 'voted:' + article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)      # 设置一个key的过期时间，时间到后，自动被Redis清除

    now = time.time()
    article = 'article:' + article_id
    conn.hmset(article, {
        'title':title,
        'link':link,
        'poster':user,
        'time':now,
        'votes':1,
    })

    conn.zadd('score:', article, now + VOTE_SCORE) # 给文章设置初始分数
    conn.zadd('time:', article, now)
    return article_id

'''
文章获取
'''
ARTICLES_PER_PAGE = 25
def get_articles(conn, page, order='score:'):
    start = (page - 1) * ARTICLES_PER_PAGE
    end = start + ARTICLES_PER_PAGE -1

    ids = conn.zrevrange(order, start, end)    # zrevrange()会根据分值大小排序并仅返回member
    articles = []
    for id in ids:
        article_data = conn.hgetall(id)        # 根据文章id获取文章详细信息
        article_data['id'] = id                # 添加一个id键值对
        articles.append(article_data)
    return articles

'''
文章分组
'''
def add_remove_groups(conn, article_id, to_all=[], to_remove=[]):
    article = 'article:' + article_id
    for group in to_all:
        conn.sadd('group:' + group, article)
    for group in to_remove:
        conn.srem('group:' + group, article)

'''
从群组中获取文章
zinterstore命令是对集合做交集，格式如下：
    ZINTERSTORE destination numkeys key [key ...] [WEIGHTS weight [weight ...]] [AGGREGATE SUM|MIN|MAX]
destination表示输出的有序集合；
numkeys表示后面跟着的列表中集合的个数；
[key ...]表示做交集的所有源集合；
weight表示对应的各源集合中score的权重；
aggregate表示集合聚集的方式：sum是将源集合中公共元素的score乘以各自的权重后相加；min是将源集合中公共元素的score乘以各自的权重后取最小的...
'''
def get_group_article(conn, group, page, order='score:'):
    key = order + group
    if not conn.exists(key):
        conn.zinterstore(key, ['group:' + group, order], aggregate='max',) # 集合和有序集合做交集，集合的所有成员的分值都被视为1
        conn.expire(key, 60)
    return get_articles(conn, page, key)

'''
单元测试
'''
class TestCh01(unittest.TestCase):
    # 初始化
    def setUp(self):
        import redis
        self.conn = redis.Redis(host='192.168.88.176', port=6379, db=15)

    # 退出清理工作
    def tearDown(self):
        del self.conn
        print()
        print()

    # 具体的测试用例，一定要以test开头
    def test_article_functionality(self):
        conn = self.conn
        import pprint
        article_id = str(post_article(conn, 'user:001', 'Game Of Thrones', 'www.gof.com'))
        print('发布新Id：' + article_id)
        self.assertTrue(article_id)

        r = conn.hgetall('article:' + article_id)
        # print(r)
        for k, v in r.items():
            print(k, ":", v)
        self.assertTrue(r)

        article_vote(conn, 'user:002', 'article:' + article_id)
        v = int(conn.hget('article:' + article_id, 'votes'))
        print('投票数：', v)
        self.assertTrue(v>1)

        articles = get_articles(conn, 1)
        pprint.pprint(articles)
        print()

        print('获取分组文章：')
        add_remove_groups(conn, article_id, ['new-group'])
        articles = get_group_article(conn, 'new-group', 1)
        pprint.pprint(articles)
        self.assertTrue(len(articles) >= 1)

        # 清除测试产生的所有key
        to_del = (conn.keys('time:*') + conn.keys('voted:*') + conn.keys('score:*') +
                  conn.keys('article:*') + conn.keys('group:*')
            )
        if to_del:
            conn.delete(*to_del)

if __name__ == '__main__':
    unittest.main()
