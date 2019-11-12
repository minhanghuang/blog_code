from app_article import models
from utils.common.serializers.serializer import MySerializerBase
from rest_framework import serializers




class UpdateArticleMsgSerializer(MySerializerBase):
    """更新文章弹框信息-序列化"""

    class Meta:
        model = models.Article
        fields = ["subtitle","state",]

    def update(self, instance, validated_data):
        """
        :param instance: 实例
        :param validated_data: Put携带的参数
        :return: instance
        """
        instance.subtitle = validated_data.get("subtitle")
        instance.state = validated_data.get("state")

        return instance





