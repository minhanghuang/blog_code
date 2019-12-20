from django_filters import rest_framework
from rest_framework import filters

from app.utils.common.mixins.mixin import MyListModeMixin
from app_article import models
from app_article.views.api_core.list_article.list_article_serializer import ListArticleSerializer
from app_article.views.filter.article.list import GetArticleListFilter


class ListArticleViewSet(MyListModeMixin):
    """查看博文列表"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    queryset = models.Article.objects.all().order_by("-createdate") # 倒序
    msg_list = "查看博文列表" # 提示信息
    filter_backends = (rest_framework.DjangoFilterBackend,filters.SearchFilter,)
    filter_class = GetArticleListFilter
    search_fields = ('title', 'subtitle', 'content',)
    serializer_class = ListArticleSerializer # 序列化类
