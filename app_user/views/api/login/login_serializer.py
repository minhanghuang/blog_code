from rest_framework import serializers
from app_user import models
from utils.common.serializers.serializer import MySerializerBase




class LoginUserSerializer(MySerializerBase):
    """用户登录-序列化"""

    username = serializers.CharField(
        label="用户名",
        help_text="用户名",
        required=True,
        allow_null=False,
        allow_blank=False,
        error_messages=MySerializerBase.field_error_msg(field="用户名")
    )
    password = serializers.CharField(
        label="密码",
        help_text="密码",
        required=True,
        allow_null=False,
        allow_blank=False,
        error_messages=MySerializerBase.field_error_msg(field="密码")
    )

    class Meta:
        model = models.UserProfile
        fields = ["username","password",]





