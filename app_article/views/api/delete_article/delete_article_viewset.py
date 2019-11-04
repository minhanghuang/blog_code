from utils.common.mixins.mixin import MyDeleteModelMixin
from app_article.views.api.delete_article.delete_article_serializer import DeleteArticleSerializer
from app_article import models








class DeleteArticleViewSet(MyDeleteModelMixin):
    """删除博文"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    queryset = models.Article.objects.all() #
    msg_delete = "成功删除博文" # 提示信息
    serializer_class = DeleteArticleSerializer # 序列化类
