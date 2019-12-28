from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from app.utils.common.mixins.mixin import MyCreateModeMixin
from app_user import models
from app_user.views.api.login.login_serializer import LoginUserSerializer


class LoginUserViewSet(MyCreateModeMixin):
    """用户登录"""

    authentication_classes = () # 验证
    permission_classes = () # 权限
    msg_create = "成功登录" # 提示信息
    results_display = False  # 是否显示序列化信息, 默认显示
    serializer_class = LoginUserSerializer # 序列化类
    throttle_scope = 'login_throttle' # 节流

    def create(self, request, *args, **kwargs):

        username = request.data.get("username", "")
        password = request.data.get("password", "")


        ret = self.is_tourists_login(username, password) # 校验登录用户
        print("ret:",ret)
        if ret["success"]: # 用户名密码不对 -> 必定是游客
            return Response({
                "success": True,
                "msg": self.msg_create,
                "results": {
                    "TOKEN": ret["results"]["TOKEN"],
                    "username": "coco",
                }
            }, status=status.HTTP_200_OK)

        # 用户名密码正确 -> admin or coco
        # self.check_auth_base(
        #     username=username,
        #     password=password,
        # ) # 校验用户名和密码

        instance = self.get_object_base( # 获取对象
            model=models.UserProfile.objects.all(),
            field=username,
        )

        token = self.create_token_base(user=instance) # 生成 TOKEN

        return Response({
            "success": True,
            "msg": self.msg_create,
            "results": {
                "TOKEN":token,
                "username":username,
            }
        }, status=status.HTTP_200_OK)


    def is_tourists_login(self, username, password):
        """

        :param username:
        :param password:
        :return:
        """

        user = authenticate(username=username, password=password) # 验证用户密码
        if user: # admin or coco
            return {
                "success":False,
                "msg":"admin",
                "results":{
                    "TOKEN": "",
                    "username": "coco",
                }
            }
        # 用户名密码不匹配 -> 分配游客账号coco
        instance = self.get_object_base( # 获取coco对象
            model=models.UserProfile.objects.all(),
            field="coco",
        )  # 获取对象
        token = self.create_token_base(user=instance) # 生成 TOKEN

        return {
                "success":True,
                "msg":"coco",
                "results":{
                    "TOKEN": token,
                    "username": "coco",
                }
            }