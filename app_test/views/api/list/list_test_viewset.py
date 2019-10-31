from utils.common.mixins.mixin import MyListModeMixin
from app_test.views.api.list.list_test_serializer import ListTestSerializer
from app_test import models





class ListTestViewSet(MyListModeMixin):
    """查看Test列表"""

    authentication_classes = () # 验证
    permission_classes = () # 权限
    msg_list = "成功查看Test列表" # 提示信息
    serializer_class = ListTestSerializer # 序列化类
    queryset = models.TestModel.objects.all() # models
