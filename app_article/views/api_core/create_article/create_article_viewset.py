from rest_framework import permissions
from app.utils.common.mixins.mixin import MyCreateModeMixin
from app_article.views.api_core.create_article.create_article_serializer import CreateArticleSerializer
from app.utils.common.mypermissions import mypermission






class CreateArticleViewSet(MyCreateModeMixin):
    """新增博文"""

    # authentication_classes = ()  # 验证
    permission_classes = (mypermission.IsMyAdminUser,)  # 权限, 只允许自定义的管理员通过
    msg_create = "成功新增博文" # 提示信息
    results_display = True  # 是否显示序列化信息, 默认显示
    serializer_class = CreateArticleSerializer # 序列化类
