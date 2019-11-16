from utils.common.mixins.mixin import MyUpdateModelMixin
from app_article.views.api_core.update_article.update_article_serializer import UpdateArticleSerializer
from app_article import models





class UpdateArticleViewSet(MyUpdateModelMixin):
    """更新博文"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    msg_update = "保存成功" # 提示信息
    queryset = models.Article.objects.all()
    results_display = True  # 是否显示序列化信息, 默认显示
    serializer_class = UpdateArticleSerializer # 序列化类
