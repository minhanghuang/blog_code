from rest_framework.response import Response
from rest_framework import status
from utils.common.mixins.mixin import MyCreateModeMixin
from app_user.views.api.login.login_serializer import LoginUserSerializer
from app_user import models

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

        self.check_auth_base(
            username=username,
            password=password,
        ) # 校验用户名和密码

        instance = self.get_object_base(
            model=models.UserProfile.objects.all(),
            field=username,
        ) # 获取对象

        token = self.create_token_base(user=instance) # 生成 TOKEN

        return Response({
            "success": True,
            "msg": self.msg_create,
            "results": {
                "TOKEN":token,
            }
        }, status=status.HTTP_200_OK)