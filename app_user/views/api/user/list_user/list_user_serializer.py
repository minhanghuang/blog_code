from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase




class ListUserSerializer(MySerializerBase):
    """查看用户列表-序列化"""

    role = serializers.CharField(source="get_role_display",)

    class Meta:
        model = models.UserProfile
        fields = ["username","role",]






