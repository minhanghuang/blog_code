from app.utils.common.mixins.mixin import MyRetrieveModelMixin
from app_user import models
from app_user.views.api.user.detail_user.detail_user_serializer import DetailUserSerializer


class DetailUserViewSet(MyRetrieveModelMixin):
    """查看用户详细信息"""

    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_detail = "查看用户详细信息" # 提示信息
    serializer_class = DetailUserSerializer # 序列化类
    queryset = models.UserProfile.objects.all() # models
    lookup_field = "username" # 用户名

