from redis import Redis
from django.conf import settings
from blog_code.config import myconfig


class MyRedisConf(Redis):

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


my_redis = MyRedisConf(**myconfig.get_redis_config())


if __name__ == "__main__":

    print(my_redis.set("kk","vv"))