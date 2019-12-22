from rest_framework import serializers
from app.utils.common.serializers.serializer import MySerializerBase
from app_user import models
from blog_code.config import myconfig





class ResetTimeLineSerializer(MySerializerBase):
    """重置时光轴-序列化"""

    class Meta:
        model = models.UserData
        fields = ["timeline",]

    def update(self, instance, validated_data):

        username = instance.user.username # 用户名

        cache_data_field = myconfig.get_sysinit_data()["cache"]["field"]["init"][username] # 获取指标文件cache缓存字段

        value = self.get_init_cache_data(cache_data_field) # 获取缓存的数据

        instance.timeline = value.get("timeline") # 保存到数据库
        instance.save()

        return instance







