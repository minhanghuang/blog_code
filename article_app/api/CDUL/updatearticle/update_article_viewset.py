from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from article_app import models
from utils.common.mixins.mixin import MyUpdateModelMixin
from article_app.api.CDUL.updatearticle.update_article_serializer import UpdateArticleSerializerCls




"""
1. 修改博文信息接口
"""
class UpdateArticleViewSetCls(MyUpdateModelMixin):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = models.Article.objects.all()
    serializer_class = UpdateArticleSerializerCls # 序列化
    lookup_field = "pk" # 主键
    results_display = False
    msg_create = "成功修改博文信息"











