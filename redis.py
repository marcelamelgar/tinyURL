import redis 

client = redis.StrictRedis(host = 'localhost', port = 6379, db = 0)

client.hset("url", "www.google.com", "www.xyz")