"""
基本单元,
"""
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from django.shortcuts import get_object_or_404
from utils.common.exceptions import exception
from rest_framework import status
from rest_framework.response import Response

class MyUnitBase(object):
    """基本单元类"""

    throttle_scope = 'throttle_base_30_Min' # 节流

    def __init__(self):

        pass

    def validation_error(self, serializer):
        """
        自定义序列化捕获异常函数
        :param serializer: 序列化后的对象
        :return: None
        """
        try:
            ret = serializer.is_valid(raise_exception=True) # 捕获异常
        except Exception as e:
            print("序列化异常处理函数,e:{}".format(e))
            dict_exception = e.__dict__.get("detail","")
            if "success" in dict_exception:
                self.msg_error = dict_exception["msg"]
            else:
                for i, v in dict_exception.items():
                    self.msg_detail = i
                    self.msg_error = v[0]
                    break # 只获取第一个异常结果
            raise exception.myException400({
                "success": False,
                "msg": "{}".format(self.msg_error), # 异常消息
                "results":{
                    "field":self.msg_detail, # 具体异常的字段
                    "detail":self.msg_error, # 异常消息
                }
            })
        return None

    def get_object_base(self, model, field):
        """
        获取对象
        :param field: 字段
        :param model: 模型
        :return: instance
        """

        try:
            instance = get_object_or_404(model, username=field)

        except:
            raise exception.myException400({
                "success": False,
                "msg": "获取instance异常",
                "results": ""
            })

        return instance

    def check_auth_base(self, username, password):
        """
        校验用户名和密码是否匹配
        :param username: 用户名
        :param password: 密码
        :return: bool
        """
        user = authenticate(username=username, password=password)
        if not user:
            raise exception.myException400({
                "success": False,
                "msg": "账号密码不匹配",
                "results": None,
            })

        return True

    def create_token_base(self, user):
        """
        生成token
        :param user: 用户对象
        :return: TOKEN
        """
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return token

    def intercept_visitor_request(self, request):

        action = self.action
        username = request.user.username
        print("action:",action)
        print("action:",request.user.username)
        if action in ["create","destroy","update"] and username == "coco": # retrieve list
            raise exception.myException403({
                "success": False,
                "msg": "游客暂无权限",
                "results": "",
            })

        return None

