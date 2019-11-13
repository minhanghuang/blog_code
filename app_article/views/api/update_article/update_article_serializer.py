from app_article import models
from utils.common.serializers.serializer import MySerializerBase
from rest_framework import serializers




class UpdateArticleSerializer(MySerializerBase):
    """更新博文-序列化"""

    class Meta:
        model = models.Article
        fields = ["id","title","content","state",]

    def update(self, instance, validated_data):
        """
        :param instance: 实例
        :param validated_data: Put携带的参数
        :return: instance
        """

        instance.title = validated_data.get("title")
        instance.content = validated_data.get("content")
        instance.state = validated_data.get("state")
        instance.save()

        return instance





