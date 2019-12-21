from app.utils.common.mixins.mixin import MyAPIView
from rest_framework.response import Response
from rest_framework import status
from app_article import models
from app_user.models import UserData
from app.utils.common.cacheredis.cacheredis import my_redis

class InitApiView(MyAPIView):
    """系统初始化"""

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限
    msg_api = "系统初始化成功"

    def post(self, request):
        """
        该接口只能调用一次, 调用后上锁
        :param request:
        :return:
        """
        if self.get_lock():
            return Response({
                "success": False,
                "msg": "来晚了,兄弟",
                "results": ""
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.set_lock()

        return Response({
            "success": True,
            "msg": self.msg_api,
            "results": ""
        }, status=status.HTTP_200_OK)

    def get_lock(self):
        """
        获取锁,获取成功,可以使用该接口,否则禁止使用
        :return: bool
        """
        value = my_redis.str_get("init_system")

        return value

    def set_lock(self):
        """
        上锁
        :return: None
        """

        my_redis.str_set("init_system", "1")
        return None


    def init_user(self):
        """
        初始化用户
        新增两个用户, 一个是超级管理员, 一个是游客
        :return: None
        """



        return None
