from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from article_app import models
from utils.common.mixins.mixin import MyListModeMixin
from article_app.api.CDUL.listarticle.get_article_list_serializer import GetArticleListSerializerCls




"""
1. 获取博文列表接口
"""
class GetArticleListViewSetCls(MyListModeMixin):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Article.objects.all()
    serializer_class = GetArticleListSerializerCls # 序列化
    msg_create = "成功获取博文列表"










