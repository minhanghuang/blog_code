from app.utils.common.mixins.mixin import MyUpdateModelMixin
from app_article import models
from app_article.views.api_core.delete_article.delete_article_serializer import DeleteArticleSerializer


class DeleteArticleViewSet(MyUpdateModelMixin):
    """删除博文"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    queryset = models.Article.objects.all() #
    msg_delete = "成功删除博文" # 提示信息
    serializer_class = DeleteArticleSerializer # 序列化类
