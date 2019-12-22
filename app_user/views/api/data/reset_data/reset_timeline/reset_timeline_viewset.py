from app.utils.common.mixins.mixin import MyUpdateModelMixin
from app_user import models
from app_user.views.api.data.reset_data.reset_timeline.reset_timeline_serializer import ResetTimeLineSerializer


class ResetTimeLineViewSet(MyUpdateModelMixin):
    """重置时光轴"""

    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_update = "重置时光轴" # 提示信息
    serializer_class = ResetTimeLineSerializer # 序列化类
    queryset = models.UserData.objects.all() # models
    lookup_field = "user__username" # 用户名


