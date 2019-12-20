from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from app.utils.common.mixins.mixin import MyCreateModeMixin
from app_user.views.api.user.create_user.create_user_serializer import CreateUserSerializer


class CreateUserViewSet(MyCreateModeMixin):
    """新增用户"""

    authentication_classes = (JSONWebTokenAuthentication,)  # 验证
    permission_classes = (permissions.IsAuthenticated,)  # 权限
    msg_create = "成功新增用户" # 提示信息
    results_display = False  # 是否显示序列化信息, 默认显示
    serializer_class = CreateUserSerializer # 序列化类
