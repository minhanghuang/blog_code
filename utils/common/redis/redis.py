from django.core.cache import cache



class MyRedisConf(object):


    def set_redis(self, key, value, cycle):

        cache.set()


        return