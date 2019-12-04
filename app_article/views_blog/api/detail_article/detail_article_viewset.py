from rest_framework import status
from rest_framework.response import Response
from utils.common.mixins.mixin import MyRetrieveModelMixin
from app_article.views_blog.api.detail_article.detail_article_serializer import DetailArticleSerializerBlog
from app_article import models
from django.db.models import F







class DetailArticleViewSetBlog(MyRetrieveModelMixin):
    """查看博文详细_客户端"""

    authentication_classes = ()  # 验证
    permission_classes = ()  # 权限
    queryset = models.Article.objects.all() #
    msg_detail = "查看博文详细_客户端" # 提示信息
    serializer_class = DetailArticleSerializerBlog # 序列化类

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.update_article_readcount(instance) # 阅读量++

        return Response({
            "success": True,
            "msg": self.msg_detail,
            "results": [serializer.data] # 以列表的格式给
        }, status=status.HTTP_200_OK)

    def update_article_readcount(self, instance):

        instance.readcount = F("readcount") + 1
        instance.save()

        return None