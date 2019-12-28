from app.utils.common.mixins.mixin import MyUpdateModelMixin
from app_user import models
from app_user.views.api.data.reset_data.reset_cloudword.reset_cloudword_serializer import ResetCloudWordSerializer


class ResetCloudWordViewSet(MyUpdateModelMixin):
    """重置云词图"""

    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_update = "重置云词图" # 提示信息
    serializer_class = ResetCloudWordSerializer # 序列化类
    queryset = models.UserData.objects.all() # models
    lookup_field = "user__username" # 用户名


