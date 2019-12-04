from utils.common.mixins.mixin import MyListModeMixin
from app_article.views_blog.api.list_article.list_article_serializer import ListArticleSerializerBlog
from app_article import models







class ListArticleViewSetBlog(MyListModeMixin):
    """查看博文列表_客户端"""

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限
    queryset = models.Article.objects.all().order_by("-createdate") # 倒序
    msg_list = "查看博文列表_客户端" # 提示信息
    serializer_class = ListArticleSerializerBlog # 序列化类
