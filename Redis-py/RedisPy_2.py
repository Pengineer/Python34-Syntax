import redis
import time

'''
需求：实现对文章进行投票并排序
key='article:id'的散列存储：存储文章信息                  title -> 简爱
key='time:'的有序集合：存储文章和文章发布时间的键值对。   article:10048 -> 1332065417.17
key='score:'的有序集合：存储文章和文章得分。              article:10048 -> 1332065689.36
key='voted:id'的集合：存储每篇文章的所有投票者。          user:23448
'''

conn = redis.StrictRedis(host='192.168.88.176', port=6379, db=0)

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432
'''
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
