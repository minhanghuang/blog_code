from rest_framework import serializers
from app.utils.common.serializers.serializer import MySerializerBase
from app_user import models
from blog_code.config import myconfig





class ResetDataSerializer(MySerializerBase):
    """重置个人中心-序列化"""

    avatar = serializers.SerializerMethodField(
        label="图片路径",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = models.UserProfile
        fields = ["name", "email", "description", "company", "department", "position", "city", "tag", "avatar", "wechat"]
        extra_kwargs = {
            'avatar': {
                'allow_null': True,
                'allow_blank': True,
                'required': False,
            },
        }

    def get_avatar(self, obj):
        return 'data:image/jpeg;base64,%s' % obj.avatar


    def update(self, instance, validated_data):

        username = instance.username # 用户名

        cache_data_field = myconfig.get_sysinit_data()["cache"]["field"]["init"][username] # 获取指标文件cache缓存字段

        value = self.get_init_cache_data(cache_data_field) # 获取缓存的数据

        instance.name = value.get("name")
        instance.wechat = value.get("wechat")
        instance.description = value.get("description")
        instance.email = value.get("email")
        instance.company = value.get("company")
        instance.department = value.get("department")
        instance.position = value.get("position")
        instance.city = value.get("city")
        instance.tag = value.get("tag")
        instance.avatar = value.get("avatar")
        instance.save()

        return instance







