from user_app import models
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from utils.common.serializers.serializer import error_instance


class LoginSerializerCls(DynamicFieldsMixin,serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        error_messages=error_instance.field_errormsg(field="用户名")
    )
    password = serializers.CharField(
        required=True,
        error_messages=error_instance.field_errormsg(field="密码")
    )
    class Meta:
        model = models.UserProfile
        fields = ["username","password",]
        # extra_kwargs = {
        #     'username': {'allow_null': True},
        #     'password': {'allow_null': True},
        # }

    def validate_username(self, username):
        """自定义校验username"""
        return username

    def validate(self, arrt):
        """自定义校验所有字段"""

        return arrt


