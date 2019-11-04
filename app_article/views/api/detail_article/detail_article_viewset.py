from utils.common.mixins.mixin import MyRetrieveModelMixin
from app_article.views.api.detail_article.detail_article_serializer import DetailArticleSerializer
from app_article import models








class DetailArticleViewSet(MyRetrieveModelMixin):
    """查看博文详细"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    queryset = models.Article.objects.all() #
    msg_detail = "查看博文详细" # 提示信息
    serializer_class = DetailArticleSerializer # 序列化类
