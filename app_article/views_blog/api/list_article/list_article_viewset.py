from app.utils.common.mixins.mixin import MyListModeMixin
from app_article import models
from app_article.views_blog.api.list_article.list_article_serializer import ListArticleSerializerBlog
from app_article.views_blog.utils.pages.page import MyArticlePagination


class ListArticleViewSetBlog(MyListModeMixin):
    """查看博文列表_客户端"""

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限
    pagination_class = MyArticlePagination # 自定义分页, 与admin分页size不同
    queryset = models.Article.objects.all().filter(state=1).order_by("-createdate") # 公开+倒序
    msg_list = "查看博文列表_客户端" # 提示信息
    serializer_class = ListArticleSerializerBlog # 序列化类
