from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from utils.common.mixins.mixin import MyCreateModeMixin
from article_app.api.CDUL.createarticle.create_article_serializer import CreateArticleSerializerCls




"""
1. 新增博文接口
"""
class CreateArticleViewSetCls(MyCreateModeMixin):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateArticleSerializerCls # 序列化
    msg_create = "发表成功"









