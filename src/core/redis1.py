from redis import StrictRedis


redis_client = StrictRedis(host='localhost', port=6379, db=0)
redis_pipe = redis_client.pipeline(transaction=False)


redis_client1 = StrictRedis(host='localhost', port=6379, db=1)
redis_pipe1 = redis_client1.pipeline(transaction=False)
