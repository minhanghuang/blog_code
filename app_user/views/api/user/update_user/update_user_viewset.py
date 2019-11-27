from utils.common.mixins.mixin import MyUpdateModelMixin
from app_user.views.api.user.update_user.update_user_serializer import UpdateUserSerializer
from app_user import models





class UpdateUserViewSet(MyUpdateModelMixin):
    """更新用户详细信息"""

    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_detail = "更新用户详细信息" # 提示信息
    serializer_class = UpdateUserSerializer # 序列化类
    queryset = models.UserProfile.objects.all() # models
    lookup_field = "username" # 用户名
