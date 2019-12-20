from redis import Redis
from blog_code.config import myconfig
from django_redis import get_redis_connection
import os,django


class MyRedisConf(Redis):

    def __init__(self, **kwargs):

        Redis.__init__(self, **kwargs)
        self.django_redis_conn = get_redis_connection("default")
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

    def redis_flushall(self):
        """
        清空redis所有数据
        :return: None
        """
        self.django_redis_conn.flushall()
        return None







my_redis = MyRedisConf(**myconfig.get_redis_config())


if __name__ == "__main__":
    """"""

    print(my_redis.hset("db","kk3","vv3"))
    print(my_redis.hset("db","kk4","vv4"))
    print(my_redis.redis_flushall())
    # my_redis.hash_del("db","key1","key2","key3")