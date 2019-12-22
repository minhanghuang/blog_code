from app.utils.common.mixins.mixin import MyCreateModeMixin
from app_user import models
from app_user.views.api.data.updata_cloudword.updata_cloudword_serializer import UpdateCloudWordSerializer


class UpdateCloudWordViewSet(MyCreateModeMixin):
    """更新云词图"""

    # authentication_classes = () # 验证
    # permission_classes = () # 权限
    msg_detail = "更新云词图" # 提示信息
    serializer_class = UpdateCloudWordSerializer # 序列化类
    queryset = models.UserData.objects.all() # models


