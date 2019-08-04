from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from article_app import models
from utils.common.mixins.mixin import MyRetrieveModelMixin
from article_app.api.CDUL.detailarticle.get_article_detail_serializer import GetArticleDetailSerializerCls




"""
1. 获取博文详细信息接口
"""
class GetArticleDetailViewSetCls(MyRetrieveModelMixin):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Article.objects.all()
    serializer_class = GetArticleDetailSerializerCls # 序列化
    lookup_field = "pk" # 主键
    msg_create = "成功获取博文详细信息"











