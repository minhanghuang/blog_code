from rest_framework import serializers

from app.utils.common.serializers.serializer import MySerializerBase
from app_user import models


class DetailUserSerializerBlog(MySerializerBase):
    """查看用户详细信息_客户端-序列化"""

    avatar = serializers.SerializerMethodField(
        label="头像base64",
        required=False,
        allow_null=True,
    )
    class Meta:
        model = models.UserProfile
        fields = ["name","email","description","company","department","position","city","tag","avatar","wechat","telegram","phone"]

    def get_avatar(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.avatar






