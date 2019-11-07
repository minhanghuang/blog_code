from app_article import models
from utils.common.serializers.serializer import MySerializerBase
from rest_framework import serializers




class DeleteArticleSerializer(MySerializerBase):
    """删除博文-序列化"""

    class Meta:
        model = models.Article
        fields = []




