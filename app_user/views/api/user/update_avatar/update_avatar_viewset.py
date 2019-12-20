from app.utils.common.mixins.mixin import MyCreateModeMixin
from app_user import models
from app_user.views.api.user.update_avatar.update_avatar_serializer import UpdateAvatarSerializer


class UpdateAvatarViewSet(MyCreateModeMixin):
    """更新用户头像"""

    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_detail = "更新用户头像" # 提示信息
    serializer_class = UpdateAvatarSerializer # 序列化类
    queryset = models.UserProfile.objects.all() # models
    lookup_field = "username"  # 主键

