from rest_framework import serializers
from app.utils.common.serializers.serializer import MySerializerBase

from app.utils.common.exceptions import exception
from app_article import models


class UpdateArticleMsgSerializer(MySerializerBase):
    """更新文章弹框信息-序列化"""

    subtitle = serializers.CharField(
        allow_null=True,
        allow_blank=True,
    )
    class Meta:
        model = models.Article
        fields = ["subtitle","state","tag"]
        extra_kwargs = {
            'subtitle':{
                'allow_null': True,
            },
            'tag':{
                'allow_null': True,
            },
        }


    def update(self, instance, validated_data):
        """
        :param instance: 实例
        :param validated_data: Put携带的参数
        :return: instance
        """
        print(validated_data)
        state = validated_data.get("state",0)
        if state == 1: # 确认发布文章, 需要上传图片
            if not instance.image: # 图片为空
                raise exception.myException400({
                    "success": False,
                    "msg": "请上传图片",
                    "results": "",
                })
        instance.subtitle = validated_data.get("subtitle","")
        instance.tag = validated_data.get("tag","{}")
        instance.state = state
        instance.save()

        return instance





