from utils.common.mixins.mixin import MyListModeMixin
from app_user.views.api.user.list_user.list_user_serializer import ListUserSerializer
from app_user import models





class ListUserViewSet(MyListModeMixin):
    """查看用户列表"""

    authentication_classes = () # 验证
    permission_classes = () # 权限
    msg_list = "成功查看用户列表" # 提示信息
    serializer_class = ListUserSerializer # 序列化类
    queryset = models.UserProfile.objects.all() # models
