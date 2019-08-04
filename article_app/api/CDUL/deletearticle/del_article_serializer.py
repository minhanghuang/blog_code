from article_app import models
from rest_framework import serializers
from utils.common.serializers.serializer import MySerializerBase



"""
1. 删除博文 序列化
"""
class DelArticleSerializerCls(MySerializerBase):

    class Meta:
        model = models.Article
        fields = []






