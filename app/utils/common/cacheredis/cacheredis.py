from redis import Redis
from blog_code.config import myconfig


class MyRedisConf(Redis):

    def __init__(self, **kwargs):

        Redis.__init__(self, **kwargs)
        # self.default_dbname = "db"

    def get(self, name):
        """
        重写get()方法,因为Redis类中的get()返回的是二进制数据,我需要的是str类型的数据
        :param name: 键
        :return: 值(str)
        """
        value = self.execute_command('GET', name)

        if not value:
            return None

        return str(value, encoding="utf8")


    # String Commands 二次封装
    def str_set(self, key, value, ex=None, px=None, nx=False, xx=False):
        """
        字符串 设置
        :param key: 键名
        :param value: 数值
        :param ex: 生命周期,默认永久 单位:seconds
        :param px: 生命周期,默认永久 单位:milliseconds
        :param nx: nx=True时,仅仅当key不存在时,才会set,如果key存在,不会覆盖原来的数据
        :param xx: xx=True时,与nx相反,仅仅当key存在时,才会覆盖,如果key不存在,不会set
        :return:
        """

        return self.set(key, value, ex=None, px=None, nx=False, xx=False)

    def str_get(self, key):
        """
        字符串 获取数据
        :param key: 键名
        :return: value
        """
        return self.get(key)

    def str_ttl(self, key):
        """
        字符串 获取某个键的生命周期
        :param key: 键名
        :return: 返回剩余的时间 / 0代表已经过期 / None 代表没有设置过期时间
        """
        return self.ttl(key)

    def str_delete(self, *names):
        """
        字符串 删除数据
        :param names: 键名 (可接受多个参数,用逗号隔开)
        :return: 返回删除的数量
        """
        return self.delete(self, *names)

    def str_keys(self, pattern='*'):
        """
        字符串 查询 / 模糊搜索
        .str_keys("key") 搜索键名为"key"的数据; .str_keys("key*") 搜索键名为"key"开头的数据;
        :param pattern: 模式匹配
        :return: 搜索结果
        """
        return self.keys(pattern='*')


    # HASH COMMANDS 二次封装
    def hash_set(self, name="db", key="", value="" ):
        """
        哈希设置
        .hash_set("db","key","value")
        :param name: 默认设置在名字叫db的字段里面
        :param key: 键名
        :param value: 数据
        :return: Returns 1 if HSET created a new field, otherwise 0
        """

        return self.hset(name=name, key=key, value=value)

    def hash_del(self, name="db", *keys):
        """
        哈希删除
        .hash_del("db","key1","key2","key3")
        :param name: 默认删除名字叫db里面数据
        :param keys: 字段s
        :return:
        """
        return self.hdel(name, *keys)

    def hash_get(self, name="db", key=""):
        """
        哈希获取数据
        :param name: 数据库名
        :param key: 键名
        :return: value
        """
        return self.hget(name=name, key=key)

    def hash_exists(self, name="db", key=""):
        """
        哈希查看某个键名是否存在
        :param name: 数据库名
        :param key: 键名
        :return: boolean
        """
        return self.hexists(name=name, key=key)

    def hash_getall(self, name="db"):
        """
        哈希获取对应数据库名的所有键值对
        :param name: 数据库名
        :return: dict
        """

        return self.hgetall(name=name)

    def hash_keys(self, name="db"):
        """
        哈希获取对应数据库名的所有键
        :param name: 数据库名
        :return: list
        """

        return self.hkeys(name=name)

    def redis_flushall(self,asynchronous=False):
        """
        清空redis所有数据
        :param asynchronous: 是否异步,默认否
        :return: None
        """

        return self.flushall(asynchronous=asynchronous)

    def redis_flushdb(self, asynchronous=False):
        """
        删除当前数据库的所有数据
        :param asynchronous: 是否异步,默认否
        :return:
        """
        return self.flushdb(asynchronous=asynchronous)

    def redis_zincrby(self, name, amount, key):
        """
        设置热词
        .redis_zincrby("weibo",10,"username") # 在weibo这个大类下,对username设置权重10, 也就是每调用一次,username自增10
        查看统计请使用.redis_zrevrange()函数
        在name的类型下,对字段key设置权重amount
        :param name: 热词类型
        :param amount: 权重
        :param key: 字段
        :return:
        """
        return self.zincrby(name=name, amount=amount, value=key)


    def redis_zrevrange(self, name, start, end, withscores=False,score_cast_func=float):
        """
        统计热词
        .redis_zrevrange("weibo",1,10,True) # 列出weibo这个大类中,从第1名到第10名的数据,结果根据权重排序
        :param name: 热词类型
        :param start: 起始点 (从第n名开始统计)
        :param end: 终止点 (从第m名结束统计)
        :param withscores: 是否据权重值排序
        :param score_cast_func:  权重数据类型 默认float
        :return: 当withscores=False时(不根据权重值排序)->list; 当withscores=True时(根据权重值排序)->list(tuple) 元组嵌套在列表里面;
        """

        return self.zrevrange(name, start, end, withscores=withscores,score_cast_func=score_cast_func)

my_redis = MyRedisConf(**myconfig.get_redis_config())


if __name__ == "__main__":
    """"""
    # my_redis.redis_zincrby("kk",1,"1")
    # my_redis.redis_zincrby("kk",1,"1")
    # my_redis.redis_zincrby("kk",1,"1")
    # my_redis.redis_zincrby("kk",2,"2")
    # my_redis.redis_zincrby("kk",2,"2")
    # my_redis.redis_zincrby("kk",2,"2")
    # my_redis.redis_zincrby("kk",2,"2")
    # print(my_redis.redis_zrevrange("kk",0,10,True))
    # print(my_redis.redis_zrevrange("kk",0,10))
    # # my_redis.flushall()

    my_redis.set()

