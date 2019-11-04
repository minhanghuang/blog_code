from utils.common.mixins.mixin import MyListModeMixin
from app_article.views.api.list_article.list_article_serializer import ListArticleSerializer
from app_article import models








class ListArticleViewSet(MyListModeMixin):
    """查看博文列表"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    queryset = models.Article.objects.all() #
    msg_list = "查看博文列表" # 提示信息
    serializer_class = ListArticleSerializer # 序列化类
