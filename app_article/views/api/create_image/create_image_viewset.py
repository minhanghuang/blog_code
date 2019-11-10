from utils.common.mixins.mixin import MyCreateModeMixin
from app_article.views.api.create_image.create_image_serializer import CreateImageSerializer






class CreateImageViewSet(MyCreateModeMixin):
    """新增图片"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    msg_create = "成功上传图片" # 提示信息
    results_display = True  # 是否显示序列化信息, 默认显示
    serializer_class = CreateImageSerializer # 序列化类
