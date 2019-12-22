from rest_framework import serializers
from app.utils.common.serializers.serializer import MySerializerBase
from app_user import models
from blog_code.config import myconfig





class ResetCloudWordSerializer(MySerializerBase):
    """重置云词图-序列化"""

    cloudword = serializers.SerializerMethodField(
        label="图片",
        required=False,
        allow_null=True,
    )
    cloudword_width = serializers.SerializerMethodField(
        label="返回图片大小",
        required=False,
        allow_null=True,
    )
    circle = serializers.CharField(
        label="图片形状(True:圆形,False:正方形)",
        required=False,
        allow_null=True,
        default=True,
    )
    tag = serializers.CharField(
        label="标签",
        required=False,
        allow_null=True,
    )
    width = serializers.IntegerField(
        label="图片大小",
        required=False,
        allow_null=True,
    )
    color = serializers.CharField(
        label="背景颜色",
        required=False,
        allow_null=True,
    )
    full = serializers.CharField(
        label="是否填充",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = models.UserData
        fields = ["cloudword","circle","tag","width","color","full","cloudword_width"]

    def get_cloudword(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.cloudword

    def get_cloudword_width(self,obj):

        return obj.cloudword_width


    def update(self, instance, validated_data):

        username = instance.user.username # 用户名

        cache_data_field = myconfig.get_sysinit_data()["cache"]["field"]["init"][username] # 获取指标文件cache缓存字段

        value = self.get_init_cache_data(cache_data_field) # 获取缓存的数据

        instance.cloudword = value.get("cloudword", "")  # 赋值 云词图base64
        instance.cloudword_width = value.get("cloudword_width", "400")  # 赋值 云词图 宽度
        instance.tag = value.get("tag", '["Python"]')  # 赋值 标签
        instance.save()

        return instance







