import redis
rd = redis.Redis(host="redis", port=6379)
rd.ping()

print('connected to redis "{}"'.format("redis"))
