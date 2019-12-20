from app.utils.common.mixins.mixin import MyRetrieveModelMixin
from app_user import models
from app_user.views.api.data.detail_data.detail_data_serializer import DetailDataSerializer


class DetailDataViewSet(MyRetrieveModelMixin):
    """查看data详细信息"""

    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_detail = "查看data详细信息" # 提示信息
    serializer_class = DetailDataSerializer # 序列化类
    queryset = models.UserData.objects.all() # models
    lookup_field = "pk"  # 主键


