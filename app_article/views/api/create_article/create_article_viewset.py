from utils.common.mixins.mixin import MyCreateModeMixin
from app_article.views.api.create_article.create_article_serializer import CreateArticleSerializer






class CreateArticleViewSet(MyCreateModeMixin):
    """新增博文"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    msg_create = "成功新增博文" # 提示信息
    # results_display = False  # 是否显示序列化信息, 默认显示
    serializer_class = CreateArticleSerializer # 序列化类
