from utils.common.mixins.mixin import MyCreateModeMixin
from app_article.views.api_core.update_image.update_image_serializer import UpdateImageSerializer






class UpdateImageViewSet(MyCreateModeMixin):
    """更新图片"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    msg_create = "保存成功" # 提示信息
    results_display = True  # 是否显示序列化信息, 默认显示
    serializer_class = UpdateImageSerializer # 序列化类
