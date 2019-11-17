from app_article import models
from utils.common.serializers.serializer import MySerializerBase
from rest_framework import serializers




class GetStateArticleSerializer(MySerializerBase):
    """查看博文列表-序列化"""

    class Meta:
        model = models.Article
        fields = ["state",]





