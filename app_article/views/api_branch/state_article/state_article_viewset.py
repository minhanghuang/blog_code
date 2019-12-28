from django_filters import rest_framework
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response

from app.utils.common.mixins.mixin import MyListModeMixin
from app_article import models
from app_article.views.api_branch.state_article.state_article_serializer import GetStateArticleSerializer
from app_article.views.filter.article.list import GetArticleListFilter


class GetStateArticleViewSet(MyListModeMixin):
    """获取文章状态数量"""

    # authentication_classes = ()  # 验证
    # permission_classes = ()  # 权限
    queryset = models.Article.objects.all().order_by("-createdate") # 倒序
    msg_list = "获取文章状态数量1" # 提示信息
    filter_backends = (rest_framework.DjangoFilterBackend,filters.SearchFilter,)
    filter_class = GetArticleListFilter
    search_fields = ('title', 'subtitle', 'content',)
    serializer_class = GetStateArticleSerializer # 序列化类


    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        results_dict = {}
        results_dict["all"] = len(queryset)
        results_dict["public"] = len(queryset.filter(state=1))
        results_dict["private"] = len(queryset.filter(state=2))
        results_dict["draft"] = len(queryset.filter(state=0))
        results_dict["del"] = len(queryset.filter(state=3))

        return Response({
            "success": True,
            "msg": self.msg_list,
            "results": results_dict
        }, status=status.HTTP_200_OK)
