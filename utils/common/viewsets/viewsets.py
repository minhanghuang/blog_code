from rest_framework.viewsets import GenericViewSet
from utils.common.serializers.serializer import SerializerPlug
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from utils.common.exceptions import exception
from user_app import models
from jsonschema import validate


class MyGenericViewSet(GenericViewSet,SerializerPlug):


    def get_user_obj(self,username=None):
        """
        获取当前用户对象,如果username为空,调用基类方法;如果传入username,从数据库获取
        此函数没有进行username校验
        :param username: 用户名
        :return: 用户obj
        """
        if not username:
            user = self.get_object()
        else:
            user = models.UserProfile.objects.get(username=username)

        return user

    def create_token(self,user):
        """
        生成token
        :param user: 用户obj
        :return: token
        """
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return token

    def check_username(self,*args,**kwargs):
        """
        校验用户账号密码
        :param args:
        :param kwargs:
        :return: None
        """
        user = authenticate(username=kwargs["username"], password=kwargs["password"])
        if not user:
            raise exception.myException400({
                "success": False,
                "msg": "用户名密码不正确"
            })
        return None