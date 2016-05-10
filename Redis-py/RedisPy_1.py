import redis

r = redis.StrictRedis(host='192.168.88.176', port=6379, db=0)

ret = r.set('foo', 'bar')   # true

res = r.get('foo')

print(ret)
print(res)
