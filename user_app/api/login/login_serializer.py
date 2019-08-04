from user_app import models
from rest_framework import serializers
from utils.common.serializers.serializer import error_instance
from django.contrib.auth import authenticate
from utils.common.exceptions import exception
from utils.common.serializers.serializer import MySerializerBase


class LoginSerializerCls(MySerializerBase):
    username = serializers.CharField(
        label="用户名",
        help_text="用户名",
        required=True,
        error_messages=error_instance.field_errormsg(field="用户名")
    )
    password = serializers.CharField(
        label="密码",
        help_text="密码",
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
        user = authenticate(username=arrt["username"], password=arrt["password"])
        if not user:
            raise exception.myException400({
                "success": False,
                "msg": "用户名密码不正确"
            })
        return arrt


