from app.utils.common.mixins.mixin import MyUpdateModelMixin
from app_user import models
from app_user.views.api.data.reset_data.reset_data.reset_data_serializer import ResetDataSerializer


class ResetDataViewSet(MyUpdateModelMixin):
    """重置个人中心"""

    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_update = "重置个人中心" # 提示信息
    serializer_class = ResetDataSerializer # 序列化类
    queryset = models.UserProfile.objects.all() # models
    lookup_field = "username" # 用户名


